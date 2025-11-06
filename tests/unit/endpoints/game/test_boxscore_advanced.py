"""Tests for Game Boxscore Advanced endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.game import BoxscoreAdvancedEndpoint, get_boxscore_advanced
from goldsberry.models.game import (
    BoxscoreAdvanced,
    PlayerBoxscoreAdvanced,
    TeamBoxscoreAdvanced,
)


# Fixture loader
@pytest.fixture
def boxscore_response():
    """Load boxscore advanced fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent
        / "fixtures"
        / "game"
        / "boxscore_advanced_response.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestBoxscoreAdvancedEndpoint:
    """Tests for BoxscoreAdvancedEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = BoxscoreAdvancedEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "boxscoreadvancedv2"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = BoxscoreAdvancedEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = BoxscoreAdvancedEndpoint()
        params = endpoint._build_params(game_id="0022400001")

        assert params["GameID"] == "0022400001"
        assert params["StartPeriod"] == 1
        assert params["EndPeriod"] == 10
        assert params["StartRange"] == 0
        assert params["EndRange"] == 28800
        assert params["RangeType"] == 2

    def test_build_params_custom_values(self):
        """Test parameter building with custom values."""
        endpoint = BoxscoreAdvancedEndpoint()
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
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        assert isinstance(result, BoxscoreAdvanced)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2

        # Test first player (Jayson Tatum)
        player1 = result.player_stats[0]
        assert isinstance(player1, PlayerBoxscoreAdvanced)
        assert player1.player_id == 1628369
        assert player1.player_name == "Jayson Tatum"
        assert player1.team_abbreviation == "BOS"
        assert player1.offensive_rating == 118.5
        assert player1.defensive_rating == 105.8
        assert player1.net_rating == 12.7
        assert player1.true_shooting_percentage == 0.615
        assert player1.usage_percentage == 28.4
        assert player1.pie == 0.185
        assert player1.start_position == "F"

        # Test team stats (Celtics)
        team1 = result.team_stats[0]
        assert isinstance(team1, TeamBoxscoreAdvanced)
        assert team1.team_id == 1610612738
        assert team1.team_name == "Celtics"
        assert team1.team_abbreviation == "BOS"
        assert team1.offensive_rating == 117.2
        assert team1.defensive_rating == 106.2
        assert team1.net_rating == 11.0
        assert team1.pace == 99.1

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, BoxscoreAdvanced)
        assert len(result.player_stats) == 0
        assert len(result.team_stats) == 0

    def test_fetch_sync(self, boxscore_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = boxscore_response

        endpoint = BoxscoreAdvancedEndpoint(mock_client)
        result = endpoint.fetch(game_id="0022400001")

        assert isinstance(result, BoxscoreAdvanced)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "boxscoreadvancedv2"
        params = call_args[1]["params"]
        assert params["GameID"] == "0022400001"
        assert params["StartPeriod"] == 1
        assert params["EndPeriod"] == 10

    @pytest.mark.asyncio
    async def test_fetch_async(self, boxscore_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=boxscore_response)

        endpoint = BoxscoreAdvancedEndpoint(mock_client)
        result = await endpoint.fetch_async(game_id="0022400001")

        assert isinstance(result, BoxscoreAdvanced)
        assert len(result.player_stats) == 6
        assert len(result.team_stats) == 2
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, boxscore_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=BoxscoreAdvanced(player_stats=[], team_stats=[]))
        monkeypatch.setattr(BoxscoreAdvancedEndpoint, "fetch", mock_fetch)

        result = get_boxscore_advanced(game_id="0022400001")

        assert isinstance(result, BoxscoreAdvanced)
        mock_fetch.assert_called_once()


class TestPlayerBoxscoreAdvancedModel:
    """Tests for PlayerBoxscoreAdvanced model."""

    def test_model_properties(self):
        """Test model with all fields."""
        player = PlayerBoxscoreAdvanced(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
            E_OFF_RATING=115.2,
            OFF_RATING=118.5,
            E_DEF_RATING=108.3,
            DEF_RATING=105.8,
            E_NET_RATING=6.9,
            NET_RATING=12.7,
            AST_PCT=23.5,
            AST_TOV=1.67,
            AST_RATIO=18.2,
            OREB_PCT=6.2,
            DREB_PCT=24.8,
            REB_PCT=15.1,
            TM_TOV_PCT=12.5,
            EFG_PCT=0.567,
            TS_PCT=0.615,
            USG_PCT=28.4,
            E_USG_PCT=29.1,
            E_PACE=98.5,
            PACE=99.2,
            PACE_PER40=99.8,
            POSS=68.5,
            PIE=0.185,
        )

        assert player.player_id == 1628369
        assert player.player_name == "Jayson Tatum"
        assert player.offensive_rating == 118.5
        assert player.defensive_rating == 105.8
        assert player.net_rating == 12.7
        assert player.true_shooting_percentage == 0.615
        assert player.usage_percentage == 28.4
        assert player.pie == 0.185
        assert player.is_starter is True

    def test_is_starter_property(self):
        """Test is_starter property."""
        starter = PlayerBoxscoreAdvanced(
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

        bench = PlayerBoxscoreAdvanced(
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

        bench_none = PlayerBoxscoreAdvanced(
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
        player = PlayerBoxscoreAdvanced(
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
        player_dnp = PlayerBoxscoreAdvanced(
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
        player_none = PlayerBoxscoreAdvanced(
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
        player = PlayerBoxscoreAdvanced(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Jayson Tatum",
            START_POSITION="F",
            COMMENT="",
            MIN="35:24",
            OFF_RATING=118.5,
            DEF_RATING=105.8,
            PIE=0.185,
        )

        str_repr = str(player)
        assert "Jayson Tatum" in str_repr
        assert "(BOS)" in str_repr
        assert "118.5" in str_repr
        assert "105.8" in str_repr
        assert "0.185" in str_repr

        repr_str = repr(player)
        assert "PlayerBoxscoreAdvanced" in repr_str
        assert "1628369" in repr_str
        assert "Jayson Tatum" in repr_str


class TestTeamBoxscoreAdvancedModel:
    """Tests for TeamBoxscoreAdvanced model."""

    def test_model_properties(self):
        """Test model with all fields."""
        team = TeamBoxscoreAdvanced(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_NAME="Celtics",
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            MIN="240:00",
            E_OFF_RATING=114.5,
            OFF_RATING=117.2,
            E_DEF_RATING=108.6,
            DEF_RATING=106.2,
            E_NET_RATING=5.9,
            NET_RATING=11.0,
            AST_PCT=62.5,
            AST_TOV=2.08,
            AST_RATIO=18.5,
            OREB_PCT=20.8,
            DREB_PCT=76.0,
            REB_PCT=48.0,
            TM_TOV_PCT=11.8,
            EFG_PCT=0.523,
            TS_PCT=0.582,
            USG_PCT=100.0,
            E_USG_PCT=100.0,
            E_PACE=98.5,
            PACE=99.1,
            PACE_PER40=99.5,
            POSS=102.4,
            PIE=0.528,
            EFG_PCT_OPP=0.482,
        )

        assert team.team_id == 1610612738
        assert team.team_name == "Celtics"
        assert team.offensive_rating == 117.2
        assert team.defensive_rating == 106.2
        assert team.net_rating == 11.0
        assert team.pace == 99.1

    def test_string_representations(self):
        """Test __str__ and __repr__ methods."""
        team = TeamBoxscoreAdvanced(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_NAME="Celtics",
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            MIN="240:00",
            OFF_RATING=117.2,
            DEF_RATING=106.2,
            PACE=99.1,
        )

        str_repr = str(team)
        assert "Celtics" in str_repr
        assert "117.2" in str_repr
        assert "106.2" in str_repr
        assert "99.1" in str_repr

        repr_str = repr(team)
        assert "TeamBoxscoreAdvanced" in repr_str
        assert "1610612738" in repr_str
        assert "Celtics" in repr_str


class TestBoxscoreAdvancedModel:
    """Tests for BoxscoreAdvanced model."""

    def test_get_team_stats(self, boxscore_response):
        """Test getting team stats by ID."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        team = result.get_team_stats(1610612738)
        assert team is not None
        assert team.team_name == "Celtics"

        not_found = result.get_team_stats(9999999)
        assert not_found is None

    def test_get_team_players(self, boxscore_response):
        """Test getting players by team."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        celtics_players = result.get_team_players(1610612738)
        assert len(celtics_players) == 3
        assert all(p.team_id == 1610612738 for p in celtics_players)

        lakers_players = result.get_team_players(1610612747)
        assert len(lakers_players) == 3

    def test_get_starters(self, boxscore_response):
        """Test getting starters."""
        endpoint = BoxscoreAdvancedEndpoint()
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
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        # All bench
        all_bench = result.get_bench_players()
        assert len(all_bench) == 2  # 1 Celtic, 1 Laker

        # Celtics bench
        celtics_bench = result.get_bench_players(team_id=1610612738)
        assert len(celtics_bench) == 1
        assert celtics_bench[0].player_name == "Payton Pritchard"

    def test_get_top_performers_by_pie(self, boxscore_response):
        """Test getting top performers by PIE."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        top_3 = result.get_top_performers_by_pie(limit=3)
        assert len(top_3) == 3
        assert top_3[0].player_name == "LeBron James"
        assert top_3[0].pie == 0.215
        assert top_3[1].player_name == "Jayson Tatum"
        assert top_3[1].pie == 0.185

    def test_get_top_performers_by_net_rating(self, boxscore_response):
        """Test getting top performers by net rating."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        top_3 = result.get_top_performers_by_net_rating(limit=3)
        assert len(top_3) == 3
        assert top_3[0].player_name == "Jayson Tatum"
        assert top_3[0].net_rating == 12.7
        assert top_3[1].player_name == "LeBron James"
        assert top_3[1].net_rating == 12.4

    def test_get_most_efficient_shooters(self, boxscore_response):
        """Test getting most efficient shooters."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        # With default min_minutes (10.0)
        efficient = result.get_most_efficient_shooters(limit=3)
        assert len(efficient) == 3
        assert efficient[0].player_name == "LeBron James"
        assert efficient[0].true_shooting_percentage == 0.638

        # With higher min_minutes threshold
        efficient_starters = result.get_most_efficient_shooters(limit=5, min_minutes=30.0)
        assert len(efficient_starters) == 4  # Only players with 30+ minutes

    def test_string_representations(self, boxscore_response):
        """Test __str__ and __repr__ methods."""
        endpoint = BoxscoreAdvancedEndpoint()
        result = endpoint._parse_response(boxscore_response)

        str_repr = str(result)
        assert "6 players" in str_repr
        assert "2 teams" in str_repr

        repr_str = repr(result)
        assert "BoxscoreAdvanced" in repr_str
        assert "players=6" in repr_str
        assert "teams=2" in repr_str

    def test_empty_boxscore(self):
        """Test empty boxscore model."""
        boxscore = BoxscoreAdvanced(player_stats=[], team_stats=[])

        assert len(boxscore.player_stats) == 0
        assert len(boxscore.team_stats) == 0
        assert boxscore.get_team_stats(1610612738) is None
        assert len(boxscore.get_team_players(1610612738)) == 0
        assert len(boxscore.get_starters()) == 0
        assert len(boxscore.get_top_performers_by_pie()) == 0

    def test_edge_case_none_values(self):
        """Test handling of None values in calculations."""
        player_no_stats = PlayerBoxscoreAdvanced(
            GAME_ID="0022400001",
            TEAM_ID=1610612738,
            TEAM_ABBREVIATION="BOS",
            TEAM_CITY="Boston",
            PLAYER_ID=1628369,
            PLAYER_NAME="Test Player",
            START_POSITION="F",
            COMMENT="",
            MIN="20:00",
            # All advanced stats are None
        )

        boxscore = BoxscoreAdvanced(player_stats=[player_no_stats], team_stats=[])

        # Should handle None values gracefully
        top_pie = boxscore.get_top_performers_by_pie(limit=1)
        assert len(top_pie) == 1
        assert top_pie[0].pie is None

        top_net = boxscore.get_top_performers_by_net_rating(limit=1)
        assert len(top_net) == 1

        efficient = boxscore.get_most_efficient_shooters(limit=1, min_minutes=15.0)
        assert len(efficient) == 1
