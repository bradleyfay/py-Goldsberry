"""TeamRoster endpoint - fetch team roster including players and coaches."""

from typing import Optional, Union

from ...client.base import BaseClient
from ...enums.common import LeagueID, Season
from ...models.team import Coach, RosterPlayer, TeamRoster


class TeamRosterEndpoint:
    """Fetch team roster including players and coaching staff.

    Provides access to the commonteamroster endpoint which returns
    the current roster of players and coaches for a specific team.

    Example:
        >>> # Synchronous usage
        >>> endpoint = TeamRosterEndpoint()
        >>> roster = endpoint.fetch(team_id=1610612738, season="2024-25")  # Celtics
        >>> print(f"Players: {len(roster.players)}, Coaches: {len(roster.coaches)}")
        >>> print(f"Head Coach: {roster.head_coach}")
        >>> for player in roster.players[:5]:
        ...     print(f"{player.player_name} - {player.position}")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = TeamRosterEndpoint(client)
        ...     roster = await endpoint.fetch_async(team_id=1610612738)

        >>> # Find specific players
        >>> player = roster.get_player_by_name("Tatum")
        >>> guards = roster.get_players_by_position("G")
    """

    ENDPOINT = "commonteamroster"  # NBA API endpoint name

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
        team_id: int,
        season: Union[str, Season] = Season.CURRENT,
        league_id: Union[str, LeagueID] = LeagueID.NBA,
    ) -> dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            league_id: League identifier (default: NBA)

        Returns:
            Dict of query parameters
        """
        # Convert enums to values (handle both enum and string)
        season_value = season.value if isinstance(season, Season) else season
        league_id_value = league_id.value if isinstance(league_id, LeagueID) else league_id

        return {
            "TeamID": team_id,
            "Season": season_value,
            "LeagueID": league_id_value,
        }

    def _parse_response(self, data: dict) -> TeamRoster:
        """Parse NBA API response into TeamRoster model.

        Args:
            data: Raw API response

        Returns:
            TeamRoster with players and coaches
        """
        result_sets = data.get("resultSets", [])
        if not result_sets:
            return TeamRoster(players=[], coaches=[])

        # The first result set contains players
        players = []
        if len(result_sets) > 0:
            player_data = result_sets[0]
            headers = player_data.get("headers", [])
            rows = player_data.get("rowSet", [])

            for row in rows:
                player_dict = dict(zip(headers, row))
                players.append(RosterPlayer(**player_dict))

        # The second result set contains coaches
        coaches = []
        if len(result_sets) > 1:
            coach_data = result_sets[1]
            headers = coach_data.get("headers", [])
            rows = coach_data.get("rowSet", [])

            for row in rows:
                coach_dict = dict(zip(headers, row))
                coaches.append(Coach(**coach_dict))

        return TeamRoster(players=players, coaches=coaches)

    def fetch(
        self,
        team_id: int,
        season: Union[str, Season] = Season.CURRENT,
        league_id: Union[str, LeagueID] = LeagueID.NBA,
    ) -> TeamRoster:
        """Fetch team roster (synchronous).

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            league_id: League identifier

        Returns:
            TeamRoster with players and coaches

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = TeamRosterEndpoint()
            >>> roster = endpoint.fetch(team_id=1610612738, season="2024-25")
            >>> print(f"Players: {len(roster.players)}")
            >>> print(f"Head Coach: {roster.head_coach}")
        """
        params = self._build_params(
            team_id=team_id,
            season=season,
            league_id=league_id,
        )
        data = self.client.get(self.ENDPOINT, params=params)
        return self._parse_response(data)

    async def fetch_async(
        self,
        team_id: int,
        season: Union[str, Season] = Season.CURRENT,
        league_id: Union[str, LeagueID] = LeagueID.NBA,
    ) -> TeamRoster:
        """Fetch team roster (asynchronous).

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            league_id: League identifier

        Returns:
            TeamRoster with players and coaches

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = TeamRosterEndpoint(client)
            ...     roster = await endpoint.fetch_async(team_id=1610612738)
        """
        params = self._build_params(
            team_id=team_id,
            season=season,
            league_id=league_id,
        )
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return self._parse_response(data)


def get_team_roster(
    team_id: int,
    season: Union[str, Season] = Season.CURRENT,
    league_id: Union[str, LeagueID] = LeagueID.NBA,
) -> TeamRoster:
    """Convenience function to fetch team roster.

    Args:
        team_id: NBA team ID
        season: NBA season (e.g., "2024-25")
        league_id: League identifier

    Returns:
        TeamRoster with players and coaches

    Example:
        >>> from goldsberry.endpoints.team import get_team_roster
        >>> roster = get_team_roster(team_id=1610612738, season="2024-25")
        >>> for player in roster.players:
        ...     print(f"{player.player_name} - {player.position}")
    """
    endpoint = TeamRosterEndpoint()
    return endpoint.fetch(
        team_id=team_id,
        season=season,
        league_id=league_id,
    )


__all__ = ["TeamRosterEndpoint", "get_team_roster"]
