"""GameLogs endpoint - fetch player game-by-game statistics."""

from typing import Optional, Union

from ...client.base import BaseClient
from ...enums.common import Season, SeasonType
from ...models.base import parse_nba_response
from ...models.player import GameLog


class GameLogsEndpoint:
    """Fetch player game-by-game statistics.

    Provides access to the playergamelog endpoint which returns
    game-by-game statistics for a player in a specific season.

    Example:
        >>> # Synchronous usage
        >>> endpoint = GameLogsEndpoint()
        >>> games = endpoint.fetch(player_id=203999, season="2024-25")
        >>> for game in games[:5]:
        ...     print(f"{game.game_date}: {game.points} PTS")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = GameLogsEndpoint(client)
        ...     games = await endpoint.fetch_async(player_id=203999)
    """

    ENDPOINT = "playergamelog"  # NBA API endpoint name

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
        player_id: int,
        season: Union[Season, str] = Season.CURRENT,
        season_type: SeasonType = SeasonType.REGULAR_SEASON,
    ) -> dict[str, str | int]:
        """Build query parameters for API request.

        Args:
            player_id: NBA player ID
            season: NBA season (e.g., "2024-25")
            season_type: Season type (Regular Season, Playoffs, etc.)

        Returns:
            Dict of query parameters
        """
        # Convert enums to values (handle both enum and string)
        season_value = season.value if isinstance(season, Season) else season
        season_type_value = (
            season_type.value if isinstance(season_type, SeasonType) else season_type
        )

        return {
            "PlayerID": player_id,
            "Season": season_value,
            "SeasonType": season_type_value,
        }

    def fetch(
        self,
        player_id: int,
        season: Union[Season, str] = Season.CURRENT,
        season_type: SeasonType = SeasonType.REGULAR_SEASON,
    ) -> list[GameLog]:
        """Fetch game logs (synchronous).

        Args:
            player_id: NBA player ID
            season: NBA season (default: current season)
            season_type: Season type (default: Regular Season)

        Returns:
            List of GameLog objects, one per game

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = GameLogsEndpoint()
            >>> games = endpoint.fetch(player_id=203999, season="2024-25")
            >>> print(f"Played {len(games)} games")
            >>> wins = [g for g in games if g.is_win]
            >>> print(f"Won {len(wins)} games")
        """
        params = self._build_params(player_id, season, season_type)
        data = self.client.get(self.ENDPOINT, params=params)
        return parse_nba_response(data, GameLog)

    async def fetch_async(
        self,
        player_id: int,
        season: Union[Season, str] = Season.CURRENT,
        season_type: SeasonType = SeasonType.REGULAR_SEASON,
    ) -> list[GameLog]:
        """Fetch game logs (asynchronous).

        Args:
            player_id: NBA player ID
            season: NBA season (default: current season)
            season_type: Season type (default: Regular Season)

        Returns:
            List of GameLog objects, one per game

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = GameLogsEndpoint(client)
            ...     games = await endpoint.fetch_async(player_id=203999)
            ...     total_points = sum(g.points for g in games)
        """
        params = self._build_params(player_id, season, season_type)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return parse_nba_response(data, GameLog)


# Convenience functions for quick access
def get_game_logs(
    player_id: int,
    season: Union[Season, str] = Season.CURRENT,
    season_type: SeasonType = SeasonType.REGULAR_SEASON,
    client: Optional[BaseClient] = None,
) -> list[GameLog]:
    """Convenience function to fetch player game logs.

    Args:
        player_id: NBA player ID
        season: NBA season (default: current)
        season_type: Season type (default: Regular Season)
        client: Optional client instance

    Returns:
        List of GameLog objects

    Example:
        >>> from goldsberry.endpoints.player import get_game_logs
        >>> games = get_game_logs(player_id=203999, season="2024-25")
        >>> for game in games[:5]:
        ...     print(f"{game.game_date}: {game.points} PTS")
    """
    endpoint = GameLogsEndpoint(client)
    return endpoint.fetch(player_id, season, season_type)


async def get_game_logs_async(
    player_id: int,
    season: Union[Season, str] = Season.CURRENT,
    season_type: SeasonType = SeasonType.REGULAR_SEASON,
    client: Optional[BaseClient] = None,
) -> list[GameLog]:
    """Async convenience function to fetch player game logs.

    Args:
        player_id: NBA player ID
        season: NBA season (default: current)
        season_type: Season type (default: Regular Season)
        client: Optional client instance

    Returns:
        List of GameLog objects

    Example:
        >>> from goldsberry.endpoints.player import get_game_logs_async
        >>> games = await get_game_logs_async(player_id=203999)
    """
    endpoint = GameLogsEndpoint(client)
    return await endpoint.fetch_async(player_id, season, season_type)


__all__ = ["GameLogsEndpoint", "get_game_logs", "get_game_logs_async"]
