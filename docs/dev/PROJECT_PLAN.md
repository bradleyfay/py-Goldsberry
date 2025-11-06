# py-Goldsberry v2.0 Project Plan

> **Last Updated**: 2025-11-06
> **Status**: Phase 1 (Foundation) Complete, Beginning Phase 2 (Core Endpoints)

## Executive Summary

**Goal**: Modernize py-Goldsberry to v2.0 with Python 3.9+, async support, type safety, and resilient design for the unreliable NBA stats API.

**Current Status**: Foundation infrastructure 100% complete. 1 of 42 endpoints implemented (2.4%).

**Estimated Remaining Work**: ~100 hours to reach feature parity with v1.x

**Key Challenge**: NBA stats API is inherently unreliable (frequent timeouts, no official documentation, some endpoints blocked).

## Project Phases

### ✅ Phase 0: Research & Foundation (COMPLETE)

**Status**: 100% Complete
**Duration**: ~20 hours
**Completed**: 2025-11-06

#### Deliverables
- [x] NBA API research and validation (see [API_STATUS.md](API_STATUS.md))
- [x] Modern build system (pyproject.toml + uv)
- [x] HTTP client with retry logic, rate limiting, circuit breaker
- [x] Exception hierarchy
- [x] Pydantic v2 base models
- [x] Type-safe enums (21 common enums)
- [x] Testing infrastructure (pytest, fixtures, mocks)
- [x] Developer documentation (architecture, patterns, testing)
- [x] Hatch scripts for common tasks

#### Key Decisions
- Use httpx for async support
- Use Pydantic v2 for validation
- Use tenacity for retry logic
- Use src/ layout for modern packaging
- Mock NBA API in tests for reliability

### ✅ Phase 1: Proof of Concept (COMPLETE)

**Status**: 100% Complete
**Duration**: ~5 hours
**Completed**: 2025-11-06

#### Deliverables
- [x] PlayerList endpoint (commonallplayers) fully implemented
- [x] Complete test coverage (8 tests, sync + async)
- [x] Mock fixtures for deterministic testing
- [x] Usage examples demonstrating patterns
- [x] Documentation of patterns for future endpoints

#### Validation
- Pattern established and repeatable
- Tests pass reliably
- Package builds successfully
- Ready to scale to remaining endpoints

### 🚧 Phase 2: Core Endpoints (IN PROGRESS)

**Status**: 0% Complete (0 of 10 endpoints)
**Estimated Duration**: ~20 hours
**Target**: Tier 1 high-value endpoints

#### Endpoints to Implement

**Player Endpoints (3)**
1. **career_stats** - Player career statistics by season
   - Priority: HIGH (foundational for player analysis)
   - NBA API: `playercareerstats`
   - Estimated effort: 2 hours

2. **game_logs** - Game-by-game player statistics
   - Priority: HIGH (most requested feature)
   - NBA API: `playergamelogs`
   - Estimated effort: 2 hours

3. **shot_dashboard** - Player shooting statistics by zone
   - Priority: MEDIUM-HIGH (analytics use case)
   - NBA API: `playerdashboardbyshootingsplits`
   - Estimated effort: 2 hours

**Team Endpoints (3)**
4. **season_stats** - Team season statistics
   - Priority: HIGH (foundational for team analysis)
   - NBA API: `leaguedashteamstats`
   - Estimated effort: 2 hours

5. **game_logs** - Game-by-game team statistics
   - Priority: HIGH (common use case)
   - NBA API: `teamgamelogs`
   - Estimated effort: 2 hours

6. **roster** - Current team roster
   - Priority: MEDIUM-HIGH (roster management)
   - NBA API: `commonteamroster`
   - Estimated effort: 2 hours

**Game Endpoints (2)**
7. **boxscore_traditional** - Traditional box score stats
   - Priority: HIGH (most common game data)
   - NBA API: `boxscoretraditionalv2`
   - Estimated effort: 2 hours

8. **boxscore_advanced** - Advanced box score metrics
   - Priority: MEDIUM-HIGH (analytics)
   - NBA API: `boxscoreadvancedv2`
   - Estimated effort: 2 hours

**League Endpoints (2)**
9. **player_stats_classic** - League-wide player stats
   - Priority: HIGH (leaderboards, rankings)
   - NBA API: `leaguedashplayerstats`
   - Estimated effort: 2 hours

10. **team_stats_classic** - League-wide team stats
    - Priority: MEDIUM-HIGH (standings, rankings)
    - NBA API: `leaguedashteamstats`
    - Estimated effort: 2 hours

#### Success Criteria
- All 10 endpoints implemented following established pattern
- 100% test coverage per endpoint
- All tests passing
- Documentation updated
- Package builds successfully
- Ready for alpha release

### ❌ Phase 3: Extended Endpoints (TODO)

**Status**: Not Started
**Estimated Duration**: ~30 hours
**Target**: Tier 2 common analytics endpoints

**Scope**: 15 endpoints
- Player: passing_dashboard, defense_dashboard, rebound_dashboard
- Team: lineups, on_off_court, passing_dashboard, shot_dashboard
- Game: boxscore_misc, boxscore_scoring, boxscore_fourfactors, boxscore_usage, play_by_play
- League: lineups, playoff_picture

**Success Criteria**:
- All Tier 2 endpoints implemented
- Test coverage maintained
- Documentation current
- Examples added for key endpoints

### ❌ Phase 4: Advanced Analytics (TODO)

**Status**: Not Started
**Estimated Duration**: ~20 hours
**Target**: Tier 3 advanced analytics endpoints

**Scope**: 10 endpoints
- Player: shot_chart, demographics
- Team: splits, shooting_splits, year_by_year, team_info
- Game: boxscore_tracking
- League: franchise_history, hustle_stats (player/team)

**Success Criteria**:
- Advanced analytics endpoints available
- Complex data structures handled correctly
- Performance acceptable for large datasets

### ❌ Phase 5: Historical & Specialty Data (TODO)

**Status**: Not Started
**Estimated Duration**: ~25 hours
**Target**: Tier 4 historical/limited endpoints

**Scope**: 25 endpoints
- SportVU (9 endpoints, 2013-2015 only)
- PlayType (11 endpoints, 2015 only)
- Draft (5 endpoints)

**Note**: These endpoints have limited data availability. Clearly document limitations.

**Success Criteria**:
- Historical endpoints implemented where data available
- Limitations clearly documented
- Graceful error handling when data unavailable

### ❌ Phase 6: Polish & Release (TODO)

**Status**: Not Started
**Estimated Duration**: ~10 hours
**Target**: Production-ready release

#### Deliverables
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Multi-Python version testing (3.9, 3.10, 3.11, 3.12)
- [ ] Multi-OS testing (Linux, macOS, Windows)
- [ ] Coverage threshold enforcement (80%+)
- [ ] Migration guide from v1.x
- [ ] User documentation and tutorials
- [ ] Jupyter notebook examples (updated for v2.0)
- [ ] Release to PyPI
- [ ] GitHub release with notes

**Success Criteria**:
- All tests passing on all platforms
- Documentation complete
- PyPI release published
- Community feedback incorporated

## Dependencies & Sequencing

### Critical Path
```
Phase 0 (Foundation) → Phase 1 (POC) → Phase 2 (Core) → Phase 3 (Extended) → Phase 4 (Advanced) → Phase 5 (Historical) → Phase 6 (Release)
```

### Per-Endpoint Dependencies
Each endpoint requires:
1. Foundation complete (✅ done)
2. Pattern established (✅ done via PlayerList)
3. Research NBA API response structure
4. No dependencies between individual endpoints (can be parallelized)

### Documentation Dependencies
- Migration guide requires: Tier 1 + Tier 2 endpoints complete
- User guide can be written incrementally per endpoint
- API reference auto-generated from docstrings

## Risk Register

### 🔴 Critical Risks

#### 1. NBA API Reliability
**Impact**: HIGH | **Probability**: CERTAIN | **Status**: ONGOING

**Description**: stats.nba.com frequently times out. Not specific to py-goldsberry, affects all NBA stat packages.

**Mitigation**:
- ✅ Aggressive retry logic (exponential backoff)
- ✅ Circuit breaker pattern
- ✅ Configurable timeouts
- ✅ Clear error messages
- ✅ Mock fixtures for testing

**Impact on Project**: Users will experience failures regardless of implementation quality. Document clearly.

#### 2. Blocked Endpoints
**Impact**: MEDIUM | **Probability**: CERTAIN | **Status**: PERMANENT

**Description**: NBA has blocked 6 endpoints:
- Player: shot_log, rebound_log, general_splits
- Team: defense_dashboard
- League: daily_scoreboard, league_leaders

**Mitigation**:
- Document blocked endpoints clearly
- Return clear error messages if attempted
- Consider alternative data sources (future)

**Impact on Project**: v2.0 will have 6 fewer endpoints than v1.x (36 working vs 42 total).

### 🟡 Medium Risks

#### 3. Response Schema Changes
**Impact**: MEDIUM | **Probability**: LOW | **Status**: ONGOING

**Description**: NBA can change API response structure without notice.

**Mitigation**:
- ✅ Pydantic validation catches schema changes immediately
- ✅ `extra="ignore"` handles new fields gracefully
- Optional integration tests to detect live changes

**Impact on Project**: May require model updates, but graceful degradation prevents crashes.

#### 4. Authentication Changes
**Impact**: HIGH | **Probability**: LOW | **Status**: MONITORING

**Description**: NBA could add API key requirements.

**Mitigation**:
- ✅ BaseClient architecture supports future auth layer
- Monitor for authentication requirements

**Impact on Project**: Would require configuration management, but architecture supports it.

### 🟢 Low Risks

#### 5. Fixture Staleness
**Impact**: LOW | **Probability**: MEDIUM | **Status**: ACCEPTED

**Description**: Mock fixtures could become outdated.

**Mitigation**:
- Optional integration tests (not yet implemented)
- Periodic manual verification

**Impact on Project**: Tests pass but real API could fail. Acceptable for reliable tests.

## Time Estimates

### By Phase
- Phase 0 (Foundation): 20 hours ✅ COMPLETE
- Phase 1 (POC): 5 hours ✅ COMPLETE
- Phase 2 (Core): 20 hours 🚧 IN PROGRESS
- Phase 3 (Extended): 30 hours ❌ TODO
- Phase 4 (Advanced): 20 hours ❌ TODO
- Phase 5 (Historical): 25 hours ❌ TODO
- Phase 6 (Polish): 10 hours ❌ TODO

**Total**: ~130 hours (25 complete, 105 remaining)

### By Task Type
- Research per endpoint: 0.5 hours × 41 = 20.5 hours
- Implementation per endpoint: 1 hour × 41 = 41 hours
- Testing per endpoint: 0.5 hours × 41 = 20.5 hours
- Documentation: 15 hours
- CI/CD setup: 5 hours
- Polish & release: 5 hours

### Velocity Assumptions
- 1 endpoint = ~2 hours (research + implement + test)
- Pattern is established, should be repeatable
- Can parallelize if multiple contributors

## Success Metrics

### Phase 2 (Core)
- [ ] 10 core endpoints implemented
- [ ] 100% test coverage maintained
- [ ] Package builds without errors
- [ ] Ready for alpha.2 release

### Phase 6 (Release)
- [ ] 36+ working endpoints (blocked endpoints excluded)
- [ ] 80%+ overall test coverage
- [ ] Documentation complete
- [ ] CI passing on all platforms
- [ ] PyPI release published
- [ ] Migration guide complete

### Community Adoption
- [ ] 100+ GitHub stars (currently ~500 for v1.x)
- [ ] 10+ external contributors
- [ ] 1000+ PyPI downloads/month

## Decision Points

### Should we implement blocked endpoints?
**Decision**: NO

**Rationale**:
- NBA has permanently blocked 6 endpoints
- Implementing them adds code/test burden with no user value
- Better to document clearly and skip

**Exception**: If NBA unblocks, re-evaluate

### Should we support Python 3.8?
**Decision**: NO (Python 3.9+ only)

**Rationale**:
- Python 3.8 EOL October 2024
- Modern features in 3.9+ (PEP 585 type hints, etc.)
- Reduces compatibility burden

### Should we maintain v1.x compatibility?
**Decision**: NO (clean break for v2.0)

**Rationale**:
- API is fundamentally different (Pydantic models vs raw dicts)
- Package structure changed (src/ layout)
- Migration guide provides path forward
- Trying to maintain compat would compromise design

### Should we add caching?
**Decision**: DEFER to post-v2.0

**Rationale**:
- Adds complexity
- User can implement external cache if needed
- Focus on core functionality first

**Future**: Optional caching layer as enhancement

## Quick Start Guide (Resuming Work)

### For Next Session

1. **Check current status**:
   ```bash
   git status
   git log --oneline -5
   cat docs/dev/ENDPOINT_ROADMAP.md  # See what's next
   ```

2. **Pick next endpoint from Tier 1** (see [ENDPOINT_ROADMAP.md](ENDPOINT_ROADMAP.md))

3. **Follow implementation guide** (see [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md))

4. **Run quality checks**:
   ```bash
   hatch run test          # Run tests
   hatch run lint          # Check code quality
   hatch run type          # Type checking
   ```

5. **Update tracking**:
   - Mark endpoint complete in ENDPOINT_ROADMAP.md
   - Update CHANGELOG.md
   - Update this file (PROJECT_PLAN.md) if phase complete

### For New Contributors

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for setup
2. Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design
3. Read [PATTERNS.md](PATTERNS.md) for coding conventions
4. Follow [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) to add endpoints
5. Check [ENDPOINT_ROADMAP.md](ENDPOINT_ROADMAP.md) for available work

## References

- [Architecture](ARCHITECTURE.md) - System design
- [Patterns](PATTERNS.md) - Coding conventions
- [Testing Strategy](TESTING.md) - Test approach
- [API Status](API_STATUS.md) - NBA API research
- [Endpoint Roadmap](ENDPOINT_ROADMAP.md) - Detailed endpoint tracking
- [Implementation Guide](IMPLEMENTATION_GUIDE.md) - Step-by-step guide
- [Decisions](DECISIONS.md) - Architecture decision records
- [Contributing](CONTRIBUTING.md) - Contributor guide
- [Migration Guide](MIGRATION.md) - v1.x to v2.0 (TODO)

---

**Maintained by**: Bradley Fay (bradley.fay@gmail.com)
**Last Updated**: 2025-11-06
