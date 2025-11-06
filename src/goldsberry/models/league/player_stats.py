"""Pydantic models for League Player Stats endpoint."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class PlayerStats(BaseModel):
    """Player statistics for a season.

    This model represents an individual player's statistics for a given season,
    including games played, shooting metrics, and comprehensive performance data.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Player identification
    player_id: int = Field(alias="PLAYER_ID")
    player_name: str = Field(alias="PLAYER_NAME")
    nickname: Optional[str] = Field(None, alias="NICKNAME")
    team_id: int = Field(alias="TEAM_ID")
    team_abbreviation: str = Field(alias="TEAM_ABBREVIATION")

    # Player info
    age: Optional[float] = Field(None, alias="AGE")

    # Season performance
    games_played: int = Field(alias="GP")
    wins: int = Field(alias="W")
    losses: int = Field(alias="L")
    win_percentage: float = Field(alias="W_PCT")
    minutes: float = Field(alias="MIN")

    # Shooting stats
    field_goals_made: float = Field(alias="FGM")
    field_goals_attempted: float = Field(alias="FGA")
    field_goal_percentage: float = Field(alias="FG_PCT")
    three_pointers_made: float = Field(alias="FG3M")
    three_pointers_attempted: float = Field(alias="FG3A")
    three_point_percentage: float = Field(alias="FG3_PCT")
    free_throws_made: float = Field(alias="FTM")
    free_throws_attempted: float = Field(alias="FTA")
    free_throw_percentage: float = Field(alias="FT_PCT")

    # Rebounding stats
    offensive_rebounds: float = Field(alias="OREB")
    defensive_rebounds: float = Field(alias="DREB")
    rebounds: float = Field(alias="REB")

    # Other stats
    assists: float = Field(alias="AST")
    turnovers: float = Field(alias="TOV")
    steals: float = Field(alias="STL")
    blocks: float = Field(alias="BLK")
    blocked_field_goal_attempts: float = Field(alias="BLKA")
    personal_fouls: float = Field(alias="PF")
    personal_fouls_drawn: float = Field(alias="PFD")
    points: float = Field(alias="PTS")

    # Advanced stats
    plus_minus: float = Field(alias="PLUS_MINUS")

    # NBA fantasy points
    nba_fantasy_points: Optional[float] = Field(None, alias="NBA_FANTASY_PTS")

    # Defensive/shooting distance stats (may not always be present)
    defensive_distance: Optional[float] = Field(None, alias="DD2")
    triple_doubles: Optional[float] = Field(None, alias="TD3")

    # Optional rank field
    cfid: Optional[int] = Field(None, alias="CFID")
    cfparams: Optional[str] = Field(None, alias="CFPARAMS")

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

    @property
    def minutes_per_game(self) -> float:
        """Calculate minutes per game."""
        if self.games_played == 0:
            return 0.0
        return self.minutes / self.games_played

    @property
    def record(self) -> str:
        """Get player's team record as string (e.g., '45-37')."""
        return f"{self.wins}-{self.losses}"

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.player_name} ({self.team_abbreviation}): {self.points_per_game:.1f} PPG, {self.rebounds_per_game:.1f} RPG, {self.assists_per_game:.1f} APG"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerStats(player_id={self.player_id}, name='{self.player_name}', team='{self.team_abbreviation}')"


class LeaguePlayerStats(BaseModel):
    """Collection of player statistics for league-wide analysis.

    This model aggregates all qualifying players' statistics with helper methods
    for filtering, searching, and sorting players by various criteria.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    players: list[PlayerStats] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"LeaguePlayerStats: {len(self.players)} players"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"LeaguePlayerStats(players={len(self.players)})"

    def get_player_by_id(self, player_id: int) -> Optional[PlayerStats]:
        """Get player stats by player ID.

        Args:
            player_id: NBA player ID

        Returns:
            PlayerStats if found, None otherwise
        """
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    def get_player_by_name(self, name: str) -> Optional[PlayerStats]:
        """Get player stats by name (case-insensitive partial match).

        Args:
            name: Player name or partial name

        Returns:
            PlayerStats if found, None otherwise
        """
        name_lower = name.lower()
        for player in self.players:
            if name_lower in player.player_name.lower():
                return player
        return None

    def filter_by_team(self, team_abbreviation: str) -> list[PlayerStats]:
        """Filter players by team abbreviation.

        Args:
            team_abbreviation: Team abbreviation (e.g., "BOS", "LAL")

        Returns:
            List of PlayerStats for the specified team
        """
        team_upper = team_abbreviation.upper()
        return [p for p in self.players if p.team_abbreviation == team_upper]

    def filter_by_min_games(self, min_games: int) -> list[PlayerStats]:
        """Filter players by minimum games played.

        Args:
            min_games: Minimum number of games played

        Returns:
            List of PlayerStats with at least min_games played
        """
        return [p for p in self.players if p.games_played >= min_games]

    def get_top_scorers(self, n: int = 10) -> list[PlayerStats]:
        """Get top N scorers by points per game.

        Args:
            n: Number of players to return

        Returns:
            List of top N PlayerStats sorted by PPG (descending)
        """
        return self.sort_by("points_per_game", reverse=True)[:n]

    def get_top_by_stat(self, stat: str, n: int = 10, reverse: bool = True) -> list[PlayerStats]:
        """Get top N players by any stat.

        Args:
            stat: Stat name (e.g., "rebounds_per_game", "assists", "field_goal_percentage")
            n: Number of players to return
            reverse: If True, sort descending (highest values first)

        Returns:
            List of top N PlayerStats sorted by the specified stat
        """
        return self.sort_by(stat, reverse=reverse)[:n]

    def sort_by(self, attribute: str, reverse: bool = True) -> list[PlayerStats]:
        """Sort players by any attribute.

        Args:
            attribute: Attribute name to sort by (can be a property or field)
            reverse: If True, sort descending (highest values first)

        Returns:
            Sorted list of PlayerStats

        Raises:
            AttributeError: If attribute doesn't exist

        Example:
            >>> stats.sort_by("points_per_game")  # Highest PPG first
            >>> stats.sort_by("field_goal_percentage", reverse=False)  # Lowest FG% first
        """
        return sorted(self.players, key=lambda p: getattr(p, attribute), reverse=reverse)

    def sort_by_points(self, reverse: bool = True) -> list[PlayerStats]:
        """Get players sorted by total points.

        Args:
            reverse: If True, sort descending (most points first)

        Returns:
            Sorted list of PlayerStats
        """
        return sorted(self.players, key=lambda p: p.points, reverse=reverse)

    def sort_by_points_per_game(self, reverse: bool = True) -> list[PlayerStats]:
        """Get players sorted by points per game.

        Args:
            reverse: If True, sort descending (highest PPG first)

        Returns:
            Sorted list of PlayerStats
        """
        return sorted(self.players, key=lambda p: p.points_per_game, reverse=reverse)

    def sort_by_rebounds_per_game(self, reverse: bool = True) -> list[PlayerStats]:
        """Get players sorted by rebounds per game.

        Args:
            reverse: If True, sort descending (highest RPG first)

        Returns:
            Sorted list of PlayerStats
        """
        return sorted(self.players, key=lambda p: p.rebounds_per_game, reverse=reverse)

    def sort_by_assists_per_game(self, reverse: bool = True) -> list[PlayerStats]:
        """Get players sorted by assists per game.

        Args:
            reverse: If True, sort descending (highest APG first)

        Returns:
            Sorted list of PlayerStats
        """
        return sorted(self.players, key=lambda p: p.assists_per_game, reverse=reverse)


__all__ = ["PlayerStats", "LeaguePlayerStats"]
