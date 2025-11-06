#!/usr/bin/env python3
"""Basic usage examples for the modernized NBA API client.

Demonstrates:
- Simple synchronous usage
- Using enums for type safety
- Filtering and working with player data
- Custom client configuration
- Async usage (commented out due to NBA API reliability issues)
"""

import asyncio
from goldsberry.client.base import BaseClient
from goldsberry.client.exceptions import NBAAPIError, TimeoutError
from goldsberry.endpoints.player import PlayerListEndpoint, get_players
from goldsberry.enums.common import IsOnlyCurrentSeason, Season


def example_1_quick_start():
    """Example 1: Quickest way to fetch players."""
    print("=" * 80)
    print("Example 1: Quick Start")
    print("=" * 80)

    try:
        # Simplest usage: convenience function with defaults
        players = get_players(season=Season.CURRENT)

        print(f"✓ Found {len(players)} players for {Season.CURRENT.value} season\n")

        # Show first 5 active players
        print("First 5 players:")
        for player in players[:5]:
            print(f"  - {player}")

    except TimeoutError as e:
        print(f"✗ Request timed out: {e}")
        print("  (NBA API is known to be unreliable)")
    except NBAAPIError as e:
        print(f"✗ NBA API error: {e}")


def example_2_filtering():
    """Example 2: Filtering player data."""
    print("\n" + "=" * 80)
    print("Example 2: Filtering Players")
    print("=" * 80)

    try:
        # Get all active players
        players = get_players(
            season=Season.CURRENT,
            only_current_season=IsOnlyCurrentSeason.CURRENT_SEASON_ONLY
        )

        # Filter to only active players
        active_players = [p for p in players if p.is_active]
        print(f"✓ Found {len(active_players)} active players\n")

        # Group by team
        by_team = {}
        for player in active_players:
            team = player.team_abbreviation or "Free Agent"
            if team not in by_team:
                by_team[team] = []
            by_team[team].append(player)

        # Show teams with most players
        sorted_teams = sorted(by_team.items(), key=lambda x: len(x[1]), reverse=True)
        print("Teams with most players:")
        for team, team_players in sorted_teams[:5]:
            print(f"  {team}: {len(team_players)} players")

        # Find players by characteristics
        print("\nCenters 7ft or taller:")
        tall_centers = [
            p for p in active_players
            if p.position and 'C' in p.position
            and p.height and int(p.height.split('-')[0]) >= 7
        ]
        for player in tall_centers[:5]:
            print(f"  - {player.full_name} ({player.height}) - {player.team_abbreviation}")

    except NBAAPIError as e:
        print(f"✗ Error: {e}")


def example_3_custom_client():
    """Example 3: Using custom client configuration."""
    print("\n" + "=" * 80)
    print("Example 3: Custom Client Configuration")
    print("=" * 80)

    # Create client with custom settings
    # Longer timeout for unreliable NBA API
    # More retries
    client = BaseClient(
        timeout=60.0,  # 60 second timeout (default is 30)
        max_retries=5,  # More retries (default is 3)
        rate_limit_interval=1.0,  # More conservative rate limiting
    )

    try:
        # Use custom client
        endpoint = PlayerListEndpoint(client)
        players = endpoint.fetch(season="2023-24")  # Can use string directly

        print(f"✓ Fetched {len(players)} players with custom client\n")
        print("Client configuration:")
        print(f"  Timeout: {client.timeout}s")
        print(f"  Max retries: {client.max_retries}")
        print(f"  Rate limit: {client.rate_limiter.min_interval}s between requests")

    except NBAAPIError as e:
        print(f"✗ Error: {e}")
    finally:
        client.close()  # Important: cleanup


def example_4_error_handling():
    """Example 4: Robust error handling."""
    print("\n" + "=" * 80)
    print("Example 4: Error Handling")
    print("=" * 80)

    # Use context manager for automatic cleanup
    with BaseClient(timeout=10.0) as client:
        endpoint = PlayerListEndpoint(client)

        try:
            players = endpoint.fetch(season=Season.CURRENT)
            print(f"✓ Successfully fetched {len(players)} players")

        except TimeoutError as e:
            print(f"✗ Timeout Error:")
            print(f"  Message: {e.message}")
            print(f"  Timeout: {e.timeout}s")
            print(f"  Context: {e.context}")

        except NBAAPIError as e:
            print(f"✗ NBA API Error:")
            print(f"  Type: {type(e).__name__}")
            print(f"  Message: {e}")


def example_5_player_details():
    """Example 5: Exploring player details."""
    print("\n" + "=" * 80)
    print("Example 5: Player Details")
    print("=" * 80)

    try:
        players = get_players(season=Season.CURRENT)

        # Find specific players
        print("Searching for star players...\n")

        search_names = ["LeBron James", "Stephen Curry", "Nikola Jokic", "Luka Doncic"]

        for search_name in search_names:
            matches = [p for p in players if search_name.lower() in p.full_name.lower()]

            if matches:
                player = matches[0]
                print(f"{player.full_name}:")
                print(f"  ID: {player.person_id}")
                print(f"  Team: {player.team_abbreviation} - {player.team_name}")
                print(f"  Position: {player.position}")
                print(f"  Height/Weight: {player.height}, {player.weight} lbs")
                print(f"  From: {player.country}")
                print(f"  College: {player.college or 'N/A'}")
                print(f"  Draft: {player.draft_year} Round {player.draft_round}, Pick {player.draft_number}")
                print(f"  NBA 75th: {player.greatest_75_flag}")
                print(f"  Career: {player.from_year}-{player.to_year}")
                print()

    except NBAAPIError as e:
        print(f"✗ Error: {e}")


async def example_6_async_usage():
    """Example 6: Async/await usage (commented due to API reliability)."""
    print("\n" + "=" * 80)
    print("Example 6: Async Usage")
    print("=" * 80)

    # Async context manager
    async with BaseClient() as client:
        endpoint = PlayerListEndpoint(client)

        try:
            # Async fetch
            players = await endpoint.fetch_async(season=Season.CURRENT)
            print(f"✓ Async fetch: {len(players)} players")

            # You could make multiple concurrent requests
            # (Though be careful with rate limiting!)

        except NBAAPIError as e:
            print(f"✗ Error: {e}")


def main():
    """Run all examples."""
    print("\n" + "=" * 80)
    print("NBA API v2.0 - Basic Usage Examples")
    print("=" * 80)
    print("\nNOTE: Due to NBA API reliability issues, some examples may timeout.")
    print("This is a known issue affecting all NBA stats API clients.")
    print("The client will automatically retry with exponential backoff.\n")

    # Run synchronous examples
    example_1_quick_start()
    example_2_filtering()
    example_3_custom_client()
    example_4_error_handling()
    example_5_player_details()

    # Async example (commented out to keep example simple)
    # Uncomment if you want to try it:
    # print("\nRunning async example...")
    # asyncio.run(example_6_async_usage())

    print("\n" + "=" * 80)
    print("Examples Complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
