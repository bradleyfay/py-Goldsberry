"""Tests for CareerStats endpoint."""

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.player import CareerStatsEndpoint, get_career_stats
from goldsberry.enums.common import PerMode
from goldsberry.models.player import SeasonTotals, CareerTotals, PlayerCareerStats


@pytest.fixture
def career_stats_data(load_fixture):
    """Load career stats fixture."""
    return load_fixture("player/career_stats_response.json")


def test_season_totals_model():
    """Test SeasonTotals model parsing."""
    data = {
        "PLAYER_ID": 203999,
        "SEASON_ID": "2023-24",
        "LEAGUE_ID": "00",
        "TEAM_ID": 1610612743,
        "TEAM_ABBREVIATION": "DEN",
        "PLAYER_AGE": 28.0,
        "GP": 79,
        "GS": 79,
        "MIN": 2868.4,
        "FGM": 795,
        "FGA": 1355,
        "FG_PCT": 0.587,
        "FG3M": 82,
        "FG3A": 224,
        "FG3_PCT": 0.366,
        "FTM": 435,
        "FTA": 517,
        "FT_PCT": 0.841,
        "OREB": 244,
        "DREB": 755,
        "REB": 999,
        "AST": 686,
        "STL": 107,
        "BLK": 61,
        "TOV": 228,
        "PF": 190,
        "PTS": 2107,
    }

    season = SeasonTotals(**data)

    assert season.player_id == 203999
    assert season.season_id == "2023-24"
    assert season.team_abbreviation == "DEN"
    assert season.games_played == 79
    assert season.points == 2107
    assert season.points_per_game == pytest.approx(26.7, abs=0.1)
    assert season.rebounds_per_game == pytest.approx(12.6, abs=0.1)
    assert season.assists_per_game == pytest.approx(8.7, abs=0.1)


def test_career_totals_model():
    """Test CareerTotals model parsing."""
    data = {
        "PLAYER_ID": 203999,
        "LEAGUE_ID": "00",
        "TEAM_ID": 0,
        "GP": 752,
        "GS": 711,
        "MIN": 25013.1,
        "FGM": 6301,
        "FGA": 11209,
        "FG_PCT": 0.562,
        "FG3M": 691,
        "FG3A": 2063,
        "FG3_PCT": 0.335,
        "FTM": 3519,
        "FTA": 4263,
        "FT_PCT": 0.826,
        "OREB": 1927,
        "DREB": 6289,
        "REB": 8216,
        "AST": 5437,
        "STL": 1005,
        "BLK": 681,
        "TOV": 2237,
        "PF": 1873,
        "PTS": 16812,
    }

    career = CareerTotals(**data)

    assert career.player_id == 203999
    assert career.games_played == 752
    assert career.points == 16812
    assert career.points_per_game == pytest.approx(22.4, abs=0.1)
    assert career.rebounds_per_game == pytest.approx(10.9, abs=0.1)
    assert career.assists_per_game == pytest.approx(7.2, abs=0.1)


def test_career_stats_endpoint_params():
    """Test parameter building."""
    client = BaseClient()
    endpoint = CareerStatsEndpoint(client)

    params = endpoint._build_params(
        player_id=203999,
        per_mode=PerMode.TOTALS,
    )

    assert params["PlayerID"] == 203999
    assert params["PerMode"] == "Totals"


def test_career_stats_parse_response(career_stats_data):
    """Test response parsing."""
    client = BaseClient()
    endpoint = CareerStatsEndpoint(client)

    stats = endpoint._parse_response(career_stats_data)

    assert isinstance(stats, PlayerCareerStats)
    assert len(stats.season_totals_regular) == 3  # Fixture has 3 seasons
    assert stats.career_totals_regular is not None
    assert len(stats.season_totals_post) == 3  # Fixture has 3 playoff seasons
    assert stats.career_totals_post is not None

    # Check first season
    first_season = stats.season_totals_regular[0]
    assert isinstance(first_season, SeasonTotals)
    assert first_season.player_id == 203999
    assert first_season.season_id == "2015-16"

    # Check career totals
    career = stats.career_totals_regular
    assert isinstance(career, CareerTotals)
    assert career.player_id == 203999
    assert career.games_played > 0


def test_career_stats_fetch(career_stats_data, mock_client_response):
    """Test synchronous fetch."""
    mock_client_response(career_stats_data)

    endpoint = CareerStatsEndpoint()
    stats = endpoint.fetch(player_id=203999)

    assert isinstance(stats, PlayerCareerStats)
    assert len(stats.season_totals_regular) == 3
    assert stats.career_totals_regular is not None


@pytest.mark.asyncio
async def test_career_stats_fetch_async(career_stats_data, mock_client_response):
    """Test asynchronous fetch."""
    mock_client_response(career_stats_data)

    endpoint = CareerStatsEndpoint()
    stats = await endpoint.fetch_async(player_id=203999)

    assert isinstance(stats, PlayerCareerStats)
    assert len(stats.season_totals_regular) == 3
    assert stats.career_totals_regular is not None


def test_convenience_function(career_stats_data, mock_client_response):
    """Test convenience function."""
    mock_client_response(career_stats_data)

    stats = get_career_stats(player_id=203999)

    assert isinstance(stats, PlayerCareerStats)
    assert len(stats.season_totals_regular) == 3


def test_season_totals_str_repr():
    """Test string representations."""
    season = SeasonTotals(
        PLAYER_ID=203999,
        SEASON_ID="2023-24",
        LEAGUE_ID="00",
        TEAM_ID=1610612743,
        TEAM_ABBREVIATION="DEN",
        GP=79,
        GS=79,
        MIN=2868.4,
        FGM=795,
        FGA=1355,
        FG_PCT=0.587,
        FG3M=82,
        FG3A=224,
        FG3_PCT=0.366,
        FTM=435,
        FTA=517,
        FT_PCT=0.841,
        OREB=244,
        DREB=755,
        REB=999,
        AST=686,
        STL=107,
        BLK=61,
        TOV=228,
        PF=190,
        PTS=2107,
    )

    str_repr = str(season)
    assert "2023-24" in str_repr
    assert "DEN" in str_repr
    assert "PPG" in str_repr

    repr_str = repr(season)
    assert "SeasonTotals" in repr_str
    assert "203999" in repr_str


def test_career_totals_str_repr():
    """Test career totals string representations."""
    career = CareerTotals(
        PLAYER_ID=203999,
        LEAGUE_ID="00",
        TEAM_ID=0,
        GP=752,
        GS=711,
        MIN=25013.1,
        FGM=6301,
        FGA=11209,
        FG_PCT=0.562,
        FG3M=691,
        FG3A=2063,
        FG3_PCT=0.335,
        FTM=3519,
        FTA=4263,
        FT_PCT=0.826,
        OREB=1927,
        DREB=6289,
        REB=8216,
        AST=5437,
        STL=1005,
        BLK=681,
        TOV=2237,
        PF=1873,
        PTS=16812,
    )

    str_repr = str(career)
    assert "Career" in str_repr
    assert "GP" in str_repr
    assert "PPG" in str_repr

    repr_str = repr(career)
    assert "CareerTotals" in repr_str
    assert "203999" in repr_str


def test_calculate_per_game_stats():
    """Test per-game stat calculations."""
    season = SeasonTotals(
        PLAYER_ID=1,
        SEASON_ID="2023-24",
        LEAGUE_ID="00",
        TEAM_ID=1,
        TEAM_ABBREVIATION="TST",
        GP=80,
        GS=80,
        MIN=2800.0,
        FGM=800,
        FGA=1600,
        FG_PCT=0.5,
        FG3M=100,
        FG3A=300,
        FG3_PCT=0.333,
        FTM=400,
        FTA=500,
        FT_PCT=0.8,
        OREB=160,
        DREB=640,
        REB=800,
        AST=640,
        STL=80,
        BLK=40,
        TOV=160,
        PF=160,
        PTS=2100,
    )

    assert season.points_per_game == 26.25
    assert season.rebounds_per_game == 10.0
    assert season.assists_per_game == 8.0


def test_zero_games_played():
    """Test per-game calculations with zero games played."""
    season = SeasonTotals(
        PLAYER_ID=1,
        SEASON_ID="2023-24",
        LEAGUE_ID="00",
        TEAM_ID=1,
        TEAM_ABBREVIATION="TST",
        GP=0,  # Zero games
        GS=0,
        MIN=0.0,
        FGM=0,
        FGA=0,
        FG_PCT=None,
        FG3M=0,
        FG3A=0,
        FG3_PCT=None,
        FTM=0,
        FTA=0,
        FT_PCT=None,
        OREB=0,
        DREB=0,
        REB=0,
        AST=0,
        STL=0,
        BLK=0,
        TOV=0,
        PF=0,
        PTS=0,
    )

    # Should not raise division by zero
    assert season.points_per_game == 0.0
    assert season.rebounds_per_game == 0.0
    assert season.assists_per_game == 0.0
