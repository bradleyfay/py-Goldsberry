"""TeamGameLogs endpoint - fetch game-by-game team statistics."""

from typing import Optional

from ...client.base import BaseClient
from ...enums.common import LeagueID, Season, SeasonType
from ...models.team import TeamGameLog, TeamGameLogs


class TeamGameLogsEndpoint:
    """Fetch game-by-game team statistics.

    Provides access to the teamgamelog endpoint which returns
    game-by-game statistics for a specific team across a season.

    Example:
        >>> # Synchronous usage
        >>> endpoint = TeamGameLogsEndpoint()
        >>> logs = endpoint.fetch(team_id=1610612738, season="2024-25")  # Celtics
        >>> print(f"Record: {logs.record}")
        >>> for game in logs.filter_wins()[:5]:
        ...     print(f"{game.game_date}: {game.matchup} - {game.points} pts")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = TeamGameLogsEndpoint(client)
        ...     logs = await endpoint.fetch_async(team_id=1610612738, season="2024-25")

        >>> # Calculate totals
        >>> totals = logs.calculate_totals()
        >>> print(f"Total points: {totals['points']}")
    """

    ENDPOINT = "teamgamelog"  # NBA API endpoint name

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
        season: str | Season = Season.CURRENT,
        season_type: str | SeasonType = SeasonType.REGULAR_SEASON,
        league_id: str | LeagueID = LeagueID.NBA,
    ) -> dict[str, str | int]:
        """Build query parameters for API request.

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            season_type: Type of season (Regular Season, Playoffs, etc.)
            league_id: League identifier (default: NBA)

        Returns:
            Dict of query parameters
        """
        # Convert enums to values (handle both enum and string)
        season_value = season.value if isinstance(season, Season) else season
        season_type_value = (
            season_type.value if isinstance(season_type, SeasonType) else season_type
        )
        league_id_value = league_id.value if isinstance(league_id, LeagueID) else league_id

        return {
            "TeamID": team_id,
            "Season": season_value,
            "SeasonType": season_type_value,
            "LeagueID": league_id_value,
        }

    def _parse_response(self, data: dict) -> TeamGameLogs:
        """Parse NBA API response into TeamGameLogs model.

        Args:
            data: Raw API response

        Returns:
            TeamGameLogs with list of game statistics
        """
        result_sets = data.get("resultSets", [])
        if not result_sets:
            return TeamGameLogs(games=[])

        # The first result set contains the game logs
        game_data = result_sets[0]
        headers = game_data.get("headers", [])
        rows = game_data.get("rowSet", [])

        # Convert rows to list of dicts
        games = []
        for row in rows:
            game_dict = dict(zip(headers, row))
            games.append(TeamGameLog(**game_dict))

        return TeamGameLogs(games=games)

    def fetch(
        self,
        team_id: int,
        season: str | Season = Season.CURRENT,
        season_type: str | SeasonType = SeasonType.REGULAR_SEASON,
        league_id: str | LeagueID = LeagueID.NBA,
    ) -> TeamGameLogs:
        """Fetch team game logs (synchronous).

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            season_type: Type of season
            league_id: League identifier

        Returns:
            TeamGameLogs with game-by-game statistics

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = TeamGameLogsEndpoint()
            >>> logs = endpoint.fetch(team_id=1610612738, season="2024-25")
            >>> print(f"Record: {logs.record}")
            >>> print(f"Games: {len(logs.games)}")
        """
        params = self._build_params(
            team_id=team_id,
            season=season,
            season_type=season_type,
            league_id=league_id,
        )
        data = self.client.get(self.ENDPOINT, params=params)
        return self._parse_response(data)

    async def fetch_async(
        self,
        team_id: int,
        season: str | Season = Season.CURRENT,
        season_type: str | SeasonType = SeasonType.REGULAR_SEASON,
        league_id: str | LeagueID = LeagueID.NBA,
    ) -> TeamGameLogs:
        """Fetch team game logs (asynchronous).

        Args:
            team_id: NBA team ID
            season: NBA season (e.g., "2024-25")
            season_type: Type of season
            league_id: League identifier

        Returns:
            TeamGameLogs with game-by-game statistics

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = TeamGameLogsEndpoint(client)
            ...     logs = await endpoint.fetch_async(team_id=1610612738)
        """
        params = self._build_params(
            team_id=team_id,
            season=season,
            season_type=season_type,
            league_id=league_id,
        )
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return self._parse_response(data)


def get_team_game_logs(
    team_id: int,
    season: str | Season = Season.CURRENT,
    season_type: str | SeasonType = SeasonType.REGULAR_SEASON,
    league_id: str | LeagueID = LeagueID.NBA,
) -> TeamGameLogs:
    """Convenience function to fetch team game logs.

    Args:
        team_id: NBA team ID
        season: NBA season (e.g., "2024-25")
        season_type: Type of season
        league_id: League identifier

    Returns:
        TeamGameLogs with game-by-game statistics

    Example:
        >>> from goldsberry.endpoints.team import get_team_game_logs
        >>> logs = get_team_game_logs(team_id=1610612738, season="2024-25")
        >>> print(f"Record: {logs.record}")
        >>> for game in logs.games[:5]:
        ...     print(f"{game.game_date}: {game.points} pts")
    """
    endpoint = TeamGameLogsEndpoint()
    return endpoint.fetch(
        team_id=team_id,
        season=season,
        season_type=season_type,
        league_id=league_id,
    )


__all__ = ["TeamGameLogsEndpoint", "get_team_game_logs"]
