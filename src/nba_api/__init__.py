"""Modern NBA Stats API client for Python.

Provides both synchronous and asynchronous interfaces to the NBA stats API
with comprehensive type safety, validation, and error handling.

Example:
    >>> from nba_api.client import BaseClient
    >>> from nba_api.endpoints.player import get_players
    >>>
    >>> # Quick usage
    >>> players = get_players(season="2024-25")
    >>> print(f"Found {len(players)} players")
    >>>
    >>> # With custom client
    >>> with BaseClient(timeout=60) as client:
    ...     endpoint = PlayerListEndpoint(client)
    ...     players = endpoint.fetch()
"""

__version__ = "2.0.0-alpha.1"
__author__ = "Bradley Fay"
__email__ = "bradley.fay@gmail.com"

from .client.base import BaseClient
from .client.exceptions import NBAAPIError

__all__ = [
    "__version__",
    "BaseClient",
    "NBAAPIError",
]
