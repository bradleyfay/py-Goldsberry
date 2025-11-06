"""LeaguePlayerStats endpoint - fetch league-wide player statistics for a season."""

from typing import Optional, Union

from ...client.base import BaseClient
from ...enums.common import (
    LeagueID,
    Location,
    MeasureType,
    Month,
    Outcome,
    PaceAdjust,
    Period,
    PerMode,
    PlayerPosition,
    PlusMinus,
    Rank,
    Season,
    SeasonSegment,
    SeasonType,
    StarterBench,
)
from ...models.league import LeaguePlayerStats, PlayerStats


class LeaguePlayerStatsEndpoint:
    """Fetch league-wide player season statistics.

    Provides access to the leaguedashplayerstats endpoint which returns
    comprehensive player statistics for all qualifying players in a given season.

    Example:
        >>> # Synchronous usage
        >>> endpoint = LeaguePlayerStatsEndpoint()
        >>> stats = endpoint.fetch(season="2024-25")
        >>> for player in stats.get_top_scorers(5):
        ...     print(f"{player.player_name}: {player.points_per_game:.1f} PPG")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = LeaguePlayerStatsEndpoint(client)
        ...     stats = await endpoint.fetch_async(season="2024-25")

        >>> # Filter by measure type and per mode
        >>> stats = endpoint.fetch(
        ...     season="2024-25",
        ...     measure_type=MeasureType.ADVANCED,
        ...     per_mode=PerMode.PER_GAME
        ... )
    """

    ENDPOINT = "leaguedashplayerstats"  # NBA API endpoint name

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
        season: Union[str, Season] = Season.CURRENT,
        season_type: Union[str, SeasonType] = SeasonType.REGULAR_SEASON,
        per_mode: Union[str, PerMode] = PerMode.TOTALS,
        measure_type: Union[str, MeasureType] = MeasureType.BASE,
        league_id: Union[str, LeagueID] = LeagueID.NBA,
        pace_adjust: Union[str, PaceAdjust] = PaceAdjust.NO,
        plus_minus: Union[str, PlusMinus] = PlusMinus.NO,
        rank: Union[str, Rank] = Rank.NO,
        outcome: Union[str, Outcome] = Outcome.ALL,
        location: Union[str, Location] = Location.ALL,
        month: Union[int, Month] = Month.ALL,
        season_segment: Union[str, SeasonSegment] = SeasonSegment.ENTIRE_SEASON,
        period: Union[int, Period] = Period.ALL,
        last_n_games: int = 0,
        team_id: int = 0,
        opponent_team_id: int = 0,
        date_from: str = "",
        date_to: str = "",
        conference: str = "",
        division: str = "",
        po_round: int = 0,
        shot_clock_range: str = "",
        player_experience: str = "",
        player_position: Union[str, PlayerPosition] = PlayerPosition.ALL,
        starter_bench: Union[str, StarterBench] = StarterBench.ALL,
        game_scope: str = "",
        game_segment: str = "",
        height: str = "",
        draft_year: str = "",
        draft_pick: str = "",
        draft_round: str = "",
        college: str = "",
        country: str = "",
        weight: str = "",
        two_way: int = 0,
        vs_conference: str = "",
        vs_division: str = "",
    ) -> dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            season: NBA season (e.g., "2024-25")
            season_type: Type of season (Regular Season, Playoffs, etc.)
            per_mode: Statistics mode (Totals, PerGame, etc.)
            measure_type: Type of measurements (Base, Advanced, etc.)
            league_id: League identifier (default: NBA)
            pace_adjust: Pace adjustment flag
            plus_minus: Plus/minus flag
            rank: Ranking flag
            outcome: Game outcome filter (W, L, or all)
            location: Game location filter (Home, Road, or all)
            month: Month filter (0 for all months)
            season_segment: Season segment filter
            period: Game period filter (0 for all periods)
            last_n_games: Filter to last N games (0 for all)
            team_id: Specific team ID filter (0 for all teams)
            opponent_team_id: Opponent team ID filter (0 for all)
            date_from: Start date filter (YYYY-MM-DD or empty)
            date_to: End date filter (YYYY-MM-DD or empty)
            conference: Conference filter (East, West, or empty)
            division: Division filter (Atlantic, Central, etc. or empty)
            po_round: Playoff round filter (0 for all)
            shot_clock_range: Shot clock range filter
            player_experience: Player experience filter (Rookie, Sophomore, Veteran)
            player_position: Player position filter (G, F, C, etc.)
            starter_bench: Starter/bench filter
            game_scope: Game scope filter
            game_segment: Game segment filter
            height: Height filter
            draft_year: Draft year filter
            draft_pick: Draft pick filter
            draft_round: Draft round filter
            college: College filter
            country: Country filter
            weight: Weight filter
            two_way: Two-way player filter
            vs_conference: Versus conference filter
            vs_division: Versus division filter

        Returns:
            Dict of query parameters
        """
        # Convert enums to values (handle both enum and string)
        season_value = season.value if isinstance(season, Season) else season
        season_type_value = (
            season_type.value if isinstance(season_type, SeasonType) else season_type
        )
        per_mode_value = per_mode.value if isinstance(per_mode, PerMode) else per_mode
        measure_type_value = (
            measure_type.value if isinstance(measure_type, MeasureType) else measure_type
        )
        league_id_value = league_id.value if isinstance(league_id, LeagueID) else league_id
        pace_adjust_value = (
            pace_adjust.value if isinstance(pace_adjust, PaceAdjust) else pace_adjust
        )
        plus_minus_value = (
            plus_minus.value if isinstance(plus_minus, PlusMinus) else plus_minus
        )
        rank_value = rank.value if isinstance(rank, Rank) else rank
        outcome_value = outcome.value if isinstance(outcome, Outcome) else outcome
        location_value = location.value if isinstance(location, Location) else location
        month_value = month.value if isinstance(month, Month) else month
        season_segment_value = (
            season_segment.value
            if isinstance(season_segment, SeasonSegment)
            else season_segment
        )
        period_value = period.value if isinstance(period, Period) else period
        player_position_value = (
            player_position.value
            if isinstance(player_position, PlayerPosition)
            else player_position
        )
        starter_bench_value = (
            starter_bench.value if isinstance(starter_bench, StarterBench) else starter_bench
        )

        return {
            "College": college,
            "Conference": conference,
            "Country": country,
            "DateFrom": date_from,
            "DateTo": date_to,
            "Division": division,
            "DraftPick": draft_pick,
            "DraftRound": draft_round,
            "DraftYear": draft_year,
            "GameScope": game_scope,
            "GameSegment": game_segment,
            "Height": height,
            "LastNGames": last_n_games,
            "LeagueID": league_id_value,
            "Location": location_value,
            "MeasureType": measure_type_value,
            "Month": month_value,
            "OpponentTeamID": opponent_team_id,
            "Outcome": outcome_value,
            "PORound": po_round,
            "PaceAdjust": pace_adjust_value,
            "PerMode": per_mode_value,
            "Period": period_value,
            "PlayerExperience": player_experience,
            "PlayerPosition": player_position_value,
            "PlusMinus": plus_minus_value,
            "Rank": rank_value,
            "Season": season_value,
            "SeasonSegment": season_segment_value,
            "SeasonType": season_type_value,
            "ShotClockRange": shot_clock_range,
            "StarterBench": starter_bench_value,
            "TeamID": team_id,
            "TwoWay": two_way,
            "VsConference": vs_conference,
            "VsDivision": vs_division,
            "Weight": weight,
        }

    def _parse_response(self, data: dict) -> LeaguePlayerStats:
        """Parse NBA API response into LeaguePlayerStats model.

        Args:
            data: Raw API response

        Returns:
            LeaguePlayerStats with list of player statistics
        """
        result_sets = data.get("resultSets", [])
        if not result_sets:
            return LeaguePlayerStats(players=[])

        # The first result set contains the player stats (Leaderboard)
        player_data = result_sets[0]
        headers = player_data.get("headers", [])
        rows = player_data.get("rowSet", [])

        # Convert rows to list of dicts
        players = []
        for row in rows:
            player_dict = dict(zip(headers, row))
            players.append(PlayerStats(**player_dict))

        return LeaguePlayerStats(players=players)

    def fetch(
        self,
        season: Union[str, Season] = Season.CURRENT,
        season_type: Union[str, SeasonType] = SeasonType.REGULAR_SEASON,
        per_mode: Union[str, PerMode] = PerMode.TOTALS,
        measure_type: Union[str, MeasureType] = MeasureType.BASE,
        **kwargs: Union[str, int],
    ) -> LeaguePlayerStats:
        """Fetch league player statistics (synchronous).

        Args:
            season: NBA season (e.g., "2024-25")
            season_type: Type of season
            per_mode: Statistics mode
            measure_type: Type of measurements
            **kwargs: Additional query parameters (see _build_params for full list)

        Returns:
            LeaguePlayerStats with all qualifying players' statistics

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = LeaguePlayerStatsEndpoint()
            >>> stats = endpoint.fetch(season="2024-25", per_mode=PerMode.PER_GAME)
            >>> top_scorer = stats.get_top_scorers(1)[0]
            >>> print(f"{top_scorer.player_name}: {top_scorer.points_per_game:.1f} PPG")
        """
        params = self._build_params(
            season=season,
            season_type=season_type,
            per_mode=per_mode,
            measure_type=measure_type,
            **kwargs,
        )
        data = self.client.get(self.ENDPOINT, params=params)
        return self._parse_response(data)

    async def fetch_async(
        self,
        season: Union[str, Season] = Season.CURRENT,
        season_type: Union[str, SeasonType] = SeasonType.REGULAR_SEASON,
        per_mode: Union[str, PerMode] = PerMode.TOTALS,
        measure_type: Union[str, MeasureType] = MeasureType.BASE,
        **kwargs: Union[str, int],
    ) -> LeaguePlayerStats:
        """Fetch league player statistics (asynchronous).

        Args:
            season: NBA season (e.g., "2024-25")
            season_type: Type of season
            per_mode: Statistics mode
            measure_type: Type of measurements
            **kwargs: Additional query parameters (see _build_params for full list)

        Returns:
            LeaguePlayerStats with all qualifying players' statistics

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = LeaguePlayerStatsEndpoint(client)
            ...     stats = await endpoint.fetch_async(season="2024-25")
        """
        params = self._build_params(
            season=season,
            season_type=season_type,
            per_mode=per_mode,
            measure_type=measure_type,
            **kwargs,
        )
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return self._parse_response(data)


def get_league_player_stats(
    season: Union[str, Season] = Season.CURRENT,
    season_type: Union[str, SeasonType] = SeasonType.REGULAR_SEASON,
    per_mode: Union[str, PerMode] = PerMode.TOTALS,
    measure_type: Union[str, MeasureType] = MeasureType.BASE,
    **kwargs: Union[str, int],
) -> LeaguePlayerStats:
    """Convenience function to fetch league player statistics.

    Args:
        season: NBA season (e.g., "2024-25")
        season_type: Type of season
        per_mode: Statistics mode
        measure_type: Type of measurements
        **kwargs: Additional query parameters

    Returns:
        LeaguePlayerStats with all qualifying players' statistics

    Example:
        >>> from goldsberry.endpoints.league import get_league_player_stats
        >>> stats = get_league_player_stats(season="2024-25", per_mode=PerMode.PER_GAME)
        >>> for player in stats.get_top_scorers(10):
        ...     print(f"{player.player_name}: {player.points_per_game:.1f} PPG")
    """
    endpoint = LeaguePlayerStatsEndpoint()
    return endpoint.fetch(
        season=season,
        season_type=season_type,
        per_mode=per_mode,
        measure_type=measure_type,
        **kwargs,
    )


__all__ = ["LeaguePlayerStatsEndpoint", "get_league_player_stats"]
