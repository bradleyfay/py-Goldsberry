class PlayerReboundLog:
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

class PlayerShotLog:
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

class PlayerShotDef:
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

class PlayerPassing:
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

class PlayerRebound:
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

class PlayerShot:
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

### Team SportVU Pulls
class TeamPassing:
    def __init__(self,teamid,leagueid='00',season='2014-15', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptpass?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
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

class TeamRebound:
    def __init__(self,teamid,leagueid='00',season='2014-15', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptreb?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
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

class TeamShot:
    def __init__(self,teamid,leagueid='00',season='2014-15', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptshots?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': leagueid,
            'Season' :  season,
            'SeasonType' : seasontype,
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