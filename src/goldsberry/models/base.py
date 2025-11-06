"""Base Pydantic models for NBA API responses.

Provides common patterns and utilities for parsing NBA API response structures.
"""

from typing import Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field


class NBABaseModel(BaseModel):
    """Base model for all NBA API response objects.

    Provides common configuration and utilities.
    """

    model_config = ConfigDict(
        # Allow extra fields from API (they add fields sometimes)
        extra="ignore",
        # Use strict type validation
        strict=False,
        # Validate on assignment
        validate_assignment=True,
        # Populate by field name (API uses different naming)
        populate_by_name=True,
    )


class NBAResultSet(NBABaseModel):
    """Represents a single NBA API result set.

    NBA API returns data as result sets with headers and rows.
    This model helps parse that structure.
    """

    name: str = Field(..., description="Name of this result set")
    headers: list[str] = Field(..., description="Column headers")
    row_set: list[list[Any]] = Field(
        ..., alias="rowSet", description="Data rows"
    )

    def to_dicts(self) -> list[dict[str, Any]]:
        """Convert rows to list of dictionaries.

        Returns:
            List of dicts mapping header names to row values
        """
        return [dict(zip(self.headers, row)) for row in self.row_set]


T = TypeVar("T", bound=NBABaseModel)


class NBAResponse(NBABaseModel, Generic[T]):
    """Generic NBA API response wrapper.

    Handles the common response structure:
    {
        "resource": "endpoint_name",
        "parameters": {...},
        "resultSets": [...]  or "resultSet": [...]
    }
    """

    resource: str = Field(..., description="API endpoint name")
    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Request parameters"
    )
    result_sets: list[NBAResultSet] = Field(
        default_factory=list,
        alias="resultSets",
        description="Result sets (plural)",
    )
    result_set: list[NBAResultSet] = Field(
        default_factory=list,
        alias="resultSet",
        description="Result set (singular)",
    )

    @property
    def results(self) -> list[NBAResultSet]:
        """Get result sets (handles both plural and singular)."""
        return self.result_sets or self.result_set

    def get_result_set(self, index: int = 0) -> NBAResultSet:
        """Get a specific result set by index.

        Args:
            index: Result set index (default: 0)

        Returns:
            Result set at that index

        Raises:
            IndexError: If index out of range
        """
        results = self.results
        if not results:
            raise ValueError("No result sets in response")
        return results[index]

    def get_dicts(self, index: int = 0) -> list[dict[str, Any]]:
        """Get result set as list of dicts.

        Args:
            index: Result set index (default: 0)

        Returns:
            List of dictionaries
        """
        return self.get_result_set(index).to_dicts()


class SingleResultMixin:
    """Mixin for endpoints that return a single result set.

    Provides convenience property to access the first result set.
    """

    result_set_index: ClassVar[int] = 0

    def get_data(self: "NBAResponse[T]") -> list[dict[str, Any]]:
        """Get the primary result set as list of dicts.

        Returns:
            List of dictionaries from primary result set
        """
        return self.get_dicts(self.result_set_index)


def parse_nba_response(
    data: dict[str, Any], model_class: type[T]
) -> list[T]:
    """Parse NBA API response into typed models.

    Takes raw API response and converts the primary result set
    into a list of typed Pydantic models.

    Args:
        data: Raw JSON response from NBA API
        model_class: Pydantic model class to parse into

    Returns:
        List of parsed model instances

    Example:
        >>> data = client.get("commonallplayers", params={...})
        >>> players = parse_nba_response(data, PlayerInfo)
    """
    # Parse response structure
    response = NBAResponse[model_class](**data)

    # Get primary result set as dicts
    dicts = response.get_dicts(0)

    # Parse each dict into model
    return [model_class(**d) for d in dicts]


__all__ = [
    "NBABaseModel",
    "NBAResultSet",
    "NBAResponse",
    "SingleResultMixin",
    "parse_nba_response",
]
