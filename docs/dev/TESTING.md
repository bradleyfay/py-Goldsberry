# Testing Strategy

This document describes the testing approach for py-Goldsberry v2.0.

## Philosophy

**Test reliability over API reliability.**

The NBA stats API is unreliable. Our tests should not be. We achieve this by:
1. **Mocking the NBA API** - Never make real requests in unit tests
2. **Fixture-based testing** - Use captured API responses for deterministic tests
3. **Fast feedback** - Tests run in milliseconds, not seconds

## Test Structure

```
tests/
├── conftest.py                  # Shared fixtures and configuration
├── fixtures/                    # Captured NBA API responses
│   └── player/
│       └── player_list_response.json
└── unit/                        # Unit tests (no external dependencies)
    └── test_player_list.py
```

## Test Types

### Unit Tests (`tests/unit/`)

Test individual components in isolation.

**Coverage**:
- Model parsing and validation
- Endpoint parameter building
- Response parsing
- Error handling
- Both sync and async code paths

**Do NOT**:
- Make real HTTP requests
- Depend on NBA API availability
- Test httpx/Pydantic internals (trust the libraries)

### Integration Tests (Future)

**TODO**: Add integration tests (optional, marked with `@pytest.mark.integration`):
- Make real requests to NBA API
- Validate live data matches our models
- Run separately (`pytest -m integration`)
- Expected to be flaky (NBA API is unreliable)

## Fixtures

### Shared Fixtures (`conftest.py`)

#### `fixtures_dir`

Returns path to fixtures directory:
```python
@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"
```

#### `load_fixture`

Factory fixture to load JSON fixtures:
```python
@pytest.fixture
def load_fixture(fixtures_dir: Path):
    def _load(fixture_path: str) -> dict[str, Any]:
        full_path = fixtures_dir / fixture_path
        with open(full_path) as f:
            return json.load(f)
    return _load

# Usage
def test_something(load_fixture):
    data = load_fixture("player/player_list_response.json")
    assert "resultSets" in data
```

#### `mock_client_response`

Factory fixture to mock `BaseClient` responses:
```python
@pytest.fixture
def mock_client_response(monkeypatch):
    def _mock(response_data: dict[str, Any]) -> None:
        from goldsberry.client.base import BaseClient

        def mock_get(self, endpoint: str, params=None):
            return response_data

        async def mock_get_async(self, endpoint: str, params=None):
            return response_data

        monkeypatch.setattr(BaseClient, "get", mock_get)
        monkeypatch.setattr(BaseClient, "get_async", mock_get_async)

    return _mock

# Usage
def test_fetch(player_list_data, mock_client_response):
    mock_client_response(player_list_data)
    endpoint = PlayerListEndpoint()
    players = endpoint.fetch()
    assert len(players) == 5
```

### Endpoint-Specific Fixtures

```python
@pytest.fixture
def player_list_data(load_fixture):
    """Load player list fixture."""
    return load_fixture("player/player_list_response.json")
```

## Creating Fixtures

To create a new fixture:

1. **Make a real API request** (one-time, save the response):
```python
import httpx
import json

response = httpx.get(
    "https://stats.nba.com/stats/commonallplayers",
    params={"LeagueID": "00", "Season": "2024-25", "IsOnlyCurrentSeason": 1},
    headers={"User-Agent": "Mozilla/5.0 ..."},
    timeout=30.0
)
data = response.json()

# Save to fixture file
with open("tests/fixtures/player/player_list_response.json", "w") as f:
    json.dump(data, f, indent=2)
```

2. **Trim if needed** - Keep 5-10 representative rows:
```python
# Full response has 500+ players
# Trim to 5 diverse examples for faster tests
data["resultSets"][0]["rowSet"] = data["resultSets"][0]["rowSet"][:5]
```

3. **Use in tests**:
```python
def test_endpoint(load_fixture, mock_client_response):
    data = load_fixture("player/player_list_response.json")
    mock_client_response(data)
    # ... test code
```

## Test Patterns

### Testing Model Parsing

```python
def test_player_info_model():
    """Test PlayerInfo model parsing."""
    data = {
        "PERSON_ID": 203999,
        "DISPLAY_FIRST_LAST": "Nikola Jokic",
        "ROSTERSTATUS": 1,
        # ... more fields
    }

    player = PlayerInfo(**data)

    assert player.person_id == 203999
    assert player.full_name == "Nikola Jokic"
    assert player.is_active is True
```

### Testing Endpoint Parameters

```python
def test_player_list_endpoint_params():
    """Test parameter building."""
    client = BaseClient()
    endpoint = PlayerListEndpoint(client)

    # Test with enums
    params = endpoint._build_params(
        season=Season.CURRENT,
        league_id=LeagueID.NBA,
    )

    assert params["Season"] == "2024-25"
    assert params["LeagueID"] == "00"

    # Test with string season
    params = endpoint._build_params(season="2023-24")
    assert params["Season"] == "2023-24"
```

### Testing Synchronous Fetch

```python
def test_player_list_fetch(player_list_data, mock_client_response):
    """Test synchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = endpoint.fetch(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)

    jokic = players[0]
    assert jokic.person_id == 203999
    assert jokic.full_name == "Nikola Jokic"
```

### Testing Asynchronous Fetch

```python
@pytest.mark.asyncio
async def test_player_list_fetch_async(player_list_data, mock_client_response):
    """Test asynchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = await endpoint.fetch_async(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)
```

### Testing Convenience Functions

```python
def test_convenience_function(player_list_data, mock_client_response):
    """Test convenience function."""
    mock_client_response(player_list_data)

    players = get_players(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)
```

### Testing String Representations

```python
def test_player_info_str_repr():
    """Test string representations."""
    player = PlayerInfo(
        person_id=203999,
        full_name="Nikola Jokic",
        team_abbreviation="DEN",
        roster_status=1,
        # ... required fields
    )

    str_rep = str(player)
    assert "Nikola Jokic" in str_rep
    assert "DEN" in str_rep
    assert "Active" in str_rep

    repr_rep = repr(player)
    assert "PlayerInfo" in repr_rep
    assert "203999" in repr_rep
```

### Testing Computed Properties

```python
def test_player_info_computed_properties():
    """Test computed properties."""
    active_player = PlayerInfo(roster_status=1, ...)
    assert active_player.is_active is True

    inactive_player = PlayerInfo(roster_status=0, ...)
    assert inactive_player.is_active is False
```

### Testing Error Handling

**TODO**: Add these tests for each endpoint:

```python
def test_timeout_error(mock_client_timeout):
    """Test handling of timeout errors."""
    endpoint = PlayerListEndpoint()
    with pytest.raises(TimeoutError) as exc_info:
        endpoint.fetch()

    assert "timeout" in str(exc_info.value).lower()

def test_validation_error():
    """Test handling of invalid response data."""
    endpoint = PlayerListEndpoint()
    # Mock with invalid data
    # ... assert ValidationError raised
```

## Running Tests

### All Tests

```bash
# With pytest directly
pytest tests/unit/ -v

# With hatch (future)
hatch run test
```

### With Coverage

```bash
# Generate coverage report
pytest tests/unit/ --cov=goldsberry --cov-report=html

# View report
open htmlcov/index.html
```

### Specific Test File

```bash
pytest tests/unit/test_player_list.py -v
```

### Specific Test Function

```bash
pytest tests/unit/test_player_list.py::test_player_info_model -v
```

### Fast Run (No Coverage)

```bash
pytest tests/unit/ -v --no-cov
```

## Coverage Goals

- **100% coverage** on implemented endpoints (models + endpoints)
- **80%+ overall** (allows for defensive code that's hard to test)
- **Focus on logic**, not boilerplate

## Test Configuration

From `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
asyncio_mode = "auto"
markers = [
    "integration: marks tests as integration tests (live NBA API calls)",
    "slow: marks tests as slow running",
]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=goldsberry",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-report=xml",
]
```

## CI/CD Testing

**TODO**: Set up GitHub Actions:
- Run tests on push/PR
- Test on Python 3.9, 3.10, 3.11, 3.12
- Test on Linux, macOS, Windows
- Fail if coverage drops below threshold

## Testing Best Practices

### DO

- ✅ Mock external dependencies (NBA API, network)
- ✅ Test both happy path and error cases
- ✅ Use descriptive test names (`test_player_info_model_parsing`)
- ✅ Keep tests independent (no shared state)
- ✅ Use fixtures for reusable test data
- ✅ Test both sync and async code paths
- ✅ Assert specific values, not just types

### DON'T

- ❌ Make real HTTP requests in unit tests
- ❌ Test library internals (httpx, Pydantic)
- ❌ Share state between tests (causes flaky tests)
- ❌ Use `assert True` (meaningless)
- ❌ Skip error case testing
- ❌ Forget to test edge cases (empty lists, None values, etc.)

## Future Testing

**TODO**: Expand testing:
- [ ] Property-based testing with Hypothesis
- [ ] Performance benchmarks
- [ ] Load testing (how many requests/second?)
- [ ] Integration tests (optional, marked separately)
- [ ] Mutation testing (test the tests)

---

**Last Updated**: 2025-11-06
**Author**: Bradley Fay
