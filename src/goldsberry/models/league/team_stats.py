"""Pydantic models for League Team Stats endpoint."""

from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class TeamStats(BaseModel):
    """Team statistics for a season.

    This model represents a team's statistics for a given season,
    including games played, wins/losses, and comprehensive performance metrics.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Team identification
    team_id: int = Field(alias="TEAM_ID")
    team_name: str = Field(alias="TEAM_NAME")

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

    # Optional video available indicator
    video_available: Optional[int] = Field(None, alias="VIDEO_AVAILABLE")

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
    def record(self) -> str:
        """Get team record as string (e.g., '45-37')."""
        return f"{self.wins}-{self.losses}"

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.team_name} ({self.record}): {self.points_per_game:.1f} PPG, {self.rebounds_per_game:.1f} RPG, {self.assists_per_game:.1f} APG"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamStats(team_id={self.team_id}, name='{self.team_name}', record='{self.record}')"


class LeagueTeamStats(BaseModel):
    """Collection of team statistics for league-wide analysis.

    This model aggregates all teams' statistics with helper methods
    for filtering, searching, and sorting teams by various criteria.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    teams: list[TeamStats] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"LeagueTeamStats: {len(self.teams)} teams"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"LeagueTeamStats(teams={len(self.teams)})"

    def get_team_by_id(self, team_id: int) -> Optional[TeamStats]:
        """Get team stats by team ID.

        Args:
            team_id: NBA team ID

        Returns:
            TeamStats if found, None otherwise
        """
        for team in self.teams:
            if team.team_id == team_id:
                return team
        return None

    def get_team_by_name(self, name: str) -> Optional[TeamStats]:
        """Get team stats by team name (case-insensitive partial match).

        Args:
            name: Team name or partial name

        Returns:
            TeamStats if found, None otherwise
        """
        name_lower = name.lower()
        for team in self.teams:
            if name_lower in team.team_name.lower():
                return team
        return None

    def sort_by_wins(self, reverse: bool = True) -> list[TeamStats]:
        """Get teams sorted by wins.

        Args:
            reverse: If True, sort descending (most wins first)

        Returns:
            Sorted list of TeamStats
        """
        return sorted(self.teams, key=lambda t: t.wins, reverse=reverse)

    def sort_by_stat(self, attribute: str, reverse: bool = True) -> list[TeamStats]:
        """Sort teams by any attribute.

        Args:
            attribute: Attribute name to sort by (can be a property or field)
            reverse: If True, sort descending (highest values first)

        Returns:
            Sorted list of TeamStats

        Raises:
            AttributeError: If attribute doesn't exist

        Example:
            >>> stats.sort_by_stat("points_per_game")  # Highest PPG first
            >>> stats.sort_by_stat("field_goal_percentage", reverse=False)  # Lowest FG% first
        """
        return sorted(self.teams, key=lambda t: getattr(t, attribute), reverse=reverse)

    def sort_by_points_per_game(self, reverse: bool = True) -> list[TeamStats]:
        """Get teams sorted by points per game.

        Args:
            reverse: If True, sort descending (highest PPG first)

        Returns:
            Sorted list of TeamStats
        """
        return sorted(self.teams, key=lambda t: t.points_per_game, reverse=reverse)

    def filter_by_conference(self, conference: str) -> list[TeamStats]:
        """Filter teams by conference.

        Note: Conference information is not included in the basic stats response.
        This method filters by team name patterns to infer conference membership.
        For precise filtering, use the conference parameter in the API call.

        Args:
            conference: Conference name ("East" or "West")

        Returns:
            List of TeamStats for teams in the specified conference
        """
        # Eastern Conference teams
        east_teams = {
            "Atlanta", "Boston", "Brooklyn", "Charlotte", "Chicago",
            "Cleveland", "Detroit", "Indiana", "Miami", "Milwaukee",
            "New York", "Orlando", "Philadelphia", "Toronto", "Washington"
        }

        # Western Conference teams
        west_teams = {
            "Dallas", "Denver", "Golden State", "Houston", "LA Clippers",
            "Los Angeles Lakers", "Memphis", "Minnesota", "New Orleans",
            "Oklahoma City", "Phoenix", "Portland", "Sacramento", "San Antonio", "Utah"
        }

        conference_lower = conference.lower()
        if conference_lower == "east":
            return [t for t in self.teams if any(city in t.team_name for city in east_teams)]
        elif conference_lower == "west":
            return [t for t in self.teams if any(city in t.team_name for city in west_teams)]
        else:
            return []

    def filter_by_division(self, division: str) -> list[TeamStats]:
        """Filter teams by division.

        Note: Division information is not included in the basic stats response.
        This method filters by team name patterns to infer division membership.
        For precise filtering, use the division parameter in the API call.

        Args:
            division: Division name (Atlantic, Central, Southeast, Northwest, Pacific, Southwest)

        Returns:
            List of TeamStats for teams in the specified division
        """
        # Division mappings
        divisions = {
            "atlantic": ["Boston", "Brooklyn", "New York", "Philadelphia", "Toronto"],
            "central": ["Chicago", "Cleveland", "Detroit", "Indiana", "Milwaukee"],
            "southeast": ["Atlanta", "Charlotte", "Miami", "Orlando", "Washington"],
            "northwest": ["Denver", "Minnesota", "Oklahoma City", "Portland", "Utah"],
            "pacific": ["Golden State", "LA Clippers", "Los Angeles Lakers", "Phoenix", "Sacramento"],
            "southwest": ["Dallas", "Houston", "Memphis", "New Orleans", "San Antonio"]
        }

        division_lower = division.lower()
        if division_lower in divisions:
            teams_in_div = divisions[division_lower]
            return [t for t in self.teams if any(city in t.team_name for city in teams_in_div)]
        return []

    def get_top_teams(self, n: int = 10, by: str = "wins") -> list[TeamStats]:
        """Get top N teams by specified stat.

        Args:
            n: Number of teams to return
            by: Stat to sort by (default: "wins")

        Returns:
            List of top N TeamStats sorted by the specified stat

        Example:
            >>> stats.get_top_teams(5)  # Top 5 by wins
            >>> stats.get_top_teams(10, by="points_per_game")  # Top 10 scorers
        """
        return self.sort_by_stat(by, reverse=True)[:n]


__all__ = ["TeamStats", "LeagueTeamStats"]
