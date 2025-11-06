# Coding Patterns and Conventions

This document describes the coding patterns, conventions, and design decisions used in py-Goldsberry v2.0.

## Table of Contents

- [File Organization](#file-organization)
- [Naming Conventions](#naming-conventions)
- [Model Patterns](#model-patterns)
- [Endpoint Patterns](#endpoint-patterns)
- [Error Handling](#error-handling)
- [Type Hints](#type-hints)
- [Testing Patterns](#testing-patterns)

## File Organization

### Source Layout

```
src/goldsberry/
├── __init__.py              # Package exports
├── py.typed                 # PEP 561 marker for type checkers
├── client/
│   ├── __init__.py
│   ├── base.py             # BaseClient
│   └── exceptions.py       # Exception hierarchy
├── models/
│   ├── __init__.py
│   ├── base.py             # BaseNBAModel, parse_nba_response
│   └── {category}/          # e.g., player/, team/, game/
│       ├── __init__.py
│       └── {endpoint}.py   # Model for specific endpoint
├── endpoints/
│   ├── __init__.py
│   └── {category}/
│       ├── __init__.py
│       └── {endpoint}.py   # Endpoint implementation
└── enums/
    ├── __init__.py
    └── common.py           # Shared enums (Season, LeagueID, etc.)
```

### One File Per Endpoint

Each endpoint gets:
- **One model file**: `models/{category}/{endpoint}.py` (~80 lines)
- **One endpoint file**: `endpoints/{category}/{endpoint}.py` (~175 lines)
- **One test file**: `tests/unit/test_{endpoint}.py` (~200 lines)
- **One fixture file**: `tests/fixtures/{category}/{endpoint}_response.json`

This keeps files focused and easy to navigate.

## Naming Conventions

### Python Style (PEP 8)

- **Modules**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions**: `snake_case()`
- **Constants**: `UPPER_CASE`
- **Private**: `_leading_underscore`

### NBA API Mapping

NBA API uses ALL_CAPS. We convert to pythonic names:

```python
# NBA API response
{"PERSON_ID": 203999, "DISPLAY_FIRST_LAST": "Nikola Jokic"}

# Our model
class PlayerInfo(BaseModel):
    person_id: int = Field(alias="PERSON_ID")
    full_name: str = Field(alias="DISPLAY_FIRST_LAST")
```

### Endpoint Names

- **Class**: `{Entity}{Action}Endpoint` (e.g., `PlayerListEndpoint`)
- **Convenience function**: `get_{entity}` or `{verb}_{entity}` (e.g., `get_players`)
- **Async variant**: `{function}_async` (e.g., `get_players_async`)

## Model Patterns

### Base Model Structure

```python
from pydantic import BaseModel, Field, ConfigDict

class PlayerInfo(BaseModel):
    """Model for player information from commonallplayers endpoint."""

    model_config = ConfigDict(
        populate_by_name=True,      # Accept both alias and field name
        validate_assignment=True     # Validate when fields are updated
    )

    # Required fields
    person_id: int = Field(alias="PERSON_ID")
    full_name: str = Field(alias="DISPLAY_FIRST_LAST")

    # Optional fields (NBA API sometimes omits them)
    team_abbreviation: Optional[str] = Field(None, alias="TEAM_ABBREVIATION")

    # Computed properties
    @property
    def is_active(self) -> bool:
        """Computed from roster_status field."""
        return self.roster_status == 1

    def __str__(self) -> str:
        """Human-readable representation."""
        status = "Active" if self.is_active else "Inactive"
        return f"{self.full_name} ({self.team_abbreviation}) - {status}"
```

### Field Alias Pattern

Always use `Field(alias="NBA_API_NAME")` for mapping:

```python
person_id: int = Field(alias="PERSON_ID")
```

This allows users to pass either:
```python
PlayerInfo(person_id=123)        # Pythonic
PlayerInfo(PERSON_ID=123)        # NBA API format
```

### Optional vs Required

- **Required**: Data always present in NBA API response
- **Optional**: Data sometimes missing (use `Optional[T] = Field(None, ...)`)

When unsure, make it optional. Pydantic will raise clear errors if field is required but missing.

### Computed Properties

Use `@property` for derived data:

```python
@property
def is_active(self) -> bool:
    """Whether player is currently active."""
    return self.roster_status == 1

@property
def years_experience(self) -> int:
    """Number of years in NBA."""
    return int(self.to_year) - int(self.from_year) + 1
```

Don't store computed values as fields (waste of memory, can get out of sync).

## Endpoint Patterns

### Standard Endpoint Structure

```python
from typing import Dict, List, Optional, Union

class PlayerListEndpoint:
    """Fetch list of all NBA players.

    Example:
        >>> endpoint = PlayerListEndpoint()
        >>> players = endpoint.fetch(season=Season.CURRENT)
    """

    ENDPOINT = "commonallplayers"  # NBA API endpoint name

    def __init__(self, client: Optional[BaseClient] = None) -> None:
        """Initialize endpoint.

        Args:
            client: HTTP client instance (creates default if None)
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
        **kwargs
    ) -> Dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            season: NBA season (e.g., "2024-25")
            league_id: League identifier
            **kwargs: Additional parameters

        Returns:
            Dict of query parameters
        """
        # Convert enums to values
        season_value = season.value if isinstance(season, Season) else season
        league_value = league_id.value if isinstance(league_id, LeagueID) else league_id

        return {
            "LeagueID": league_value,
            "Season": season_value,
            # ... more params
        }

    def fetch(self, **kwargs) -> List[PlayerInfo]:
        """Fetch player list (synchronous).

        Args:
            **kwargs: Parameters passed to _build_params

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails
        """
        params = self._build_params(**kwargs)
        data = self.client.get(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)

    async def fetch_async(self, **kwargs) -> List[PlayerInfo]:
        """Fetch player list (asynchronous).

        Args:
            **kwargs: Parameters passed to _build_params

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails
        """
        params = self._build_params(**kwargs)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)
```

### Convenience Function Pattern

Provide quick access without manual client creation:

```python
def get_players(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Convenience function to fetch player list.

    Example:
        >>> from goldsberry.endpoints.player import get_players
        >>> players = get_players(season="2024-25")
    """
    endpoint = PlayerListEndpoint(client)
    return endpoint.fetch(season, league_id)

async def get_players_async(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Async convenience function."""
    endpoint = PlayerListEndpoint(client)
    return await endpoint.fetch_async(season, league_id)
```

### Client Ownership Pattern

If user provides client, they own it. If we create it, we clean it up:

```python
def __init__(self, client: Optional[BaseClient] = None):
    self.client = client or BaseClient()
    self._owns_client = client is None

def __del__(self):
    if self._owns_client and hasattr(self, "client"):
        self.client.close()
```

## Error Handling

### Raise Specific Exceptions

```python
from goldsberry.client.exceptions import TimeoutError, ValidationError

# Bad
raise Exception("Request timed out")

# Good
raise TimeoutError(
    message="Request to commonallplayers timed out after 30s",
    context={"endpoint": "commonallplayers", "timeout": 30.0}
)
```

### Context in Exceptions

Always provide context for debugging:

```python
try:
    data = self.client.get(endpoint, params)
except httpx.TimeoutException as e:
    raise TimeoutError(
        message=f"Request to {endpoint} timed out",
        context={
            "endpoint": endpoint,
            "params": params,
            "timeout": self.client.timeout
        },
        original_error=e
    )
```

### Don't Catch Without Re-raising

```python
# Bad
try:
    data = fetch_data()
except Exception:
    pass  # Silently fails, user has no idea what went wrong

# Good
try:
    data = fetch_data()
except httpx.HTTPError as e:
    raise NBAAPIError(
        message="Failed to fetch data",
        context={"error": str(e)},
        original_error=e
    )
```

## Type Hints

### Always Use Type Hints

```python
# Bad
def fetch(self, season):
    return parse_response(data)

# Good
def fetch(self, season: Union[Season, str]) -> List[PlayerInfo]:
    return parse_nba_response(data, PlayerInfo)
```

### Use Union for Multiple Types

```python
from typing import Union

def fetch(self, season: Union[Season, str]) -> List[PlayerInfo]:
    """Accept either enum or string."""
    pass
```

### Use Optional for Nullable

```python
from typing import Optional

def __init__(self, client: Optional[BaseClient] = None) -> None:
    """client can be None (default value)."""
    pass
```

### Generic Types

```python
from typing import Dict, List, Any

def _build_params(self) -> Dict[str, Union[str, int]]:
    """Return dict with string keys, string/int values."""
    pass

def fetch(self) -> List[PlayerInfo]:
    """Return list of PlayerInfo objects."""
    pass
```

## Testing Patterns

See [TESTING.md](TESTING.md) for detailed testing patterns.

### Key Principles

1. **Mock the NBA API** - Don't make real requests in tests
2. **Test both sync and async** - Both code paths must work
3. **Test error cases** - Timeouts, validation errors, etc.
4. **Use fixtures** - Reusable test data

## Design Principles

### SOLID Principles

#### Single Responsibility
Each class has one job:
- `BaseClient`: HTTP communication
- `PlayerListEndpoint`: Player list fetching
- `PlayerInfo`: Player data representation

#### Open/Closed
New endpoints extend the pattern without modifying existing code.

#### Liskov Substitution
All endpoints follow the same interface pattern.

#### Interface Segregation
Endpoints only expose `fetch()` and `fetch_async()`.

#### Dependency Inversion
Endpoints depend on `BaseClient` abstraction, not implementation.

### DRY (Don't Repeat Yourself)

- Base models share configuration via `BaseNBAModel`
- Response parsing logic in `parse_nba_response()`
- Retry/rate-limit logic in `BaseClient`

### Explicit Over Implicit

```python
# Bad (implicit)
def fetch(self, season="2024-25"):
    pass

# Good (explicit)
def fetch(self, season: Union[Season, str] = Season.CURRENT):
    pass
```

## Code Style

### Line Length

Max 100 characters (configured in pyproject.toml).

### Docstrings

Use Google style:

```python
def fetch(self, season: Season) -> List[PlayerInfo]:
    """Fetch player list for given season.

    Args:
        season: NBA season to query

    Returns:
        List of PlayerInfo objects

    Raises:
        TimeoutError: If request times out
        ValidationError: If response is invalid

    Example:
        >>> endpoint = PlayerListEndpoint()
        >>> players = endpoint.fetch(season=Season.CURRENT)
        >>> print(f"Found {len(players)} players")
    """
```

### Imports

Organize in three groups:
1. Standard library
2. Third-party
3. Local

```python
import asyncio
from typing import Dict, List

import httpx
from pydantic import BaseModel

from goldsberry.client.base import BaseClient
from goldsberry.models.player import PlayerInfo
```

## Future Patterns

**TODO**: Document as they emerge:
- [ ] Caching pattern
- [ ] Batch request pattern
- [ ] Plugin pattern for extensions
- [ ] Alternative backend pattern

---

**Last Updated**: 2025-11-06
**Author**: Bradley Fay
