class PlayByPlay:
    def __init__(self, gameid, startperiod=0, endperiod=0):
        self._url = "http://stats.nba.com/stats/playbyplay?"
        self._api_param = {'GameID':gameid,
                          'StartPeriod': startperiod,
                          'EndPeriod':endperiod,
                          }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def pbp(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']
