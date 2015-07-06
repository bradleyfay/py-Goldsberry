import requests

class Roster:
    def __init__(self, teamid, season='2014-15',leagueid='00'):
        self._url = "http://stats.nba.com/stats/commonteamroster?"
        self._api_param = {'TeamID':teamid,
                          'Season': season,
                          'LeagueID': leagueid
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def Players(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Coaches(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class History:
    def __init__(self, teamid):
        self._url = "".join(["http://stats.nba.com/feeds/teams/profile/",str(teamid),"_TeamProfile.js"])
        self._pull = requests.get(self._url)
    def Details(self):
        return self._pull.json()['TeamDetails'][0]['Details']
    def History(self):
        return self._pull.json()['TeamDetails'][1]['History']
    def SocialSites(self):
        return self._pull.json()['TeamDetails'][2]['SocialSites']
    def Championships(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships']
    def ConferenceTitles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles']
    def DivisionalTitles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles'] == []:
            return ['None']
        else: return self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles']
    def HallOfFameInductees(self):
        return self._pull.json()['TeamDetails'][4]['HallOfFameInductees']
    def RetiredMembers(self):
        return self._pull.json()['TeamDetails'][5]['RetiredMembers']

class Splits:
    def __init__(self, teamid, season='2014-15',leagueid='00', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype='Base',
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?"
        self._api_param = {'TeamID':teamid,
                          'Season': season,
                          'LeagueID': leagueid,
                          'DateFrom':datefrom,
                          'DateTo':dateto,
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
                          'SeasonType':seasontype,
                          'VsConference':vsconference,
                          'VsDivision':vsdivision
                          }
        self._pull = requests.get(self._url, params=self._api_param)
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
    def DaysRest(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class SeasonStats:
    def __init__(self, teamid, season='2014-15',leagueid='00', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype='Base',
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamplayerdashboard?"
        self._api_param = {'TeamID':teamid,
                          'Season': season,
                          'LeagueID': leagueid,
                          'DateFrom':datefrom,
                          'DateTo':dateto,
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
                          'SeasonType':seasontype,
                          'VsConference':vsconference,
                          'VsDivision':vsdivision
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def TeamOverall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PlayersSeasonTotals(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class OnOff:
    def __init__(self, teamid, season='2014-15',leagueid='00', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype='Base',
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamplayeronoffdetails?"
        self._api_param = {'TeamID':teamid,
                          'Season': season,
                          'LeagueID': leagueid,
                          'DateFrom':datefrom,
                          'DateTo':dateto,
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
                          'SeasonType':seasontype,
                          'VsConference':vsconference,
                          'VsDivision':vsdivision
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def Overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PlayersOnCourt(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PlayersOffCourt(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class YearlyStats:
    def __init__(self, teamid, permode='Totals',leagueid='00', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teamyearbyyearstats?"
        self._api_param = {'TeamID':teamid,
                          'PerMode': permode,
                          'LeagueID': leagueid,
                          'SeasonType':seasontype
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def TeamStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class GameLogs:
    def __init__(self, teamid, season='2014-15',leagueid='00', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teamgamelog?"
        self._api_param = {'TeamID':teamid,
                          'LeagueID': leagueid,
                          'SeasonType':seasontype,
                          'Season':season
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def TeamGameLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Info:
    def __init__(self, teamid, season='2014-15',leagueid='00', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teaminfocommon?"
        self._api_param = {'TeamID':teamid,
                          'LeagueID': leagueid,
                          'SeasonType':seasontype,
                          'Season':season
                          }
        self._pull = requests.get(self._url, params=self._api_param)
    def TeamInfo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonRanks(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class TeamPassingSV:
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

class TeamReboundSV:
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

class TeamShotSV:
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
