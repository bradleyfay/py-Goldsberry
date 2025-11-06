"""Tests for TeamSeasonStats endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.team import TeamSeasonStatsEndpoint, get_team_season_stats
from goldsberry.enums.common import MeasureType, PerMode, Season, SeasonType
from goldsberry.models.team import TeamSeasonStats, TeamStats


# Fixture loader
@pytest.fixture
def season_stats_response():
    """Load team season stats fixture."""
    fixture_path = Path(__file__).parent.parent.parent.parent / "fixtures" / "team" / "season_stats_response.json"
    with open(fixture_path) as f:
        return json.load(f)


class TestTeamSeasonStatsEndpoint:
    """Tests for TeamSeasonStatsEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = TeamSeasonStatsEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "leaguedashteamstats"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = TeamSeasonStatsEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = TeamSeasonStatsEndpoint()
        params = endpoint._build_params()

        assert params["Season"] == "2024-25"
        assert params["SeasonType"] == "Regular Season"
        assert params["PerMode"] == "Totals"
        assert params["MeasureType"] == "Base"
        assert params["LeagueID"] == "00"
        assert params["LastNGames"] == 0
        assert params["TeamID"] == 0

    def test_build_params_with_enums(self):
        """Test parameter building with enum values."""
        endpoint = TeamSeasonStatsEndpoint()
        params = endpoint._build_params(
            season=Season.SEASON_2023_24,
            season_type=SeasonType.PLAYOFFS,
            per_mode=PerMode.PER_GAME,
            measure_type=MeasureType.ADVANCED,
        )

        assert params["Season"] == "2023-24"
        assert params["SeasonType"] == "Playoffs"
        assert params["PerMode"] == "PerGame"
        assert params["MeasureType"] == "Advanced"

    def test_build_params_with_strings(self):
        """Test parameter building with string values."""
        endpoint = TeamSeasonStatsEndpoint()
        params = endpoint._build_params(
            season="2022-23",
            season_type="Pre Season",
            per_mode="Per36",
            measure_type="Four Factors",
        )

        assert params["Season"] == "2022-23"
        assert params["SeasonType"] == "Pre Season"
        assert params["PerMode"] == "Per36"
        assert params["MeasureType"] == "Four Factors"

    def test_build_params_with_filters(self):
        """Test parameter building with various filters."""
        endpoint = TeamSeasonStatsEndpoint()
        params = endpoint._build_params(
            conference="East",
            division="Atlantic",
            last_n_games=10,
            team_id=1610612738,
            date_from="2024-01-01",
            date_to="2024-03-01",
        )

        assert params["Conference"] == "East"
        assert params["Division"] == "Atlantic"
        assert params["LastNGames"] == 10
        assert params["TeamID"] == 1610612738
        assert params["DateFrom"] == "2024-01-01"
        assert params["DateTo"] == "2024-03-01"

    def test_parse_response(self, season_stats_response):
        """Test parsing of NBA API response."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        assert isinstance(result, TeamSeasonStats)
        assert len(result.teams) == 3

        # Test first team (Celtics)
        celtics = result.teams[0]
        assert isinstance(celtics, TeamStats)
        assert celtics.team_id == 1610612738
        assert celtics.team_name == "Boston Celtics"
        assert celtics.games_played == 82
        assert celtics.wins == 64
        assert celtics.losses == 18
        assert celtics.win_percentage == 0.780
        assert celtics.points == 10014.0
        assert celtics.record == "64-18"

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, TeamSeasonStats)
        assert len(result.teams) == 0

    def test_fetch_sync(self, season_stats_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = season_stats_response

        endpoint = TeamSeasonStatsEndpoint(mock_client)
        result = endpoint.fetch(season="2024-25")

        assert isinstance(result, TeamSeasonStats)
        assert len(result.teams) == 3
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "leaguedashteamstats"
        params = call_args[1]["params"]
        assert params["Season"] == "2024-25"

    @pytest.mark.asyncio
    async def test_fetch_async(self, season_stats_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=season_stats_response)

        endpoint = TeamSeasonStatsEndpoint(mock_client)
        result = await endpoint.fetch_async(season="2024-25")

        assert isinstance(result, TeamSeasonStats)
        assert len(result.teams) == 3
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, season_stats_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=TeamSeasonStats(teams=[]))
        monkeypatch.setattr(TeamSeasonStatsEndpoint, "fetch", mock_fetch)

        result = get_team_season_stats(season="2024-25")

        assert isinstance(result, TeamSeasonStats)
        mock_fetch.assert_called_once()


class TestTeamStatsModel:
    """Tests for TeamStats model."""

    def test_model_properties(self):
        """Test computed properties."""
        team = TeamStats(
            TEAM_ID=1610612738,
            TEAM_NAME="Boston Celtics",
            GP=82,
            W=64,
            L=18,
            W_PCT=0.780,
            MIN=19780.0,
            FGM=3598.0,
            FGA=7658.0,
            FG_PCT=0.470,
            FG3M=1344.0,
            FG3A=3607.0,
            FG3_PCT=0.373,
            FTM=1474.0,
            FTA=1961.0,
            FT_PCT=0.752,
            OREB=899.0,
            DREB=3196.0,
            REB=4095.0,
            AST=2048.0,
            TOV=1046.0,
            STL=621.0,
            BLK=476.0,
            BLKA=412.0,
            PF=1592.0,
            PFD=1653.0,
            PTS=10014.0,
            PLUS_MINUS=7.2,
        )

        assert team.record == "64-18"
        assert team.points_per_game == pytest.approx(122.1, rel=0.1)
        assert team.rebounds_per_game == pytest.approx(49.9, rel=0.1)
        assert team.assists_per_game == pytest.approx(25.0, rel=0.1)

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        team = TeamStats(
            TEAM_ID=1610612738,
            TEAM_NAME="Boston Celtics",
            GP=82,
            W=64,
            L=18,
            W_PCT=0.780,
            MIN=19780.0,
            FGM=3598.0,
            FGA=7658.0,
            FG_PCT=0.470,
            FG3M=1344.0,
            FG3A=3607.0,
            FG3_PCT=0.373,
            FTM=1474.0,
            FTA=1961.0,
            FT_PCT=0.752,
            OREB=899.0,
            DREB=3196.0,
            REB=4095.0,
            AST=2048.0,
            TOV=1046.0,
            STL=621.0,
            BLK=476.0,
            BLKA=412.0,
            PF=1592.0,
            PFD=1653.0,
            PTS=10014.0,
            PLUS_MINUS=7.2,
        )

        str_repr = str(team)
        assert "Boston Celtics" in str_repr
        assert "64-18" in str_repr

        repr_str = repr(team)
        assert "TeamStats" in repr_str
        assert "1610612738" in repr_str


class TestTeamSeasonStatsModel:
    """Tests for TeamSeasonStats model."""

    def test_get_team_by_id(self, season_stats_response):
        """Test getting team by ID."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        celtics = result.get_team_by_id(1610612738)
        assert celtics is not None
        assert celtics.team_name == "Boston Celtics"

        not_found = result.get_team_by_id(9999999)
        assert not_found is None

    def test_get_team_by_name(self, season_stats_response):
        """Test getting team by name."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        # Full name
        celtics = result.get_team_by_name("Boston Celtics")
        assert celtics is not None
        assert celtics.team_id == 1610612738

        # Partial name (case insensitive)
        celtics = result.get_team_by_name("celtics")
        assert celtics is not None

        # Not found
        not_found = result.get_team_by_name("Lakers")
        assert not_found is None

    def test_sort_by_wins(self, season_stats_response):
        """Test sorting teams by wins."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        sorted_teams = result.sort_by_wins()
        assert sorted_teams[0].team_name == "Boston Celtics"  # 64 wins
        assert sorted_teams[1].team_name == "Brooklyn Nets"  # 32 wins
        assert sorted_teams[2].team_name == "Detroit Pistons"  # 14 wins

        # Ascending order
        sorted_teams_asc = result.sort_by_wins(reverse=False)
        assert sorted_teams_asc[0].team_name == "Detroit Pistons"

    def test_sort_by_points_per_game(self, season_stats_response):
        """Test sorting teams by PPG."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        sorted_teams = result.sort_by_points_per_game()
        # Celtics: 10014/82 = 122.1, Nets: 8823/82 = 107.6, Pistons: 8256/82 = 100.7
        assert sorted_teams[0].team_name == "Boston Celtics"
        assert sorted_teams[2].team_name == "Detroit Pistons"

    def test_string_representations(self, season_stats_response):
        """Test __str__ and __repr__ methods."""
        endpoint = TeamSeasonStatsEndpoint()
        result = endpoint._parse_response(season_stats_response)

        str_repr = str(result)
        assert "3 teams" in str_repr

        repr_str = repr(result)
        assert "TeamSeasonStats" in repr_str
        assert "teams=3" in repr_str
