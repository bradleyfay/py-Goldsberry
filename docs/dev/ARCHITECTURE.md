# Architecture

This document describes the architectural design of py-Goldsberry v2.0.

## Design Philosophy

py-Goldsberry v2.0 is built around three core principles:

1. **Resilience**: The NBA stats API is unreliable. Our architecture assumes failure and handles it gracefully.
2. **Type Safety**: Full type hints and Pydantic validation catch errors at development time.
3. **Developer Experience**: Modern Python patterns, async support, and clear error messages.

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         User Code                            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Endpoint Layer                            │
│  (PlayerListEndpoint, convenience functions)                 │
│  - Parameter validation via enums                            │
│  - Response parsing to Pydantic models                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                     Model Layer                              │
│  (Pydantic v2 models)                                        │
│  - Type validation                                           │
│  - Field aliases (NBA_API_NAME → pythonic_name)             │
│  - Computed properties                                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    HTTP Client Layer                         │
│  (BaseClient)                                                │
│  - Retry logic (exponential backoff via tenacity)           │
│  - Rate limiting (token bucket algorithm)                   │
│  - Circuit breaker (avoid hammering broken endpoints)       │
│  - Timeout management                                        │
│  - Sync + Async support (httpx)                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   NBA Stats API                              │
│              (stats.nba.com/stats/*)                         │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. HTTP Client Layer (`src/goldsberry/client/`)

**Purpose**: Provide a resilient, type-safe HTTP client for the unreliable NBA API.

#### BaseClient (`client/base.py`)

The core HTTP client that handles all communication with stats.nba.com.

**Key Features**:
- **Sync and Async**: Uses `httpx` for both `client.get()` and `await client.get_async()`
- **Automatic Retries**: Configured via `tenacity` with exponential backoff
  - Default: 3 retries, 2x backoff, up to 10s wait
  - Retries on: timeouts, 5xx errors, connection errors
- **Rate Limiting**: Token bucket algorithm ensures minimum interval between requests
  - Default: 0.6s between requests (configurable)
  - Prevents overwhelming the API
- **Circuit Breaker**: Tracks consecutive failures per endpoint
  - After N failures, temporarily stops requests to that endpoint
  - Prevents wasting time on broken endpoints
- **Context Manager**: Proper resource cleanup with `with` statement

**Configuration**:
```python
client = BaseClient(
    timeout=30.0,           # Request timeout in seconds
    max_retries=3,          # Number of retry attempts
    rate_limit_interval=0.6 # Minimum seconds between requests
)
```

#### Exception Hierarchy (`client/exceptions.py`)

Structured exceptions for clear error handling:

```
NBAAPIError (base)
├── HTTPError
│   ├── TimeoutError
│   ├── RateLimitError
│   └── ServerError
├── ValidationError
└── EndpointNotFoundError
```

Each exception includes:
- `.message`: Human-readable description
- `.context`: Dict with request details
- `.original_error`: Underlying exception (if any)

### 2. Model Layer (`src/goldsberry/models/`)

**Purpose**: Type-safe, validated representations of NBA API responses.

#### Base Model (`models/base.py`)

All models inherit from `BaseNBAModel`:
```python
class BaseNBAModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True # Validate on field updates
    )
```

**Key Features**:
- **Field Aliases**: Map `PERSON_ID` → `person_id`
- **Computed Properties**: Derived fields (e.g., `full_name` from first/last)
- **Validation**: Pydantic v2 validation on instantiation

#### Response Parser (`models/base.py`)

`parse_nba_response()` function:
1. Extracts `resultSets` from NBA API response
2. Maps column headers to data rows
3. Instantiates Pydantic models
4. Returns list of validated objects

**NBA API Response Format**:
```json
{
  "resultSets": [{
    "name": "CommonAllPlayers",
    "headers": ["PERSON_ID", "DISPLAY_FIRST_LAST", ...],
    "rowSet": [
      [203999, "Nikola Jokic", ...],
      [2544, "LeBron James", ...]
    ]
  }]
}
```

### 3. Endpoint Layer (`src/goldsberry/endpoints/`)

**Purpose**: High-level interfaces for specific NBA API endpoints.

#### Endpoint Pattern

Each endpoint follows this structure:

```python
class PlayerListEndpoint:
    ENDPOINT = "commonallplayers"  # NBA API endpoint name

    def __init__(self, client: Optional[BaseClient] = None):
        """Initialize with optional client (creates default if None)"""

    def _build_params(self, **kwargs) -> Dict[str, Any]:
        """Convert Python args to NBA API parameters"""

    def fetch(self, **kwargs) -> List[Model]:
        """Synchronous fetch"""

    async def fetch_async(self, **kwargs) -> List[Model]:
        """Asynchronous fetch"""
```

**Convenience Functions**:
```python
def get_players(**kwargs) -> List[PlayerInfo]:
    """Quick access without manual client/endpoint creation"""
```

### 4. Enum Layer (`src/goldsberry/enums/`)

**Purpose**: Type-safe parameter values with IDE autocomplete.

**Example**:
```python
class Season(str, Enum):
    CURRENT = "2024-25"
    SEASON_2023_24 = "2023-24"
    # ... more seasons
```

**Benefits**:
- IDE autocomplete
- Type checking catches invalid values
- Self-documenting code

## Data Flow

### Synchronous Request

```
User calls get_players(season=Season.CURRENT)
         ↓
Endpoint._build_params() converts to {"Season": "2024-25", ...}
         ↓
BaseClient.get() with retry/rate-limit logic
         ↓
HTTP GET to stats.nba.com/stats/commonallplayers
         ↓
Response JSON → parse_nba_response()
         ↓
List[PlayerInfo] returned to user
```

### Asynchronous Request

Same flow, but uses:
- `await endpoint.fetch_async()`
- `await client.get_async()`
- httpx async client

## Design Decisions

### Why httpx over requests?

- Native async/await support
- Connection pooling
- HTTP/2 support
- Better timeout handling
- Active maintenance

### Why Pydantic v2?

- 5-50x faster than v1
- Better validation errors
- Native Python type hint support
- Strong ecosystem

### Why tenacity over retrying?

- More flexible retry strategies
- Better async support
- Active maintenance
- Clear API

### Why src/ layout?

- Prevents accidental imports from development code
- Clearer separation of package vs tests
- Modern Python packaging best practice

## Testing Strategy

See [TESTING.md](TESTING.md) for detailed testing approach.

**Key Points**:
- Mock fixtures prevent flaky tests from unreliable API
- Test both sync and async code paths
- Validate error handling and edge cases
- 100% coverage on implemented endpoints

## Performance Considerations

### Rate Limiting

Default 0.6s between requests balances:
- Not overwhelming NBA servers
- Reasonable performance for bulk operations
- Configurable for specific needs

### Connection Pooling

httpx maintains connection pool:
- Reuses TCP connections
- Reduces latency on subsequent requests
- Automatically managed by client

### Memory

Pydantic models use `__slots__` for memory efficiency on large datasets.

## Extensibility

### Adding New Endpoints

1. Create model in `src/goldsberry/models/{category}/{endpoint}.py`
2. Create endpoint in `src/goldsberry/endpoints/{category}/{endpoint}.py`
3. Add tests in `tests/unit/test_{endpoint}.py`
4. Add fixture in `tests/fixtures/{category}/{endpoint}_response.json`

See [PATTERNS.md](PATTERNS.md) for detailed patterns and examples.

## Security Considerations

### No Authentication Required

Currently, NBA stats API requires no authentication. If this changes:
- Add authentication layer to BaseClient
- Support for API keys, OAuth, etc.

### User-Agent Spoofing

Required to avoid NBA API blocking. We mimic a real browser:
```python
headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Accept": "application/json",
    # ...
}
```

### Rate Limiting

Built-in rate limiting respects NBA's infrastructure and reduces risk of being blocked.

## Future Architecture

### Planned Enhancements

**TODO**: Document these as they're implemented:
- [ ] Caching layer (optional, for reducing API calls)
- [ ] Batch request support (multiple endpoints in parallel)
- [ ] Plugin system for custom endpoints
- [ ] Alternative backend adapters (if NBA changes API)
- [ ] GraphQL support (if NBA moves to GraphQL)

---

**Last Updated**: 2025-11-06
**Author**: Bradley Fay
