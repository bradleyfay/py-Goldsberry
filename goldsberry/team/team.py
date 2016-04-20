import goldsberry.masterclass
from goldsberry.apiparams import *


class defense_dashboard(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashptshotdefend'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base,
                                                        TeamID=team_id, **kwargs)

    def defending_shot(self):
        return self._get_table_from_data(self._data_tables, 0)


class game_logs(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamgamelog'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_ply_gamelogs,
                                                        TeamID=team_id, **kwargs)

    def logs(self):
        return self._get_table_from_data(self._data_tables, 0)


class lineups(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashlineups'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_lineups,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def lineups(self):
        return self._get_table_from_data(self._data_tables, 1)


class passing_dashboard(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashptpass'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd,
                                                        TeamID=team_id, **kwargs)

    def passes_made(self):
        return self._get_table_from_data(self._data_tables, 0)

    def passes_received(self):
        return self._get_table_from_data(self._data_tables, 1)


class on_off_court(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamplayeronoffdetails'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_onoff,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def on_court(self):
        return self._get_table_from_data(self._data_tables, 1)

    def off_court(self):
        return self._get_table_from_data(self._data_tables, 2)

    def overall_summary(self):
        return self._get_table_from_data(self._data_tables, 3)

    def on_court_summary(self):
        return self._get_table_from_data(self._data_tables, 4)

    def off_court_summary(self):
        return self._get_table_from_data(self._data_tables, 5)


class rebound_dashboard(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashptreb'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def shot_type(self):
        return self._get_table_from_data(self._data_tables, 1)

    def contesting_rebounders(self):
        return self._get_table_from_data(self._data_tables, 2)

    def shot_distance(self):
        return self._get_table_from_data(self._data_tables, 3)

    def rebound_distance(self):
        return self._get_table_from_data(self._data_tables, 4)


class roster(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'commonteamroster'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base,
                                                        TeamID=team_id, **kwargs)

    def player(self):
        return self._get_table_from_data(self._data_tables, 0)

    def coaches(self):
        return self._get_table_from_data(self._data_tables, 1)


class season_stats(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamplayerdashboard'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_season,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def player_totals(self):
        return self._get_table_from_data(self._data_tables, 1)


class shot_dashboard(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashptshots'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_dashbd,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def general(self):
        return self._get_table_from_data(self._data_tables, 1)

    def shot_clock(self):
        return self._get_table_from_data(self._data_tables, 2)

    def dribble(self):
        return self._get_table_from_data(self._data_tables, 3)

    def closest_defender(self):
        return self._get_table_from_data(self._data_tables, 4)

    def closest_defender_10ft(self):
        return self._get_table_from_data(self._data_tables, 5)

    def touch_time(self):
        return self._get_table_from_data(self._data_tables, 6)


class shooting_splits(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashboardbyshootingsplits'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_shooting,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def shot_5ft(self):
        return self._get_table_from_data(self._data_tables, 1)

    def shot_8ft(self):
        return self._get_table_from_data(self._data_tables, 2)

    def shot_area(self):
        return self._get_table_from_data(self._data_tables, 3)

    def assisted_shot(self):
        return self._get_table_from_data(self._data_tables, 4)

    def shot_type(self):
        return self._get_table_from_data(self._data_tables, 5)

    def assisted_by(self):
        return self._get_table_from_data(self._data_tables, 6)


class splits(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamdashboardbygeneralsplits'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_team_split,
                                                        TeamID=team_id, **kwargs)

    def overall(self):
        return self._get_table_from_data(self._data_tables, 0)

    def location(self):
        return self._get_table_from_data(self._data_tables, 1)

    def wins_losses(self):
        return self._get_table_from_data(self._data_tables, 2)

    def month(self):
        return self._get_table_from_data(self._data_tables, 3)

    def pre_post_allstar(self):
        return self._get_table_from_data(self._data_tables, 4)

    def days_rest(self):
        return self._get_table_from_data(self._data_tables, 5)


class team_info(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teaminfocommon'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_info,
                                                        TeamID=team_id, **kwargs)

    def info(self):
        return self._get_table_from_data(self._data_tables, 0)

    def season_ranks(self):
        return self._get_table_from_data(self._data_tables, 1)


class year_by_year(goldsberry.masterclass.NbaDataProvider):
    def __init__(self, team_id, **kwargs):
        url_modifier = 'teamyearbyyearstats'
        goldsberry.masterclass.NbaDataProvider.__init__(self, url_modifier=url_modifier, default_params=p_base,
                                                        TeamID=team_id, **kwargs)

    def team_stats(self):
        return self._get_table_from_data(self._data_tables, 0)


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