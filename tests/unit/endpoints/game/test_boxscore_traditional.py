"""Tests for Game Boxscore Traditional endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.game import BoxscoreTraditionalEndpoint, get_boxscore_traditional
from goldsberry.models.game import (
    BoxscoreTraditional,
    PlayerBoxscoreTraditional,
    TeamBoxscoreTraditional,
)


# Fixture loader
@pytest.fixture
def boxscore_response():
    """Load boxscore traditional fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent
        / "fixtures"
        / "game"
        / "boxscore_traditional_response.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestBoxscoreTraditionalEndpoint:
    """Tests for BoxscoreTraditionalEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = BoxscoreTraditionalEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "boxscoretraditionalv2"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = BoxscoreTraditionalEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = BoxscoreTraditionalEndpoint()
        params = endpoint._build_params(game_id="0022400001")

        assert params["GameID"] == "0022400001"
        assert params["StartPeriod"] == 1
        assert params["EndPeriod"] == 10
        assert params["StartRange"] == 0
        assert params["EndRange"] == 28800
        assert params["RangeType"] == 2

    def test_build_params_custom_values(self):
        """Test parameter building with custom values."""
        endpoint = BoxscoreTraditionalEndpoint()
        params = endpoint._build_params(
            game_id="0022400001",
            start_period=2,
            end_period=4,
            start_range=100,
            end_range=1000,
            range_type=1,
        )

        assert params["GameID"] == "0022400001"
        assert params["StartPeriod"] == 2
        assert params["EndPeriod"] == 4
        assert params["StartRange"] == 100
        assert params["EndRange"] == 1000
        assert params["RangeType"] == 1

    def test_parse_response(self, boxscore_response):
        """Test parsing of NBA API response."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        assert isinstance(result, BoxscoreTraditional)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2

        # Test first player (Jayson Tatum)
        player1 = result.player_stats[0]
        assert isinstance(player1, PlayerBoxscoreTraditional)
        assert player1.player_id == 1628369
        assert player1.player_name == "Jayson Tatum"
        assert player1.team_abbreviation == "BOS"
        assert player1.points == 30
        assert player1.rebounds == 10
        assert player1.assists == 5
        assert player1.start_position == "F"

        # Test team stats (Celtics)
        team1 = result.team_stats[0]
        assert isinstance(team1, TeamBoxscoreTraditional)
        assert team1.team_id == 1610612738
        assert team1.team_name == "Celtics"
        assert team1.team_abbreviation == "BOS"
        assert team1.points == 120

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, BoxscoreTraditional)
        assert len(result.player_stats) == 0
        assert len(result.team_stats) == 0

    def test_fetch_sync(self, boxscore_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = boxscore_response

        endpoint = BoxscoreTraditionalEndpoint(mock_client)
        result = endpoint.fetch(game_id="0022400001")

        assert isinstance(result, BoxscoreTraditional)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "boxscoretraditionalv2"
        params = call_args[1]["params"]
        assert params["GameID"] == "0022400001"
        assert params["StartPeriod"] == 1
        assert params["EndPeriod"] == 10

    @pytest.mark.asyncio
    async def test_fetch_async(self, boxscore_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=boxscore_response)

        endpoint = BoxscoreTraditionalEndpoint(mock_client)
        result = await endpoint.fetch_async(game_id="0022400001")

        assert isinstance(result, BoxscoreTraditional)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, boxscore_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=BoxscoreTraditional(player_stats=[], team_stats=[]))
        monkeypatch.setattr(BoxscoreTraditionalEndpoint, "fetch", mock_fetch)

        result = get_boxscore_traditional(game_id="0022400001")

        assert isinstance(result, BoxscoreTraditional)
        mock_fetch.assert_called_once()


class TestPlayerBoxscoreTraditionalModel:
    """Tests for PlayerBoxscoreTraditional model."""

    def test_model_properties(self):
        """Test model with all fields."""
        player = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
            FGM=10,
            FGA=20,
            FG_PCT=0.5,
            FG3M=4,
            FG3A=10,
            FG3_PCT=0.4,
            FTM=6,
            FTA=8,
            FT_PCT=0.75,
            OREB=2,
            DREB=8,
            REB=10,
            AST=5,
            STL=1,
            BLK=1,
            TO=3,
            PF=2,
            PTS=30,
            PLUS_MINUS=12,
        )

        assert player.player_id == 1628369
        assert player.player_name == "Jayson Tatum"
        assert player.points == 30
        assert player.rebounds == 10
        assert player.assists == 5
        assert player.is_starter is True

    def test_is_starter_property(self):
        """Test is_starter property."""
        starter = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
        )
        assert starter.is_starter is True

        bench = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1630162,
            PLAYER_NAME="Payton Pritchard",
            START_POSITION="",
            COMMENT="",
            MIN="18:45",
        )
        assert bench.is_starter is False

        bench_none = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1630162,
            PLAYER_NAME="Payton Pritchard",
            START_POSITION=None,
            COMMENT="",
            MIN="18:45",
        )
        assert bench_none.is_starter is False

    def test_minutes_played_property(self):
        """Test minutes_played property."""
        # Test normal time format
        player = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
        )
        assert abs(player.minutes_played - 35.4) < 0.01

        # Test no minutes
        player_dnp = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="",
        )
        assert player_dnp.minutes_played == 0.0

        # Test None minutes
        player_none = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN=None,
        )
        assert player_none.minutes_played == 0.0

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        player = PlayerBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
            PTS=30,
            REB=10,
            AST=5,
        )

        str_repr = str(player)
        assert "Jayson Tatum" in str_repr
        assert "(BOS)" in str_repr
        assert "30 PTS" in str_repr
        assert "10 REB" in str_repr
        assert "5 AST" in str_repr

        repr_str = repr(player)
        assert "PlayerBoxscoreTraditional" in repr_str
        assert "1628369" in repr_str
        assert "Jayson Tatum" in repr_str


class TestTeamBoxscoreTraditionalModel:
    """Tests for TeamBoxscoreTraditional model."""

    def test_model_properties(self):
        """Test model with all fields."""
        team = TeamBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_NAME="Celtics",
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            MIN="240:00",
            FGM=40,
            FGA=88,
            FG_PCT=0.455,
            FG3M=15,
            FG3A=42,
            FG3_PCT=0.357,
            FTM=25,
            FTA=30,
            FT_PCT=0.833,
            OREB=10,
            DREB=38,
            REB=48,
            AST=25,
            STL=8,
            BLK=5,
            TO=12,
            PF=18,
            PTS=120,
            PLUS_MINUS=10,
        )

        assert team.team_id == 1610612738
        assert team.team_name == "Celtics"
        assert team.points == 120

    def test_string_representations(self):
        """Test __str__ and __repr__ methods."""
        team = TeamBoxscoreTraditional(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_NAME="Celtics",
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            MIN="240:00",
            PTS=120,
        )

        str_repr = str(team)
        assert "Celtics" in str_repr
        assert "120 PTS" in str_repr

        repr_str = repr(team)
        assert "TeamBoxscoreTraditional" in repr_str
        assert "1610612738" in repr_str
        assert "Celtics" in repr_str


class TestBoxscoreTraditionalModel:
    """Tests for BoxscoreTraditional model."""

    def test_get_team_stats(self, boxscore_response):
        """Test getting team stats by ID."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        team = result.get_team_stats(1610612738)
        assert team is not None
        assert team.team_name == "Celtics"

        not_found = result.get_team_stats(9999999)
        assert not_found is None

    def test_get_team_players(self, boxscore_response):
        """Test getting players by team."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        celtics_players = result.get_team_players(1610612738)
        assert len(celtics_players) == 3
        assert all(p.team_id == 1610612738 for p in celtics_players)

        lakers_players = result.get_team_players(1610612747)
        assert len(lakers_players) == 3

    def test_get_starters(self, boxscore_response):
        """Test getting starters."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        # All starters
        all_starters = result.get_starters()
        assert len(all_starters) == 4  # 2 Celtics, 2 Lakers

        # Celtics starters
        celtics_starters = result.get_starters(team_id=1610612738)
        assert len(celtics_starters) == 2
        assert all(p.team_id == 1610612738 for p in celtics_starters)

    def test_get_bench_players(self, boxscore_response):
        """Test getting bench players."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        # All bench
        all_bench = result.get_bench_players()
        assert len(all_bench) == 2  # 1 Celtic, 1 Laker

        # Celtics bench
        celtics_bench = result.get_bench_players(team_id=1610612738)
        assert len(celtics_bench) == 1
        assert celtics_bench[0].player_name == "Payton Pritchard"

    def test_get_top_scorers(self, boxscore_response):
        """Test getting top scorers."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        top_3 = result.get_top_scorers(limit=3)
        assert len(top_3) == 3
        assert top_3[0].player_name == "LeBron James"
        assert top_3[0].points == 35
        assert top_3[1].player_name == "Jayson Tatum"
        assert top_3[1].points == 30

    def test_string_representations(self, boxscore_response):
        """Test __str__ and __repr__ methods."""
        endpoint = BoxscoreTraditionalEndpoint()
        result = endpoint._parse_response(boxscore_response)

        str_repr = str(result)
        assert "6 players" in str_repr
        assert "2 teams" in str_repr

        repr_str = repr(result)
        assert "BoxscoreTraditional" in repr_str
        assert "players=6" in repr_str
        assert "teams=2" in repr_str
