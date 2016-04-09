from goldsberry._masterclass import *
from goldsberry._apiparams import *

class boxscore_advanced(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_bs)
        self._url_modifier = 'boxscoreadvancedv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_fourfactors(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_bs)
        self._url_modifier = 'boxscorefourfactorsv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_miscellaneous(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_bs)
        self._url_modifier = 'boxscoremiscv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_scoring(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_base)
        self._url_modifier = 'boxscorescoringv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_summary(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid)
        self._url_modifier = 'boxscoresummaryv2'
        self.GET_raw_data()
    def game_summary(self):
        return self._get_table_from_data(self._datatables, 0)
    def other_stats(self):
        return self._get_table_from_data(self._datatables, 1)
    def officials(self):
        return self._get_table_from_data(self._datatables, 2)
    def inactive_players(self):
        return self._get_table_from_data(self._datatables, 3)
    def game_info(self):
        return self._get_table_from_data(self._datatables, 4)
    def line_score(self):
        return self._get_table_from_data(self._datatables, 5)
    def last_meeting(self):
        return self._get_table_from_data(self._datatables, 6)
    def season_series(self):
        return self._get_table_from_data(self._datatables, 7)
    def _available_video(self):
        return self._get_table_from_data(self._datatables, 8)

class boxscore_tracking(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid)
        self._url_modifier = 'boxscoreplayertrackv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_traditional(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_bs)
        self._url_modifier = 'boxscoretraditionalv2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_usage(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_bs)
        self._url_modifier = 'boxscoreusagev2'
        self.GET_raw_data()
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class play_by_play(NBA_datapull):
    def __init__(self, gameid):
        NBA_datapull.__init__(self)
        self.SET_parameters(GameID = gameid, **p_game_pbp)
        self._url_modifier = 'playbyplayv2'
        self.GET_raw_data()
    def player_info(self):
        return self._get_table_from_data(self._datatables, 0)
    def _available_video(self):
        return self._get_table_from_data(self._datatables, 1)

# Courtesy of daniel.silvis@gmail.com
class GameIDs(NBA_datapull):
    def __init__(self):
        NBA_datapull.__init__(self)
        self.SET_parameters(**p_game_ids)
        self._url_modifier = 'leaguegamelog'
        self.GET_raw_data()
    def game_list(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ['play_by_play', 'boxscore_summary', 'boxscore_traditional', 
           'boxscore_advanced', 'boxscore_miscellaneous', 'boxscore_scoring',
           'boxscore_fourfactors', 'boxscore_usage', 'boxscore_tracking']