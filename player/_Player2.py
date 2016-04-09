from goldsberry._apiparams import *
from goldsberry._masterclass import NbaDataProvider


class demographics(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_base)
        self._url_modifier = 'commonplayerinfo'
        self._set_class_data()

    def player_info(self):
        return self.get_table_from_data(self.data_tables, 0)

    def headline_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class career_stats(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_career)
        self._url_modifier = 'playerprofilev2'
        self._set_class_data()

    def season_totals_regular(self):
        return self.get_table_from_data(self.data_tables, 0)

    def career_totals_regular(self):
        return self.get_table_from_data(self.data_tables, 1)

    def season_totals_post(self):
        return self.get_table_from_data(self.data_tables, 2)

    def career_totals_post(self):
        return self.get_table_from_data(self.data_tables, 3)

    def season_totals_allstar(self):
        return self.get_table_from_data(self.data_tables, 4)

    def career_totals_allstar(self):
        return self.get_table_from_data(self.data_tables, 5)

    def season_totals_college(self):
        return self.get_table_from_data(self.data_tables, 6)

    def career_totals_college(self):
        return self.get_table_from_data(self.data_tables, 7)

    def season_rankings_regular(self):
        return self.get_table_from_data(self.data_tables, 8)

    def season_rankings_post(self):
        return self.get_table_from_data(self.data_tables, 9)

    def season_high(self):
        return self.get_table_from_data(self.data_tables, 10)

    def career_high(self):
        return self.get_table_from_data(self.data_tables, 11)

    def next_game(self):
        return self.get_table_from_data(self.data_tables, 12)


class game_logs(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_gamelogs)
        self._url_modifier = 'playergamelog'
        self._set_class_data()

    def logs(self):
        return self.get_table_from_data(self.data_tables, 0)


class shot_dashboard(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptshots'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def general(self):
        return self.get_table_from_data(self.data_tables, 1)

    def shot_clock(self):
        return self.get_table_from_data(self.data_tables, 2)

    def dribble(self):
        return self.get_table_from_data(self.data_tables, 3)

    def closest_defender(self):
        return self.get_table_from_data(self.data_tables, 4)

    def closest_defender_10ft(self):
        return self.get_table_from_data(self.data_tables, 5)

    def touch_time(self):
        return self.get_table_from_data(self.data_tables, 6)


class rebound_dashboard(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptreb'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def shot_type(self):
        return self.get_table_from_data(self.data_tables, 1)

    def contesting_rebounders(self):
        return self.get_table_from_data(self.data_tables, 2)

    def shot_distance(self):
        return self.get_table_from_data(self.data_tables, 3)

    def rebound_distanct(self):
        return self.get_table_from_data(self.data_tables, 4)


class passing_dashboard(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptpass'
        self._set_class_data()

    def passes_made(self):
        return self.get_table_from_data(self.data_tables, 0)

    def passes_received(self):
        return self.get_table_from_data(self.data_tables, 1)


class defense_dashboard(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_dashboard)
        self._url_modifier = 'playerdashptshotdefend'
        self._set_class_data()

    def defending_shot(self):
        return self.get_table_from_data(self.data_tables, 0)


class shot_chart(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_shotchart)
        self._url_modifier = 'shotchartdetail'
        self._set_class_data()

    def chart(self):
        return self.get_table_from_data(self.data_tables, 0)

    def leagueaverage(self):
        return self.get_table_from_data(self.data_tables, 1)


class PlayerList(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_ply_list)
        self._url_modifier = 'commonallplayers'
        self._set_class_data()

    def players(self):
        return self.get_table_from_data(self.data_tables, 0)


# BLOCKED BY NBA
class shot_log(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_base)
        self._url_modifier = 'playerdashptsshotlog'
        self._set_class_data()

    def log(self):
        return self.get_table_from_data(self.data_tables, 0)


# BLOCKED BY NBA
class rebound_log(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_base)
        self._url_modifier = 'playerdashptreboundlogs'
        self._set_class_data()

    def log(self):
        return self.get_table_from_data(self.data_tables, 0)


# BLOCKED BY NBA
class general_splits(NbaDataProvider):
    def __init__(self, playerid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(PlayerID=playerid, **p_ply_career)
        self._url_modifier = 'playerdashboardbygeneralsplits'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def location(self):
        return self.get_table_from_data(self.data_tables, 1)

    def wins_losses(self):
        return self.get_table_from_data(self.data_tables, 2)

    def month(self):
        return self.get_table_from_data(self.data_tables, 3)

    def pre_post_allstar(self):
        return self.get_table_from_data(self.data_tables, 4)

    def starting_position(self):
        return self.get_table_from_data(self.data_tables, 5)

    def days_rest(self):
        return self.get_table_from_data(self.data_tables, 6)


__all__ = ["demographics", "career_stats",
           "game_logs", "shot_dashboard", "rebound_dashboard",
           "passing_dashboard", "defense_dashboard",
           "shot_chart"]
