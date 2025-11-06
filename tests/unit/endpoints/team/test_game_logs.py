"""Tests for Team GameLogs endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.team import TeamGameLogsEndpoint, get_team_game_logs
from goldsberry.enums.common import Season, SeasonType
from goldsberry.models.team import TeamGameLog, TeamGameLogs


# Fixture loader
@pytest.fixture
def game_logs_response():
    """Load team game logs fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent
        / "fixtures"
        / "team"
        / "game_logs_response.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestTeamGameLogsEndpoint:
    """Tests for TeamGameLogsEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = TeamGameLogsEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "teamgamelog"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = TeamGameLogsEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = TeamGameLogsEndpoint()
        params = endpoint._build_params(team_id=1610612738)

        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2024-25"
        assert params["SeasonType"] == "Regular Season"
        assert params["LeagueID"] == "00"

    def test_build_params_with_enums(self):
        """Test parameter building with enum values."""
        endpoint = TeamGameLogsEndpoint()
        params = endpoint._build_params(
            team_id=1610612738,
            season=Season.SEASON_2023_24,
            season_type=SeasonType.PLAYOFFS,
        )

        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2023-24"
        assert params["SeasonType"] == "Playoffs"

    def test_build_params_with_strings(self):
        """Test parameter building with string values."""
        endpoint = TeamGameLogsEndpoint()
        params = endpoint._build_params(
            team_id=1610612738,
            season="2022-23",
            season_type="Pre Season",
        )

        assert params["Season"] == "2022-23"
        assert params["SeasonType"] == "Pre Season"

    def test_parse_response(self, game_logs_response):
        """Test parsing of NBA API response."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        assert isinstance(result, TeamGameLogs)
        assert len(result.games) == 3

        # Test first game (most recent win vs MIA)
        game1 = result.games[0]
        assert isinstance(game1, TeamGameLog)
        assert game1.team_id == 1610612738
        assert game1.game_id == "0022400234"
        assert game1.game_date == "2024-11-05"
        assert game1.matchup == "BOS vs. MIA"
        assert game1.win_loss == "W"
        assert game1.points == 118.0
        assert game1.rebounds == 48.0
        assert game1.assists == 28.0

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, TeamGameLogs)
        assert len(result.games) == 0

    def test_fetch_sync(self, game_logs_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = game_logs_response

        endpoint = TeamGameLogsEndpoint(mock_client)
        result = endpoint.fetch(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamGameLogs)
        assert len(result.games) == 3
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "teamgamelog"
        params = call_args[1]["params"]
        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2024-25"

    @pytest.mark.asyncio
    async def test_fetch_async(self, game_logs_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=game_logs_response)

        endpoint = TeamGameLogsEndpoint(mock_client)
        result = await endpoint.fetch_async(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamGameLogs)
        assert len(result.games) == 3
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, game_logs_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=TeamGameLogs(games=[]))
        monkeypatch.setattr(TeamGameLogsEndpoint, "fetch", mock_fetch)

        result = get_team_game_logs(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamGameLogs)
        mock_fetch.assert_called_once()


class TestTeamGameLogModel:
    """Tests for TeamGameLog model."""

    def test_model_properties(self):
        """Test computed properties."""
        game = TeamGameLog(
            TEAM_ID=1610612738,
            GAME_ID="0022400234",
            GAME_DATE="2024-11-05",
            MATCHUP="BOS vs. MIA",
            WL="W",
            MIN=240.0,
            FGM=44.0,
            FGA=92.0,
            FG_PCT=0.478,
            FG3M=16.0,
            FG3A=45.0,
            FG3_PCT=0.356,
            FTM=14.0,
            FTA=20.0,
            FT_PCT=0.700,
            OREB=10.0,
            DREB=38.0,
            REB=48.0,
            AST=28.0,
            STL=8.0,
            BLK=6.0,
            TOV=12.0,
            PF=18.0,
            PTS=118.0,
            PLUS_MINUS=12.0,
        )

        assert game.is_win is True
        assert game.is_home_game is True
        assert game.opponent == "MIA"

    def test_model_away_game_properties(self):
        """Test properties for away game."""
        game = TeamGameLog(
            TEAM_ID=1610612738,
            GAME_ID="0022400212",
            GAME_DATE="2024-11-03",
            MATCHUP="BOS @ ATL",
            WL="L",
            MIN=240.0,
            FGM=42.0,
            FGA=88.0,
            FG_PCT=0.477,
            FG3M=18.0,
            FG3A=47.0,
            FG3_PCT=0.383,
            FTM=13.0,
            FTA=17.0,
            FT_PCT=0.765,
            OREB=8.0,
            DREB=40.0,
            REB=48.0,
            AST=25.0,
            STL=9.0,
            BLK=5.0,
            TOV=14.0,
            PF=20.0,
            PTS=115.0,
            PLUS_MINUS=8.0,
        )

        assert game.is_win is False
        assert game.is_home_game is False
        assert game.opponent == "ATL"

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        game = TeamGameLog(
            TEAM_ID=1610612738,
            GAME_ID="0022400234",
            GAME_DATE="2024-11-05",
            MATCHUP="BOS vs. MIA",
            WL="W",
            MIN=240.0,
            FGM=44.0,
            FGA=92.0,
            FG_PCT=0.478,
            FG3M=16.0,
            FG3A=45.0,
            FG3_PCT=0.356,
            FTM=14.0,
            FTA=20.0,
            FT_PCT=0.700,
            OREB=10.0,
            DREB=38.0,
            REB=48.0,
            AST=28.0,
            STL=8.0,
            BLK=6.0,
            TOV=12.0,
            PF=18.0,
            PTS=118.0,
            PLUS_MINUS=12.0,
        )

        str_repr = str(game)
        assert "2024-11-05" in str_repr
        assert "BOS vs. MIA" in str_repr
        assert "(W)" in str_repr
        assert "118" in str_repr

        repr_str = repr(game)
        assert "TeamGameLog" in repr_str
        assert "0022400234" in repr_str


class TestTeamGameLogsModel:
    """Tests for TeamGameLogs model."""

    def test_filter_wins(self, game_logs_response):
        """Test filtering wins."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        wins = result.filter_wins()
        assert len(wins) == 2
        assert all(game.win_loss == "W" for game in wins)

    def test_filter_losses(self, game_logs_response):
        """Test filtering losses."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        losses = result.filter_losses()
        assert len(losses) == 1
        assert all(game.win_loss == "L" for game in losses)

    def test_filter_home_games(self, game_logs_response):
        """Test filtering home games."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        home_games = result.filter_home_games()
        assert len(home_games) == 2
        assert all(" vs. " in game.matchup for game in home_games)

    def test_filter_away_games(self, game_logs_response):
        """Test filtering away games."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        away_games = result.filter_away_games()
        assert len(away_games) == 1
        assert all(" @ " in game.matchup for game in away_games)

    def test_calculate_totals(self, game_logs_response):
        """Test calculating totals."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        totals = result.calculate_totals()
        assert totals["games"] == 3
        assert totals["wins"] == 2
        assert totals["losses"] == 1
        assert totals["points"] == 337.0  # 118 + 115 + 104
        assert totals["rebounds"] == 140.0  # 48 + 48 + 44
        assert totals["assists"] == 75.0  # 28 + 25 + 22

    def test_calculate_totals_empty(self):
        """Test calculating totals with no games."""
        logs = TeamGameLogs(games=[])
        totals = logs.calculate_totals()
        assert totals == {}

    def test_record_property(self, game_logs_response):
        """Test record property."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        assert result.record == "2-1"

    def test_string_representations(self, game_logs_response):
        """Test __str__ and __repr__ methods."""
        endpoint = TeamGameLogsEndpoint()
        result = endpoint._parse_response(game_logs_response)

        str_repr = str(result)
        assert "3 games" in str_repr

        repr_str = repr(result)
        assert "TeamGameLogs" in repr_str
        assert "games=3" in repr_str
