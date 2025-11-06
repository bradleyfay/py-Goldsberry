"""Tests for GameLogs endpoint."""

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.player import GameLogsEndpoint, get_game_logs
from goldsberry.enums.common import Season, SeasonType
from goldsberry.models.player import GameLog


@pytest.fixture
def game_logs_data(load_fixture):
    """Load game logs fixture."""
    return load_fixture("player/game_logs_response.json")


def test_game_log_model():
    """Test GameLog model parsing."""
    data = {
        "SEASON_ID": "22024",
        "Player_ID": 203999,
        "Game_ID": "0022401193",
        "GAME_DATE": "Apr 13, 2025",
        "MATCHUP": "DEN @ HOU",
        "WL": "W",
        "MIN": 35.2,
        "FGM": 12,
        "FGA": 20,
        "FG_PCT": 0.600,
        "FG3M": 2,
        "FG3A": 5,
        "FG3_PCT": 0.400,
        "FTM": 8,
        "FTA": 10,
        "FT_PCT": 0.800,
        "OREB": 3,
        "DREB": 11,
        "REB": 14,
        "AST": 10,
        "STL": 2,
        "BLK": 1,
        "TOV": 3,
        "PF": 2,
        "PTS": 34,
        "PLUS_MINUS": 12,
        "VIDEO_AVAILABLE": 1,
    }

    game = GameLog(**data)

    assert game.player_id == 203999
    assert game.game_id == "0022401193"
    assert game.game_date == "Apr 13, 2025"
    assert game.matchup == "DEN @ HOU"
    assert game.win_loss == "W"
    assert game.points == 34
    assert game.rebounds == 14
    assert game.assists == 10
    assert game.is_win is True


def test_game_log_properties():
    """Test GameLog computed properties."""
    # Home game win
    home_game = GameLog(
        SEASON_ID="22024",
        Player_ID=203999,
        Game_ID="001",
        GAME_DATE="Jan 01, 2025",
        MATCHUP="DEN vs. LAL",
        WL="W",
        FGM=10,
        FGA=20,
        FG_PCT=0.5,
        FG3M=2,
        FG3A=6,
        FG3_PCT=0.333,
        FTM=5,
        FTA=6,
        FT_PCT=0.833,
        OREB=2,
        DREB=8,
        REB=10,
        AST=8,
        STL=1,
        BLK=1,
        TOV=2,
        PF=2,
        PTS=27,
    )

    assert home_game.is_win is True
    assert home_game.is_home_game is True
    assert home_game.opponent == "LAL"

    # Away game loss
    away_game = GameLog(
        SEASON_ID="22024",
        Player_ID=203999,
        Game_ID="002",
        GAME_DATE="Jan 03, 2025",
        MATCHUP="DEN @ GSW",
        WL="L",
        FGM=8,
        FGA=18,
        FG_PCT=0.444,
        FG3M=1,
        FG3A=5,
        FG3_PCT=0.200,
        FTM=4,
        FTA=5,
        FT_PCT=0.800,
        OREB=1,
        DREB=7,
        REB=8,
        AST=6,
        STL=0,
        BLK=0,
        TOV=3,
        PF=3,
        PTS=21,
    )

    assert away_game.is_win is False
    assert away_game.is_home_game is False
    assert away_game.opponent == "GSW"


def test_game_logs_endpoint_params():
    """Test parameter building."""
    client = BaseClient()
    endpoint = GameLogsEndpoint(client)

    params = endpoint._build_params(
        player_id=203999,
        season=Season.CURRENT,
        season_type=SeasonType.REGULAR_SEASON,
    )

    assert params["PlayerID"] == 203999
    assert params["Season"] == "2024-25"
    assert params["SeasonType"] == "Regular Season"


def test_game_logs_fetch(game_logs_data, mock_client_response):
    """Test synchronous fetch."""
    mock_client_response(game_logs_data)

    endpoint = GameLogsEndpoint()
    games = endpoint.fetch(player_id=203999, season="2024-25")

    assert len(games) == 5  # Fixture has 5 games
    assert all(isinstance(g, GameLog) for g in games)
    assert games[0].player_id == 203999


@pytest.mark.asyncio
async def test_game_logs_fetch_async(game_logs_data, mock_client_response):
    """Test asynchronous fetch."""
    mock_client_response(game_logs_data)

    endpoint = GameLogsEndpoint()
    games = await endpoint.fetch_async(player_id=203999, season="2024-25")

    assert len(games) == 5
    assert all(isinstance(g, GameLog) for g in games)


def test_convenience_function(game_logs_data, mock_client_response):
    """Test convenience function."""
    mock_client_response(game_logs_data)

    games = get_game_logs(player_id=203999, season="2024-25")

    assert len(games) == 5
    assert all(isinstance(g, GameLog) for g in games)


def test_game_log_str_repr():
    """Test string representations."""
    game = GameLog(
        SEASON_ID="22024",
        Player_ID=203999,
        Game_ID="0022401193",
        GAME_DATE="Apr 13, 2025",
        MATCHUP="DEN @ HOU",
        WL="W",
        FGM=12,
        FGA=20,
        FG_PCT=0.600,
        FG3M=2,
        FG3A=5,
        FG3_PCT=0.400,
        FTM=8,
        FTA=10,
        FT_PCT=0.800,
        OREB=3,
        DREB=11,
        REB=14,
        AST=10,
        STL=2,
        BLK=1,
        TOV=3,
        PF=2,
        PTS=34,
    )

    str_repr = str(game)
    assert "Apr 13, 2025" in str_repr
    assert "DEN @ HOU" in str_repr
    assert "34" in str_repr and "PTS" in str_repr
    assert "14" in str_repr and "REB" in str_repr
    assert "10" in str_repr and "AST" in str_repr

    repr_str = repr(game)
    assert "GameLog" in repr_str
    assert "0022401193" in repr_str


def test_filter_wins_and_losses(game_logs_data, mock_client_response):
    """Test filtering wins and losses."""
    mock_client_response(game_logs_data)

    games = get_game_logs(player_id=203999)

    wins = [g for g in games if g.is_win]
    losses = [g for g in games if not g.is_win]

    assert len(wins) + len(losses) == len(games)


def test_home_away_games(game_logs_data, mock_client_response):
    """Test filtering home and away games."""
    mock_client_response(game_logs_data)

    games = get_game_logs(player_id=203999)

    home_games = [g for g in games if g.is_home_game]
    away_games = [g for g in games if not g.is_home_game]

    assert len(home_games) + len(away_games) == len(games)


def test_calculate_totals(game_logs_data, mock_client_response):
    """Test calculating totals across games."""
    mock_client_response(game_logs_data)

    games = get_game_logs(player_id=203999)

    total_points = sum(g.points for g in games)
    total_rebounds = sum(g.rebounds for g in games)
    total_assists = sum(g.assists for g in games)

    assert total_points > 0
    assert total_rebounds > 0
    assert total_assists > 0


def test_opponent_extraction():
    """Test opponent extraction from matchup string."""
    home = GameLog(
        SEASON_ID="22024",
        Player_ID=1,
        Game_ID="1",
        GAME_DATE="Jan 1, 2025",
        MATCHUP="DEN vs. LAL",
        FGM=0,
        FGA=0,
        FG3M=0,
        FG3A=0,
        FTM=0,
        FTA=0,
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
    assert home.opponent == "LAL"

    away = GameLog(
        SEASON_ID="22024",
        Player_ID=1,
        Game_ID="2",
        GAME_DATE="Jan 2, 2025",
        MATCHUP="DEN @ GSW",
        FGM=0,
        FGA=0,
        FG3M=0,
        FG3A=0,
        FTM=0,
        FTA=0,
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
    assert away.opponent == "GSW"
