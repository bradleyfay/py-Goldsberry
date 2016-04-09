from goldsberry._masterclass import *
from goldsberry._apiparams import *

class daily_scoreboard(NBA_datapull):
    def __init__(self, date):
        NBA_datapull.__init__(self)
        self.SET_parameters(gameDate=date,**p_league_sb)
        self._url_modifier = 'scoreboardV2'
        self.GET_raw_data()
    def game_header(self):
        return self._get_table_from_data(self._datatables, 0)
    def linescore(self):
        return self._get_table_from_data(self._datatables, 1)
    def series_standings(self):
        return self._get_table_from_data(self._datatables, 2)
    def last_meeting(self):
        return self._get_table_from_data(self._datatables, 3)
    def eastern_conference_standings(self):
        return self._get_table_from_data(self._datatables, 4)
    def western_conference_standings(self):
        return self._get_table_from_data(self._datatables, 5)
    def available(self):
        return self._get_table_from_data(self._datatables, 6)
    def team_leaders(self):
        return self._get_table_from_data(self._datatables, 7)
    def _ticket_links(self):
        return self._get_table_from_data(self._datatables, 8)
    def win_probability(self):
        return self._get_table_from_data(self._datatables, 9)

class franchise_history(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_history)
        self._url_modifier = 'franchisehistory'
        self.GET_raw_data()
    def current_teams(self):
        return self._get_table_from_data(self._datatables, 0)
    def defunct_teams(self):
        return self._get_table_from_data(self._datatables, 1)

## This one might not work because it's the key 'resultSet', not 'resultSets'
## Confirmed does not work
class league_leaders(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_leaders)
        self._url_modifier = 'leagueleaders'
        self.GET_raw_data()
    def leaders(self):
        return self._get_table_from_data(self._datatables, 0)

class lineups(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'leaguedashlineups'
        self.GET_raw_data()
    def lineups(self):
        return self._get_table_from_data(self._datatables, 0)

# Doubl Check Stem
class playoff_picture(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'playoffpicture'
        self.GET_raw_data()
    def eastern_conf_playoff_picture(self):
        return self._get_table_from_data(self._datatables, 0)
    def western_conf_playoff_picture(self):
        return self._get_table_from_data(self._datatables, 1)
    def eastern_conf_standings(self):
        return self._get_table_from_data(self._datatables, 2)
    def western_conf_standings(self):
        return self._get_table_from_data(self._datatables, 3)
    def eastern_conf_remaining_games(self):
        return self._get_table_from_data(self._datatables, 4)
    def western_conf_remaining_games(self):
        return self._get_table_from_data(self._datatables, 5)

class team_stats_classic(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_classic)
        self._url_modifier = 'leaguedashteamstats'
        self.GET_raw_data()
    def stats(self):
        return self._get_table_from_data(self._datatables, 0)

class player_stats_classic(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_classic)
        self._url_modifier = 'leaguedashplayerstats'
        self.GET_raw_data()
    def stats(self):
        return self._get_table_from_data(self._datatables, 0)

class team_stats_clutch(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_clutch)
        self._url_modifier = 'leaguedashteamclutch'
        self.GET_raw_data()
    def clutch_stats(self):
        return self._get_table_from_data(self._datatables, 0)

class player_stats_clutch(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_league_clutch)
        self._url_modifier = 'leaguedashplayerclutch'
        self.GET_raw_data()
    def clutch_stats(self):
        return self._get_table_from_data(self._datatables, 0)



# class transactions(BASE):
#     _pull_url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
#     def transactions(self):
#         return #self._pull.json()['ListItems']

# ## Shooting class needs some further study of the data because it classifies shots in two levels. This class will be used for Player & Team as well as Self & Opponent

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
#             'DistanceRange':_distance_range(distancerange),
#             'GameScope':_game_scope(gamescope),
#             'GameSegment':_game_segment(gamesegment),
#             'LastNGames':lastngames,
#             'LeagueID':_nbaLeague(league),
#             'Location':_location(location),
#             'MeasureType':measure,
#             'Month':month,
#             'OpponentTeamID':opponentteamid,
#             'Outcome':_outcome(outcome),
#             'PaceAdjust':_pace_adjust(paceadjust),
#             'PerMode':_per_mode_large(permode),
#             'Period':period,
#             'PlayerExperience':_player_experience(playerexperience),
#             'PlayerPosition':_player_position(playerposition),
#             'PlusMinus':_plus_minus(plusminus),
#             'Rank':_rank(rank),
#             'Season':_nbaSeason(season),
#             'SeasonSegment':_season_segment(seasonsegment),
#             'SeasonType':_season_type(seasontype),
#             'StarterBench':_starter_bench(starterbench),
#             'VsConference':_vs_conference(vsconference),
#             'VsDivision':_vs_division(vsdivision)
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