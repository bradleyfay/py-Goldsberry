"""Tests for PlayerList endpoint."""

import pytest

from nba_api.client.base import BaseClient
from nba_api.endpoints.player import PlayerListEndpoint, get_players
from nba_api.enums.common import IsOnlyCurrentSeason, LeagueID, Season
from nba_api.models.player import PlayerInfo


@pytest.fixture
def player_list_data(load_fixture):
    """Load player list fixture."""
    return load_fixture("player/player_list_response.json")


def test_player_info_model():
    """Test PlayerInfo model parsing."""
    data = {
        "PERSON_ID": 203999,
        "DISPLAY_LAST_COMMA_FIRST": "Jokic, Nikola",
        "DISPLAY_FIRST_LAST": "Nikola Jokic",
        "ROSTERSTATUS": 1,
        "FROM_YEAR": "2015",
        "TO_YEAR": "2024",
        "PLAYERCODE": "nikola_jokic",
        "TEAM_ID": 1610612743,
        "TEAM_CITY": "Denver",
        "TEAM_NAME": "Nuggets",
        "TEAM_ABBREVIATION": "DEN",
        "JERSEY_NUMBER": "15",
        "POSITION": "C",
        "HEIGHT": "6-11",
        "WEIGHT": "284",
        "COLLEGE": "Serbia",
        "COUNTRY": "Serbia",
        "DRAFT_YEAR": "2014",
        "DRAFT_ROUND": "2",
        "DRAFT_NUMBER": "41",
        "GREATEST_75_FLAG": "N",
    }

    player = PlayerInfo(**data)

    assert player.person_id == 203999
    assert player.full_name == "Nikola Jokic"
    assert player.display_last_comma_first == "Jokic, Nikola"
    assert player.is_active is True
    assert player.team_abbreviation == "DEN"
    assert player.position == "C"
    assert player.height == "6-11"
    assert player.weight == "284"


def test_player_info_inactive():
    """Test inactive player."""
    data = {
        "PERSON_ID": 123,
        "DISPLAY_LAST_COMMA_FIRST": "Jordan, Michael",
        "DISPLAY_FIRST_LAST": "Michael Jordan",
        "ROSTERSTATUS": 0,
        "FROM_YEAR": "1984",
        "TO_YEAR": "2003",
        "PLAYERCODE": "michael_jordan",
        "TEAM_ID": 0,
        "TEAM_CITY": None,
        "TEAM_NAME": None,
        "TEAM_ABBREVIATION": None,
        "JERSEY_NUMBER": None,
        "POSITION": None,
        "HEIGHT": "6-6",
        "WEIGHT": "216",
        "COLLEGE": "North Carolina",
        "COUNTRY": "USA",
        "DRAFT_YEAR": "1984",
        "DRAFT_ROUND": "1",
        "DRAFT_NUMBER": "3",
        "GREATEST_75_FLAG": "Y",
    }

    player = PlayerInfo(**data)

    assert player.is_active is False
    assert player.team_abbreviation is None


def test_player_list_endpoint_params():
    """Test parameter building."""
    client = BaseClient()
    endpoint = PlayerListEndpoint(client)

    # Test with enums
    params = endpoint._build_params(
        season=Season.CURRENT,
        league_id=LeagueID.NBA,
        only_current_season=IsOnlyCurrentSeason.CURRENT_SEASON_ONLY,
    )

    assert params["Season"] == "2024-25"
    assert params["LeagueID"] == "00"
    assert params["IsOnlyCurrentSeason"] == 1

    # Test with string season
    params = endpoint._build_params(season="2023-24")
    assert params["Season"] == "2023-24"


def test_player_list_fetch(player_list_data, mock_client_response):
    """Test synchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = endpoint.fetch(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)

    # Check first player (Jokic)
    jokic = players[0]
    assert jokic.person_id == 203999
    assert jokic.full_name == "Nikola Jokic"
    assert jokic.is_active
    assert jokic.team_abbreviation == "DEN"

    # Check LeBron
    lebron = players[1]
    assert lebron.person_id == 2544
    assert lebron.full_name == "LeBron James"
    assert lebron.greatest_75_flag == "Y"


@pytest.mark.asyncio
async def test_player_list_fetch_async(player_list_data, mock_client_response):
    """Test asynchronous fetch."""
    mock_client_response(player_list_data)

    endpoint = PlayerListEndpoint()
    players = await endpoint.fetch_async(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)

    # Check Wembanyama
    wemby = players[4]
    assert wemby.person_id == 1630162
    assert wemby.full_name == "Victor Wembanyama"
    assert wemby.team_abbreviation == "SAS"
    assert wemby.height == "7-4"


def test_convenience_function(player_list_data, mock_client_response):
    """Test convenience function."""
    mock_client_response(player_list_data)

    players = get_players(season=Season.CURRENT)

    assert len(players) == 5
    assert all(isinstance(p, PlayerInfo) for p in players)


def test_player_info_str_repr():
    """Test string representations."""
    data = {
        "PERSON_ID": 203999,
        "DISPLAY_LAST_COMMA_FIRST": "Jokic, Nikola",
        "DISPLAY_FIRST_LAST": "Nikola Jokic",
        "ROSTERSTATUS": 1,
        "FROM_YEAR": "2015",
        "TO_YEAR": "2024",
        "PLAYERCODE": "nikola_jokic",
        "TEAM_ID": 1610612743,
        "TEAM_CITY": "Denver",
        "TEAM_NAME": "Nuggets",
        "TEAM_ABBREVIATION": "DEN",
        "JERSEY_NUMBER": "15",
        "POSITION": "C",
        "HEIGHT": "6-11",
        "WEIGHT": "284",
        "COLLEGE": "Serbia",
        "COUNTRY": "Serbia",
        "DRAFT_YEAR": "2014",
        "DRAFT_ROUND": "2",
        "DRAFT_NUMBER": "41",
        "GREATEST_75_FLAG": "N",
    }

    player = PlayerInfo(**data)

    str_rep = str(player)
    assert "Nikola Jokic" in str_rep
    assert "DEN" in str_rep
    assert "Active" in str_rep

    repr_rep = repr(player)
    assert "PlayerInfo" in repr_rep
    assert "203999" in repr_rep
    assert "Nikola Jokic" in repr_rep


def test_filter_active_players(player_list_data, mock_client_response):
    """Test filtering active players."""
    mock_client_response(player_list_data)

    players = get_players()
    active_players = [p for p in players if p.is_active]

    assert len(active_players) == 5  # All in fixture are active
    assert all(p.roster_status == 1 for p in active_players)
