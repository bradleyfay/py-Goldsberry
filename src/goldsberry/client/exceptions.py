"""Exception hierarchy for NBA API client.

Provides structured error handling with clear distinction between
different failure modes (network, API, validation, rate limiting).
"""

from typing import Any, Optional


class NBAAPIError(Exception):
    """Base exception for all NBA API errors.

    All exceptions raised by this library inherit from this base class,
    making it easy to catch any NBA API-related error.
    """

    def __init__(self, message: str, **context: Any) -> None:
        """Initialize exception with message and optional context.

        Args:
            message: Human-readable error description
            **context: Additional context (endpoint, parameters, response, etc.)
        """
        super().__init__(message)
        self.message = message
        self.context = context

    def __str__(self) -> str:
        """String representation including context if available."""
        if self.context:
            context_str = ", ".join(f"{k}={v!r}" for k, v in self.context.items())
            return f"{self.message} [{context_str}]"
        return self.message


class NetworkError(NBAAPIError):
    """Network-level errors (connection failures, DNS, etc.).

    Raised when the request cannot reach the NBA API servers.
    Usually indicates network connectivity issues or service unavailability.
    """


class TimeoutError(NetworkError):
    """Request timeout errors.

    Raised when the NBA API does not respond within the configured timeout period.
    This is unfortunately common with stats.nba.com endpoints.

    Attributes:
        timeout: The timeout value that was exceeded (seconds)
    """

    def __init__(self, message: str, timeout: float, **context: Any) -> None:
        """Initialize timeout error.

        Args:
            message: Error description
            timeout: Timeout value in seconds
            **context: Additional context
        """
        super().__init__(message, timeout=timeout, **context)
        self.timeout = timeout


class RateLimitError(NBAAPIError):
    """Rate limiting errors.

    Raised when too many requests have been made and the API
    is rejecting further requests. May include retry-after information.

    Attributes:
        retry_after: Seconds to wait before retrying (if known)
    """

    def __init__(
        self, message: str, retry_after: Optional[float] = None, **context: Any
    ) -> None:
        """Initialize rate limit error.

        Args:
            message: Error description
            retry_after: Suggested wait time in seconds (if provided by API)
            **context: Additional context
        """
        super().__init__(message, retry_after=retry_after, **context)
        self.retry_after = retry_after


class HTTPError(NBAAPIError):
    """HTTP-level errors (4xx, 5xx responses).

    Raised when the NBA API returns an HTTP error status code.

    Attributes:
        status_code: HTTP status code (e.g., 404, 500)
        response_text: Raw response body (if available)
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        response_text: Optional[str] = None,
        **context: Any,
    ) -> None:
        """Initialize HTTP error.

        Args:
            message: Error description
            status_code: HTTP status code
            response_text: Raw response body
            **context: Additional context
        """
        super().__init__(
            message, status_code=status_code, response_text=response_text, **context
        )
        self.status_code = status_code
        self.response_text = response_text


class NotFoundError(HTTPError):
    """Resource not found (404).

    Raised when the requested endpoint or resource does not exist.
    """

    def __init__(self, message: str, **context: Any) -> None:
        """Initialize not found error."""
        super().__init__(message, status_code=404, **context)


class ServerError(HTTPError):
    """Server-side errors (5xx).

    Raised when the NBA API server encounters an internal error.
    Usually indicates a problem on NBA's side, not ours.
    """


class ValidationError(NBAAPIError):
    """Request validation errors.

    Raised when request parameters are invalid or missing required fields.
    This is caught before making the actual API request.

    Attributes:
        invalid_params: Dictionary of parameter names to error messages
    """

    def __init__(
        self, message: str, invalid_params: Optional[dict[str, str]] = None, **context: Any
    ) -> None:
        """Initialize validation error.

        Args:
            message: Error description
            invalid_params: Map of param names to validation errors
            **context: Additional context
        """
        super().__init__(message, invalid_params=invalid_params, **context)
        self.invalid_params = invalid_params or {}


class ParseError(NBAAPIError):
    """Response parsing errors.

    Raised when the API response cannot be parsed or validated.
    May indicate API schema changes or malformed responses.

    Attributes:
        raw_response: The raw response that failed to parse
    """

    def __init__(self, message: str, raw_response: Optional[str] = None, **context: Any) -> None:
        """Initialize parse error.

        Args:
            message: Error description
            raw_response: Raw response text that failed parsing
            **context: Additional context
        """
        super().__init__(message, raw_response=raw_response, **context)
        self.raw_response = raw_response


class CircuitBreakerError(NBAAPIError):
    """Circuit breaker open error.

    Raised when the circuit breaker is open due to too many consecutive failures.
    Prevents hammering a known-bad endpoint.

    Attributes:
        failure_count: Number of consecutive failures
        reset_timeout: Seconds until circuit breaker resets
    """

    def __init__(
        self, message: str, failure_count: int, reset_timeout: float, **context: Any
    ) -> None:
        """Initialize circuit breaker error.

        Args:
            message: Error description
            failure_count: Consecutive failures that triggered breaker
            reset_timeout: Seconds until breaker resets
            **context: Additional context
        """
        super().__init__(
            message, failure_count=failure_count, reset_timeout=reset_timeout, **context
        )
        self.failure_count = failure_count
        self.reset_timeout = reset_timeout


class ConfigurationError(NBAAPIError):
    """Client configuration errors.

    Raised when the client is misconfigured (invalid timeout, bad base URL, etc.).
    """


__all__ = [
    "NBAAPIError",
    "NetworkError",
    "TimeoutError",
    "RateLimitError",
    "HTTPError",
    "NotFoundError",
    "ServerError",
    "ValidationError",
    "ParseError",
    "CircuitBreakerError",
    "ConfigurationError",
]
