from goldsberry.masterclass import NbaDataProvider
from goldsberry.apiparams import *


class demographics(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'commonplayerinfo'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_player_common, PlayerID=player_id)

    def player_info(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def headline_stats(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)


class career_stats(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerprofilev2'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_career, PlayerID=player_id)

    def season_totals_regular(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def career_totals_regular(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def season_totals_post(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def career_totals_post(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def season_totals_allstar(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)

    def career_totals_allstar(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 5)

    def season_totals_college(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 6)

    def career_totals_college(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 7)

    def season_rankings_regular(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 8)

    def season_rankings_post(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 9)

    def season_high(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 10)

    def career_high(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 11)

    def next_game(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 12)


class game_logs(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playergamelog'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_gamelogs, PlayerID=player_id,
                                 Season=season)

    def logs(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class shot_dashboard(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptshots'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_dashboard, PlayerID=player_id,
                                 Season=season)

    def overall(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def general(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def shot_clock(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def dribble(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def closest_defender(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)

    def closest_defender_10ft(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 5)

    def touch_time(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 6)


class rebound_dashboard(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptreb'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_dashboard, PlayerID=player_id,
                                 Season=season)

    def overall(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def shot_type(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def contesting_rebounders(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def shot_distance(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def rebound_distanct(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)


class passing_dashboard(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptpass'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_dashboard, PlayerID=player_id,
                                 Season=season)

    def passes_made(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def passes_received(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)


class defense_dashboard(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptshotdefend'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_dashboard, PlayerID=player_id,
                                 Season=season)

    def defending_shot(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


class shot_chart(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'shotchartdetail'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_shotchart, PlayerID=player_id,
                                 Season=season)

    def chart(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def leagueaverage(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)


class PlayerList(NbaDataProvider):
    def __init__(self, season=default_season, is_only_current_season=1):
        url_modifier = 'commonallplayers'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_list, Season=season,
                                 IsOnlyCurrentSeason=is_only_current_season)

    def players(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


# BLOCKED BY NBA
class shot_log(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptsshotlog'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base, PlayerID=player_id,
                                 Season=season)

    def log(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


# BLOCKED BY NBA
class rebound_log(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashptreboundlogs'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base, PlayerID=player_id,
                                 Season=season)

    def log(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)


# BLOCKED BY NBA
class general_splits(NbaDataProvider):
    def __init__(self, player_id, season=default_season):
        url_modifier = 'playerdashboardbygeneralsplits'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_career, PlayerID=player_id,
                                 Season=season)

    def overall(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def location(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    def wins_losses(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 2)

    def month(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 3)

    def pre_post_allstar(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 4)

    def starting_position(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 5)

    def days_rest(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 6)


__all__ = ["demographics", "career_stats",
           "game_logs", "shot_dashboard", "rebound_dashboard",
           "passing_dashboard", "defense_dashboard",
           "shot_chart"]
