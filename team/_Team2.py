from goldsberry._masterclass import *
from goldsberry._apiparams import *


class defense_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_base)
        self._url_modifier = 'teamdashptshotdefend'
        self._set_class_data()

    def defending_shot(self):
        return self.get_table_from_data(self.data_tables, 0)


class game_logs(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_ply_gamelogs)
        self._url_modifier = 'teamgamelog'
        self._set_class_data()

    def logs(self):
        return self.get_table_from_data(self.data_tables, 0)


class lineups(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_lineups)
        self._url_modifier = 'teamdashlineups'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def lineups(self):
        return self.get_table_from_data(self.data_tables, 1)


class passing_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptpass'
        self._set_class_data()

    def passes_made(self):
        return self.get_table_from_data(self.data_tables, 0)

    def passes_received(self):
        return self.get_table_from_data(self.data_tables, 1)


class on_off_court(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_onoff)
        self._url_modifier = 'teamplayeronoffdetails'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def on_court(self):
        return self.get_table_from_data(self.data_tables, 1)

    def off_court(self):
        return self.get_table_from_data(self.data_tables, 2)

    def overall_summary(self):
        return self.get_table_from_data(self.data_tables, 3)

    def on_court_summary(self):
        return self.get_table_from_data(self.data_tables, 4)

    def off_court_summary(self):
        return self.get_table_from_data(self.data_tables, 5)


class rebound_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptreb'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def shot_type(self):
        return self.get_table_from_data(self.data_tables, 1)

    def contesting_rebounders(self):
        return self.get_table_from_data(self.data_tables, 2)

    def shot_distance(self):
        return self.get_table_from_data(self.data_tables, 3)

    def rebound_distance(self):
        return self.get_table_from_data(self.data_tables, 4)


class roster(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_base)
        self._url_modifier = 'commonteamroster'
        self._set_class_data()

    def player(self):
        return self.get_table_from_data(self.data_tables, 0)

    def coaches(self):
        return self.get_table_from_data(self.data_tables, 1)


class season_stats(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_season)
        self._url_modifier = 'teamplayerdashboard'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def player_totals(self):
        return self.get_table_from_data(self.data_tables, 1)


class shot_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptshots'
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


class shooting_splits(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_shooting)
        self._url_modifier = 'teamdashboardbyshootingsplits'
        self._set_class_data()

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def shot_5ft(self):
        return self.get_table_from_data(self.data_tables, 1)

    def shot_8ft(self):
        return self.get_table_from_data(self.data_tables, 2)

    def shot_area(self):
        return self.get_table_from_data(self.data_tables, 3)

    def assisted_shot(self):
        return self.get_table_from_data(self.data_tables, 4)

    def shot_type(self):
        return self.get_table_from_data(self.data_tables, 5)

    def assisted_by(self):
        return self.get_table_from_data(self.data_tables, 6)


class splits(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_team_split)
        self._url_modifier = 'teamdashboardbygeneralsplits'
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

    def days_rest(self):
        return self.get_table_from_data(self.data_tables, 5)


class team_info(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_info)
        self._url_modifier = 'teaminfocommon'
        self._set_class_data()

    def info(self):
        return self.get_table_from_data(self.data_tables, 0)

    def season_ranks(self):
        return self.get_table_from_data(self.data_tables, 1)


class year_by_year(NbaDataProvider):
    def __init__(self, teamid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(TeamID=teamid, **p_base)
        self._url_modifier = 'teamyearbyyearstats'
        self._set_class_data()

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 0)


__all__ = ['defense_dashboard', 'game_logs', 'lineups', 'passing_dashboard',
           'on_off_court', 'rebound_dashboard', 'roster', 'season_stats',
           'shot_dashboard', 'shooting_splits', 'splits', 'team_info',
           'year_by_year']

# class history:
#     def __init__(self, teamid):
#         self._url = "".join(["http://stats.nba.com/feeds/teams/profile/",str(teamid),"_TeamProfile.js"])
#         self._pull = _requests.get(self._url)
#     def details(self):
#         return self._pull.json()['TeamDetails'][0]['Details']
#     def history(self):
#         return self._pull.json()['TeamDetails'][1]['History']
#     def social_sites(self):
#         return self._pull.json()['TeamDetails'][2]['SocialSites']
#     def championships(self):
#         if self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships'] == []:
#             return ["None"]
#         else: return self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships']
#     def conference_titles(self):
#         if self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles'] == []:
#             return ["None"]
#         else: return self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles']
#     def divisional_titles(self):
#         if self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles'] == []:
#             return ['None']
#         else: return self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles']
#     def hof_inductees(self):
#         return self._pull.json()['TeamDetails'][4]['HallOfFameInductees']
#     def retired_members(self):
#         return self._pull.json()['TeamDetails'][5]['RetiredMembers']
