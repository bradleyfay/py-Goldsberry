"""Pydantic models for Team Roster endpoint."""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RosterPlayer(BaseModel):
    """Player on a team roster.

    This model represents a player's information including their position,
    jersey number, and basic biographical data.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow both alias and field name
        validate_assignment=True,  # Validate when fields are updated
    )

    # Player identification
    team_id: int = Field(alias="TeamID")
    season: str = Field(alias="SEASON")
    league_id: str = Field(alias="LeagueID")
    player_id: int = Field(alias="PLAYER_ID")
    player_name: str = Field(alias="PLAYER")
    jersey_number: Optional[str] = Field(None, alias="NUM")
    position: Optional[str] = Field(None, alias="POSITION")

    # Player details
    height: Optional[str] = Field(None, alias="HEIGHT")
    weight: Optional[str] = Field(None, alias="WEIGHT")
    birth_date: Optional[str] = Field(None, alias="BIRTH_DATE")
    age: Optional[float] = Field(None, alias="AGE")
    experience: Optional[str] = Field(None, alias="EXP")
    school: Optional[str] = Field(None, alias="SCHOOL")

    # Roster status
    how_acquired: Optional[str] = Field(None, alias="HOW_ACQUIRED")

    def __str__(self) -> str:
        """Human-readable string representation."""
        position = f" ({self.position})" if self.position else ""
        number = f" #{self.jersey_number}" if self.jersey_number else ""
        return f"{self.player_name}{number}{position}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"RosterPlayer(player_id={self.player_id}, name='{self.player_name}', position='{self.position}')"


class Coach(BaseModel):
    """Coach on a team staff.

    This model represents a coach's information including their role,
    experience, and biographical data.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    # Coach identification
    team_id: int = Field(alias="TEAM_ID")
    season: str = Field(alias="SEASON")
    coach_id: str = Field(alias="COACH_ID")
    first_name: str = Field(alias="FIRST_NAME")
    last_name: str = Field(alias="LAST_NAME")
    coach_name: str = Field(alias="COACH_NAME")

    # Coach details
    coach_type: Optional[str] = Field(None, alias="COACH_TYPE")
    is_assistant: Optional[int] = Field(None, alias="IS_ASSISTANT")
    school: Optional[str] = Field(None, alias="SCHOOL")

    # Experience
    sort_sequence: Optional[int] = Field(None, alias="SORT_SEQUENCE")

    @property
    def is_head_coach(self) -> bool:
        """Whether this is the head coach."""
        return self.is_assistant == 0 if self.is_assistant is not None else False

    def __str__(self) -> str:
        """Human-readable string representation."""
        role = "Head Coach" if self.is_head_coach else "Assistant Coach"
        return f"{self.coach_name} ({role})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Coach(coach_id='{self.coach_id}', name='{self.coach_name}')"


class TeamRoster(BaseModel):
    """Complete team roster including players and coaches.

    This model aggregates all roster information for a team including
    the player roster and coaching staff.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    players: list[RosterPlayer] = Field(default_factory=list)
    coaches: list[Coach] = Field(default_factory=list)

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"TeamRoster: {len(self.players)} players, {len(self.coaches)} coaches"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"TeamRoster(players={len(self.players)}, coaches={len(self.coaches)})"

    def get_player_by_id(self, player_id: int) -> Optional[RosterPlayer]:
        """Get player by ID.

        Args:
            player_id: NBA player ID

        Returns:
            RosterPlayer if found, None otherwise
        """
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    def get_player_by_name(self, name: str) -> Optional[RosterPlayer]:
        """Get player by name (case-insensitive partial match).

        Args:
            name: Player name or partial name

        Returns:
            RosterPlayer if found, None otherwise
        """
        name_lower = name.lower()
        for player in self.players:
            if name_lower in player.player_name.lower():
                return player
        return None

    def get_players_by_position(self, position: str) -> list[RosterPlayer]:
        """Get all players at a specific position.

        Args:
            position: Position code (e.g., 'G', 'F', 'C', 'PG', 'SF')

        Returns:
            List of RosterPlayer objects
        """
        return [
            player
            for player in self.players
            if player.position and position.upper() in player.position.upper()
        ]

    @property
    def head_coach(self) -> Optional[Coach]:
        """Get the head coach.

        Returns:
            Coach object for head coach, None if not found
        """
        for coach in self.coaches:
            if coach.is_head_coach:
                return coach
        return None

    @property
    def assistant_coaches(self) -> list[Coach]:
        """Get all assistant coaches.

        Returns:
            List of Coach objects for assistant coaches
        """
        return [coach for coach in self.coaches if not coach.is_head_coach]


__all__ = ["RosterPlayer", "Coach", "TeamRoster"]
