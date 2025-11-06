# py-Goldsberry

A Python package for easily acquiring NBA data for analysis

> **Note**: Version 2.0 is a complete rewrite with modern Python 3.9+, async support, and type safety. See [migration guide](docs/dev/MIGRATION.md) for upgrading from v1.x.

## What is py-Goldsberry?

`py-Goldsberry` is designed to give users easy access to data available from stats.nba.com in a form that facilitates innovative analysis. With a few simple commands, you can access virtually any data available on the site in an easy-to-analyze format.

## Why was it built?

I attended the 2015 Sloan Sports Analytics conference and had the fortunate opportunity to listen to [Kirk Goldsberry](http://twitter.com/kirkgoldsberry) address the crowd regarding the state of analytics in sports ([watch the talk](https://www.youtube.com/watch?v=wLf2hLHlFI8)). One of the questions he addressed was related to the availability of data (or lack thereof in some instances). He concluded that the lack of availability of some of the newest data is hindering the progression of analytics in sports. Innovation is now restricted to those with access to data instead of the entire community of interested parties. I wrote this package in an attempt to help address this issue.

**Note**: The NBA has masked some previously available tables. Shot-level and rebound-level log data is no longer accessible. This is disappointing as there was a multitude of research opportunities available. Hopefully, the NBA will make this data available again in the future.

## Installation

```bash
pip install py-goldsberry
```

## Quick Start (v2.0)

```python
from goldsberry.endpoints.player import get_players
from goldsberry.enums.common import Season

# Get current season players
players = get_players(season=Season.CURRENT)

# Filter active players
active_players = [p for p in players if p.is_active]

for player in active_players[:5]:
    print(f"{player.full_name} - {player.team_abbreviation}")
```

### Async Support

```python
from goldsberry.endpoints.player import get_players_async
from goldsberry.enums.common import Season

players = await get_players_async(season=Season.CURRENT)
```

### Custom Client Configuration

```python
from goldsberry.client.base import BaseClient
from goldsberry.endpoints.player import PlayerListEndpoint

# Configure timeout and retries for unreliable NBA API
with BaseClient(timeout=60, max_retries=5) as client:
    endpoint = PlayerListEndpoint(client)
    players = endpoint.fetch(season="2024-25")
```

## Features (v2.0)

- **Modern Python 3.9+**: Drop Python 2, embrace modern type hints
- **Async/Await Support**: Full async support with `httpx`
- **Type Safety**: Pydantic v2 models with full validation
- **Resilient Design**: Automatic retries, rate limiting, circuit breaker
- **Developer Experience**: IDE autocomplete, mypy strict mode compatible

## API Reliability

The NBA stats API (`stats.nba.com`) is inherently unreliable and experiences frequent timeouts. This is not specific to `py-goldsberry`, all NBA stat packages face these challenges. Version 2.0 includes aggressive retry logic and configurable timeouts to handle this.

See [docs/dev/API_STATUS.md](docs/dev/API_STATUS.md) for detailed research findings.

## Documentation

- [Architecture](docs/dev/ARCHITECTURE.md) - System design and components
- [Patterns](docs/dev/PATTERNS.md) - Coding patterns and conventions
- [Testing](docs/dev/TESTING.md) - Testing strategy and guidelines
- [Contributing](docs/dev/CONTRIBUTING.md) - How to contribute

## Status

**v2.0.0-alpha**: Core infrastructure complete. Currently supports:
- PlayerList endpoint (commonallplayers)
- Additional endpoints coming in future releases

## Credits

**Development Lead**: Bradley Fay (bradley.fay@gmail.com)

**Contributors**:
- [omermazig](https://github.com/omermazig)

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**TODO**: Update README with:
- [ ] Complete endpoint coverage list
- [ ] Migration guide link (once created)
- [ ] Badge for build status, coverage, PyPI version
- [ ] More comprehensive examples
