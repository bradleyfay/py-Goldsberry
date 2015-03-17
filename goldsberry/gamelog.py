class GameLog:
    def __init__(self, playerid, season='2013-14',seasontype='Regular Season', leagueid=''):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID':playerid,
                          'SeasonType': seasontype,
                          'Season': season,
                          'LeagueID': leagueid
                          }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def log(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']
