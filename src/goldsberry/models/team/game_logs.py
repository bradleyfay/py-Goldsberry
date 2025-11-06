"""Pydantic models for Team Game Logs endpoint."""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TeamGameLog(BaseModel):
    """Individual game statistics for a team.

    This model represents a single game's statistics for a team including the matchup,
    result, minutes, shooting stats, and other per-game metrics.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Game identification
    team_id: int = Field(alias="TEAM_ID")
    game_id: str = Field(alias="GAME_ID")
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
        # Matchup format: "BOS @ MIA" or "BOS vs. MIA"
        parts = self.matchup.replace(" @ ", "|").replace(" vs. ", "|").split("|")
        return parts[1] if len(parts) > 1 else ""

    def __str__(self) -> str:
        """Human-readable string representation."""
        result = "W" if self.is_win else "L"
        return f"{self.game_date} {self.matchup} ({result}): {self.points} PTS, {self.rebounds} REB, {self.assists} AST"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamGameLog(game_id='{self.game_id}', date='{self.game_date}', pts={self.points})"


class TeamGameLogs(BaseModel):
    """Collection of game logs for a team.

    This model aggregates all game logs for a team across a season.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    games: list[TeamGameLog] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"TeamGameLogs: {len(self.games)} games"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamGameLogs(games={len(self.games)})"

    def filter_wins(self) -> list[TeamGameLog]:
        """Get only winning games.

        Returns:
            List of TeamGameLog objects for wins
        """
        return [game for game in self.games if game.is_win]

    def filter_losses(self) -> list[TeamGameLog]:
        """Get only losing games.

        Returns:
            List of TeamGameLog objects for losses
        """
        return [game for game in self.games if not game.is_win]

    def filter_home_games(self) -> list[TeamGameLog]:
        """Get only home games.

        Returns:
            List of TeamGameLog objects for home games
        """
        return [game for game in self.games if game.is_home_game]

    def filter_away_games(self) -> list[TeamGameLog]:
        """Get only away games.

        Returns:
            List of TeamGameLog objects for away games
        """
        return [game for game in self.games if not game.is_home_game]

    def calculate_totals(self) -> dict[str, float]:
        """Calculate total statistics across all games.

        Returns:
            Dict with totals for points, rebounds, assists, etc.
        """
        if not self.games:
            return {}

        return {
            "games": len(self.games),
            "wins": len(self.filter_wins()),
            "losses": len(self.filter_losses()),
            "points": sum(g.points for g in self.games),
            "rebounds": sum(g.rebounds for g in self.games),
            "assists": sum(g.assists for g in self.games),
            "steals": sum(g.steals for g in self.games),
            "blocks": sum(g.blocks for g in self.games),
            "turnovers": sum(g.turnovers for g in self.games),
        }

    @property
    def record(self) -> str:
        """Get team record as string (e.g., '45-37')."""
        wins = len(self.filter_wins())
        losses = len(self.filter_losses())
        return f"{wins}-{losses}"


__all__ = ["TeamGameLog", "TeamGameLogs"]
