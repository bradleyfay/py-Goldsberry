"""Modern NBA Stats API client for Python.

Provides both synchronous and asynchronous interfaces to the NBA stats API
with comprehensive type safety, validation, and error handling.

Example:
    >>> from goldsberry.client import BaseClient
    >>> from goldsberry.endpoints.player import get_players
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

from importlib.metadata import version

__version__ = version("py-goldsberry")

from .client.base import BaseClient
from .client.exceptions import NBAAPIError

__all__ = [
    "__version__",
    "BaseClient",
    "NBAAPIError",
]
