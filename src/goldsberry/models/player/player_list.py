"""Player list models.

Models for the commonallplayers endpoint which returns a list of all players.
"""

from typing import Optional

from pydantic import Field

from ..base import NBABaseModel


class PlayerInfo(NBABaseModel):
    """Individual player information from player list endpoint.

    Represents a single player's basic information as returned
    by the commonallplayers endpoint.
    """

    person_id: int = Field(..., alias="PERSON_ID", description="Player's unique ID")
    display_last_comma_first: str = Field(
        ..., alias="DISPLAY_LAST_COMMA_FIRST", description="Name as 'Last, First'"
    )
    display_first_last: str = Field(
        ..., alias="DISPLAY_FIRST_LAST", description="Name as 'First Last'"
    )
    roster_status: int = Field(
        ..., alias="ROSTERSTATUS", description="1 if active, 0 if inactive"
    )
    from_year: str = Field(..., alias="FROM_YEAR", description="First season")
    to_year: str = Field(..., alias="TO_YEAR", description="Last season")
    player_code: str = Field(
        ..., alias="PLAYERCODE", description="Internal player code"
    )
    team_id: int = Field(..., alias="TEAM_ID", description="Current team ID (0 if none)")
    team_city: Optional[str] = Field(
        None, alias="TEAM_CITY", description="Current team city"
    )
    team_name: Optional[str] = Field(
        None, alias="TEAM_NAME", description="Current team name"
    )
    team_abbreviation: Optional[str] = Field(
        None, alias="TEAM_ABBREVIATION", description="Current team abbreviation"
    )
    jersey_number: Optional[str] = Field(
        None, alias="JERSEY_NUMBER", description="Current jersey number"
    )
    position: Optional[str] = Field(None, alias="POSITION", description="Position")
    height: Optional[str] = Field(None, alias="HEIGHT", description="Height (e.g., '6-9')")
    weight: Optional[str] = Field(None, alias="WEIGHT", description="Weight (e.g., '250')")
    college: Optional[str] = Field(None, alias="COLLEGE", description="College attended")
    country: Optional[str] = Field(None, alias="COUNTRY", description="Country of origin")
    draft_year: Optional[str] = Field(None, alias="DRAFT_YEAR", description="Draft year")
    draft_round: Optional[str] = Field(None, alias="DRAFT_ROUND", description="Draft round")
    draft_number: Optional[str] = Field(
        None, alias="DRAFT_NUMBER", description="Draft pick number"
    )
    greatest_75_flag: Optional[str] = Field(
        None, alias="GREATEST_75_FLAG", description="NBA 75th anniversary team flag"
    )

    @property
    def is_active(self) -> bool:
        """Check if player is currently active.

        Returns:
            True if player is on an active roster
        """
        return self.roster_status == 1

    @property
    def full_name(self) -> str:
        """Get player's full name in 'First Last' format.

        Returns:
            Player's display name
        """
        return self.display_first_last

    def __str__(self) -> str:
        """String representation."""
        status = "Active" if self.is_active else "Inactive"
        team_info = f" ({self.team_abbreviation})" if self.team_abbreviation else ""
        return f"{self.full_name}{team_info} [{status}]"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PlayerInfo(id={self.person_id}, name='{self.full_name}', active={self.is_active})"


__all__ = ["PlayerInfo"]
