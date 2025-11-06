# Endpoint Implementation Guide

> **Last Updated**: 2025-11-06
> **Purpose**: Step-by-step guide for implementing NBA API endpoints in py-Goldsberry v2.0

## Overview

This guide walks through the complete process of adding a new endpoint to py-Goldsberry v2.0. We'll use **PlayerList** as the reference example since it's fully implemented.

**Time per endpoint**: ~2 hours (0.5h research, 1h implementation, 0.5h testing)

## Prerequisites

Before implementing an endpoint, ensure:

- [x] Development environment set up (see [CONTRIBUTING.md](CONTRIBUTING.md))
- [x] Familiar with project architecture (see [ARCHITECTURE.md](ARCHITECTURE.md))
- [x] Understand coding patterns (see [PATTERNS.md](PATTERNS.md))
- [x] Tests pass: `hatch run test`
- [x] Chosen an endpoint from [ENDPOINT_ROADMAP.md](ENDPOINT_ROADMAP.md)

## Step 1: Research the NBA API (30 minutes)

### 1.1 Find the NBA API Endpoint Name

Check the legacy code to find the endpoint name:

```bash
# Search legacy code for the endpoint
grep -r "endpoint_name" goldsberry_legacy/
```

**Example (PlayerList)**:
```python
# Found in goldsberry_legacy/player/player.py
url = "https://stats.nba.com/stats/commonallplayers"
```

NBA API endpoint: `commonallplayers`

### 1.2 Capture a Live Response

Create a test script to fetch and save the response:

```python
# test_capture.py
import httpx
import json
from pathlib import Path

def capture_response(endpoint: str, params: dict, output_file: str):
    """Capture NBA API response for fixture."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://stats.nba.com/",
        "Origin": "https://stats.nba.com",
    }

    url = f"https://stats.nba.com/stats/{endpoint}"

    try:
        response = httpx.get(
            url,
            params=params,
            headers=headers,
            timeout=30.0
        )
        response.raise_for_status()
        data = response.json()

        # Save full response
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"✓ Saved {len(json.dumps(data))} bytes to {output_file}")
        print(f"✓ Response has {len(data.get('resultSets', []))} result sets")

        # Print structure
        for rs in data.get("resultSets", []):
            print(f"  - {rs['name']}: {len(rs['headers'])} columns, {len(rs['rowSet'])} rows")

        return data

    except Exception as e:
        print(f"✗ Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    data = capture_response(
        endpoint="commonallplayers",
        params={
            "LeagueID": "00",
            "Season": "2024-25",
            "IsOnlyCurrentSeason": 1
        },
        output_file="tests/fixtures/player/player_list_response.json"
    )
```

Run the script:
```bash
python test_capture.py
```

### 1.3 Trim the Fixture

Full responses can be large. Trim to 5-10 representative rows for faster tests:

```python
import json

# Load full response
with open("tests/fixtures/player/player_list_response.json") as f:
    data = json.load(f)

# Keep only first 5 rows (diverse examples)
data["resultSets"][0]["rowSet"] = data["resultSets"][0]["rowSet"][:5]

# Save trimmed version
with open("tests/fixtures/player/player_list_response.json", "w") as f:
    json.dump(data, f, indent=2)
```

### 1.4 Document the Endpoint

Note the following:
- NBA API endpoint name
- Required parameters
- Optional parameters
- Response structure (headers, row count)
- Any special behaviors or gotchas

## Step 2: Create the Pydantic Model (30 minutes)

### 2.1 Create Model File

**File**: `src/goldsberry/models/{category}/{endpoint}.py`

**Example**: `src/goldsberry/models/player/player_list.py`

### 2.2 Define the Model

```python
"""Pydantic models for PlayerList endpoint."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class PlayerInfo(BaseModel):
    """Player information from commonallplayers endpoint.

    This model represents basic player information including biographical
    data, team affiliation, and career span.
    """

    model_config = ConfigDict(
        populate_by_name=True,      # Allow both alias and field name
        validate_assignment=True,   # Validate when fields are updated
    )

    # Required fields (always present in NBA API response)
    person_id: int = Field(alias="PERSON_ID")
    display_last_comma_first: str = Field(alias="DISPLAY_LAST_COMMA_FIRST")
    full_name: str = Field(alias="DISPLAY_FIRST_LAST")
    roster_status: int = Field(alias="ROSTERSTATUS")
    from_year: str = Field(alias="FROM_YEAR")
    to_year: str = Field(alias="TO_YEAR")
    playercode: str = Field(alias="PLAYERCODE")

    # Optional fields (sometimes missing in NBA API response)
    team_id: Optional[int] = Field(None, alias="TEAM_ID")
    team_city: Optional[str] = Field(None, alias="TEAM_CITY")
    team_name: Optional[str] = Field(None, alias="TEAM_NAME")
    team_abbreviation: Optional[str] = Field(None, alias="TEAM_ABBREVIATION")
    jersey_number: Optional[str] = Field(None, alias="JERSEY_NUMBER")
    position: Optional[str] = Field(None, alias="POSITION")
    height: Optional[str] = Field(None, alias="HEIGHT")
    weight: Optional[str] = Field(None, alias="WEIGHT")
    college: Optional[str] = Field(None, alias="COLLEGE")
    country: Optional[str] = Field(None, alias="COUNTRY")
    draft_year: Optional[str] = Field(None, alias="DRAFT_YEAR")
    draft_round: Optional[str] = Field(None, alias="DRAFT_ROUND")
    draft_number: Optional[str] = Field(None, alias="DRAFT_NUMBER")
    greatest_75_flag: Optional[str] = Field(None, alias="GREATEST_75_FLAG")

    # Computed properties
    @property
    def is_active(self) -> bool:
        """Whether player is currently active (on a roster)."""
        return self.roster_status == 1

    # String representations
    def __str__(self) -> str:
        """Human-readable string representation."""
        status = "Active" if self.is_active else "Inactive"
        team = self.team_abbreviation or "FA"
        return f"{self.full_name} ({team}) - {status}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerInfo(person_id={self.person_id}, name='{self.full_name}')"


__all__ = ["PlayerInfo"]
```

### 2.3 Key Model Patterns

**Field Aliases**:
```python
person_id: int = Field(alias="PERSON_ID")
```
Maps NBA API's `PERSON_ID` to pythonic `person_id`.

**Optional vs Required**:
```python
# Required (always present)
person_id: int = Field(alias="PERSON_ID")

# Optional (sometimes missing)
team_id: Optional[int] = Field(None, alias="TEAM_ID")
```

**Computed Properties**:
```python
@property
def is_active(self) -> bool:
    return self.roster_status == 1
```

**String Methods**:
```python
def __str__(self) -> str:
    """For print(player)"""
    return f"{self.full_name} ({self.team_abbreviation})"

def __repr__(self) -> str:
    """For debugging"""
    return f"PlayerInfo(person_id={self.person_id})"
```

## Step 3: Create the Endpoint (30 minutes)

### 3.1 Create Endpoint File

**File**: `src/goldsberry/endpoints/{category}/{endpoint}.py`

**Example**: `src/goldsberry/endpoints/player/player_list.py`

### 3.2 Implement the Endpoint Class

```python
"""PlayerList endpoint - fetch all NBA players."""

from typing import Dict, List, Optional, Union

from ...client.base import BaseClient
from ...enums.common import IsOnlyCurrentSeason, LeagueID, Season
from ...models.base import parse_nba_response
from ...models.player import PlayerInfo


class PlayerListEndpoint:
    """Fetch list of all NBA players.

    Provides access to the commonallplayers endpoint which returns
    basic information about all players, with optional filtering.

    Example:
        >>> # Synchronous usage
        >>> endpoint = PlayerListEndpoint()
        >>> players = endpoint.fetch(season=Season.CURRENT)
        >>> for player in players[:5]:
        ...     print(player.full_name, player.team_abbreviation)

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = PlayerListEndpoint(client)
        ...     players = await endpoint.fetch_async(season=Season.CURRENT)
    """

    ENDPOINT = "commonallplayers"  # NBA API endpoint name

    def __init__(self, client: Optional[BaseClient] = None) -> None:
        """Initialize endpoint.

        Args:
            client: HTTP client instance (creates default if not provided)
        """
        self.client = client or BaseClient()
        self._owns_client = client is None  # Track if we created it

    def __del__(self) -> None:
        """Cleanup client if we created it."""
        if self._owns_client and hasattr(self, "client"):
            self.client.close()

    def _build_params(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> Dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            season: NBA season (e.g., "2024-25")
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only

        Returns:
            Dict of query parameters
        """
        # Convert enums to values (handle both enum and string)
        season_value = season.value if isinstance(season, Season) else season
        league_value = league_id.value if isinstance(league_id, LeagueID) else league_id
        only_current_value = (
            only_current_season.value
            if isinstance(only_current_season, IsOnlyCurrentSeason)
            else only_current_season
        )

        return {
            "LeagueID": league_value,
            "Season": season_value,
            "IsOnlyCurrentSeason": only_current_value,
        }

    def fetch(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> List[PlayerInfo]:
        """Fetch player list (synchronous).

        Args:
            season: NBA season (default: current season)
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only (default: yes)

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = PlayerListEndpoint()
            >>> players = endpoint.fetch(season="2024-25")
            >>> active = [p for p in players if p.is_active]
        """
        params = self._build_params(season, league_id, only_current_season)
        data = self.client.get(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)

    async def fetch_async(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> List[PlayerInfo]:
        """Fetch player list (asynchronous).

        Args:
            season: NBA season (default: current season)
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only (default: yes)

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = PlayerListEndpoint(client)
            ...     players = await endpoint.fetch_async(season="2024-25")
        """
        params = self._build_params(season, league_id, only_current_season)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)


# Convenience functions for quick access
def get_players(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Convenience function to fetch player list.

    Args:
        season: NBA season (default: current)
        league_id: League identifier (default: NBA)
        only_current_season: Filter for current season only (default: yes)
        client: Optional client instance

    Returns:
        List of PlayerInfo objects

    Example:
        >>> from goldsberry.endpoints.player import get_players
        >>> players = get_players(season="2024-25")
        >>> print(f"Found {len(players)} players")
    """
    endpoint = PlayerListEndpoint(client)
    return endpoint.fetch(season, league_id, only_current_season)


async def get_players_async(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Async convenience function to fetch player list.

    Args:
        season: NBA season (default: current)
        league_id: League identifier (default: NBA)
        only_current_season: Filter for current season only (default: yes)
        client: Optional client instance

    Returns:
        List of PlayerInfo objects

    Example:
        >>> from goldsberry.endpoints.player import get_players_async
        >>> players = await get_players_async(season="2024-25")
    """
    endpoint = PlayerListEndpoint(client)
    return await endpoint.fetch_async(season, league_id, only_current_season)


__all__ = ["PlayerListEndpoint", "get_players", "get_players_async"]
```

### 3.3 Key Endpoint Patterns

**Client Ownership**:
```python
def __init__(self, client: Optional[BaseClient] = None):
    self.client = client or BaseClient()
    self._owns_client = client is None

def __del__(self):
    if self._owns_client and hasattr(self, "client"):
        self.client.close()
```

**Parameter Building**:
```python
def _build_params(self, season: Union[Season, str], ...) -> Dict:
    # Handle both enum and string
    season_value = season.value if isinstance(season, Season) else season
    return {"Season": season_value, ...}
```

**Sync and Async**:
```python
def fetch(self, **kwargs) -> List[Model]:
    data = self.client.get(self.ENDPOINT, params=params)
    return parse_nba_response(data, Model)

async def fetch_async(self, **kwargs) -> List[Model]:
    data = await self.client.get_async(self.ENDPOINT, params=params)
    return parse_nba_response(data, Model)
```

## Step 4: Write Tests (30 minutes)

### 4.1 Create Test File

**File**: `tests/unit/test_{endpoint}.py`

**Example**: `tests/unit/test_player_list.py`

### 4.2 Write Comprehensive Tests

```python
"""Tests for PlayerList endpoint."""

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.player import PlayerListEndpoint, get_players
from goldsberry.enums.common import IsOnlyCurrentSeason, LeagueID, Season
from goldsberry.models.player import PlayerInfo


@pytest.fixture
def player_list_data(load_fixture):
    """Load player list fixture."""
    return load_fixture("player/player_list_response.json")


def test_player_info_model():
    """Test PlayerInfo model parsing."""
    data = {
        "PERSON_ID": 203999,
        "DISPLAY_LAST_COMMA_FIRST": "Jokic, Nikola",
        "DISPLAY_FIRST_LAST": "Nikola Jokic",
        "ROSTERSTATUS": 1,
        "FROM_YEAR": "2015",
        "TO_YEAR": "2024",
        "PLAYERCODE": "nikola_jokic",
        "TEAM_ID": 1610612743,
        "TEAM_ABBREVIATION": "DEN",
        # ... more fields
    }

    player = PlayerInfo(**data)

    assert player.person_id == 203999
    assert player.full_name == "Nikola Jokic"
    assert player.is_active is True


def test_player_list_endpoint_params():
    """Test parameter building."""
    client = BaseClient()
    endpoint = PlayerListEndpoint(client)

    params = endpoint._build_params(
        season=Season.CURRENT,
        league_id=LeagueID.NBA,
    )

    assert params["Season"] == "2024-25"
    assert params["LeagueID"] == "00"


def test_player_list_fetch(player_list_data, mock_client_response):
    """Test synchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = endpoint.fetch(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)


@pytest.mark.asyncio
async def test_player_list_fetch_async(player_list_data, mock_client_response):
    """Test asynchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = await endpoint.fetch_async(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)


def test_convenience_function(player_list_data, mock_client_response):
    """Test convenience function."""
    mock_client_response(player_list_data)

    players = get_players(season=Season.CURRENT)

    assert len(players) == 5
```

### 4.3 Run Tests

```bash
# Run tests for this endpoint
pytest tests/unit/test_player_list.py -v

# Check coverage
pytest tests/unit/test_player_list.py --cov=goldsberry.endpoints.player.player_list --cov=goldsberry.models.player.player_list
```

## Step 5: Update Documentation (15 minutes)

### 5.1 Update ENDPOINT_ROADMAP.md

Mark the endpoint as complete:

```markdown
| ✅ | PlayerList | commonallplayers | models/player/player_list.py | endpoints/player/player_list.py | test_player_list.py | HIGH | ✅ Complete |
```

### 5.2 Update CHANGELOG.md

```markdown
## [2.0.0-alpha.2] - 2025-11-XX

### Added
- PlayerList endpoint (commonallplayers)
```

### 5.3 Update README.md (if Tier 1)

For high-priority endpoints, add to README examples.

## Step 6: Quality Gates

Before marking complete, verify:

```bash
# All tests pass
hatch run test

# Linting passes
hatch run lint

# Type checking passes
hatch run type

# Code formatted
hatch run format-check

# Package builds
uv build
```

## Common Gotchas

### 1. Optional Fields

**Problem**: Field is optional but Pydantic raises error.

**Solution**: Use `Optional[T] = Field(None, ...)`:
```python
team_id: Optional[int] = Field(None, alias="TEAM_ID")
```

### 2. Enum Handling

**Problem**: Parameter can be enum or string.

**Solution**: Use `Union` and check type:
```python
season: Union[Season, str] = Season.CURRENT

season_value = season.value if isinstance(season, Season) else season
```

### 3. Client Cleanup

**Problem**: Memory leak if client not closed.

**Solution**: Use `__del__` for owned clients:
```python
def __init__(self, client: Optional[BaseClient] = None):
    self.client = client or BaseClient()
    self._owns_client = client is None

def __del__(self):
    if self._owns_client and hasattr(self, "client"):
        self.client.close()
```

### 4. Async Testing

**Problem**: Forgot to test async path.

**Solution**: Always add `@pytest.mark.asyncio` test:
```python
@pytest.mark.asyncio
async def test_fetch_async(data, mock_client_response):
    mock_client_response(data)
    endpoint = MyEndpoint()
    result = await endpoint.fetch_async()
    assert len(result) > 0
```

### 5. Mock Fixture

**Problem**: Test makes real HTTP request.

**Solution**: Use `mock_client_response` fixture:
```python
def test_fetch(data, mock_client_response):
    mock_client_response(data)  # Mock before calling endpoint
    endpoint = MyEndpoint()
    result = endpoint.fetch()
```

## Checklist Summary

Use this for each endpoint:

- [ ] Research NBA API (capture fixture, document params)
- [ ] Create model (`models/{category}/{endpoint}.py`)
- [ ] Create endpoint (`endpoints/{category}/{endpoint}.py`)
- [ ] Write tests (`tests/unit/test_{endpoint}.py`)
- [ ] Update ENDPOINT_ROADMAP.md
- [ ] Update CHANGELOG.md
- [ ] Run quality gates (test, lint, type, format, build)
- [ ] Verify 100% coverage for endpoint

---

**Last Updated**: 2025-11-06
**Maintained by**: Bradley Fay (bradley.fay@gmail.com)
