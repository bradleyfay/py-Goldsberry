"""PlayerList endpoint - fetch all NBA players.

Endpoint: commonallplayers
Returns a list of all players in NBA history or current season.
"""

from typing import Dict, List, Optional, Union

from ...client.base import BaseClient
from ...enums.common import IsOnlyCurrentSeason, LeagueID, Season
from ...models.base import parse_nba_response
from ...models.player import PlayerInfo


class PlayerListEndpoint:
    """Fetch list of all NBA players.

    Provides access to the commonallplayers endpoint which returns
    basic information about all players, with optional filtering.

    Example:
        >>> # Synchronous usage
        >>> client = BaseClient()
        >>> endpoint = PlayerListEndpoint(client)
        >>> players = endpoint.fetch(season=Season.CURRENT)
        >>> print(f"Found {len(players)} players")
        >>> for player in players[:5]:
        ...     print(player.full_name, player.team_abbreviation)

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = PlayerListEndpoint(client)
        ...     players = await endpoint.fetch_async(season=Season.CURRENT)
        ...     print(f"Found {len(players)} players")

        >>> # Filter for current season only
        >>> active_players = endpoint.fetch(
        ...     season=Season.CURRENT,
        ...     only_current_season=IsOnlyCurrentSeason.CURRENT_SEASON_ONLY
        ... )
    """

    ENDPOINT = "commonallplayers"

    def __init__(self, client: Optional[BaseClient] = None) -> None:
        """Initialize endpoint.

        Args:
            client: HTTP client instance (creates default if not provided)
        """
        self.client = client or BaseClient()
        self._owns_client = client is None

    def __del__(self) -> None:
        """Cleanup client if we created it."""
        if self._owns_client and hasattr(self, "client"):
            self.client.close()

    def _build_params(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> Dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            season: NBA season (e.g., "2024-25")
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only

        Returns:
            Dict of query parameters
        """
        # Convert enums to values
        season_value = season.value if isinstance(season, Season) else season
        league_value = league_id.value if isinstance(league_id, LeagueID) else league_id
        only_current_value = (
            only_current_season.value
            if isinstance(only_current_season, IsOnlyCurrentSeason)
            else only_current_season
        )

        return {
            "LeagueID": league_value,
            "Season": season_value,
            "IsOnlyCurrentSeason": only_current_value,
        }

    def fetch(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> List[PlayerInfo]:
        """Fetch player list (synchronous).

        Args:
            season: NBA season (default: current season)
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only (default: yes)

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = PlayerListEndpoint()
            >>> current_players = endpoint.fetch(season="2024-25")
            >>> all_time = endpoint.fetch(
            ...     season="2024-25",
            ...     only_current_season=IsOnlyCurrentSeason.ALL_TIME
            ... )
        """
        params = self._build_params(season, league_id, only_current_season)
        data = self.client.get(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)

    async def fetch_async(
        self,
        season: Union[Season, str] = Season.CURRENT,
        league_id: LeagueID = LeagueID.NBA,
        only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    ) -> List[PlayerInfo]:
        """Fetch player list (asynchronous).

        Args:
            season: NBA season (default: current season)
            league_id: League identifier (default: NBA)
            only_current_season: Filter for current season only (default: yes)

        Returns:
            List of PlayerInfo objects

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = PlayerListEndpoint(client)
            ...     players = await endpoint.fetch_async(season="2024-25")
            ...     for player in players:
            ...         if player.is_active:
            ...             print(f"{player.full_name} - {player.team_abbreviation}")
        """
        params = self._build_params(season, league_id, only_current_season)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return parse_nba_response(data, PlayerInfo)


# Convenience function for quick access
def get_players(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Convenience function to fetch player list.

    Args:
        season: NBA season (default: current)
        league_id: League identifier (default: NBA)
        only_current_season: Filter for current season only (default: yes)
        client: Optional client instance

    Returns:
        List of PlayerInfo objects

    Example:
        >>> from goldsberry.endpoints.player import get_players
        >>> players = get_players(season="2024-25")
        >>> active = [p for p in players if p.is_active]
        >>> print(f"{len(active)} active players")
    """
    endpoint = PlayerListEndpoint(client)
    return endpoint.fetch(season, league_id, only_current_season)


async def get_players_async(
    season: Union[Season, str] = Season.CURRENT,
    league_id: LeagueID = LeagueID.NBA,
    only_current_season: IsOnlyCurrentSeason = IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    client: Optional[BaseClient] = None,
) -> List[PlayerInfo]:
    """Convenience async function to fetch player list.

    Args:
        season: NBA season (default: current)
        league_id: League identifier (default: NBA)
        only_current_season: Filter for current season only (default: yes)
        client: Optional client instance

    Returns:
        List of PlayerInfo objects

    Example:
        >>> from goldsberry.endpoints.player import get_players_async
        >>> players = await get_players_async(season="2024-25")
    """
    endpoint = PlayerListEndpoint(client)
    return await endpoint.fetch_async(season, league_id, only_current_season)


__all__ = ["PlayerListEndpoint", "get_players", "get_players_async"]
