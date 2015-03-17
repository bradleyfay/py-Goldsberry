class BoxScore:
    def __init__(self, gameid, rangetype=0, startperiod=0, endperiod=0, startrange=0, endrange=0):
        self._url = "http://stats.nba.com/stats/boxscore?"
        self._api_param = {'GameID':gameid,
                     'RangeType':rangetype,
                     'StartPeriod':startperiod,
                     'EndPeriod':endperiod,
                     'StartRange':startrange,
                     'EndRange':endrange}
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def gamesummary(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']
    def linescore(self):
        return self._x['resultSets'][1]['rowSet'],columns=self._x['resultSets'][1]['headers']
    def seasonseries(self):
        return self._x['resultSets'][2]['rowSet'],columns=self._x['resultSets'][2]['headers']
    def lastmeeting(self):
        return self._x['resultSets'][3]['rowSet'],columns=self._x['resultSets'][3]['headers']
    def playerstats(self):
        return self._x['resultSets'][4]['rowSet'],columns=self._x['resultSets'][4]['headers']
    def teamstats(self):
        return self._x['resultSets'][5]['rowSet'],columns=self._x['resultSets'][5]['headers']
    def otherstats(self):
        return self._x['resultSets'][6]['rowSet'],columns=self._x['resultSets'][6]['headers']
    def officials(self):
        return self._x['resultSets'][7]['rowSet'],columns=self._x['resultSets'][7]['headers']
    def gameinfo(self):
        return self._x['resultSets'][8]['rowSet'],columns=self._x['resultSets'][8]['headers']
    def inactives(self):
        return self._x['resultSets'][9]['rowSet'],columns=self._x['resultSets'][9]['headers']
    def playertrack(self):
        return self._x['resultSets'][11]['rowSet'],columns=self._x['resultSets'][11]['headers']
    def teamtrack(self):
        return self._x['resultSets'][12]['rowSet'],columns=self._x['resultSets'][12]['headers']
