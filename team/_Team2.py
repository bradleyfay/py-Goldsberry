from goldsberry._masterclass import *
from goldsberry._apiparams import *


class defense_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamdashptshotdefend'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base, TeamID=teamid)

    def defending_shot(self):
        return self.get_table_from_data(self.data_tables, 0)


class game_logs(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamgamelog'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_gamelogs, TeamID=teamid)

    def logs(self):
        return self.get_table_from_data(self.data_tables, 0)


class lineups(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamdashlineups'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_lineups, TeamID=teamid)

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def lineups(self):
        return self.get_table_from_data(self.data_tables, 1)


class passing_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamdashptpass'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd, TeamID=teamid)

    def passes_made(self):
        return self.get_table_from_data(self.data_tables, 0)

    def passes_received(self):
        return self.get_table_from_data(self.data_tables, 1)


class on_off_court(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamplayeronoffdetails'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_onoff, TeamID=teamid)

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
        url_modifier = 'teamdashptreb'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd, TeamID=teamid)

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
        url_modifier = 'commonteamroster'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base, TeamID=teamid)

    def player(self):
        return self.get_table_from_data(self.data_tables, 0)

    def coaches(self):
        return self.get_table_from_data(self.data_tables, 1)


class season_stats(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamplayerdashboard'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_season, TeamID=teamid)

    def overall(self):
        return self.get_table_from_data(self.data_tables, 0)

    def player_totals(self):
        return self.get_table_from_data(self.data_tables, 1)


class shot_dashboard(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamdashptshots'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd, TeamID=teamid)

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
        url_modifier = 'teamdashboardbyshootingsplits'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_shooting, TeamID=teamid)

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
        url_modifier = 'teamdashboardbygeneralsplits'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_split, TeamID=teamid)

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
        url_modifier = 'teaminfocommon'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_info, TeamID=teamid)

    def info(self):
        return self.get_table_from_data(self.data_tables, 0)

    def season_ranks(self):
        return self.get_table_from_data(self.data_tables, 1)


class year_by_year(NbaDataProvider):
    def __init__(self, teamid):
        url_modifier = 'teamyearbyyearstats'
        NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base, TeamID=teamid)

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
