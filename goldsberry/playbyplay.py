import requests

class PlayByPlay:
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/playbyplayv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def Plays(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def AvailableVideo(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]