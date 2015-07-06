# measuretype = "(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)"
import requests

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
                         'LeagueID': leagueid,
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

class Career:
    def __init__(self, playerid, leagueid='00',permode="PerGame"):
      self._url = "http://stats.nba.com/stats/playercareerstats?"
      self._api_param = {'PlayerID':playerid,
                         'LeagueID':leagueid,
                         'PerMode':permode}
      self._pull = requests.get(self.url, params = self._api_param)
    def SeasonTotalsRegularSeason(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def CareerTotalsRegularSeason(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonTotalsPostSeason(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def CareerTotalsPostSeason(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonTotalsAllStarSeason(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def CareerTotalsAllStarSeason(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonTotalsCollegeSeason(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def CareerTotalsCollegeSeason(self):
        _headers = self._pull.json()['resultSets'][7]['headers']
        _values = self._pull.json()['resultSets'][7]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonRankingsRegularSeason(self):
        _headers = self._pull.json()['resultSets'][8]['headers']
        _values = self._pull.json()['resultSets'][8]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonRankingsPostSeason(self):
        _headers = self._pull.json()['resultSets'][9]['headers']
        _values = self._pull.json()['resultSets'][9]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Demo:
    def __init__(self, playerid):
      self._url = "http://stats.nba.com/stats/commonplayerinfo?"
      self._api_param = {'PlayerID':playerid}
      self._pull = requests.get(self.url, params = self._api_param)
    def CommonPlayerInfo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class ShotChart:
    def __init__(self,playerid,leagueid='',season='2013-14', seasontype='Regular Season',teamid=0,gameid='',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',position='',
              period=0,lastngames=0,aheadbehind='',contextmeasure='FGM',clutchtime='',rookieyear='', contextfilter='',
              startperiod='1',endperiod='10',startrange='0', endrange='28800', gamesegment='', rangetype='2'):
        self._url = "http://stats.nba.com/stats/shotchartdetail?"
        self._api_param = {
             'LeagueID': leagueid,
             'Season' :  season,
             'SeasonType' : seasontype,
             'TeamID' : teamid,
             'PlayerID' : playerid,
             'GameID' : gameid,
             'Outcome' : outcome,
             'Location' : location,
             'Month' : month,
             'SeasonSegment' : seasonsegment,
             'DateFrom' :  datefrom,
             'DateTo' : dateto,
             'OpponentTeamID' : opponentteamid,
             'VsConference' : vsconf,
             'VsDivision' : vsdiv,
             'Position' : position,
             'GameSegment' : gamesegment,
             'Period' :  period,
             'LastNGames' : lastngames,
             'AheadBehind' : aheadbehind,
             'ContextMeasure' : contextmeasure,
             'ClutchTime' : clutchtime,
             'RookieYear' : rookieyear,
             'ContextFilter':contextfilter,
             'StartPeriod':startperiod,
             'EndPeriod':endperiod,
             'StartRange':startrange,
             'EndRange':endrange,
             'RangeType':rangetype,
             }
        self._pull = requests.get(self._url, params=self._api_param)
    def shotchart(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def leagueaverage(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerReboundLogSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptreboundlogs?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def PtRebLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerShotLogSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptshotlog?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def PtShotLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerShotDefSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/playerdashptshotdefend?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames,
            'PerMode' : permode
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def DefendingShot(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerPassingSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/playerdashptpass?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames,
            'PerMode' : permode
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def PassesMade(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PassesReceived(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerReboundSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames,
            'PerMode' : permode
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def Overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ShotType(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def NumContested(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ShotDistance(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def RebDistance(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerShotSV:
    def __init__(self,playerid,leagueid='00',season='2014-15', seasontype='Regular Season',teamid=0,outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/playerdashptshots?"
        self._api_param = {
            'PlayerID' : playerid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
            'TeamID' : teamid,
            'Outcome' : outcome,
            'Location' : location,
            'Month' : month,
            'SeasonSegment' : seasonsegment,
            'DateFrom' :  datefrom,
            'DateTo' : dateto,
            'OpponentTeamID' : opponentteamid,
            'VsConference' : vsconf,
            'VsDivision' : vsdiv,
            'GameSegment' : gamesegment,
            'Period' :  period,
            'LastNGames' : lastngames,
            'PerMode' : permode
            }
        self._pull = requests.get(self._url, params=self._api_param)
    def Overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def General(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ShotClock(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Dribble(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ClosestDefender(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ClosestDefender10ftPlus(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TouchTime(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]