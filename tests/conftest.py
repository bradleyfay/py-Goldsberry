"""Pytest configuration and shared fixtures."""

import json
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture
def fixtures_dir() -> Path:
    """Get fixtures directory path."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def load_fixture(fixtures_dir: Path):
    """Factory fixture to load JSON fixtures.

    Usage:
        def test_something(load_fixture):
            data = load_fixture("player/player_list_response.json")
            assert "resultSets" in data
    """

    def _load(fixture_path: str) -> dict[str, Any]:
        """Load JSON fixture from file.

        Args:
            fixture_path: Relative path to fixture file

        Returns:
            Parsed JSON data
        """
        full_path = fixtures_dir / fixture_path
        with open(full_path) as f:
            return json.load(f)

    return _load


@pytest.fixture
def mock_client_response(monkeypatch):
    """Factory fixture to mock BaseClient responses.

    Usage:
        def test_endpoint(mock_client_response):
            mock_client_response({"resultSets": [...]})
            # Now client.get() will return mocked data
    """

    def _mock(response_data: dict[str, Any]) -> None:
        """Mock client.get() and client.get_async() to return data.

        Args:
            response_data: Data to return from mocked client
        """
        from nba_api.client.base import BaseClient

        def mock_get(self, endpoint: str, params=None):
            return response_data

        async def mock_get_async(self, endpoint: str, params=None):
            return response_data

        monkeypatch.setattr(BaseClient, "get", mock_get)
        monkeypatch.setattr(BaseClient, "get_async", mock_get_async)

    return _mock
