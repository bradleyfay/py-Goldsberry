# Architecture Decision Records (ADR)

> **Last Updated**: 2025-11-06
> **Purpose**: Document significant architectural and technical decisions made during py-Goldsberry v2.0 development

## Overview

This document records key decisions, the context in which they were made, alternatives considered, and the rationale for the final choice. This helps future contributors understand "why" not just "what."

---

## ADR-001: HTTP Client Library

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

py-Goldsberry v1.x used the `requests` library for HTTP communication. For v2.0, we need an HTTP client that supports:
- Synchronous requests (for simple usage)
- Asynchronous requests (for concurrent operations)
- Connection pooling (for performance)
- Modern Python features

### Decision

Use **httpx** as the HTTP client library.

### Alternatives Considered

1. **requests** (v1.x choice)
   - Pros: Battle-tested, widely used, familiar
   - Cons: No async support, would need separate async library
   - Verdict: Rejected (can't meet async requirement)

2. **aiohttp**
   - Pros: Async-first, mature async library
   - Cons: Async-only, would need requests for sync, two dependencies
   - Verdict: Rejected (forces async, want sync to be simple)

3. **httpx**
   - Pros: Both sync and async, single API, modern, active maintenance
   - Cons: Newer than requests (less battle-tested)
   - Verdict: **Selected**

### Rationale

httpx provides a unified API for both sync and async requests. Users who want simple synchronous code can use it directly. Users who need performance can use async without changing libraries. Single dependency is cleaner than requests + aiohttp.

### Consequences

**Positive**:
- Single import for both sync and async
- Consistent API regardless of sync/async choice
- HTTP/2 support (future benefit)
- Active development and maintenance

**Negative**:
- Slightly less proven than requests (mitigated by solid test suite)
- Learning curve for contributors familiar with requests (minimal, API is similar)

**Neutral**:
- Need to learn httpx-specific features (timeout handling, connection pooling)

---

## ADR-002: Validation Library

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

NBA API responses are untyped JSON. We need runtime validation to:
- Catch schema changes immediately
- Provide type safety to users
- Convert API responses to Python objects
- Handle missing/optional fields gracefully

### Decision

Use **Pydantic v2** for data validation and modeling.

### Alternatives Considered

1. **dataclasses** (stdlib)
   - Pros: No external dependency, built-in, simple
   - Cons: No validation, no alias support, manual parsing
   - Verdict: Rejected (insufficient features)

2. **attrs**
   - Pros: Lightweight, battle-tested
   - Cons: No validation, would need separate validation library
   - Verdict: Rejected (need validation)

3. **Pydantic v1**
   - Pros: Excellent validation, field aliases, battle-tested
   - Cons: Slower than v2, older architecture
   - Verdict: Rejected (v2 is significantly better)

4. **Pydantic v2**
   - Pros: 5-50x faster than v1, better errors, modern features
   - Cons: Newer (less tested), breaking changes from v1
   - Verdict: **Selected**

### Rationale

Pydantic v2 provides exactly what we need: runtime validation, field aliases (for NBA API's ALL_CAPS names), computed properties, and excellent error messages. The performance improvement over v1 is significant for large datasets (e.g., all players). Since this is a new major version, we can start with v2 without migration burden.

### Consequences

**Positive**:
- Fast validation (5-50x faster than Pydantic v1)
- Clear error messages when API schema changes
- Type hints work perfectly with mypy
- Field aliases handle NBA API naming conventions
- Computed properties for derived data

**Negative**:
- Pydantic v2 is newer (less battle-tested than v1)
- Breaking changes if we ever need to support v1

**Neutral**:
- Contributors need to learn Pydantic patterns
- Model definitions are verbose (but explicit and safe)

---

## ADR-003: Retry Logic Library

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

NBA stats API is unreliable (frequent timeouts, 5xx errors). We need automatic retry logic with:
- Exponential backoff (don't hammer failing endpoints)
- Configurable retry count
- Different strategies for different errors
- Support for both sync and async

### Decision

Use **tenacity** for retry logic.

### Alternatives Considered

1. **retrying** (v1.x choice)
   - Pros: Simple API, worked in v1.x
   - Cons: No async support, less flexible, maintenance unclear
   - Verdict: Rejected (no async)

2. **backoff**
   - Pros: Decorator-based, simple
   - Cons: Less flexible, harder to customize per-endpoint
   - Verdict: Rejected (insufficient flexibility)

3. **tenacity**
   - Pros: Flexible, async support, active maintenance, composable
   - Cons: Slightly more complex API
   - Verdict: **Selected**

4. **Custom implementation**
   - Pros: Full control, no dependency
   - Cons: Reimplementing well-solved problem, testing burden
   - Verdict: Rejected (not worth the effort)

### Rationale

tenacity provides a clean, flexible API for retry logic that works with both sync and async code. The composable retry strategies (retry on timeout, retry on 5xx, exponential backoff) fit our needs perfectly. Active maintenance and good documentation.

### Consequences

**Positive**:
- Works seamlessly with both sync and async
- Exponential backoff prevents hammering broken endpoints
- Can customize retry behavior per endpoint if needed
- Clear logs of retry attempts

**Negative**:
- Slightly more complex than `retrying` (mitigated by good docs)
- One more dependency

**Neutral**:
- Need to configure retry strategies explicitly (forces us to think through error handling)

---

## ADR-004: Project Layout

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

Python packaging has evolved. Need to choose between flat layout and src layout:

**Flat layout**:
```
goldsberry/
    __init__.py
    client.py
tests/
```

**Src layout**:
```
src/
    goldsberry/
        __init__.py
        client.py
tests/
```

### Decision

Use **src/ layout**.

### Alternatives Considered

1. **Flat layout** (v1.x choice)
   - Pros: Simpler, fewer directories, traditional
   - Cons: Can accidentally import development code instead of installed package
   - Verdict: Rejected (error-prone)

2. **Src layout**
   - Pros: Prevents import errors, forces proper installation, modern best practice
   - Cons: Extra directory level
   - Verdict: **Selected**

### Rationale

The src layout prevents a common bug: importing from the development directory instead of the installed package. When tests run, they use the installed package, ensuring we're testing what users will actually install. This is the modern Python packaging best practice (PEP 517/518).

### Consequences

**Positive**:
- Tests always use installed package (catches packaging issues)
- Clear separation between source and tests
- Follows modern best practices
- Prevents accidental imports from wrong location

**Negative**:
- One extra directory level
- Contributors need to install in editable mode (`pip install -e .`)

**Neutral**:
- Different from v1.x structure (breaking change anyway)

---

## ADR-005: Testing Strategy

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

NBA stats API is unreliable. Unit tests that make real HTTP requests would be:
- Slow (30+ seconds timeout per request)
- Flaky (API frequently fails)
- Blocked by rate limiting
- Not CI-friendly

Need to decide: mock the API or make real requests?

### Decision

**Mock the NBA API in unit tests** using captured fixtures.

Optional integration tests (marked separately) can make real requests.

### Alternatives Considered

1. **Real HTTP requests in all tests**
   - Pros: Tests actual API behavior
   - Cons: Slow, flaky, rate-limited, CI unfriendly
   - Verdict: Rejected (unusable in practice)

2. **VCR.py (record/replay)**
   - Pros: Automatic fixture creation, real requests once
   - Cons: Fixtures become stale, large fixture files, complexity
   - Verdict: Rejected (overly complex)

3. **Mock with captured fixtures** (+ optional integration tests)
   - Pros: Fast, reliable, CI-friendly, fixtures explicit
   - Cons: Fixtures can become stale
   - Verdict: **Selected**

### Rationale

Fast, reliable tests are more valuable than tests that exercise the actual (unreliable) API. By capturing real responses as fixtures, we test our code's ability to parse real data without depending on API availability. Optional integration tests (marked with `@pytest.mark.integration`) can run separately for those who want to verify live API compatibility.

### Consequences

**Positive**:
- Tests run in milliseconds, not seconds
- Tests never fail due to API timeouts
- Can run tests offline
- CI is fast and reliable
- Can run tests frequently during development

**Negative**:
- Fixtures can become stale if NBA changes API
- Not testing actual HTTP layer (httpx, retries)

**Mitigation**:
- Optional integration tests to detect API changes
- Periodic manual verification against live API
- Capture new fixtures when API changes detected

---

## ADR-006: Python Version Support

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

Need to decide minimum Python version. Considerations:
- Modern features (type hints, async, etc.)
- User base (who's still on older Python?)
- Maintenance burden (more versions = more testing)

### Decision

Require **Python 3.9+** (no Python 3.8 or Python 2 support).

### Alternatives Considered

1. **Python 3.7+**
   - Pros: Wider compatibility
   - Cons: Missing modern features, 3.7 EOL June 2023
   - Verdict: Rejected (already EOL)

2. **Python 3.8+**
   - Pros: Still relatively common
   - Cons: EOL October 2024, missing PEP 585 type hints
   - Verdict: Rejected (EOL imminent)

3. **Python 3.9+**
   - Pros: PEP 585 (list[str] vs List[str]), stable, long support
   - Cons: Some users still on 3.8
   - Verdict: **Selected**

4. **Python 3.11+**
   - Pros: Latest features, best performance
   - Cons: Too aggressive, many users on 3.9/3.10
   - Verdict: Rejected (too limiting)

### Rationale

Python 3.9 provides modern type hints (PEP 585) without being too aggressive. Python 3.8 is EOL October 2024, so supporting it provides minimal value. By starting with 3.9+, we avoid technical debt from day one. Users on older Python can use v1.x.

### Consequences

**Positive**:
- Modern type hints (list[str] instead of List[str])
- Cleaner code (no compatibility hacks)
- Fewer test matrices (3.9, 3.10, 3.11, 3.12 instead of 7 versions)
- Long support window (3.9 EOL October 2025)

**Negative**:
- Users on Python 3.8 or earlier cannot upgrade to v2.0
- Some corporate environments lag on Python versions

**Mitigation**:
- v1.x remains available for older Python
- Clear communication of requirements
- Python 3.9+ is 3+ years old (released October 2020)

---

## ADR-007: Error Handling Strategy

**Date**: 2025-11-06
**Status**: Accepted
**Deciders**: Bradley Fay

### Context

NBA API can fail in many ways:
- Timeouts (most common)
- 5xx errors (server issues)
- 4xx errors (bad parameters)
- Network errors (DNS, connection)
- Invalid JSON responses
- Schema validation errors

Need structured error handling that:
- Distinguishes error types
- Provides context for debugging
- Allows users to handle different errors differently

### Decision

Create **structured exception hierarchy** with rich context.

### Alternatives Considered

1. **Generic exceptions**
   - Pros: Simple
   - Cons: Users can't distinguish error types, no context
   - Verdict: Rejected (insufficient)

2. **Exception codes**
   - Pros: Programmatic error handling
   - Cons: Hard to remember codes, docs required
   - Verdict: Rejected (Python isn't Go)

3. **Structured exception hierarchy with context**
   - Pros: Pythonic, self-documenting, rich context
   - Cons: More exception classes to maintain
   - Verdict: **Selected**

### Rationale

Python's exception system is designed for inheritance hierarchies. By creating specific exception types (TimeoutError, ValidationError, etc.), users can catch exactly what they want. Including context (endpoint, params, timeout value) in exceptions makes debugging much easier.

### Consequences

**Positive**:
- Users can catch specific exceptions
- Exception messages are informative
- Easy to debug failures
- Follows Python conventions

**Negative**:
- More exception classes to document
- Need to be disciplined about adding context

**Exception Hierarchy**:
```
NBAAPIError (base)
├── HTTPError
│   ├── TimeoutError
│   ├── RateLimitError
│   └── ServerError
├── ValidationError
├── ParseError
└── EndpointNotFoundError
```

---

## ADR-008: Package Naming (nba_api vs goldsberry)

**Date**: 2025-11-06
**Status**: Corrected
**Deciders**: Bradley Fay

### Context

During initial development, the package was mistakenly named `nba_api` (conflicting with an existing popular package). This was corrected before release.

### Decision

Keep **goldsberry** as the package name (PyPI: py-goldsberry, import: goldsberry).

### Alternatives Considered

1. **nba_api**
   - Pros: Descriptive, clear purpose
   - Cons: Name collision with existing package (https://pypi.org/project/nba-api/)
   - Verdict: Rejected (namespace collision)

2. **goldsberry** (original)
   - Pros: Unique name, honors Kirk Goldsberry, established brand
   - Cons: Not immediately descriptive
   - Verdict: **Selected**

3. **goldsberry2** or **goldsberry-ng**
   - Pros: Differentiates from v1.x
   - Cons: Awkward, suggests permanent fork
   - Verdict: Rejected (v2.0 is the successor, not a fork)

### Rationale

The existing `goldsberry` name has value (GitHub stars, PyPI downloads, community). The name honors Kirk Goldsberry, whose work inspired the package. Choosing `nba_api` would cause confusion with the existing package and was a mistake during initial development.

### Consequences

**Positive**:
- Unique namespace (no collision)
- Maintains brand recognition
- Honors the original inspiration

**Negative**:
- Name doesn't immediately convey "NBA stats API"
- Need to explain the name to new users

**Mitigation**:
- Clear tagline: "NBA stats API client"
- Comprehensive documentation
- Good SEO (basketball, NBA, stats, analytics)

---

## Future Decisions (To Be Made)

### FD-001: Caching Layer

**Context**: Users may want to cache API responses to reduce requests.

**Options**:
- No caching (current)
- Optional caching middleware
- Built-in caching with TTL

**Status**: Deferred to post-v2.0

### FD-002: Authentication

**Context**: NBA could add API key requirements.

**Options**:
- No auth (current)
- API key support
- OAuth support

**Status**: Deferred until NBA requires it

### FD-003: Alternative Backends

**Context**: NBA could change API structure or offer GraphQL.

**Options**:
- Single backend (current)
- Pluggable backend system
- Multi-backend support

**Status**: Deferred until needed

---

**Last Updated**: 2025-11-06
**Maintained by**: Bradley Fay (bradley.fay@gmail.com)
