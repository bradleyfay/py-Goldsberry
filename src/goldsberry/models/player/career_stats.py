"""Pydantic models for CareerStats endpoint."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class SeasonTotals(BaseModel):
    """Season totals statistics for a player.

    This model represents a single season's totals (regular season, playoffs, etc.)
    including games played, minutes, shooting stats, and other per-season metrics.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Required fields
    player_id: int = Field(alias="PLAYER_ID")
    season_id: str = Field(alias="SEASON_ID")
    league_id: str = Field(alias="LEAGUE_ID")
    team_id: int = Field(alias="TEAM_ID")
    team_abbreviation: str = Field(alias="TEAM_ABBREVIATION")
    player_age: Optional[float] = Field(None, alias="PLAYER_AGE")
    games_played: int = Field(alias="GP")
    games_started: int = Field(alias="GS")
    minutes: float = Field(alias="MIN")

    # Shooting stats
    field_goals_made: float = Field(alias="FGM")
    field_goals_attempted: float = Field(alias="FGA")
    field_goal_percentage: Optional[float] = Field(None, alias="FG_PCT")
    three_pointers_made: float = Field(alias="FG3M")
    three_pointers_attempted: float = Field(alias="FG3A")
    three_point_percentage: Optional[float] = Field(None, alias="FG3_PCT")
    free_throws_made: float = Field(alias="FTM")
    free_throws_attempted: float = Field(alias="FTA")
    free_throw_percentage: Optional[float] = Field(None, alias="FT_PCT")

    # Rebounding stats
    offensive_rebounds: float = Field(alias="OREB")
    defensive_rebounds: float = Field(alias="DREB")
    rebounds: float = Field(alias="REB")

    # Other stats
    assists: float = Field(alias="AST")
    steals: float = Field(alias="STL")
    blocks: float = Field(alias="BLK")
    turnovers: float = Field(alias="TOV")
    personal_fouls: float = Field(alias="PF")
    points: float = Field(alias="PTS")

    @property
    def points_per_game(self) -> float:
        """Calculate points per game."""
        if self.games_played == 0:
            return 0.0
        return self.points / self.games_played

    @property
    def rebounds_per_game(self) -> float:
        """Calculate rebounds per game."""
        if self.games_played == 0:
            return 0.0
        return self.rebounds / self.games_played

    @property
    def assists_per_game(self) -> float:
        """Calculate assists per game."""
        if self.games_played == 0:
            return 0.0
        return self.assists / self.games_played

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.season_id} ({self.team_abbreviation}): {self.points_per_game:.1f} PPG, {self.rebounds_per_game:.1f} RPG, {self.assists_per_game:.1f} APG"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"SeasonTotals(player_id={self.player_id}, season='{self.season_id}', team='{self.team_abbreviation}')"


class CareerTotals(BaseModel):
    """Career totals statistics for a player.

    This model represents aggregate career statistics across all seasons,
    including total games, minutes, and cumulative stats.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    # Required fields
    player_id: int = Field(alias="PLAYER_ID")
    league_id: str = Field(alias="LEAGUE_ID")
    team_id: int = Field(alias="TEAM_ID")
    games_played: int = Field(alias="GP")
    games_started: int = Field(alias="GS")
    minutes: float = Field(alias="MIN")

    # Shooting stats
    field_goals_made: float = Field(alias="FGM")
    field_goals_attempted: float = Field(alias="FGA")
    field_goal_percentage: Optional[float] = Field(None, alias="FG_PCT")
    three_pointers_made: float = Field(alias="FG3M")
    three_pointers_attempted: float = Field(alias="FG3A")
    three_point_percentage: Optional[float] = Field(None, alias="FG3_PCT")
    free_throws_made: float = Field(alias="FTM")
    free_throws_attempted: float = Field(alias="FTA")
    free_throw_percentage: Optional[float] = Field(None, alias="FT_PCT")

    # Rebounding stats
    offensive_rebounds: float = Field(alias="OREB")
    defensive_rebounds: float = Field(alias="DREB")
    rebounds: float = Field(alias="REB")

    # Other stats
    assists: float = Field(alias="AST")
    steals: float = Field(alias="STL")
    blocks: float = Field(alias="BLK")
    turnovers: float = Field(alias="TOV")
    personal_fouls: float = Field(alias="PF")
    points: float = Field(alias="PTS")

    @property
    def points_per_game(self) -> float:
        """Calculate career points per game."""
        if self.games_played == 0:
            return 0.0
        return self.points / self.games_played

    @property
    def rebounds_per_game(self) -> float:
        """Calculate career rebounds per game."""
        if self.games_played == 0:
            return 0.0
        return self.rebounds / self.games_played

    @property
    def assists_per_game(self) -> float:
        """Calculate career assists per game."""
        if self.games_played == 0:
            return 0.0
        return self.assists / self.games_played

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"Career: {self.games_played} GP, {self.points_per_game:.1f} PPG, {self.rebounds_per_game:.1f} RPG, {self.assists_per_game:.1f} APG"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"CareerTotals(player_id={self.player_id}, games={self.games_played})"


class PlayerCareerStats(BaseModel):
    """Complete career statistics for a player.

    This model aggregates all career data including season-by-season breakdowns
    and career totals for both regular season and playoffs.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    season_totals_regular: list[SeasonTotals] = Field(default_factory=list)
    career_totals_regular: Optional[CareerTotals] = None
    season_totals_post: list[SeasonTotals] = Field(default_factory=list)
    career_totals_post: Optional[CareerTotals] = None

    def __str__(self) -> str:
        """Human-readable string representation."""
        seasons = len(self.season_totals_regular)
        if self.career_totals_regular:
            return f"Career: {seasons} seasons, {self.career_totals_regular.points_per_game:.1f} PPG"
        return f"Career: {seasons} seasons"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerCareerStats(seasons={len(self.season_totals_regular)})"


__all__ = ["SeasonTotals", "CareerTotals", "PlayerCareerStats"]
