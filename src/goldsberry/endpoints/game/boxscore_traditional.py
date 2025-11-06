"""BoxscoreTraditional endpoint - fetch traditional boxscore statistics for a game."""

from typing import Optional

from ...client.base import BaseClient
from ...models.game import BoxscoreTraditional, PlayerBoxscoreTraditional, TeamBoxscoreTraditional


class BoxscoreTraditionalEndpoint:
    """Fetch traditional boxscore statistics for a specific game.

    Provides access to the boxscoretraditionalv2 endpoint which returns
    player and team statistics for a game.

    Example:
        >>> # Synchronous usage
        >>> endpoint = BoxscoreTraditionalEndpoint()
        >>> boxscore = endpoint.fetch(game_id="0022400001")
        >>> print(f"Players: {len(boxscore.player_stats)}, Teams: {len(boxscore.team_stats)}")
        >>> top_scorers = boxscore.get_top_scorers(limit=3)
        >>> for player in top_scorers:
        ...     print(f"{player.player_name}: {player.points} PTS")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = BoxscoreTraditionalEndpoint(client)
        ...     boxscore = await endpoint.fetch_async(game_id="0022400001")

        >>> # Filter by team
        >>> team_players = boxscore.get_team_players(team_id=1610612738)
        >>> starters = boxscore.get_starters(team_id=1610612738)
    """

    ENDPOINT = "boxscoretraditionalv2"  # NBA API endpoint name

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
        game_id: str,
        start_period: int = 1,
        end_period: int = 10,
        start_range: int = 0,
        end_range: int = 28800,
        range_type: int = 2,
    ) -> dict[str, str | int]:
        """Build query parameters for API request.

        Args:
            game_id: NBA game ID (e.g., "0022400001")
            start_period: Starting period (default: 1)
            end_period: Ending period (default: 10)
            start_range: Start range in seconds (default: 0)
            end_range: End range in seconds (default: 28800 = 8 hours)
            range_type: Range type (default: 2)

        Returns:
            Dict of query parameters
        """
        return {
            "GameID": game_id,
            "StartPeriod": start_period,
            "EndPeriod": end_period,
            "StartRange": start_range,
            "EndRange": end_range,
            "RangeType": range_type,
        }

    def _parse_response(self, data: dict) -> BoxscoreTraditional:
        """Parse NBA API response into BoxscoreTraditional model.

        Args:
            data: Raw API response

        Returns:
            BoxscoreTraditional with player and team stats
        """
        result_sets = data.get("resultSets", [])
        if not result_sets:
            return BoxscoreTraditional(player_stats=[], team_stats=[])

        # The first result set contains player stats
        player_stats = []
        if len(result_sets) > 0:
            player_data = result_sets[0]
            headers = player_data.get("headers", [])
            rows = player_data.get("rowSet", [])

            for row in rows:
                player_dict = dict(zip(headers, row))
                player_stats.append(PlayerBoxscoreTraditional(**player_dict))

        # The second result set contains team stats
        team_stats = []
        if len(result_sets) > 1:
            team_data = result_sets[1]
            headers = team_data.get("headers", [])
            rows = team_data.get("rowSet", [])

            for row in rows:
                team_dict = dict(zip(headers, row))
                team_stats.append(TeamBoxscoreTraditional(**team_dict))

        return BoxscoreTraditional(player_stats=player_stats, team_stats=team_stats)

    def fetch(
        self,
        game_id: str,
        start_period: int = 1,
        end_period: int = 10,
        start_range: int = 0,
        end_range: int = 28800,
        range_type: int = 2,
    ) -> BoxscoreTraditional:
        """Fetch traditional boxscore (synchronous).

        Args:
            game_id: NBA game ID (e.g., "0022400001")
            start_period: Starting period (default: 1)
            end_period: Ending period (default: 10)
            start_range: Start range in seconds (default: 0)
            end_range: End range in seconds (default: 28800)
            range_type: Range type (default: 2)

        Returns:
            BoxscoreTraditional with player and team stats

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = BoxscoreTraditionalEndpoint()
            >>> boxscore = endpoint.fetch(game_id="0022400001")
            >>> print(f"Players: {len(boxscore.player_stats)}")
            >>> top_scorers = boxscore.get_top_scorers(limit=5)
        """
        params = self._build_params(
            game_id=game_id,
            start_period=start_period,
            end_period=end_period,
            start_range=start_range,
            end_range=end_range,
            range_type=range_type,
        )
        data = self.client.get(self.ENDPOINT, params=params)
        return self._parse_response(data)

    async def fetch_async(
        self,
        game_id: str,
        start_period: int = 1,
        end_period: int = 10,
        start_range: int = 0,
        end_range: int = 28800,
        range_type: int = 2,
    ) -> BoxscoreTraditional:
        """Fetch traditional boxscore (asynchronous).

        Args:
            game_id: NBA game ID (e.g., "0022400001")
            start_period: Starting period (default: 1)
            end_period: Ending period (default: 10)
            start_range: Start range in seconds (default: 0)
            end_range: End range in seconds (default: 28800)
            range_type: Range type (default: 2)

        Returns:
            BoxscoreTraditional with player and team stats

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = BoxscoreTraditionalEndpoint(client)
            ...     boxscore = await endpoint.fetch_async(game_id="0022400001")
        """
        params = self._build_params(
            game_id=game_id,
            start_period=start_period,
            end_period=end_period,
            start_range=start_range,
            end_range=end_range,
            range_type=range_type,
        )
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return self._parse_response(data)


def get_boxscore_traditional(
    game_id: str,
    start_period: int = 1,
    end_period: int = 10,
    start_range: int = 0,
    end_range: int = 28800,
    range_type: int = 2,
) -> BoxscoreTraditional:
    """Convenience function to fetch traditional boxscore.

    Args:
        game_id: NBA game ID (e.g., "0022400001")
        start_period: Starting period (default: 1)
        end_period: Ending period (default: 10)
        start_range: Start range in seconds (default: 0)
        end_range: End range in seconds (default: 28800)
        range_type: Range type (default: 2)

    Returns:
        BoxscoreTraditional with player and team stats

    Example:
        >>> from goldsberry.endpoints.game import get_boxscore_traditional
        >>> boxscore = get_boxscore_traditional(game_id="0022400001")
        >>> for player in boxscore.get_top_scorers(limit=5):
        ...     print(f"{player.player_name}: {player.points} PTS")
    """
    endpoint = BoxscoreTraditionalEndpoint()
    return endpoint.fetch(
        game_id=game_id,
        start_period=start_period,
        end_period=end_period,
        start_range=start_range,
        end_range=end_range,
        range_type=range_type,
    )


__all__ = ["BoxscoreTraditionalEndpoint", "get_boxscore_traditional"]
