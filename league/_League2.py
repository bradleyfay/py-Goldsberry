from goldsberry.masterclass import NbaDataProvider
from goldsberry.apiparams import *


class daily_scoreboard(NbaDataProvider):
    def __init__(self, date):
        url_modifier = 'scoreboardV2'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_sb, gameDate=date)

    def game_header(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def linescore(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def series_standings(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def last_meeting(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def eastern_conference_standings(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)

    def western_conference_standings(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 5)

    def available(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 6)

    def team_leaders(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 7)

    def _ticket_links(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 8)

    def win_probability(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 9)


class franchise_history(NbaDataProvider):
    def __init__(self):
        url_modifier = 'franchisehistory'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_history)

    def current_teams(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def defunct_teams(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)


# This one might not work because it's the key 'resultSet', not 'resultSets'
# Confirmed does not work
class league_leaders(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leagueleaders'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_leaders)

    def leaders(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class lineups(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leaguedashlineups'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_lineups)

    def lineups(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


# Doubl Check Stem
class playoff_picture(NbaDataProvider):
    def __init__(self):
        url_modifier = 'playoffpicture'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_game_ids)

    def eastern_conf_playoff_picture(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def western_conf_playoff_picture(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def eastern_conf_standings(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def western_conf_standings(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def eastern_conf_remaining_games(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)

    def western_conf_remaining_games(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 5)


class team_stats_classic(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leaguedashteamstats'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_classic)

    def stats(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class player_stats_classic(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leaguedashplayerstats'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_classic)

    def stats(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class team_stats_clutch(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leaguedashteamclutch'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_clutch)

    def clutch_stats(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class player_stats_clutch(NbaDataProvider):
    def __init__(self):
        url_modifier = 'leaguedashplayerclutch'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_league_clutch)

    def clutch_stats(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


# class transactions(BASE):
#     _pull_url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
#     def transactions(self):
#         return #self._pull.json()['ListItems']

# # Shooting class needs some further study of the data because it classifies shots in two levels.
# # This class will be used for Player & Team as well as Self & Opponent

# class shooting(object):
#     def __init__(self,team=False, measure=1, season=2015, datefrom='', dateto='',distancerange=1,
#     gamescope=1, gamesegment=1, lastngames=0, league="NBA", location=1, month=0, opponentteamid=0,
#     outcome=1, paceadjust=1, permode=1, period=0, playerexperience=1, playerposition=1, plusminus=1,
#     rank=1, seasonsegment=1, seasontype=1, starterbench=1, vsconference=1, vsdivision=1):
#         if team:
#             self._url = "http://stats.nba.com/stats/leaguedashteamshotlocations?"
#         else: self._url = "http://stats.nba.com/stats/leaguedashplayershotlocations?"
#         if measure == 2:
#             measure="Opponent"
#         else: measure='Base'
#         self._api_param = {
#             'DateFrom':datefrom,
#             'DateTo':dateto,
#             'DistanceRange':distance_range(distancerange),
#             'GameScope':game_scope(gamescope),
#             'GameSegment':game_segment(gamesegment),
#             'LastNGames':lastngames,
#             'LeagueID':_nbaLeague(league),
#             'Location':location(location),
#             'MeasureType':measure,
#             'Month':month,
#             'OpponentTeamID':opponentteamid,
#             'Outcome':outcome(outcome),
#             'PaceAdjust':pace_adjust(paceadjust),
#             'PerMode':per_mode_large(permode),
#             'Period':period,
#             'PlayerExperience':player_experience(playerexperience),
#             'PlayerPosition':player_position(playerposition),
#             'PlusMinus':plus_minus(plusminus),
#             'Rank':rank(rank),
#             'Season':_nbaSeason(season),
#             'SeasonSegment':season_segment(seasonsegment),
#             'SeasonType':season_type(seasontype),
#             'StarterBench':starter_bench(starterbench),
#             'VsConference':vs_conference(vsconference),
#             'VsDivision':vs_division(vsdivision)
#         }
#         self._pull = _requests.get(self._url, params=self._api_param)
#     def headers(self):
#         _skip = self._pull.json()['resultSets']['headers'][0]['columnsToSkip']
#         _span = self._pull.json()['resultSets']['headers'][0]['columnSpan']
#         _headers = []
#         for i in self._pull.json()['resultSets']['headers'][0]['columnNames']:
#             for j in self._pull.json()['resultSets']['headers'][1]['columnNames'][_skip:_skip+_span]:
#                 _headers.append(j + " " + i)
#         _headers = self._pull.json()['resultSets']['headers'][1]['columnNames'][:_skip] + _headers
#         return _headers
#     def shooting(self):
#         _headers = self.headers()
#         _values = self._pull.json()['resultSets']['rowSet']
#         return [dict(zip(_headers, value)) for value in _values]

__all__ = ['daily_scoreboard', 'franchise_history', 'playoff_picture',
           'team_stats_classic', 'player_stats_classic', 'lineups',
           'team_stats_clutch', 'player_stats_clutch', 'league_leaders']
