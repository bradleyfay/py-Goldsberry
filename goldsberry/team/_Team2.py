from goldsberry._masterclass import *
from goldsberry._apiparams import *

class history:
    def __init__(self, teamid):
        self._url = "".join(["http://stats.nba.com/feeds/teams/profile/",str(teamid),"_TeamProfile.js"])
        self._pull = _requests.get(self._url)
    def details(self):
        return self._pull.json()['TeamDetails'][0]['Details']
    def history(self):
        return self._pull.json()['TeamDetails'][1]['History']
    def social_sites(self):
        return self._pull.json()['TeamDetails'][2]['SocialSites']
    def championships(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships']
    def conference_titles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles']
    def divisional_titles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles'] == []:
            return ['None']
        else: return self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles']
    def hof_inductees(self):
        return self._pull.json()['TeamDetails'][4]['HallOfFameInductees']
    def retired_members(self):
        return self._pull.json()['TeamDetails'][5]['RetiredMembers']

class team_info(TEAM, default_parameters):
    _url_modifier = 'teaminfocommon'
    def info(self):
        return self._get_table_from_data(self._datatables, 0)
    def season_ranks(self):
        return self._get_table_from_data(self._datatables, 1)

class roster(TEAM, default_parameters):
    _url_modifier = 'commonteamroster'
    def player(self):
        return self._get_table_from_data(self._datatables, 0)
    def coaches(self):
        return self._get_table_from_data(self._datatables, 1)

class splits(TEAM, default_parameters):
    _url_modifier = 'teamdashboardbygeneralsplits'
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

class season_stats(TEAM, default_parameters):
    _url_modifier = 'teamplayerdashboard'
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def player_totals(self):
        return self._get_table_from_data(self._datatables, 1)

class on_off_court(TEAM, default_parameters):
    _url_modifier = 'teamplayeronoffdetails'
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

class year_by_year(TEAM, default_parameters):
    _url_modifier = 'teamyearbyyearstats'
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 0)

class game_logs(TEAM, default_parameters):
    _url_modifier = 'teamgamelog'
    def logs(self):
        return self._get_table_from_data(self._datatables, 0)

class lineups(TEAM, default_parameters):
    _url_modifier = 'teamdashlineups'
    def overall(self):
        return self._get_table_from_data(self._datatables, 0)
    def lineups(self):
        return self._get_table_from_data(self._datatables, 1)

class shooting_splits(TEAM, default_parameters):
    _url_modifier = 'teamdashboardbyshootingsplits'
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

class passing_dashboard(TEAM, default_parameters):
    _url_modifier = 'teamdashptpass'
    def passes_made(self):
        return self._get_table_from_data(self._datatables, 0)
    def passes_received(self):
        return self._get_table_from_data(self._datatables, 1)

class rebound_dashboard(TEAM, default_parameters):
    _url_modifier = 'teamdashptreb'
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

class shot_dashboard(TEAM, default_parameters):
    _url_modifier = 'teamdashptshots'
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

class defense_dashboard(TEAM, default_parameters):
    _url_modifier = 'teamdashptshotdefend'
    def defending_shot(self):
        return self._get_table_from_data(self._datatables, 0)

__all__ = ['team_info', 'roster', 'history', 'splits','season_stats', 'on_off_court', 
           'on_off_court', 'game_logs', 'lineups', 'shooting_splits', 'passing_dashboard',
           'passing_dashboard', 'shot_dashboard']