#!/usr/bin/env python3
"""
API Validation Script for py-Goldsberry
Tests existing endpoints against live NBA API to determine which still work.
"""

import json
import sys
from pathlib import Path

# Add goldsberry to path
sys.path.insert(0, str(Path(__file__).parent))

import goldsberry.player._Player2 as player
import goldsberry.team._Team2 as team
import goldsberry.league._League2 as league
import goldsberry.game._Game2 as game

# Test parameters
SAMPLE_PLAYER_ID = 203999  # Nikola Jokic
SAMPLE_TEAM_ID = 1610612743  # Denver Nuggets
SAMPLE_GAME_ID = "0022300001"  # Sample game ID
CURRENT_SEASON = "2024-25"
PREVIOUS_SEASON = "2023-24"

def test_endpoint(name, test_func, category):
    """Test a single endpoint and return result"""
    print(f"Testing {category}/{name}...", end=" ")
    try:
        result = test_func()
        if result and len(result) > 0:
            print(f"✓ SUCCESS ({len(result)} records)")
            return {
                "name": name,
                "category": category,
                "status": "working",
                "record_count": len(result),
                "sample": result[0] if result else None
            }
        else:
            print(f"⚠ WARNING (empty response)")
            return {
                "name": name,
                "category": category,
                "status": "empty",
                "error": "No data returned"
            }
    except Exception as e:
        print(f"✗ FAILED: {str(e)[:100]}")
        return {
            "name": name,
            "category": category,
            "status": "failed",
            "error": str(e)[:200]
        }

def test_player_endpoints():
    """Test player endpoints"""
    results = []

    # Test demographics
    results.append(test_endpoint(
        "demographics",
        lambda: player.demographics(SAMPLE_PLAYER_ID).player_info(),
        "player"
    ))

    # Test career_stats
    results.append(test_endpoint(
        "career_stats",
        lambda: player.career_stats(SAMPLE_PLAYER_ID).season_totals_regular(),
        "player"
    ))

    # Test game_logs
    results.append(test_endpoint(
        "game_logs",
        lambda: player.game_logs(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).logs(),
        "player"
    ))

    # Test shot_dashboard
    results.append(test_endpoint(
        "shot_dashboard",
        lambda: player.shot_dashboard(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).overall(),
        "player"
    ))

    # Test rebound_dashboard
    results.append(test_endpoint(
        "rebound_dashboard",
        lambda: player.rebound_dashboard(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).overall(),
        "player"
    ))

    # Test passing_dashboard
    results.append(test_endpoint(
        "passing_dashboard",
        lambda: player.passing_dashboard(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).passes_made(),
        "player"
    ))

    # Test defense_dashboard
    results.append(test_endpoint(
        "defense_dashboard",
        lambda: player.defense_dashboard(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).defending_shot(),
        "player"
    ))

    # Test shot_chart
    results.append(test_endpoint(
        "shot_chart",
        lambda: player.shot_chart(SAMPLE_PLAYER_ID, Season=PREVIOUS_SEASON).chart(),
        "player"
    ))

    # Test PlayerList
    results.append(test_endpoint(
        "PlayerList",
        lambda: player.PlayerList(Season=CURRENT_SEASON).players(),
        "player"
    ))

    return results

def test_team_endpoints():
    """Test team endpoints"""
    results = []

    # Test game_logs
    results.append(test_endpoint(
        "game_logs",
        lambda: team.game_logs(SAMPLE_TEAM_ID, Season=PREVIOUS_SEASON).logs(),
        "team"
    ))

    # Test roster
    results.append(test_endpoint(
        "roster",
        lambda: team.roster(SAMPLE_TEAM_ID, Season=CURRENT_SEASON).players(),
        "team"
    ))

    # Test team_info
    results.append(test_endpoint(
        "team_info",
        lambda: team.team_info(SAMPLE_TEAM_ID).info_common(),
        "team"
    ))

    # Test year_by_year
    results.append(test_endpoint(
        "year_by_year",
        lambda: team.year_by_year(SAMPLE_TEAM_ID).stats(),
        "team"
    ))

    # Test season_stats
    results.append(test_endpoint(
        "season_stats",
        lambda: team.season_stats(SAMPLE_TEAM_ID, Season=PREVIOUS_SEASON).stats(),
        "team"
    ))

    # Test shot_dashboard
    results.append(test_endpoint(
        "shot_dashboard",
        lambda: team.shot_dashboard(SAMPLE_TEAM_ID, Season=PREVIOUS_SEASON).overall(),
        "team"
    ))

    # Test passing_dashboard
    results.append(test_endpoint(
        "passing_dashboard",
        lambda: team.passing_dashboard(SAMPLE_TEAM_ID, Season=PREVIOUS_SEASON).passes_made(),
        "team"
    ))

    # Test rebound_dashboard
    results.append(test_endpoint(
        "rebound_dashboard",
        lambda: team.rebound_dashboard(SAMPLE_TEAM_ID, Season=PREVIOUS_SEASON).overall(),
        "team"
    ))

    return results

def test_league_endpoints():
    """Test league endpoints"""
    results = []

    # Test team_stats
    results.append(test_endpoint(
        "team_stats_classic",
        lambda: league.team_stats(Season=PREVIOUS_SEASON).overall(),
        "league"
    ))

    # Test player_stats
    results.append(test_endpoint(
        "player_stats_classic",
        lambda: league.player_stats(Season=PREVIOUS_SEASON).overall()[:10],  # Limit to 10
        "league"
    ))

    # Test franchise_history
    results.append(test_endpoint(
        "franchise_history",
        lambda: league.franchise_history().active(),
        "league"
    ))

    # Test lineups
    results.append(test_endpoint(
        "lineups",
        lambda: league.lineups(Season=PREVIOUS_SEASON).overall()[:10],  # Limit to 10
        "league"
    ))

    return results

def test_game_endpoints():
    """Test game endpoints"""
    results = []

    # Test play_by_play
    results.append(test_endpoint(
        "play_by_play",
        lambda: game.play_by_play(SAMPLE_GAME_ID).plays(),
        "game"
    ))

    # Test boxscore_summary
    results.append(test_endpoint(
        "boxscore_summary",
        lambda: game.boxscore_summary(SAMPLE_GAME_ID).line_score(),
        "game"
    ))

    # Test boxscore_traditional
    results.append(test_endpoint(
        "boxscore_traditional",
        lambda: game.boxscore_traditional(SAMPLE_GAME_ID).player_stats(),
        "game"
    ))

    # Test boxscore_advanced
    results.append(test_endpoint(
        "boxscore_advanced",
        lambda: game.boxscore_advanced(SAMPLE_GAME_ID).player_stats(),
        "game"
    ))

    # Test GameIDs
    results.append(test_endpoint(
        "GameIDs",
        lambda: game.GameIDs().game_list()[:10],  # Limit to 10
        "game"
    ))

    return results

def main():
    """Run all endpoint tests and generate report"""
    print("=" * 80)
    print("NBA API Endpoint Validation")
    print("=" * 80)
    print()

    all_results = []

    print("\n" + "=" * 80)
    print("PLAYER ENDPOINTS")
    print("=" * 80)
    all_results.extend(test_player_endpoints())

    print("\n" + "=" * 80)
    print("TEAM ENDPOINTS")
    print("=" * 80)
    all_results.extend(test_team_endpoints())

    print("\n" + "=" * 80)
    print("LEAGUE ENDPOINTS")
    print("=" * 80)
    all_results.extend(test_league_endpoints())

    print("\n" + "=" * 80)
    print("GAME ENDPOINTS")
    print("=" * 80)
    all_results.extend(test_game_endpoints())

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    working = [r for r in all_results if r["status"] == "working"]
    empty = [r for r in all_results if r["status"] == "empty"]
    failed = [r for r in all_results if r["status"] == "failed"]

    print(f"\nTotal endpoints tested: {len(all_results)}")
    print(f"Working: {len(working)} ({len(working)/len(all_results)*100:.1f}%)")
    print(f"Empty response: {len(empty)} ({len(empty)/len(all_results)*100:.1f}%)")
    print(f"Failed: {len(failed)} ({len(failed)/len(all_results)*100:.1f}%)")

    if failed:
        print("\nFailed endpoints:")
        for r in failed:
            print(f"  - {r['category']}/{r['name']}: {r['error'][:80]}")

    # Save results
    output_file = Path("api_validation_results.json")
    with open(output_file, "w") as f:
        json.dump({
            "summary": {
                "total": len(all_results),
                "working": len(working),
                "empty": len(empty),
                "failed": len(failed)
            },
            "results": all_results
        }, f, indent=2)

    print(f"\nDetailed results saved to: {output_file}")

    return 0 if len(failed) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
