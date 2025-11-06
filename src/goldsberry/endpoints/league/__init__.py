"""League-level endpoints."""

from .player_stats import LeaguePlayerStatsEndpoint, get_league_player_stats
from .team_stats import LeagueTeamStatsEndpoint, get_league_team_stats

__all__ = [
    "LeaguePlayerStatsEndpoint",
    "get_league_player_stats",
    "LeagueTeamStatsEndpoint",
    "get_league_team_stats",
]
