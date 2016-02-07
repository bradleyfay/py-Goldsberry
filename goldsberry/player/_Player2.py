
from goldsberry._apiparams import *
from goldsberry._masterclass import *

class demographics(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_base)
        self._url_modifier = 'commonplayerinfo'
    def player_info(self):
        return self._get_table_from_data(self._datatables, 0)
    def headline_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class career_stats(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_career)
        self._url_modifier = 'playerprofilev2'
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

# BLOCKED BY NBA
class general_splits(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_career)
        self._url_modifier = 'playerdashboardbygeneralsplits'
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

class game_logs(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_gamelogs)
        self._url_modifier = 'playergamelog'
    def logs(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_dashboard(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptshots'
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

# BLOCKED BY NBA
class rebound_dashboard(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptreb'
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

class passing_dashboard(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptpass'
    def passes_made(self):
        return self._get_table_from_data(self._datatables, 0)
    def passes_received(self):
        return self._get_table_from_data(self._datatables, 1)

class defense_dashboard(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptshotdefend'
    def defending_shot(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_log(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_base)
        self._url_modifier = 'playerdashptsshotlog'
    def log(self):
        return self._get_table_from_data(self._datatables, 0)

class rebound_log(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_base)
        self._url_modifier = 'playerdashptreboundlogs'
    def log(self):
        return self._get_table_from_data(self._datatables, 0)

class shot_chart(NBA_datapull):
    def __init__(self, playerid):
        NBA_datapull.__init__(self)
        self.SET_parameters(PlayerID = playerid, **p_base)
        self._url_modifier = 'shotchartdetail'
    def chart(self):
        return self._get_table_from_data(self._datatables, 0)
    def leagueaverage(self):
        return self._get_table_from_data(self._datatables, 1)

class PlayerList(NBA_datapull):
    _url_modifier = 'commonallplayers'
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_ply_list)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)
    def players(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ["demographics", "career_stats", "general_splits", 
           "game_logs", "shot_dashboard", "rebound_dashboard",
           "passing_dashboard", "defense_dashboard", "shot_log", 
           "rebound_log", "shot_chart"]