from goldsberry._masterclass import *
from goldsberry._apiparams import *

class play_by_play(GAME, default_parameters):
    _url_modifier = 'playbyplayv2'
    def player_info(self):
        return self._get_table_from_data(self._datatables, 0)
    def _available_video(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_summary(GAME, default_parameters):
    _url_modifier = 'boxscoresummaryv2'
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

class boxscore_traditional(GAME, default_parameters):
    _url_modifier = 'boxscoretraditionalv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_advanced(GAME, default_parameters):
    _url_modifier = 'boxscoreadvancedv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_miscellaneous(GAME, default_parameters):
    _url_modifier = 'boxscoremiscv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_scoring(GAME, default_parameters):
    _url_modifier = 'boxscorescoringv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_fourfactors(GAME, default_parameters):
    _url_modifier = 'boxscorefourfactorsv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_usage(GAME, default_parameters):
    _url_modifier = 'boxscoreusagev2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

class boxscore_tracking(GAME, default_parameters):
    _url_modifier = 'boxscoretrackingv2'
    def player_stats(self):
        return self._get_table_from_data(self._datatables, 0)
    def team_stats(self):
        return self._get_table_from_data(self._datatables, 1)

# Replace this with code from email
def GameIDs():
    _url = "https://raw.github.com/bradleyfay/py-Goldsberry/master/data/gameids.json"
    _pull = _requests.get(_url)
    return _pull.json()

__all__ = ['play_by_play', 'boxscore_summary', 'boxscore_traditional', 
            'boxscore_advanced', 'boxscore_misc', 'boxscore_scoring',
            'boxscore_fourfactors', 'boxscore_usage', 'boxscore_tracking']