"""Tests for LeaguePlayerStats endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.league import (
    LeaguePlayerStatsEndpoint,
    get_league_player_stats,
)
from goldsberry.enums.common import (
    MeasureType,
    PerMode,
    PlayerPosition,
    Season,
    SeasonType,
    StarterBench,
)
from goldsberry.models.league import LeaguePlayerStats, PlayerStats


# Fixture loader
@pytest.fixture
def player_stats_response():
    """Load league player stats fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent
        / "fixtures"
        / "league"
        / "player_stats_response.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestLeaguePlayerStatsEndpoint:
    """Tests for LeaguePlayerStatsEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = LeaguePlayerStatsEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "leaguedashplayerstats"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = LeaguePlayerStatsEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = LeaguePlayerStatsEndpoint()
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
        endpoint = LeaguePlayerStatsEndpoint()
        params = endpoint._build_params(
            season=Season.SEASON_2023_24,
            season_type=SeasonType.PLAYOFFS,
            per_mode=PerMode.PER_GAME,
            measure_type=MeasureType.ADVANCED,
            player_position=PlayerPosition.GUARD,
            starter_bench=StarterBench.STARTERS,
        )

        assert params["Season"] == "2023-24"
        assert params["SeasonType"] == "Playoffs"
        assert params["PerMode"] == "PerGame"
        assert params["MeasureType"] == "Advanced"
        assert params["PlayerPosition"] == "G"
        assert params["StarterBench"] == "Starters"

    def test_build_params_with_strings(self):
        """Test parameter building with string values."""
        endpoint = LeaguePlayerStatsEndpoint()
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
        endpoint = LeaguePlayerStatsEndpoint()
        params = endpoint._build_params(
            conference="East",
            division="Atlantic",
            last_n_games=10,
            team_id=1610612738,
            date_from="2024-01-01",
            date_to="2024-03-01",
            player_experience="Rookie",
            draft_year="2023",
        )

        assert params["Conference"] == "East"
        assert params["Division"] == "Atlantic"
        assert params["LastNGames"] == 10
        assert params["TeamID"] == 1610612738
        assert params["DateFrom"] == "2024-01-01"
        assert params["DateTo"] == "2024-03-01"
        assert params["PlayerExperience"] == "Rookie"
        assert params["DraftYear"] == "2023"

    def test_parse_response(self, player_stats_response):
        """Test parsing of NBA API response."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        assert isinstance(result, LeaguePlayerStats)
        assert len(result.players) == 8

        # Test first player (SGA)
        sga = result.players[0]
        assert isinstance(sga, PlayerStats)
        assert sga.player_id == 1630162
        assert sga.player_name == "Shai Gilgeous-Alexander"
        assert sga.nickname == "SGA"
        assert sga.team_abbreviation == "OKC"
        assert sga.games_played == 82
        assert sga.points == 2507.0
        assert sga.record == "57-25"

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, LeaguePlayerStats)
        assert len(result.players) == 0

    def test_fetch_sync(self, player_stats_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = player_stats_response

        endpoint = LeaguePlayerStatsEndpoint(mock_client)
        result = endpoint.fetch(season="2024-25")

        assert isinstance(result, LeaguePlayerStats)
        assert len(result.players) == 8
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "leaguedashplayerstats"
        params = call_args[1]["params"]
        assert params["Season"] == "2024-25"

    @pytest.mark.asyncio
    async def test_fetch_async(self, player_stats_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=player_stats_response)

        endpoint = LeaguePlayerStatsEndpoint(mock_client)
        result = await endpoint.fetch_async(season="2024-25")

        assert isinstance(result, LeaguePlayerStats)
        assert len(result.players) == 8
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, player_stats_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=LeaguePlayerStats(players=[]))
        monkeypatch.setattr(LeaguePlayerStatsEndpoint, "fetch", mock_fetch)

        result = get_league_player_stats(season="2024-25")

        assert isinstance(result, LeaguePlayerStats)
        mock_fetch.assert_called_once()


class TestPlayerStatsModel:
    """Tests for PlayerStats model."""

    def test_model_properties(self):
        """Test computed properties."""
        player = PlayerStats(
            PLAYER_ID=1630162,
            PLAYER_NAME="Shai Gilgeous-Alexander",
            NICKNAME="SGA",
            TEAM_ID=1610612760,
            TEAM_ABBREVIATION="OKC",
            AGE=26.0,
            GP=82,
            W=57,
            L=25,
            W_PCT=0.695,
            MIN=2880.0,
            FGM=896.0,
            FGA=1738.0,
            FG_PCT=0.516,
            FG3M=117.0,
            FG3A=345.0,
            FG3_PCT=0.339,
            FTM=598.0,
            FTA=675.0,
            FT_PCT=0.886,
            OREB=66.0,
            DREB=447.0,
            REB=513.0,
            AST=451.0,
            TOV=143.0,
            STL=164.0,
            BLK=86.0,
            BLKA=18.0,
            PF=128.0,
            PFD=432.0,
            PTS=2507.0,
            PLUS_MINUS=8.2,
        )

        assert player.record == "57-25"
        assert player.points_per_game == pytest.approx(30.6, rel=0.1)
        assert player.rebounds_per_game == pytest.approx(6.3, rel=0.1)
        assert player.assists_per_game == pytest.approx(5.5, rel=0.1)
        assert player.minutes_per_game == pytest.approx(35.1, rel=0.1)

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        player = PlayerStats(
            PLAYER_ID=1630162,
            PLAYER_NAME="Shai Gilgeous-Alexander",
            NICKNAME="SGA",
            TEAM_ID=1610612760,
            TEAM_ABBREVIATION="OKC",
            AGE=26.0,
            GP=82,
            W=57,
            L=25,
            W_PCT=0.695,
            MIN=2880.0,
            FGM=896.0,
            FGA=1738.0,
            FG_PCT=0.516,
            FG3M=117.0,
            FG3A=345.0,
            FG3_PCT=0.339,
            FTM=598.0,
            FTA=675.0,
            FT_PCT=0.886,
            OREB=66.0,
            DREB=447.0,
            REB=513.0,
            AST=451.0,
            TOV=143.0,
            STL=164.0,
            BLK=86.0,
            BLKA=18.0,
            PF=128.0,
            PFD=432.0,
            PTS=2507.0,
            PLUS_MINUS=8.2,
        )

        str_repr = str(player)
        assert "Shai Gilgeous-Alexander" in str_repr
        assert "OKC" in str_repr

        repr_str = repr(player)
        assert "PlayerStats" in repr_str
        assert "1630162" in repr_str


class TestLeaguePlayerStatsModel:
    """Tests for LeaguePlayerStats model."""

    def test_get_player_by_id(self, player_stats_response):
        """Test getting player by ID."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        sga = result.get_player_by_id(1630162)
        assert sga is not None
        assert sga.player_name == "Shai Gilgeous-Alexander"

        not_found = result.get_player_by_id(9999999)
        assert not_found is None

    def test_get_player_by_name(self, player_stats_response):
        """Test getting player by name."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        # Full name
        luka = result.get_player_by_name("Luka Doncic")
        assert luka is not None
        assert luka.player_id == 1629029

        # Partial name (case insensitive)
        luka = result.get_player_by_name("doncic")
        assert luka is not None

        # Not found
        not_found = result.get_player_by_name("LeBron James")
        assert not_found is None

    def test_filter_by_team(self, player_stats_response):
        """Test filtering players by team."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        celtics = result.filter_by_team("BOS")
        assert len(celtics) == 2
        assert all(p.team_abbreviation == "BOS" for p in celtics)

        # Case insensitive
        celtics = result.filter_by_team("bos")
        assert len(celtics) == 2

    def test_filter_by_min_games(self, player_stats_response):
        """Test filtering by minimum games played."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        # Players with 70+ games: SGA(82), Luka(70), Giannis(73), Tatum(80), Edwards(79), Brown(70), Durant(75)
        players_70_plus = result.filter_by_min_games(70)
        assert len(players_70_plus) == 7

        # Filter to 80+ games: SGA(82), Tatum(80)
        players_80_plus = result.filter_by_min_games(80)
        assert len(players_80_plus) == 2

    def test_get_top_scorers(self, player_stats_response):
        """Test getting top scorers by PPG."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        top_3 = result.get_top_scorers(3)
        assert len(top_3) == 3
        # get_top_scorers sorts by PPG, so verify descending order
        assert top_3[0].points_per_game >= top_3[1].points_per_game >= top_3[2].points_per_game

    def test_get_top_by_stat(self, player_stats_response):
        """Test getting top players by specific stat."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        # Top 3 assisters
        top_assisters = result.get_top_by_stat("assists", n=3)
        assert len(top_assisters) == 3
        assert top_assisters[0].assists >= top_assisters[1].assists

        # Top 3 rebounders
        top_rebounders = result.get_top_by_stat("rebounds", n=3)
        assert len(top_rebounders) == 3
        assert top_rebounders[0].rebounds >= top_rebounders[1].rebounds

        # Bottom 3 by turnovers (reverse=False)
        low_turnovers = result.get_top_by_stat("turnovers", n=3, reverse=False)
        assert len(low_turnovers) == 3
        assert low_turnovers[0].turnovers <= low_turnovers[1].turnovers

    def test_sort_by_generic(self, player_stats_response):
        """Test generic sort_by method."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        # Sort by field goal percentage
        sorted_by_fg = result.sort_by("field_goal_percentage")
        assert sorted_by_fg[0].field_goal_percentage >= sorted_by_fg[-1].field_goal_percentage

        # Sort by games played (ascending)
        sorted_by_gp = result.sort_by("games_played", reverse=False)
        assert sorted_by_gp[0].games_played <= sorted_by_gp[-1].games_played

    def test_sort_by_points(self, player_stats_response):
        """Test sorting by total points."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        sorted_players = result.sort_by_points()
        # SGA and Luka both have 2507 points (tied for most)
        assert sorted_players[0].points >= 2507.0
        assert sorted_players[-1].points <= sorted_players[0].points

    def test_sort_by_points_per_game(self, player_stats_response):
        """Test sorting by points per game."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        sorted_players = result.sort_by_points_per_game()
        # Luka: 2507/70 = 35.8 PPG (highest)
        # SGA: 2507/82 = 30.6 PPG
        assert sorted_players[0].player_name == "Luka Doncic"
        assert sorted_players[0].points_per_game == pytest.approx(35.8, rel=0.1)

    def test_sort_by_rebounds_per_game(self, player_stats_response):
        """Test sorting by rebounds per game."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        sorted_players = result.sort_by_rebounds_per_game()
        # Giannis has 951 rebounds in 73 games = 13.0 RPG
        assert sorted_players[0].player_name == "Giannis Antetokounmpo"

    def test_sort_by_assists_per_game(self, player_stats_response):
        """Test sorting by assists per game."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        sorted_players = result.sort_by_assists_per_game()
        # Tyrese Haliburton has 736 assists in 69 games = 10.7 APG
        assert sorted_players[0].player_name == "Tyrese Haliburton"

    def test_string_representations(self, player_stats_response):
        """Test __str__ and __repr__ methods."""
        endpoint = LeaguePlayerStatsEndpoint()
        result = endpoint._parse_response(player_stats_response)

        str_repr = str(result)
        assert "8 players" in str_repr

        repr_str = repr(result)
        assert "LeaguePlayerStats" in repr_str
        assert "players=8" in repr_str

    def test_optional_fields(self):
        """Test that optional fields work correctly."""
        player = PlayerStats(
            PLAYER_ID=1630162,
            PLAYER_NAME="Test Player",
            TEAM_ID=1610612760,
            TEAM_ABBREVIATION="OKC",
            GP=82,
            W=57,
            L=25,
            W_PCT=0.695,
            MIN=2880.0,
            FGM=896.0,
            FGA=1738.0,
            FG_PCT=0.516,
            FG3M=117.0,
            FG3A=345.0,
            FG3_PCT=0.339,
            FTM=598.0,
            FTA=675.0,
            FT_PCT=0.886,
            OREB=66.0,
            DREB=447.0,
            REB=513.0,
            AST=451.0,
            TOV=143.0,
            STL=164.0,
            BLK=86.0,
            BLKA=18.0,
            PF=128.0,
            PFD=432.0,
            PTS=2507.0,
            PLUS_MINUS=8.2,
        )

        # Optional fields should be None if not provided
        assert player.nickname is None
        assert player.age is None
        assert player.nba_fantasy_points is None
        assert player.triple_doubles is None

    def test_properties_zero_games(self):
        """Test computed properties when games_played is 0."""
        player = PlayerStats(
            PLAYER_ID=1,
            PLAYER_NAME="Test Player",
            TEAM_ID=1,
            TEAM_ABBREVIATION="TST",
            GP=0,
            W=0,
            L=0,
            W_PCT=0.0,
            MIN=0.0,
            FGM=0.0,
            FGA=0.0,
            FG_PCT=0.0,
            FG3M=0.0,
            FG3A=0.0,
            FG3_PCT=0.0,
            FTM=0.0,
            FTA=0.0,
            FT_PCT=0.0,
            OREB=0.0,
            DREB=0.0,
            REB=0.0,
            AST=0.0,
            TOV=0.0,
            STL=0.0,
            BLK=0.0,
            BLKA=0.0,
            PF=0.0,
            PFD=0.0,
            PTS=0.0,
            PLUS_MINUS=0.0,
        )

        assert player.points_per_game == 0.0
        assert player.rebounds_per_game == 0.0
        assert player.assists_per_game == 0.0
        assert player.minutes_per_game == 0.0
