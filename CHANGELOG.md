# Changelog

All notable changes to py-Goldsberry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **LeagueTeamStats endpoint** (leaguedashteamstats) with league-wide team statistics, conference/division filtering, and sorting capabilities (Endpoint #10)
- **LeaguePlayerStats endpoint** (leaguedashplayerstats) with league-wide player statistics and filtering capabilities (Endpoint #9)
- **BoxscoreAdvanced endpoint** (boxscoreadvancedv2) with advanced metrics including offensive/defensive ratings, usage percentage, true shooting, PIE, and efficiency stats (Endpoint #8)
- **CareerStats endpoint** (playercareerstats) with season-by-season and career totals
- **GameLogs endpoint** (playergamelog) with game-by-game player statistics
- **TeamSeasonStats endpoint** (leaguedashteamstats) with league-wide team statistics
- **TeamGameLogs endpoint** (teamgamelog) with game-by-game team statistics
- **TeamRoster endpoint** (commonteamroster) with players and coaching staff
- **BoxscoreTraditional endpoint** (boxscoretraditionalv2) with player and team game statistics

### Changed
- Version metadata now read from package using `importlib.metadata` (single source of truth in pyproject.toml)

## [2.0.0-alpha.1] - 2025-11-06

### Added
- **Modern Python 3.9+ architecture** with type hints throughout
- **Async/await support** for all endpoints using `httpx`
- **Type safety** with Pydantic v2 models and comprehensive validation
- **Resilient HTTP client** with automatic retries, exponential backoff, and circuit breaker
- **Rate limiting** (configurable, default 0.6s between requests)
- **Comprehensive testing** infrastructure with pytest, mock fixtures
- **PlayerList endpoint** (commonallplayers) as first fully implemented endpoint
- **Usage examples** demonstrating sync, async, and custom client configuration
- **Developer documentation** structure (architecture, patterns, testing)
- Modern build system with `pyproject.toml` and `uv`
- Pre-commit hooks for code quality (ruff, black, mypy)

### Changed
- **BREAKING**: Dropped Python 2 support (now requires Python 3.9+)
- **BREAKING**: New package structure using `src/goldsberry/` layout
- **BREAKING**: New API with different class/function names (though similar concepts)
- **BREAKING**: Replaced `requests` with `httpx` for HTTP client
- **BREAKING**: All responses now use Pydantic models instead of raw dicts
- Upgraded to Pydantic v2 from v1
- HTTP base URLs changed from `http://` to `https://`

### Removed
- Python 2 compatibility layers
- Legacy `setup.py` and `setup.cfg` (consolidated to `pyproject.toml`)
- Makefile (replaced with hatch scripts)

### Fixed
- Improved handling of NBA API timeouts and reliability issues
- Better error messages distinguishing timeout vs API errors

### Known Issues
- NBA stats API is inherently unreliable with frequent timeouts (documented in API_STATUS.md)
- Some endpoints previously available are now blocked by NBA
- Only PlayerList endpoint implemented so far (41 more to come)

## [1.x] - Historical

Version 1.x history is not documented in this changelog. See git history for details on legacy releases.

---

**TODO**: Add as endpoints are implemented:
- Document each new endpoint addition
- Track breaking changes
- Document deprecations
- Add migration guides
