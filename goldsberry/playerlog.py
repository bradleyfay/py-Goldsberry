class GameLog:
    def __init__(self, playerid, season='2014-15',seasontype='Regular Season', leagueid='00'):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID':playerid,
                          'SeasonType': seasontype,
                          'Season': season,
                          'LeagueID': leagueid
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def Log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Splits:
    def __init__(self, playerid, season='2014-15',seasontype='Regular Season', leagueid='00',
      dateto='', datefrom='', gamesegment='', lastngames=0, location='', measuretype="Base",
      month=0, opponentteamid=0, outcome='', paceadjust="N", permode="PerGame", period=0,
      plusminus="N", rank="N", seasonsegment='', vsconference="", vsdivision=""):
      self._url = "http://stats.nba.com/stats/playerdashboardbygeneralsplits?"
      self._api_param = {'PlayerID':playerid,
                         'SeasonType': seasontype,
                         'Season': season,
                         'LeagueID': leagueid
                         'DateTo':dateto,
                         'DateFrom':datefrom,
                         'GameSegment':gamesegment,
                         'LastNGames':lastngames,
                         'Location':location,
                         'MeasureType':measuretype,
                         'Month':month,
                         'OpponentTeamID':opponentteamid,
                         'Outcome':outcome,
                         'PaceAdjust':paceadjust,
                         'PerMode':permode,
                         'Period':period,
                         'PlusMinus':plusminus,
                         'Rank':rank,
                         'SeasonSegment':seasonsegment,
                         'VsConference':vsconference,
                         'VsDivision':vsdivision}
      self._pull = requests.get(self.url, params = self._api_param)
    def Overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Location(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WinsLosses(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Month(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PrePostAllStar(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def StartingPosition(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def DaysRest(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


measuretype = "(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)"


