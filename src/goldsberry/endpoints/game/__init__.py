"""Game endpoints."""

from .boxscore_advanced import BoxscoreAdvancedEndpoint, get_boxscore_advanced
from .boxscore_traditional import BoxscoreTraditionalEndpoint, get_boxscore_traditional

__all__ = [
    "BoxscoreAdvancedEndpoint",
    "BoxscoreTraditionalEndpoint",
    "get_boxscore_advanced",
    "get_boxscore_traditional",
]
