class LeagueLeaders:
    def __init__(self, leagueid='00', permode='Per48',statcat='PTS',season='2013-14',seasontype='Regular Season',scope='S'):
        self._url = "http://stats.nba.com/stats/leagueleaders?"
        self._api_param = {'LeagueID':leagueid,
                          'PerMode':permode,
                          'StatCategory':statcat,
                          'Season':season,
                          'SeasonType':seasontype,
                          'Scope':scope,
             }
        self._season = season
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def line(self):
        return self._x['resultSet']['rowSet'],columns=self._x['resultSet']['headers']
    def players(self):
        if self._season == 'All Time':
            return self.line().PLAYER_NAME.values,index=self.line().PLAYER_ID
        else:
            return self.line().PLAYER.values,index=self.line().PLAYER_ID
