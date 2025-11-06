"""Pydantic models for Advanced Boxscore endpoint."""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerBoxscoreAdvanced(BaseModel):
    """Advanced boxscore statistics for a player in a game.

    This model represents a player's advanced statistics in a specific game,
    including offensive/defensive rating, usage percentage, true shooting, and other efficiency metrics.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Player identification
    game_id: str = Field(alias="GAME_ID")
    team_id: int = Field(alias="TEAM_ID")
    team_abbreviation: str = Field(alias="TEAM_ABBREVIATION")
    team_city: str = Field(alias="TEAM_CITY")
    player_id: int = Field(alias="PLAYER_ID")
    player_name: str = Field(alias="PLAYER_NAME")
    start_position: Optional[str] = Field(None, alias="START_POSITION")
    comment: Optional[str] = Field(None, alias="COMMENT")

    # Playing time
    minutes: Optional[str] = Field(None, alias="MIN")

    # Advanced metrics
    e_offensive_rating: Optional[float] = Field(None, alias="E_OFF_RATING")
    offensive_rating: Optional[float] = Field(None, alias="OFF_RATING")
    e_defensive_rating: Optional[float] = Field(None, alias="E_DEF_RATING")
    defensive_rating: Optional[float] = Field(None, alias="DEF_RATING")
    e_net_rating: Optional[float] = Field(None, alias="E_NET_RATING")
    net_rating: Optional[float] = Field(None, alias="NET_RATING")
    assist_percentage: Optional[float] = Field(None, alias="AST_PCT")
    assist_to_turnover: Optional[float] = Field(None, alias="AST_TOV")
    assist_ratio: Optional[float] = Field(None, alias="AST_RATIO")
    offensive_rebound_percentage: Optional[float] = Field(None, alias="OREB_PCT")
    defensive_rebound_percentage: Optional[float] = Field(None, alias="DREB_PCT")
    rebound_percentage: Optional[float] = Field(None, alias="REB_PCT")
    true_shooting_percentage: Optional[float] = Field(None, alias="TS_PCT")
    effective_field_goal_percentage: Optional[float] = Field(None, alias="EFG_PCT")
    usage_percentage: Optional[float] = Field(None, alias="USG_PCT")
    e_usage_percentage: Optional[float] = Field(None, alias="E_USG_PCT")
    e_pace: Optional[float] = Field(None, alias="E_PACE")
    pace: Optional[float] = Field(None, alias="PACE")
    pace_per_40: Optional[float] = Field(None, alias="PACE_PER40")
    possessions: Optional[float] = Field(None, alias="POSS")
    pie: Optional[float] = Field(None, alias="PIE")

    @property
    def is_starter(self) -> bool:
        """Whether the player started the game."""
        return self.start_position is not None and self.start_position != ""

    @property
    def minutes_played(self) -> float:
        """Convert minutes string to float (e.g., '25:30' -> 25.5)."""
        if not self.minutes or self.minutes == "":
            return 0.0
        try:
            parts = self.minutes.split(":")
            if len(parts) == 2:
                return float(parts[0]) + float(parts[1]) / 60.0
            return float(self.minutes)
        except (ValueError, IndexError):
            return 0.0

    def __str__(self) -> str:
        """Human-readable string representation."""
        ortg = self.offensive_rating or 0
        drtg = self.defensive_rating or 0
        pie_val = self.pie or 0
        return f"{self.player_name} ({self.team_abbreviation}): ORtg {ortg:.1f}, DRtg {drtg:.1f}, PIE {pie_val:.3f}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerBoxscoreAdvanced(player_id={self.player_id}, name='{self.player_name}', net_rating={self.net_rating})"


class TeamBoxscoreAdvanced(BaseModel):
    """Advanced boxscore statistics for a team in a game.

    This model represents a team's aggregate advanced statistics in a specific game.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    # Team identification
    game_id: str = Field(alias="GAME_ID")
    team_id: int = Field(alias="TEAM_ID")
    team_name: str = Field(alias="TEAM_NAME")
    team_abbreviation: str = Field(alias="TEAM_ABBREVIATION")
    team_city: str = Field(alias="TEAM_CITY")

    # Playing time
    minutes: Optional[str] = Field(None, alias="MIN")

    # Advanced metrics
    e_offensive_rating: Optional[float] = Field(None, alias="E_OFF_RATING")
    offensive_rating: Optional[float] = Field(None, alias="OFF_RATING")
    e_defensive_rating: Optional[float] = Field(None, alias="E_DEF_RATING")
    defensive_rating: Optional[float] = Field(None, alias="DEF_RATING")
    e_net_rating: Optional[float] = Field(None, alias="E_NET_RATING")
    net_rating: Optional[float] = Field(None, alias="NET_RATING")
    assist_percentage: Optional[float] = Field(None, alias="AST_PCT")
    assist_to_turnover: Optional[float] = Field(None, alias="AST_TOV")
    assist_ratio: Optional[float] = Field(None, alias="AST_RATIO")
    offensive_rebound_percentage: Optional[float] = Field(None, alias="OREB_PCT")
    defensive_rebound_percentage: Optional[float] = Field(None, alias="DREB_PCT")
    rebound_percentage: Optional[float] = Field(None, alias="REB_PCT")
    true_shooting_percentage: Optional[float] = Field(None, alias="TS_PCT")
    effective_field_goal_percentage: Optional[float] = Field(None, alias="EFG_PCT")
    turnover_percentage: Optional[float] = Field(None, alias="TM_TOV_PCT")
    effective_field_goal_percentage_opponent: Optional[float] = Field(None, alias="EFG_PCT_OPP")
    e_pace: Optional[float] = Field(None, alias="E_PACE")
    pace: Optional[float] = Field(None, alias="PACE")
    pace_per_40: Optional[float] = Field(None, alias="PACE_PER40")
    possessions: Optional[float] = Field(None, alias="POSS")
    pie: Optional[float] = Field(None, alias="PIE")

    def __str__(self) -> str:
        """Human-readable string representation."""
        ortg = self.offensive_rating or 0
        drtg = self.defensive_rating or 0
        pace_val = self.pace or 0
        return f"{self.team_name}: ORtg {ortg:.1f}, DRtg {drtg:.1f}, Pace {pace_val:.1f}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamBoxscoreAdvanced(team_id={self.team_id}, name='{self.team_name}', net_rating={self.net_rating})"


class BoxscoreAdvanced(BaseModel):
    """Complete advanced boxscore for a game.

    This model aggregates all advanced boxscore data including
    player statistics for both teams and team totals.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    player_stats: list[PlayerBoxscoreAdvanced] = Field(default_factory=list)
    team_stats: list[TeamBoxscoreAdvanced] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"BoxscoreAdvanced: {len(self.player_stats)} players, {len(self.team_stats)} teams"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"BoxscoreAdvanced(players={len(self.player_stats)}, teams={len(self.team_stats)})"

    def get_team_stats(self, team_id: int) -> Optional[TeamBoxscoreAdvanced]:
        """Get team stats by team ID.

        Args:
            team_id: NBA team ID

        Returns:
            TeamBoxscoreAdvanced if found, None otherwise
        """
        for team in self.team_stats:
            if team.team_id == team_id:
                return team
        return None

    def get_team_players(self, team_id: int) -> list[PlayerBoxscoreAdvanced]:
        """Get all players for a specific team.

        Args:
            team_id: NBA team ID

        Returns:
            List of PlayerBoxscoreAdvanced for the team
        """
        return [player for player in self.player_stats if player.team_id == team_id]

    def get_starters(self, team_id: Optional[int] = None) -> list[PlayerBoxscoreAdvanced]:
        """Get starting players.

        Args:
            team_id: Optional team ID to filter by

        Returns:
            List of PlayerBoxscoreAdvanced who started
        """
        starters = [player for player in self.player_stats if player.is_starter]
        if team_id is not None:
            starters = [p for p in starters if p.team_id == team_id]
        return starters

    def get_bench_players(self, team_id: Optional[int] = None) -> list[PlayerBoxscoreAdvanced]:
        """Get bench players.

        Args:
            team_id: Optional team ID to filter by

        Returns:
            List of PlayerBoxscoreAdvanced who came off the bench
        """
        bench = [player for player in self.player_stats if not player.is_starter]
        if team_id is not None:
            bench = [p for p in bench if p.team_id == team_id]
        return bench

    def get_top_performers_by_pie(self, limit: int = 5) -> list[PlayerBoxscoreAdvanced]:
        """Get top performers by PIE (Player Impact Estimate).

        Args:
            limit: Number of players to return

        Returns:
            List of top performers by PIE
        """
        return sorted(
            self.player_stats,
            key=lambda p: p.pie or 0,
            reverse=True
        )[:limit]

    def get_top_performers_by_net_rating(self, limit: int = 5) -> list[PlayerBoxscoreAdvanced]:
        """Get top performers by net rating.

        Args:
            limit: Number of players to return

        Returns:
            List of top performers by net rating
        """
        return sorted(
            self.player_stats,
            key=lambda p: p.net_rating or -999,
            reverse=True
        )[:limit]

    def get_most_efficient_shooters(self, limit: int = 5, min_minutes: float = 10.0) -> list[PlayerBoxscoreAdvanced]:
        """Get most efficient shooters by true shooting percentage.

        Args:
            limit: Number of players to return
            min_minutes: Minimum minutes played to qualify

        Returns:
            List of most efficient shooters
        """
        qualified = [p for p in self.player_stats if p.minutes_played >= min_minutes]
        return sorted(
            qualified,
            key=lambda p: p.true_shooting_percentage or 0,
            reverse=True
        )[:limit]


__all__ = ["PlayerBoxscoreAdvanced", "TeamBoxscoreAdvanced", "BoxscoreAdvanced"]
