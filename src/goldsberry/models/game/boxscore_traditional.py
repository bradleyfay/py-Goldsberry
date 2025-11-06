"""Pydantic models for Traditional Boxscore endpoint."""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PlayerBoxscoreTraditional(BaseModel):
    """Traditional boxscore statistics for a player in a game.

    This model represents a player's traditional statistics in a specific game,
    including points, rebounds, assists, and shooting stats.
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

    # Shooting stats
    field_goals_made: Optional[int] = Field(None, alias="FGM")
    field_goals_attempted: Optional[int] = Field(None, alias="FGA")
    field_goal_percentage: Optional[float] = Field(None, alias="FG_PCT")
    three_pointers_made: Optional[int] = Field(None, alias="FG3M")
    three_pointers_attempted: Optional[int] = Field(None, alias="FG3A")
    three_point_percentage: Optional[float] = Field(None, alias="FG3_PCT")
    free_throws_made: Optional[int] = Field(None, alias="FTM")
    free_throws_attempted: Optional[int] = Field(None, alias="FTA")
    free_throw_percentage: Optional[float] = Field(None, alias="FT_PCT")

    # Rebounding stats
    offensive_rebounds: Optional[int] = Field(None, alias="OREB")
    defensive_rebounds: Optional[int] = Field(None, alias="DREB")
    rebounds: Optional[int] = Field(None, alias="REB")

    # Other stats
    assists: Optional[int] = Field(None, alias="AST")
    steals: Optional[int] = Field(None, alias="STL")
    blocks: Optional[int] = Field(None, alias="BLK")
    turnovers: Optional[int] = Field(None, alias="TO")
    personal_fouls: Optional[int] = Field(None, alias="PF")
    points: Optional[int] = Field(None, alias="PTS")
    plus_minus: Optional[int] = Field(None, alias="PLUS_MINUS")

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
        pts = self.points or 0
        reb = self.rebounds or 0
        ast = self.assists or 0
        return f"{self.player_name} ({self.team_abbreviation}): {pts} PTS, {reb} REB, {ast} AST"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerBoxscoreTraditional(player_id={self.player_id}, name='{self.player_name}', pts={self.points})"


class TeamBoxscoreTraditional(BaseModel):
    """Traditional boxscore statistics for a team in a game.

    This model represents a team's aggregate traditional statistics in a specific game.
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

    # Shooting stats
    field_goals_made: Optional[int] = Field(None, alias="FGM")
    field_goals_attempted: Optional[int] = Field(None, alias="FGA")
    field_goal_percentage: Optional[float] = Field(None, alias="FG_PCT")
    three_pointers_made: Optional[int] = Field(None, alias="FG3M")
    three_pointers_attempted: Optional[int] = Field(None, alias="FG3A")
    three_point_percentage: Optional[float] = Field(None, alias="FG3_PCT")
    free_throws_made: Optional[int] = Field(None, alias="FTM")
    free_throws_attempted: Optional[int] = Field(None, alias="FTA")
    free_throw_percentage: Optional[float] = Field(None, alias="FT_PCT")

    # Rebounding stats
    offensive_rebounds: Optional[int] = Field(None, alias="OREB")
    defensive_rebounds: Optional[int] = Field(None, alias="DREB")
    rebounds: Optional[int] = Field(None, alias="REB")

    # Other stats
    assists: Optional[int] = Field(None, alias="AST")
    steals: Optional[int] = Field(None, alias="STL")
    blocks: Optional[int] = Field(None, alias="BLK")
    turnovers: Optional[int] = Field(None, alias="TO")
    personal_fouls: Optional[int] = Field(None, alias="PF")
    points: Optional[int] = Field(None, alias="PTS")
    plus_minus: Optional[int] = Field(None, alias="PLUS_MINUS")

    def __str__(self) -> str:
        """Human-readable string representation."""
        pts = self.points or 0
        return f"{self.team_name}: {pts} PTS"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamBoxscoreTraditional(team_id={self.team_id}, name='{self.team_name}', pts={self.points})"


class BoxscoreTraditional(BaseModel):
    """Complete traditional boxscore for a game.

    This model aggregates all traditional boxscore data including
    player statistics for both teams and team totals.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    player_stats: list[PlayerBoxscoreTraditional] = Field(default_factory=list)
    team_stats: list[TeamBoxscoreTraditional] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"BoxscoreTraditional: {len(self.player_stats)} players, {len(self.team_stats)} teams"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"BoxscoreTraditional(players={len(self.player_stats)}, teams={len(self.team_stats)})"

    def get_team_stats(self, team_id: int) -> Optional[TeamBoxscoreTraditional]:
        """Get team stats by team ID.

        Args:
            team_id: NBA team ID

        Returns:
            TeamBoxscoreTraditional if found, None otherwise
        """
        for team in self.team_stats:
            if team.team_id == team_id:
                return team
        return None

    def get_team_players(self, team_id: int) -> list[PlayerBoxscoreTraditional]:
        """Get all players for a specific team.

        Args:
            team_id: NBA team ID

        Returns:
            List of PlayerBoxscoreTraditional for the team
        """
        return [player for player in self.player_stats if player.team_id == team_id]

    def get_starters(self, team_id: Optional[int] = None) -> list[PlayerBoxscoreTraditional]:
        """Get starting players.

        Args:
            team_id: Optional team ID to filter by

        Returns:
            List of PlayerBoxscoreTraditional who started
        """
        starters = [player for player in self.player_stats if player.is_starter]
        if team_id is not None:
            starters = [p for p in starters if p.team_id == team_id]
        return starters

    def get_bench_players(self, team_id: Optional[int] = None) -> list[PlayerBoxscoreTraditional]:
        """Get bench players.

        Args:
            team_id: Optional team ID to filter by

        Returns:
            List of PlayerBoxscoreTraditional who came off the bench
        """
        bench = [player for player in self.player_stats if not player.is_starter]
        if team_id is not None:
            bench = [p for p in bench if p.team_id == team_id]
        return bench

    def get_top_scorers(self, limit: int = 5) -> list[PlayerBoxscoreTraditional]:
        """Get top scorers in the game.

        Args:
            limit: Number of players to return

        Returns:
            List of top scoring players
        """
        return sorted(
            self.player_stats,
            key=lambda p: p.points or 0,
            reverse=True
        )[:limit]


__all__ = ["PlayerBoxscoreTraditional", "TeamBoxscoreTraditional", "BoxscoreTraditional"]
