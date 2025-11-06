"""Team endpoints."""

from .game_logs import TeamGameLogsEndpoint, get_team_game_logs
from .roster import TeamRosterEndpoint, get_team_roster
from .season_stats import TeamSeasonStatsEndpoint, get_team_season_stats

__all__ = [
    "TeamGameLogsEndpoint",
    "TeamRosterEndpoint",
    "TeamSeasonStatsEndpoint",
    "get_team_game_logs",
    "get_team_roster",
    "get_team_season_stats",
]
