import requests as _requests
from goldsberry.apiconvertor import *

class play_by_play:
    def __init__(self, gameid, startperiod=1, endperiod=10):
        self._url = "http://stats.nba.com/stats/playbyplayv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'GameID':gameid,
                           'StartPeriod':startperiod
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def plays(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def _available_video(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_summary:
    def __init__(self, gameid):
        self._url = "http://stats.nba.com/stats/boxscoresummaryv2?"
        self._api_param = {'GameID':gameid}
        self._pull = _requests.get(self._url, params=self._api_param)
    def game_summary(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def other_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def officials(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def inactive_players(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def game_info(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def line_score(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def last_meeting(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_series(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def _available_video(self):
        _headers = self._pull.json()['resultSets'][7]['headers']
        _values = self._pull.json()['resultSets'][7]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_traditional:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoretraditionalv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_advanced:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoreadvancedv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_misc:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoremiscv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_scoring:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscorescoringv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_fourfactors:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscorefourfactorsv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_usage:
    """
    """
    def __init__(self, gameid, startperiod=1, endperiod=10, startrange=0,
                endrange=28800, rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoreusagev2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class boxscore_tracking:
    """
    """
    def __init__(self, gameid):
        self._url = "http://stats.nba.com/stats/boxscoreplayertrackv2?"
        self._api_param = {'GameID':gameid}
        self._pull = _requests.get(self._url, params=self._api_param)
    def player_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

def GameIDs():
    _url = "https://raw.github.com/bradleyfay/py-Goldsberry/master/data/gameids.json"
    _pull = _requests.get(_url)
    return _pull.json()

__all__ = ['play_by_play', 'boxscore_summary', 'boxscore_traditional',
            'boxscore_advanced', 'boxscore_misc', 'boxscore_scoring',
            'boxscore_fourfactors', 'boxscore_usage', 'boxscore_tracking']
