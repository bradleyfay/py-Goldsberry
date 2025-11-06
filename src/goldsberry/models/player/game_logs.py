"""Pydantic models for GameLogs endpoint."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class GameLog(BaseModel):
    """Individual game statistics for a player.

    This model represents a single game's statistics including the matchup,
    result, minutes played, shooting stats, and other per-game metrics.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Game identification
    season_id: str = Field(alias="SEASON_ID")
    player_id: int = Field(alias="Player_ID")
    game_id: str = Field(alias="Game_ID")
    game_date: str = Field(alias="GAME_DATE")
    matchup: str = Field(alias="MATCHUP")
    win_loss: Optional[str] = Field(None, alias="WL")

    # Playing time
    minutes: Optional[float] = Field(None, alias="MIN")

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
    plus_minus: Optional[float] = Field(None, alias="PLUS_MINUS")
    video_available: Optional[int] = Field(None, alias="VIDEO_AVAILABLE")

    @property
    def is_win(self) -> bool:
        """Whether the game was a win."""
        return self.win_loss == "W"

    @property
    def is_home_game(self) -> bool:
        """Whether the game was played at home."""
        return " vs. " in self.matchup if self.matchup else False

    @property
    def opponent(self) -> str:
        """Extract opponent abbreviation from matchup."""
        if not self.matchup:
            return ""
        # Matchup format: "DEN @ HOU" or "DEN vs. HOU"
        parts = self.matchup.replace(" @ ", "|").replace(" vs. ", "|").split("|")
        return parts[1] if len(parts) > 1 else ""

    def __str__(self) -> str:
        """Human-readable string representation."""
        result = "W" if self.is_win else "L"
        return f"{self.game_date} {self.matchup} ({result}): {self.points} PTS, {self.rebounds} REB, {self.assists} AST"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"GameLog(game_id='{self.game_id}', date='{self.game_date}', pts={self.points})"


__all__ = ["GameLog"]
