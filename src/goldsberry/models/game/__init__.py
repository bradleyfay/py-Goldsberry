"""Game-related Pydantic models."""

from .boxscore_advanced import (
    BoxscoreAdvanced,
    PlayerBoxscoreAdvanced,
    TeamBoxscoreAdvanced,
)
from .boxscore_traditional import (
    BoxscoreTraditional,
    PlayerBoxscoreTraditional,
    TeamBoxscoreTraditional,
)

__all__ = [
    "BoxscoreAdvanced",
    "BoxscoreTraditional",
    "PlayerBoxscoreAdvanced",
    "PlayerBoxscoreTraditional",
    "TeamBoxscoreAdvanced",
    "TeamBoxscoreTraditional",
]
