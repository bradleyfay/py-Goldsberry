import requests as _requests
from goldsberry._apiFunc import _nbaSeason, _nbaLeague, _measureType

class Roster:
    def __init__(self, teamid, season='2014',league='NBA'):
        self._url = "http://stats.nba.com/stats/commonteamroster?"
        self._api_param = {'TeamID':teamid,
                          'Season': _nbaSeason(season),
                          'LeagueID': _nbaLeague(league)
                          }
        self._pull = _requests.get(self._url, params=self._api_param)
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
        self._pull = _requests.get(self._url)
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
    def __init__(self, teamid, season='2014',league='NBA', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype=1,
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?"
        self._api_param = {'TeamID':teamid,
                          'Season': _nbaSeason(season),
                          'LeagueID': _nbaLeague(league),
                          'DateFrom':datefrom,
                          'DateTo':dateto,
                          'GameSegment':gamesegment,
                          'LastNGames':lastngames,
                          'Location':location,
                          'MeasureType': _measureType(measuretype),
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
        self._pull = _requests.get(self._url, params=self._api_param)
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
    def __init__(self, teamid, season='2014',league='NBA', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype=1,
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamplayerdashboard?"
        self._api_param = {'TeamID':teamid,
                          'Season': _nbaSeason(season),
                          'LeagueID': _nbaLeague(league),
                          'DateFrom':datefrom,
                          'DateTo':dateto,
                          'GameSegment':gamesegment,
                          'LastNGames':lastngames,
                          'Location':location,
                          'MeasureType': _measureType(measuretype),
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
        self._pull = _requests.get(self._url, params=self._api_param)
    def TeamOverall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PlayersSeasonTotals(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class OnOff:
    def __init__(self, teamid, season='2014',league='NBA', datefrom='',
      dateto='', gamesegment='', lastngames='0', location='', measuretype=1,
      month='0', opponentteamid='0', outcome='', paceadjust='N', permode='PerGame',
      period='0', plusminus='N', seasonsegment='', seasontype='Regular Season',
      vsconference='', vsdivision='', rank='N'):
        self._url = "http://stats.nba.com/stats/teamplayeronoffdetails?"
        self._api_param = {'TeamID':teamid,
                          'Season': _nbaSeason(season),
                          'LeagueID': _nbaLeague(league),
                          'DateFrom':datefrom,
                          'DateTo':dateto,
                          'GameSegment':gamesegment,
                          'LastNGames':lastngames,
                          'Location':location,
                          'MeasureType': _measureType(measuretype),
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
        self._pull = _requests.get(self._url, params=self._api_param)
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
    def __init__(self, teamid, permode='Totals',league='NBA', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teamyearbyyearstats?"
        self._api_param = {'TeamID':teamid,
                          'PerMode': permode,
                          'LeagueID': _nbaLeague(league),
                          'SeasonType':seasontype
                          }
        self._pull = _requests.get(self._url, params=self._api_param)
    def TeamStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class GameLogs:
    def __init__(self, teamid, season='2014',league='NBA', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teamgamelog?"
        self._api_param = {'TeamID':teamid,
                          'LeagueID': _nbaLeague(league),
                          'SeasonType':seasontype,
                          'Season': _nbaSeason(season)
                          }
        self._pull = _requests.get(self._url, params=self._api_param)
    def TeamGameLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class Info:
    def __init__(self, teamid, season='2014',league='NBA', seasontype='Regular Season'):
        self._url = "http://stats.nba.com/stats/teaminfocommon?"
        self._api_param = {'TeamID':teamid,
                          'LeagueID': _nbaLeague(league),
                          'SeasonType':seasontype,
                          'Season': _nbaSeason(season)
                          }
        self._pull = _requests.get(self._url, params=self._api_param)
    def TeamInfo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonRanks(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class TeamPassingSV:
    def __init__(self,teamid,league='NBA',season='2014', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptpass?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': _nbaLeague(league),
            'Season' :  _nbaSeason(season),
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
        self._pull = _requests.get(self._url, params=self._api_param)
    def PassesMade(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PassesReceived(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class TeamReboundSV:
    def __init__(self,teamid,league='NBA',season='2014', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptreb?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': _nbaLeague(league),
            'Season' :  _nbaSeason(season),
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
        self._pull = _requests.get(self._url, params=self._api_param)
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
    def __init__(self,teamid,league='NBA',season='2014', seasontype='Regular Season',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',gamesegment='',period=0, 
              lastngames=0, permode="PerGame"):
        self._url = "http://stats.nba.com/stats/teamdashptshots?"
        self._api_param = {
            'TeamID' : teamid,
            'LeagueID': _nbaLeague(league),
            'Season' :  _nbaSeason(season),
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
        self._pull = _requests.get(self._url, params=self._api_param)
    def General(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ShotClock(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Dribble(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ClosestDefender(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def ClosestDefender10ftPlus(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TouchTime(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class Lineups:
  def __init__(self, teamid, groupsize=5, gameid='',season=2014, league="NBA", datefrom='', dateto='',  
    measure=1, month=0, opponentteamid=0, paceadjust=1, permode=1, period=0, plusminus=1, rank=1,
    seasonsegment=1, seasontype=1, vsconf=1, vsdiv=1, lastngames=0, location=1, outcome=1):
    self._url = "http://stats.nba.com/stats/teamdashlineups?"
    self._api_param = {
        'DateFrom':datefrom,
        'DateTo':dateto,
        'GameID':gameid,
        'GameSegment':_GameSegment(gamesegment),
        'GroupQuantity':groupsize,
        'LastNGames':lastngames,
        'LeagueID':_nbaLeague(league),
        'Location':_Location(location),
        'MeasureType':_measureType(measure),
        'Month':month,
        'OpponentTeamID':opponentteamid,
        'Outcome':_Outcome(outcome),
        'PaceAdjust':_PaceAdjust(paceadjust),
        'PerMode':_PerMode(permode),
        'Period':period,
        'PlusMinus':_PlusMinus(plusminus),
        'Rank':_Rank(rank),
        'Season':_nbaSeason(season),
        'SeasonSegment':_SeasonSegment(seasonsegment),
        'SeasonType':_SeasonType(seasontype),
        'TeamID':teamid,
        'VsConference':_VsConference(vsconf),
        'VsDivision':_VsDivision(vsdiv)
    }
    self._pull = _requests.get(self._url, params=self._api_param)
    def Overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Lineups(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]



__all__ = ['Roster', 'History', 'Splits', 'SeasonStats', 'OnOff', 'YearlyStats', 'Gamelogs',
          'Info', 'TeamPassingSV', 'TeamReboundsSV', 'TeamShotSV']