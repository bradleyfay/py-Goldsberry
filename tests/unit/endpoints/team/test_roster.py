"""Tests for Team Roster endpoint."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from goldsberry.client.base import BaseClient
from goldsberry.endpoints.team import TeamRosterEndpoint, get_team_roster
from goldsberry.enums.common import Season
from goldsberry.models.team import Coach, RosterPlayer, TeamRoster


# Fixture loader
@pytest.fixture
def roster_response():
    """Load team roster fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent
        / "fixtures"
        / "team"
        / "roster_response.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestTeamRosterEndpoint:
    """Tests for TeamRosterEndpoint class."""

    def test_init_default_client(self):
        """Test initialization with default client."""
        endpoint = TeamRosterEndpoint()
        assert endpoint.client is not None
        assert endpoint._owns_client is True
        assert endpoint.ENDPOINT == "commonteamroster"

    def test_init_custom_client(self):
        """Test initialization with custom client."""
        client = BaseClient()
        endpoint = TeamRosterEndpoint(client)
        assert endpoint.client is client
        assert endpoint._owns_client is False

    def test_build_params_defaults(self):
        """Test parameter building with default values."""
        endpoint = TeamRosterEndpoint()
        params = endpoint._build_params(team_id=1610612738)

        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2024-25"
        assert params["LeagueID"] == "00"

    def test_build_params_with_enums(self):
        """Test parameter building with enum values."""
        endpoint = TeamRosterEndpoint()
        params = endpoint._build_params(
            team_id=1610612738,
            season=Season.SEASON_2023_24,
        )

        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2023-24"

    def test_build_params_with_strings(self):
        """Test parameter building with string values."""
        endpoint = TeamRosterEndpoint()
        params = endpoint._build_params(
            team_id=1610612738,
            season="2022-23",
        )

        assert params["Season"] == "2022-23"

    def test_parse_response(self, roster_response):
        """Test parsing of NBA API response."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        assert isinstance(result, TeamRoster)
        assert len(result.players) == 3
        assert len(result.coaches) == 3

        # Test first player (Payton Pritchard)
        player1 = result.players[0]
        assert isinstance(player1, RosterPlayer)
        assert player1.player_id == 1630162
        assert player1.player_name == "Payton Pritchard"
        assert player1.jersey_number == "11"
        assert player1.position == "G"
        assert player1.height == "6-1"
        assert player1.weight == "195"

        # Test head coach
        coach1 = result.coaches[0]
        assert isinstance(coach1, Coach)
        assert coach1.coach_id == "203099"
        assert coach1.coach_name == "Joe Mazzulla"
        assert coach1.is_head_coach is True

    def test_parse_response_empty(self):
        """Test parsing empty response."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response({"resultSets": []})

        assert isinstance(result, TeamRoster)
        assert len(result.players) == 0
        assert len(result.coaches) == 0

    def test_fetch_sync(self, roster_response):
        """Test synchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get.return_value = roster_response

        endpoint = TeamRosterEndpoint(mock_client)
        result = endpoint.fetch(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamRoster)
        assert len(result.players) == 3
        assert len(result.coaches) == 3
        mock_client.get.assert_called_once()

        # Verify parameters passed to client
        call_args = mock_client.get.call_args
        assert call_args[0][0] == "commonteamroster"
        params = call_args[1]["params"]
        assert params["TeamID"] == 1610612738
        assert params["Season"] == "2024-25"

    @pytest.mark.asyncio
    async def test_fetch_async(self, roster_response):
        """Test asynchronous fetch."""
        mock_client = Mock(spec=BaseClient)
        mock_client.get_async = AsyncMock(return_value=roster_response)

        endpoint = TeamRosterEndpoint(mock_client)
        result = await endpoint.fetch_async(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamRoster)
        assert len(result.players) == 3
        assert len(result.coaches) == 3
        mock_client.get_async.assert_called_once()

    def test_convenience_function(self, roster_response, monkeypatch):
        """Test convenience function."""
        mock_fetch = Mock(return_value=TeamRoster(players=[], coaches=[]))
        monkeypatch.setattr(TeamRosterEndpoint, "fetch", mock_fetch)

        result = get_team_roster(team_id=1610612738, season="2024-25")

        assert isinstance(result, TeamRoster)
        mock_fetch.assert_called_once()


class TestRosterPlayerModel:
    """Tests for RosterPlayer model."""

    def test_model_properties(self):
        """Test model with all fields."""
        player = RosterPlayer(
            TeamID=1610612738,
            SEASON="2024-25",
            LeagueID="00",
            PLAYER_ID=1630162,
            PLAYER="Payton Pritchard",
            NUM="11",
            POSITION="G",
            HEIGHT="6-1",
            WEIGHT="195",
            BIRTH_DATE="1998-01-28T00:00:00",
            AGE=26.0,
            EXP="4",
            SCHOOL="Oregon",
            HOW_ACQUIRED="Draft",
        )

        assert player.player_id == 1630162
        assert player.player_name == "Payton Pritchard"
        assert player.jersey_number == "11"
        assert player.position == "G"

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        player = RosterPlayer(
            TeamID=1610612738,
            SEASON="2024-25",
            LeagueID="00",
            PLAYER_ID=1630162,
            PLAYER="Payton Pritchard",
            NUM="11",
            POSITION="G",
            HEIGHT="6-1",
            WEIGHT="195",
            BIRTH_DATE="1998-01-28T00:00:00",
            AGE=26.0,
            EXP="4",
            SCHOOL="Oregon",
            HOW_ACQUIRED="Draft",
        )

        str_repr = str(player)
        assert "Payton Pritchard" in str_repr
        assert "#11" in str_repr
        assert "(G)" in str_repr

        repr_str = repr(player)
        assert "RosterPlayer" in repr_str
        assert "1630162" in repr_str


class TestCoachModel:
    """Tests for Coach model."""

    def test_head_coach_property(self):
        """Test head coach identification."""
        coach = Coach(
            TEAM_ID=1610612738,
            SEASON="2024-25",
            COACH_ID="203099",
            FIRST_NAME="Joe",
            LAST_NAME="Mazzulla",
            COACH_NAME="Joe Mazzulla",
            COACH_TYPE="Head Coach",
            IS_ASSISTANT=0,
            SCHOOL="West Virginia",
            SORT_SEQUENCE=1,
        )

        assert coach.is_head_coach is True

    def test_assistant_coach_property(self):
        """Test assistant coach identification."""
        coach = Coach(
            TEAM_ID=1610612738,
            SEASON="2024-25",
            COACH_ID="203098",
            FIRST_NAME="Sam",
            LAST_NAME="Cassell",
            COACH_NAME="Sam Cassell",
            COACH_TYPE="Assistant Coach",
            IS_ASSISTANT=1,
            SCHOOL="Florida State",
            SORT_SEQUENCE=2,
        )

        assert coach.is_head_coach is False

    def test_model_string_representations(self):
        """Test __str__ and __repr__ methods."""
        coach = Coach(
            TEAM_ID=1610612738,
            SEASON="2024-25",
            COACH_ID="203099",
            FIRST_NAME="Joe",
            LAST_NAME="Mazzulla",
            COACH_NAME="Joe Mazzulla",
            COACH_TYPE="Head Coach",
            IS_ASSISTANT=0,
            SCHOOL="West Virginia",
            SORT_SEQUENCE=1,
        )

        str_repr = str(coach)
        assert "Joe Mazzulla" in str_repr
        assert "Head Coach" in str_repr

        repr_str = repr(coach)
        assert "Coach" in repr_str
        assert "203099" in repr_str


class TestTeamRosterModel:
    """Tests for TeamRoster model."""

    def test_get_player_by_id(self, roster_response):
        """Test getting player by ID."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        player = result.get_player_by_id(1630162)
        assert player is not None
        assert player.player_name == "Payton Pritchard"

        not_found = result.get_player_by_id(9999999)
        assert not_found is None

    def test_get_player_by_name(self, roster_response):
        """Test getting player by name."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        # Full name
        player = result.get_player_by_name("Jayson Tatum")
        assert player is not None
        assert player.player_id == 1628369

        # Partial name (case insensitive)
        player = result.get_player_by_name("tatum")
        assert player is not None

        # Not found
        not_found = result.get_player_by_name("LeBron")
        assert not_found is None

    def test_get_players_by_position(self, roster_response):
        """Test getting players by position."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        # Guards (including combo positions)
        guards = result.get_players_by_position("G")
        assert len(guards) == 3  # All 3 players have G in their position

        # Forwards
        forwards = result.get_players_by_position("F")
        assert len(forwards) == 2  # Tatum (F-G) and Brown (G-F)

    def test_head_coach_property(self, roster_response):
        """Test head coach property."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        head_coach = result.head_coach
        assert head_coach is not None
        assert head_coach.coach_name == "Joe Mazzulla"
        assert head_coach.is_head_coach is True

    def test_assistant_coaches_property(self, roster_response):
        """Test assistant coaches property."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        assistants = result.assistant_coaches
        assert len(assistants) == 2
        assert all(not coach.is_head_coach for coach in assistants)

    def test_string_representations(self, roster_response):
        """Test __str__ and __repr__ methods."""
        endpoint = TeamRosterEndpoint()
        result = endpoint._parse_response(roster_response)

        str_repr = str(result)
        assert "3 players" in str_repr
        assert "3 coaches" in str_repr

        repr_str = repr(result)
        assert "TeamRoster" in repr_str
        assert "players=3" in repr_str
        assert "coaches=3" in repr_str
