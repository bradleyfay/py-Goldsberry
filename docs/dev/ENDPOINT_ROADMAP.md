# Endpoint Implementation Roadmap

> **Last Updated**: 2025-11-06
> **Progress**: 3 of 42 endpoints complete (7.1%)

## Overview

This document tracks all 42 endpoints from the legacy v1.x package and their implementation status in v2.0.

**Legend**:
- ✅ Complete - Implemented, tested, documented
- 🚧 In Progress - Work started but not complete
- ❌ Not Started - No work done yet
- 🚫 Blocked - NBA API has blocked this endpoint (permanent)
- ⚠️ Limited - Data only available for specific seasons

## Progress by Category

| Category | Complete | In Progress | Not Started | Blocked | Total |
|----------|----------|-------------|-------------|---------|-------|
| Player   | 3        | 0           | 6           | 3       | 12    |
| Team     | 0        | 0           | 12          | 1       | 13    |
| Game     | 0        | 0           | 9           | 0       | 9     |
| League   | 0        | 0           | 6           | 2       | 8     |
| SportVU  | 0        | 0           | 9           | 0       | 9     |
| PlayType | 0        | 0           | 11          | 0       | 11    |
| Draft    | 0        | 0           | 5           | 0       | 5     |
| **Total**| **3**    | **0**       | **58**      | **6**   | **67**|

Note: Total is 67 because some endpoints appear in multiple categories or have variants.

## Tier 1: Core Endpoints (Priority: HIGH)

Must-have endpoints for basic functionality. Target for Phase 2.

### Player Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ✅ | PlayerList | commonallplayers | models/player/player_list.py | endpoints/player/player_list.py | test_player_list.py | HIGH | ✅ Complete |
| ✅ | career_stats | playercareerstats | models/player/career_stats.py | endpoints/player/career_stats.py | test_career_stats.py | HIGH | ✅ Complete |
| ✅ | game_logs | playergamelog | models/player/game_logs.py | endpoints/player/game_logs.py | test_game_logs.py | HIGH | ✅ Complete |
| ❌ | shot_dashboard | playerdashboardbyshootingsplits | - | - | - | MEDIUM | Shooting splits/zones |

### Team Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | season_stats | leaguedashteamstats | - | - | - | HIGH | Season team statistics |
| ❌ | game_logs | teamgamelogs | - | - | - | HIGH | Game-by-game team stats |
| ❌ | roster | commonteamroster | - | - | - | MEDIUM | Current team roster |

### Game Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | boxscore_traditional | boxscoretraditionalv2 | - | - | - | HIGH | Traditional box score |
| ❌ | boxscore_advanced | boxscoreadvancedv2 | - | - | - | MEDIUM | Advanced box score |

### League Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | player_stats_classic | leaguedashplayerstats | - | - | - | HIGH | League-wide player stats |
| ❌ | team_stats_classic | leaguedashteamstats | - | - | - | MEDIUM | League-wide team stats |

**Tier 1 Progress**: 3 of 10 complete (30%)

---

## Tier 2: Common Analytics (Priority: MEDIUM-HIGH)

Frequently used analytics endpoints. Target for Phase 3.

### Player Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | passing_dashboard | playerdashboardbypassing | - | - | - | MEDIUM | Passing statistics |
| ❌ | defense_dashboard | playerdashboardbydefense | - | - | - | MEDIUM | Defensive statistics |
| ❌ | rebound_dashboard | playerdashboardbyrebounding | - | - | - | MEDIUM | Rebounding statistics |

### Team Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | lineups | teamdashboardbylineups | - | - | - | MEDIUM | Lineup statistics |
| ❌ | on_off_court | teamplayeronoffdetails | - | - | - | MEDIUM | On/off court impact |
| ❌ | passing_dashboard | teamdashboardbypassing | - | - | - | MEDIUM | Team passing stats |
| ❌ | shot_dashboard | teamdashboardbyshootingsplits | - | - | - | MEDIUM | Team shooting splits |

### Game Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | boxscore_misc | boxscoremiscv2 | - | - | - | MEDIUM | Misc box score stats |
| ❌ | boxscore_scoring | boxscorescoringv2 | - | - | - | MEDIUM | Scoring box score |
| ❌ | boxscore_fourfactors | boxscorefourfactorsv2 | - | - | - | MEDIUM | Four factors stats |
| ❌ | boxscore_usage | boxscoreusagev2 | - | - | - | MEDIUM | Usage box score |
| ❌ | play_by_play | playbyplayv2 | - | - | - | MEDIUM | Play-by-play data |

### League Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | lineups | leaguedashlineups | - | - | - | MEDIUM | League lineup stats |
| ❌ | playoff_picture | playoffpicture | - | - | - | MEDIUM | Playoff standings |

**Tier 2 Progress**: 0 of 15 complete (0%)

---

## Tier 3: Advanced Analytics (Priority: MEDIUM)

Advanced analytics features. Target for Phase 4.

### Player Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | shot_chart | shotchartdetail | - | - | - | MEDIUM | Shot chart coordinates |
| ❌ | demographics | commonplayerinfo | - | - | - | LOW | Player biographical info |

### Team Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | splits | teamdashboardbygeneralsplits | - | - | - | MEDIUM | Team splits |
| ❌ | shooting_splits | teamdashboardbyshootingsplits | - | - | - | MEDIUM | Shooting splits |
| ❌ | year_by_year | teamyearbyyearstats | - | - | - | LOW | Historical team stats |
| ❌ | team_info | teaminfocommon | - | - | - | LOW | Team information |

### Game Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | boxscore_tracking | boxscoreplayertrackv2 | - | - | - | MEDIUM | Player tracking data |

### League Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | franchise_history | franchisehistory | - | - | - | LOW | Franchise history |
| ❌ | player_stats_hustle | leaguehustlestatsplayer | - | - | - | MEDIUM | Hustle stats (players) |
| ❌ | team_stats_hustle | leaguehustlestatsteam | - | - | - | MEDIUM | Hustle stats (teams) |

**Tier 3 Progress**: 0 of 10 complete (0%)

---

## Tier 4: Historical & Specialty (Priority: LOW)

Historical data with limited availability. Target for Phase 5.

### SportVU Endpoints ⚠️ (2013-2015 seasons only)

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | catch_and_shoot | playerdashptcatchshoot | - | - | - | LOW | Catch & shoot tracking |
| ❌ | defense | playerdashptdefense | - | - | - | LOW | Defensive tracking |
| ❌ | drives | playerdashptdrives | - | - | - | LOW | Drive tracking |
| ❌ | passing | playerdashptpass | - | - | - | LOW | Passing tracking |
| ❌ | touches | playerdashpttouches | - | - | - | LOW | Touch tracking |
| ❌ | pull_up_shooting | playerdashptpullup | - | - | - | LOW | Pull-up shot tracking |
| ❌ | rebounding | playerdashptreb | - | - | - | LOW | Rebound tracking |
| ❌ | shooting | playerdashptshots | - | - | - | LOW | Shot tracking |
| ❌ | speed | playerdashptspeed | - | - | - | LOW | Speed/distance tracking |

### PlayType Endpoints ⚠️ (2015 season only)

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | transition | synergyplaytypes (transition) | - | - | - | LOW | Transition plays |
| ❌ | isolation | synergyplaytypes (isolation) | - | - | - | LOW | Isolation plays |
| ❌ | pick_and_roll_bh | synergyplaytypes (pickandroll) | - | - | - | LOW | P&R ball handler |
| ❌ | pick_and_roll_man | synergyplaytypes (rollman) | - | - | - | LOW | P&R roll man |
| ❌ | postup | synergyplaytypes (postup) | - | - | - | LOW | Post-up plays |
| ❌ | spotup | synergyplaytypes (spotup) | - | - | - | LOW | Spot-up plays |
| ❌ | handoff | synergyplaytypes (handoff) | - | - | - | LOW | Handoff plays |
| ❌ | cut | synergyplaytypes (cut) | - | - | - | LOW | Cut plays |
| ❌ | offscreen | synergyplaytypes (offscreen) | - | - | - | LOW | Off-screen plays |
| ❌ | offrebound | synergyplaytypes (offrebound) | - | - | - | LOW | Off-rebound plays |
| ❌ | misc | synergyplaytypes (misc) | - | - | - | LOW | Miscellaneous plays |

### Draft Endpoints

| Status | Endpoint | NBA API | Model File | Endpoint File | Test File | Priority | Notes |
|--------|----------|---------|------------|---------------|-----------|----------|-------|
| ❌ | anthro | draftcombineplayeranthro | - | - | - | LOW | Anthropometric data |
| ❌ | agility | draftcombinedrillresults | - | - | - | LOW | Agility drills |
| ❌ | non_stationary_shooting | draftcombinenonstationaryshooting | - | - | - | LOW | Non-stationary shots |
| ❌ | spot_up_shooting | draftcombinespotup shooting | - | - | - | LOW | Spot-up shooting |
| ❌ | draft_history | drafthistory | - | - | - | LOW | Historical draft data |

**Tier 4 Progress**: 0 of 25 complete (0%)

---

## Blocked Endpoints 🚫 (Not Implementing)

These endpoints are permanently blocked by the NBA API. Do not implement.

### Player

| Endpoint | NBA API | Status | Notes |
|----------|---------|--------|-------|
| 🚫 shot_log | shotchartlineupdetail | BLOCKED | Shot-level log data unavailable |
| 🚫 rebound_log | reboundtracking | BLOCKED | Rebound-level log data unavailable |
| 🚫 general_splits | playerdashboardbygeneralsplits | BLOCKED | General splits unavailable |

### Team

| Endpoint | NBA API | Status | Notes |
|----------|---------|--------|-------|
| 🚫 defense_dashboard | teamdashboardbydefense | BLOCKED | Team defense dashboard unavailable |

### League

| Endpoint | NBA API | Status | Notes |
|----------|---------|--------|-------|
| 🚫 daily_scoreboard | scoreboardv2 | BLOCKED | Daily scoreboard unavailable |
| 🚫 league_leaders | leagueleaders | BLOCKED | League leaders unavailable |

**Total Blocked**: 6 endpoints

---

## Implementation Checklist Template

Use this checklist for each endpoint:

### Research Phase
- [ ] Identify NBA API endpoint name
- [ ] Capture live API response (save as fixture)
- [ ] Document required parameters
- [ ] Document optional parameters
- [ ] Note any special cases or gotchas

### Model Phase
- [ ] Create model file: `models/{category}/{endpoint}.py`
- [ ] Define Pydantic model with field aliases
- [ ] Add computed properties if needed
- [ ] Add `__str__` and `__repr__` methods
- [ ] Add type hints for all fields

### Endpoint Phase
- [ ] Create endpoint file: `endpoints/{category}/{endpoint}.py`
- [ ] Implement `__init__` with optional client
- [ ] Implement `_build_params` method
- [ ] Implement `fetch` method (sync)
- [ ] Implement `fetch_async` method (async)
- [ ] Add convenience function(s)
- [ ] Add comprehensive docstrings with examples

### Testing Phase
- [ ] Create test file: `tests/unit/test_{endpoint}.py`
- [ ] Add fixture loader
- [ ] Test model parsing
- [ ] Test parameter building
- [ ] Test synchronous fetch
- [ ] Test asynchronous fetch
- [ ] Test convenience function
- [ ] Test string representations
- [ ] Verify 100% coverage for this endpoint

### Documentation Phase
- [ ] Update ENDPOINT_ROADMAP.md (mark complete)
- [ ] Update CHANGELOG.md
- [ ] Add usage example to `examples/` if warranted
- [ ] Update README.md if Tier 1 endpoint

### Quality Gates
- [ ] All tests pass (`hatch run test`)
- [ ] Linting passes (`hatch run lint`)
- [ ] Type checking passes (`hatch run type`)
- [ ] Code formatted (`hatch run format`)
- [ ] Package builds (`uv build`)

---

## Quick Reference: Next 5 Endpoints

Based on priority, the next 5 endpoints to implement are:

1. **Player: career_stats** (HIGH priority)
   - NBA API: `playercareerstats`
   - Use case: Career statistics by season
   - Estimated effort: 2 hours

2. **Player: game_logs** (HIGH priority)
   - NBA API: `playergamelogs`
   - Use case: Game-by-game player statistics
   - Estimated effort: 2 hours

3. **Team: season_stats** (HIGH priority)
   - NBA API: `leaguedashteamstats`
   - Use case: Season team statistics
   - Estimated effort: 2 hours

4. **Team: game_logs** (HIGH priority)
   - NBA API: `teamgamelogs`
   - Use case: Game-by-game team statistics
   - Estimated effort: 2 hours

5. **Game: boxscore_traditional** (HIGH priority)
   - NBA API: `boxscoretraditionalv2`
   - Use case: Traditional box score stats
   - Estimated effort: 2 hours

**Total estimated effort for next 5**: ~10 hours

---

**Last Updated**: 2025-11-06
**Maintained by**: Bradley Fay (bradley.fay@gmail.com)
