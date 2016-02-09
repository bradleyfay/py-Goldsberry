from goldsberry._masterclass import *
from goldsberry._apiparams import *

class defense_dashboard(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_base)
        self._url_modifier = 'teamdashptshotdefend'
        self.GET_raw_data()
    def defending_shot(self):
        return self._get_table_from_data(self._datatables, 0)

class game_logs(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_ply_gamelogs)
        self._url_modifier = 'teamgamelog'
        self.GET_raw_data()
    def logs(self):
        return self._get_table_from_data(self._datatables, 0)

class lineups(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_lineups)
        self._url_modifier = 'teamdashlineups'
        self.GET_raw_data()
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def lineups(self):
        return self._get_table_from_data(self._datatables, 1)

class passing_dashboard(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptpass'
        self.GET_raw_data()
    def passes_made(self):
        return self._get_table_from_data(self._datatables, 0)
    def passes_received(self):
        return self._get_table_from_data(self._datatables, 1)

class on_off_court(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_onoff)
        self._url_modifier =  'teamplayeronoffdetails'
        self.GET_raw_data()
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def on_court(self):
        return self._get_table_from_data(self._datatables, 1)
    def off_court(self):
        return self._get_table_from_data(self._datatables, 2)
    def overall_summary(self):
        return self._get_table_from_data(self._datatables, 3)
    def on_court_summary(self):
        return self._get_table_from_data(self._datatables, 4)
    def off_court_summary(self):
        return self._get_table_from_data(self._datatables, 5)

class rebound_dashboard(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptreb'
        self.GET_raw_data()
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def shot_type(self):
        return self._get_table_from_data(self._datatables, 1)
    def contesting_rebounders(self):
        return self._get_table_from_data(self._datatables, 2)
    def shot_distance(self):
        return self._get_table_from_data(self._datatables, 3)
    def rebound_distance(self):
        return self._get_table_from_data(self._datatables, 4)

class roster(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_base)
        self._url_modifier = 'commonteamroster'
        self.GET_raw_data()
    def player(self):
        return self._get_table_from_data(self._datatables, 0)
    def coaches(self):
        return self._get_table_from_data(self._datatables, 1)

class season_stats(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_season)
        self._url_modifier = 'teamplayerdashboard'
        self.GET_raw_data()
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def player_totals(self):
        return self._get_table_from_data(self._datatables, 1)

class shot_dashboard(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_dashbd)
        self._url_modifier = 'teamdashptshots'
        self.GET_raw_data()
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

class shooting_splits(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_shooting)
        self._url_modifier = 'teamdashboardbyshootingsplits'
        self.GET_raw_data()
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def shot_5ft(self):
        return self._get_table_from_data(self._datatables, 1)
    def shot_8ft(self):
        return self._get_table_from_data(self._datatables, 2)
    def shot_area(self):
        return self._get_table_from_data(self._datatables, 3)
    def assisted_shot(self):
        return self._get_table_from_data(self._datatables, 4)
    def shot_type(self):
        return self._get_table_from_data(self._datatables, 5)
    def assisted_by(self):
        return self._get_table_from_data(self._datatables, 6)

class splits(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_team_split)
        self._url_modifier = 'teamdashboardbygeneralsplits'
        self.GET_raw_data()
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
    def days_rest(self):
        return self._get_table_from_data(self._datatables, 5)

class team_info(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_info)
        self._url_modifier = 'teaminfocommon'
        self.GET_raw_data()
    def info(self):
        return self._get_table_from_data(self._datatables, 0)
    def season_ranks(self):
        return self._get_table_from_data(self._datatables, 1)

class year_by_year(NBA_datapull):
    def __init__(self, teamid):
        NBA_datapull.__init__(self)
        self.SET_parameters(TeamID = teamid, **p_base)
        self._url_modifier = 'teamyearbyyearstats'
        self.GET_raw_data()
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ['defense_dashboard', 'game_logs', 'lineups', 'passing_dashboard',
           'on_off_court', 'rebound_dashboard', 'roster', 'season_stats',
           'shot_dashboard', 'shooting_splits', 'splits', 'team_info',
           'year_by_year']

# 
class history:
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