from goldsberry._masterclass import *
from goldsberry._apiparams import *

class demographics(PLAYER, default_parameters):
    _url_modifier = 'commonplayerinfo'
    def player_info(self):
        return self._get_table_from_data(self._datatables, 0)
    def headline_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class career_stats(PLAYER, default_params):
    _url_modifier = 'playerprofilev2'
    def season_totals_regular(self):
        return self._get_table_from_data(self._datatables, 0)
    def career_totals_regular(self):
        return self._get_table_from_data(self._datatables, 1)
    def season_totals_post(self):
        return self._get_table_from_data(self._datatables, 2)
    def career_totals_post(self):
        return self._get_table_from_data(self._datatables, 3)
    def season_totals_allstar(self):
        return self._get_table_from_data(self._datatables, 4)
    def career_totals_allstar(self):
        return self._get_table_from_data(self._datatables, 5)
    def season_totals_college(self):
        return self._get_table_from_data(self._datatables, 6)
    def career_totals_college(self):
        return self._get_table_from_data(self._datatables, 7)
    def season_rankings_regular(self):
        return self._get_table_from_data(self._datatables, 8)
    def season_rankings_post(self):
        return self._get_table_from_data(self._datatables, 9)
    def season_high(self):
        return self._get_table_from_data(self._datatables, 10)
    def career_high(self):
        return self._get_table_from_data(self._datatables, 11)
    def next_game(self):
        return self._get_table_from_data(self._datatables, 12)

class general_splits(PLAYER, default_parameters):
    _url_modifier = 'playerdashboardbygeneralsplits'
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def location(self):
        return self._get_table_from_data(self._datatables, 1)
    def wins_losses(self):
        return self._get_table_from_data(self._datatables, 2)
    def month(self):
        return self._get_table_from_data(self._datatables, 3)
    def pre_post_allstar(self):
        return self._get_table_from_data(self._datatables, 4)
    def starting_position(self):
        return self._get_table_from_data(self._datatables, 5)
    def days_rest(self):
        return self._get_table_from_data(self._datatables, 6)

class game_logs(PLAYER, default_parameters):
    _url_modifier = 'playergamelog'
    def logs(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_dashboard(PLAYER, default_parameters):
    _url_modifier = 'playerdashptshots'
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def general(self):
        return self._get_table_from_data(self._datatables, 1)
    def shot_clock(self):
        return self._get_table_from_data(self._datatables, 2)
    def dribble(self):
        return self._get_table_from_data(self._datatables, 3)
    def closest_defender(self):
        return self._get_table_from_data(self._datatables, 4)
    def closest_defender_10ft(self):
        return self._get_table_from_data(self._datatables, 5)
    def touch_time(self):
        return self._get_table_from_data(self._datatables, 6)

class rebound_dashboard(PLAYER, default_parameters):
    _url_modifier = 'playerdashptreb'
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def shot_type(self):
        return self._get_table_from_data(self._datatables, 1)
    def contesting_rebounders(self):
        return self._get_table_from_data(self._datatables, 2)
    def shot_distance(self):
        return self._get_table_from_data(self._datatables, 3)
    def rebound_distanct(self):
        return self._get_table_from_data(self._datatables, 4)

class passing_dashboard(PLAYER, default_parameters):
    _url_modifier = 'playerdashptpass'
    def passes_made(self):
        return self._get_table_from_data(self._datatables, 0)
    def passes_received(self):
        return self._get_table_from_data(self._datatables, 1)

class defense_dashboard(PLAYER, default_parameters):
    _url_modifier = 'playerdashptshotdefend'
    def defending_shot(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_log(PLAYER, default_parameters):
    _url_modifier = 'playerdashptsshotlog'
    def log(self):
        return self._get_table_from_data(self._datatables, 0)

class rebound_log(PLAYER, default_parameters):
    _url_modifier = 'playerdashptreboundlogs'
    def log(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_chart(PLAYER, default_parameters):
    _url_modifier = 'shotchartdetail'
    def chart(self):
        return self._get_table_from_data(self._datatables, 0)
    def leagueaverage(self):
        return self._get_table_from_data(self._datatables, 1)

def PlayerList(season='2015', AllTime=False, league='NBA'):
    if AllTime:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"0",
                      'LeagueID':_nbaLeague(league),
                      'Season': "2015-16"}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    else:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"1",
                      'LeagueID': _nbaLeague(league),
                      'Season': _nbaSeason(season)}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ["demographics", "career_stats", "general_splits", 
           "game_logs", "shot_dashboard", "rebound_dashboard",
           "passing_dashboard", "defense_dashboard", "shot_log", 
           "rebound_log", "shot_chart"]