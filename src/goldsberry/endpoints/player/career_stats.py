"""CareerStats endpoint - fetch player career statistics."""

from typing import Optional, Union

from ...client.base import BaseClient
from ...enums.common import PerMode
from ...models.player import SeasonTotals, CareerTotals, PlayerCareerStats


class CareerStatsEndpoint:
    """Fetch player career statistics.

    Provides access to the playercareerstats endpoint which returns
    season-by-season totals and career totals for regular season and playoffs.

    Example:
        >>> # Synchronous usage
        >>> endpoint = CareerStatsEndpoint()
        >>> stats = endpoint.fetch(player_id=203999)  # Nikola Jokic
        >>> print(f"{len(stats.season_totals_regular)} seasons")
        >>> if stats.career_totals_regular:
        ...     print(f"{stats.career_totals_regular.points_per_game:.1f} PPG")

        >>> # Async usage
        >>> async with BaseClient() as client:
        ...     endpoint = CareerStatsEndpoint(client)
        ...     stats = await endpoint.fetch_async(player_id=203999)
    """

    ENDPOINT = "playercareerstats"  # NBA API endpoint name

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
        per_mode: PerMode = PerMode.TOTALS,
    ) -> dict[str, Union[str, int]]:
        """Build query parameters for API request.

        Args:
            player_id: NBA player ID
            per_mode: Per mode statistic type (default: Totals)

        Returns:
            Dict of query parameters
        """
        # Convert enum to value (handle both enum and string)
        per_mode_value = per_mode.value if isinstance(per_mode, PerMode) else per_mode

        return {
            "PlayerID": player_id,
            "PerMode": per_mode_value,
        }

    def _parse_response(self, data: dict) -> PlayerCareerStats:
        """Parse NBA API response into PlayerCareerStats model.

        Args:
            data: Raw API response

        Returns:
            PlayerCareerStats with season and career totals
        """
        result_sets = {rs["name"]: rs for rs in data.get("resultSets", [])}

        # Parse season totals regular season
        season_regular = []
        if "SeasonTotalsRegularSeason" in result_sets:
            headers = result_sets["SeasonTotalsRegularSeason"]["headers"]
            for row in result_sets["SeasonTotalsRegularSeason"]["rowSet"]:
                row_dict = dict(zip(headers, row))
                season_regular.append(SeasonTotals(**row_dict))

        # Parse career totals regular season
        career_regular = None
        if "CareerTotalsRegularSeason" in result_sets:
            headers = result_sets["CareerTotalsRegularSeason"]["headers"]
            rows = result_sets["CareerTotalsRegularSeason"]["rowSet"]
            if rows:
                row_dict = dict(zip(headers, rows[0]))
                career_regular = CareerTotals(**row_dict)

        # Parse season totals playoffs
        season_post = []
        if "SeasonTotalsPostSeason" in result_sets:
            headers = result_sets["SeasonTotalsPostSeason"]["headers"]
            for row in result_sets["SeasonTotalsPostSeason"]["rowSet"]:
                row_dict = dict(zip(headers, row))
                season_post.append(SeasonTotals(**row_dict))

        # Parse career totals playoffs
        career_post = None
        if "CareerTotalsPostSeason" in result_sets:
            headers = result_sets["CareerTotalsPostSeason"]["headers"]
            rows = result_sets["CareerTotalsPostSeason"]["rowSet"]
            if rows:
                row_dict = dict(zip(headers, rows[0]))
                career_post = CareerTotals(**row_dict)

        return PlayerCareerStats(
            season_totals_regular=season_regular,
            career_totals_regular=career_regular,
            season_totals_post=season_post,
            career_totals_post=career_post,
        )

    def fetch(
        self,
        player_id: int,
        per_mode: PerMode = PerMode.TOTALS,
    ) -> PlayerCareerStats:
        """Fetch career statistics (synchronous).

        Args:
            player_id: NBA player ID
            per_mode: Per mode statistic type (default: Totals)

        Returns:
            PlayerCareerStats object with season and career data

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> endpoint = CareerStatsEndpoint()
            >>> stats = endpoint.fetch(player_id=203999)  # Nikola Jokic
            >>> for season in stats.season_totals_regular:
            ...     print(f"{season.season_id}: {season.points_per_game:.1f} PPG")
        """
        params = self._build_params(player_id, per_mode)
        data = self.client.get(self.ENDPOINT, params=params)
        return self._parse_response(data)

    async def fetch_async(
        self,
        player_id: int,
        per_mode: PerMode = PerMode.TOTALS,
    ) -> PlayerCareerStats:
        """Fetch career statistics (asynchronous).

        Args:
            player_id: NBA player ID
            per_mode: Per mode statistic type (default: Totals)

        Returns:
            PlayerCareerStats object with season and career data

        Raises:
            NBAAPIError: If request fails

        Example:
            >>> async with BaseClient() as client:
            ...     endpoint = CareerStatsEndpoint(client)
            ...     stats = await endpoint.fetch_async(player_id=203999)
            ...     print(stats.career_totals_regular)
        """
        params = self._build_params(player_id, per_mode)
        data = await self.client.get_async(self.ENDPOINT, params=params)
        return self._parse_response(data)


# Convenience functions for quick access
def get_career_stats(
    player_id: int,
    per_mode: PerMode = PerMode.TOTALS,
    client: Optional[BaseClient] = None,
) -> PlayerCareerStats:
    """Convenience function to fetch player career statistics.

    Args:
        player_id: NBA player ID
        per_mode: Per mode statistic type (default: Totals)
        client: Optional client instance

    Returns:
        PlayerCareerStats object

    Example:
        >>> from goldsberry.endpoints.player import get_career_stats
        >>> stats = get_career_stats(player_id=203999)  # Nikola Jokic
        >>> print(stats.career_totals_regular)
    """
    endpoint = CareerStatsEndpoint(client)
    return endpoint.fetch(player_id, per_mode)


async def get_career_stats_async(
    player_id: int,
    per_mode: PerMode = PerMode.TOTALS,
    client: Optional[BaseClient] = None,
) -> PlayerCareerStats:
    """Async convenience function to fetch player career statistics.

    Args:
        player_id: NBA player ID
        per_mode: Per mode statistic type (default: Totals)
        client: Optional client instance

    Returns:
        PlayerCareerStats object

    Example:
        >>> from goldsberry.endpoints.player import get_career_stats_async
        >>> stats = await get_career_stats_async(player_id=203999)
    """
    endpoint = CareerStatsEndpoint(client)
    return await endpoint.fetch_async(player_id, per_mode)


__all__ = ["CareerStatsEndpoint", "get_career_stats", "get_career_stats_async"]
