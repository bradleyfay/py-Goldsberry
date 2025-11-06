# Contributing to py-Goldsberry

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Git

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/bradleyfay/py-Goldsberry.git
cd py-Goldsberry

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
# or
.venv\Scripts\activate  # Windows

# Install in editable mode with dev dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Verify Setup

```bash
# Run tests
pytest tests/unit/ -v

# Run linting
ruff check src/

# Run type checking
mypy src/
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

### 2. Make Changes

Follow our [coding patterns](PATTERNS.md) and [architecture guidelines](ARCHITECTURE.md).

### 3. Write Tests

All new code must include tests. See [TESTING.md](TESTING.md) for testing patterns.

```bash
# Run tests as you develop
pytest tests/unit/ -v --no-cov  # Fast, no coverage
pytest tests/unit/ -v            # With coverage
```

### 4. Run Pre-commit Hooks

```bash
# Hooks run automatically on commit, but you can run manually:
pre-commit run --all-files
```

This runs:
- `ruff` - Linting and auto-fixes
- `black` - Code formatting
- `mypy` - Type checking

### 5. Commit Changes

```bash
git add .
git commit -m "feat: add player game log endpoint"
```

Use [conventional commits](https://www.conventionalcommits.org/):
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Adding New Endpoints

Follow this pattern for adding new endpoints:

### 1. Create Model

`src/goldsberry/models/{category}/{endpoint}.py`:

```python
from typing import Optional
from pydantic import BaseModel, Field

class YourModel(BaseModel):
    """Model for your endpoint response."""

    field_name: int = Field(alias="NBA_API_NAME")
    # ... more fields
```

### 2. Create Endpoint

`src/goldsberry/endpoints/{category}/{endpoint}.py`:

```python
from typing import List, Optional
from goldsberry.client.base import BaseClient
from goldsberry.models.your_category import YourModel

class YourEndpoint:
    """Description of endpoint."""

    ENDPOINT = "nba_endpoint_name"

    def __init__(self, client: Optional[BaseClient] = None):
        self.client = client or BaseClient()
        self._owns_client = client is None

    def fetch(self, **kwargs) -> List[YourModel]:
        """Fetch data synchronously."""
        params = self._build_params(**kwargs)
        data = self.client.get(self.ENDPOINT, params=params)
        return parse_nba_response(data, YourModel)

    async def fetch_async(self, **kwargs) -> List[YourModel]:
        """Fetch data asynchronously."""
        params = self._build_params(**kwargs)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return parse_nba_response(data, YourModel)
```

### 3. Create Fixture

1. Make a real API request (one-time)
2. Save response to `tests/fixtures/{category}/{endpoint}_response.json`
3. Trim to 5-10 representative rows

### 4. Write Tests

`tests/unit/test_{endpoint}.py`:

```python
import pytest
from goldsberry.endpoints.your_category import YourEndpoint
from goldsberry.models.your_category import YourModel

@pytest.fixture
def your_data(load_fixture):
    return load_fixture("{category}/{endpoint}_response.json")

def test_model_parsing():
    """Test model parsing."""
    # ...

def test_endpoint_fetch(your_data, mock_client_response):
    """Test synchronous fetch."""
    # ...

@pytest.mark.asyncio
async def test_endpoint_fetch_async(your_data, mock_client_response):
    """Test asynchronous fetch."""
    # ...
```

### 5. Update Documentation

- Add endpoint to README.md
- Update CHANGELOG.md
- Add example to `examples/` if needed

## Code Quality

### Linting

```bash
# Check for issues
ruff check src/

# Auto-fix issues
ruff check --fix src/
```

### Formatting

```bash
# Format code
black src/ tests/
```

### Type Checking

```bash
# Run mypy
mypy src/
```

### All Checks

```bash
# Run all quality checks
pre-commit run --all-files
```

## Testing

### Run Tests

```bash
# All tests
pytest tests/unit/ -v

# Specific file
pytest tests/unit/test_player_list.py -v

# With coverage
pytest tests/unit/ --cov=goldsberry --cov-report=html

# Fast (no coverage)
pytest tests/unit/ -v --no-cov
```

### Coverage Requirements

- **100% coverage** on new endpoints
- **No decrease** in overall coverage

## Documentation

### Code Documentation

- All public functions/classes need docstrings
- Use Google-style docstrings
- Include examples in docstrings

```python
def fetch(self, season: Season) -> List[PlayerInfo]:
    """Fetch player list for given season.

    Args:
        season: NBA season to query

    Returns:
        List of PlayerInfo objects

    Raises:
        TimeoutError: If request times out

    Example:
        >>> endpoint = PlayerListEndpoint()
        >>> players = endpoint.fetch(season=Season.CURRENT)
    """
```

### Developer Documentation

Update docs/dev/ when adding significant features:
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design changes
- [PATTERNS.md](PATTERNS.md) - New coding patterns
- [TESTING.md](TESTING.md) - Testing approach changes

## Pull Request Process

### Before Submitting

- [ ] Tests pass (`pytest tests/unit/ -v`)
- [ ] Coverage maintained or improved
- [ ] Linting passes (`ruff check src/`)
- [ ] Type checking passes (`mypy src/`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated

### PR Template

Your PR description should include:

```markdown
## Summary
Brief description of changes

## Changes
- List of specific changes

## Testing
How you tested the changes

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG updated
```

### Review Process

1. Automated checks run (tests, linting, type checking)
2. Code review by maintainer
3. Address feedback
4. Approval and merge

## Release Process

**TODO**: Document release process once established:
- Version bumping
- PyPI publication
- GitHub releases
- Documentation deployment

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/bradleyfay/py-Goldsberry/issues)
- **Discussions**: [GitHub Discussions](https://github.com/bradleyfay/py-Goldsberry/discussions)
- **Email**: bradley.fay@gmail.com

## Code of Conduct

**TODO**: Add CODE_OF_CONDUCT.md

In the meantime:
- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Assume good intentions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Last Updated**: 2025-11-06
**Maintainer**: Bradley Fay (bradley.fay@gmail.com)
