"""Base HTTP client for NBA Stats API with retry logic and rate limiting.

Provides both synchronous and asynchronous interfaces with:
- Configurable timeouts and retries
- Exponential backoff for transient failures
- Rate limiting to avoid API blocks
- Comprehensive error handling
- Request/response logging support
"""

import asyncio
import logging
import time
from typing import Any, Optional
from urllib.parse import urljoin

import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
)

from .exceptions import (
    CircuitBreakerError,
    ConfigurationError,
    HTTPError,
    NetworkError,
    NotFoundError,
    ParseError,
    RateLimitError,
    ServerError,
    TimeoutError as NBATimeoutError,
)

logger = logging.getLogger(__name__)


# Default headers that mimic a browser to avoid blocking
DEFAULT_HEADERS = {
    "Host": "stats.nba.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://stats.nba.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}


class RateLimiter:
    """Token bucket rate limiter for API requests.

    Thread-safe implementation that ensures minimum time between requests.
    """

    def __init__(self, min_interval: float = 0.6) -> None:
        """Initialize rate limiter.

        Args:
            min_interval: Minimum seconds between requests (default 0.6s)
        """
        self.min_interval = min_interval
        self._last_request_time: float = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        """Wait if necessary to respect rate limit (async)."""
        async with self._lock:
            current_time = time.time()
            time_since_last = current_time - self._last_request_time

            if time_since_last < self.min_interval:
                wait_time = self.min_interval - time_since_last
                logger.debug(f"Rate limiting: waiting {wait_time:.2f}s")
                await asyncio.sleep(wait_time)

            self._last_request_time = time.time()

    def acquire_sync(self) -> None:
        """Wait if necessary to respect rate limit (sync)."""
        current_time = time.time()
        time_since_last = current_time - self._last_request_time

        if time_since_last < self.min_interval:
            wait_time = self.min_interval - time_since_last
            logger.debug(f"Rate limiting: waiting {wait_time:.2f}s")
            time.sleep(wait_time)

        self._last_request_time = time.time()


class CircuitBreaker:
    """Circuit breaker to prevent hammering broken endpoints.

    Opens after consecutive failures, closes after reset timeout.
    """

    def __init__(
        self, failure_threshold: int = 5, reset_timeout: float = 60.0
    ) -> None:
        """Initialize circuit breaker.

        Args:
            failure_threshold: Consecutive failures before opening
            reset_timeout: Seconds before attempting to close
        """
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self._failure_count = 0
        self._opened_at: Optional[float] = None
        self._lock = asyncio.Lock()

    @property
    def is_open(self) -> bool:
        """Check if circuit breaker is open."""
        if self._opened_at is None:
            return False

        # Check if enough time has passed to attempt reset
        if time.time() - self._opened_at >= self.reset_timeout:
            logger.info("Circuit breaker reset timeout reached, attempting to close")
            self._opened_at = None
            self._failure_count = 0
            return False

        return True

    async def call(self, func: Any, *args: Any, **kwargs: Any) -> Any:
        """Execute function with circuit breaker protection (async).

        Args:
            func: Async function to call
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Function result

        Raises:
            CircuitBreakerError: If circuit is open
        """
        async with self._lock:
            if self.is_open:
                raise CircuitBreakerError(
                    "Circuit breaker is open due to consecutive failures",
                    failure_count=self._failure_count,
                    reset_timeout=self.reset_timeout,
                )

        try:
            result = await func(*args, **kwargs)
            # Success: reset failure count
            async with self._lock:
                self._failure_count = 0
            return result

        except Exception as e:
            # Failure: increment count and potentially open breaker
            async with self._lock:
                self._failure_count += 1
                if self._failure_count >= self.failure_threshold:
                    self._opened_at = time.time()
                    logger.warning(
                        f"Circuit breaker opened after {self._failure_count} failures"
                    )
            raise e


class BaseClient:
    """Base HTTP client for NBA Stats API.

    Provides both sync and async methods with retry logic, rate limiting,
    and comprehensive error handling.
    """

    def __init__(
        self,
        base_url: str = "https://stats.nba.com/stats/",
        timeout: float = 30.0,
        max_retries: int = 3,
        rate_limit_interval: float = 0.6,
        enable_circuit_breaker: bool = True,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        """Initialize NBA API client.

        Args:
            base_url: Base URL for NBA Stats API
            timeout: Request timeout in seconds (default: 30s)
            max_retries: Maximum retry attempts for transient failures
            rate_limit_interval: Minimum seconds between requests
            enable_circuit_breaker: Enable circuit breaker pattern
            headers: Custom headers (merged with defaults)

        Raises:
            ConfigurationError: If configuration is invalid
        """
        if timeout <= 0:
            raise ConfigurationError("Timeout must be positive")
        if max_retries < 0:
            raise ConfigurationError("Max retries cannot be negative")
        if rate_limit_interval < 0:
            raise ConfigurationError("Rate limit interval cannot be negative")

        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

        # Merge custom headers with defaults
        self.headers = DEFAULT_HEADERS.copy()
        if headers:
            self.headers.update(headers)

        # Rate limiting and circuit breaker
        self.rate_limiter = RateLimiter(min_interval=rate_limit_interval)
        self.circuit_breaker = (
            CircuitBreaker() if enable_circuit_breaker else None
        )

        # HTTP clients (created lazily)
        self._sync_client: Optional[httpx.Client] = None
        self._async_client: Optional[httpx.AsyncClient] = None

    def _get_sync_client(self) -> httpx.Client:
        """Get or create sync HTTP client."""
        if self._sync_client is None:
            self._sync_client = httpx.Client(
                timeout=httpx.Timeout(self.timeout),
                follow_redirects=True,
                headers=self.headers,
            )
        return self._sync_client

    def _get_async_client(self) -> httpx.AsyncClient:
        """Get or create async HTTP client."""
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                timeout=httpx.Timeout(self.timeout),
                follow_redirects=True,
                headers=self.headers,
            )
        return self._async_client

    def close(self) -> None:
        """Close sync client (cleanup)."""
        if self._sync_client is not None:
            self._sync_client.close()
            self._sync_client = None

    async def aclose(self) -> None:
        """Close async client (cleanup)."""
        if self._async_client is not None:
            await self._async_client.aclose()
            self._async_client = None

    def __enter__(self) -> "BaseClient":
        """Context manager support."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager cleanup."""
        self.close()

    async def __aenter__(self) -> "BaseClient":
        """Async context manager support."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Async context manager cleanup."""
        await self.aclose()

    def _build_url(self, endpoint: str) -> str:
        """Build full URL from endpoint.

        Args:
            endpoint: API endpoint path

        Returns:
            Full URL
        """
        return urljoin(self.base_url, endpoint)

    def _handle_http_error(self, response: httpx.Response) -> None:
        """Convert HTTP error responses to exceptions.

        Args:
            response: HTTP response object

        Raises:
            HTTPError: For any non-2xx status code
        """
        if response.status_code == 404:
            raise NotFoundError(
                f"Endpoint not found: {response.url}",
                response_text=response.text,
            )

        if 400 <= response.status_code < 500:
            raise HTTPError(
                f"Client error {response.status_code}: {response.text[:200]}",
                status_code=response.status_code,
                response_text=response.text,
            )

        if response.status_code >= 500:
            raise ServerError(
                f"Server error {response.status_code}: {response.text[:200]}",
                status_code=response.status_code,
                response_text=response.text,
            )

    def _should_retry(self, exception: Exception) -> bool:
        """Determine if exception is retryable.

        Args:
            exception: Exception that occurred

        Returns:
            True if should retry
        """
        # Retry on network errors, timeouts, and server errors
        if isinstance(exception, (NetworkError, NBATimeoutError, ServerError)):
            return True

        # Retry on specific httpx exceptions
        if isinstance(exception, (httpx.TimeoutException, httpx.NetworkError)):
            return True

        return False

    @retry(
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.NetworkError, ServerError)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True,
    )
    async def _request_async(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make async HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters

        Returns:
            JSON response as dict

        Raises:
            Various NBA API exceptions
        """
        # Rate limiting
        await self.rate_limiter.acquire()

        # Build request
        url = self._build_url(endpoint)
        client = self._get_async_client()

        logger.debug(f"Request: {method} {url} params={params}")

        try:
            # Make request
            response = await client.request(method, url, params=params)

            # Check for HTTP errors
            if not response.is_success:
                self._handle_http_error(response)

            # Parse JSON
            try:
                data = response.json()
                logger.debug(f"Response: {len(str(data))} bytes")
                return data

            except ValueError as e:
                raise ParseError(
                    f"Failed to parse JSON response: {e}",
                    raw_response=response.text[:500],
                ) from e

        except httpx.TimeoutException as e:
            raise NBATimeoutError(
                f"Request timed out after {self.timeout}s",
                timeout=self.timeout,
                endpoint=endpoint,
            ) from e

        except httpx.NetworkError as e:
            raise NetworkError(
                f"Network error: {e}",
                endpoint=endpoint,
            ) from e

    def _request_sync(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make sync HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters

        Returns:
            JSON response as dict

        Raises:
            Various NBA API exceptions
        """
        # Rate limiting
        self.rate_limiter.acquire_sync()

        # Build request
        url = self._build_url(endpoint)
        client = self._get_sync_client()

        logger.debug(f"Request: {method} {url} params={params}")

        # Retry logic (manual for sync)
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                # Make request
                response = client.request(method, url, params=params)

                # Check for HTTP errors
                if not response.is_success:
                    self._handle_http_error(response)

                # Parse JSON
                try:
                    data = response.json()
                    logger.debug(f"Response: {len(str(data))} bytes")
                    return data

                except ValueError as e:
                    raise ParseError(
                        f"Failed to parse JSON response: {e}",
                        raw_response=response.text[:500],
                    ) from e

            except httpx.TimeoutException as e:
                last_exception = NBATimeoutError(
                    f"Request timed out after {self.timeout}s",
                    timeout=self.timeout,
                    endpoint=endpoint,
                )
                if attempt < self.max_retries - 1:
                    wait_time = min(2 ** attempt, 10)
                    logger.warning(f"Timeout, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                raise last_exception from e

            except httpx.NetworkError as e:
                last_exception = NetworkError(
                    f"Network error: {e}",
                    endpoint=endpoint,
                )
                if attempt < self.max_retries - 1:
                    wait_time = min(2 ** attempt, 10)
                    logger.warning(f"Network error, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                raise last_exception from e

            except ServerError as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    wait_time = min(2 ** attempt, 10)
                    logger.warning(f"Server error, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                raise

        # Should never reach here, but just in case
        if last_exception:
            raise last_exception
        raise NetworkError("Unknown error during request")

    async def get_async(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make async GET request.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            JSON response

        Raises:
            Various NBA API exceptions
        """
        if self.circuit_breaker:
            return await self.circuit_breaker.call(
                self._request_async, "GET", endpoint, params
            )
        return await self._request_async("GET", endpoint, params)

    def get(
        self, endpoint: str, params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """Make sync GET request.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            JSON response

        Raises:
            Various NBA API exceptions
        """
        return self._request_sync("GET", endpoint, params)


__all__ = ["BaseClient", "RateLimiter", "CircuitBreaker"]
