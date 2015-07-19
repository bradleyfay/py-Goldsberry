import requests as _requests
from goldsberry._apiFunc import *

class GameLog:
    def __init__(self, playerid, season='2014',seasontype=1, league='NBA'):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID':playerid,
                                            'SeasonType': _SeasonType(seasontype),
                                            'Season': _nbaSeason(season),
                                            'LeagueID': _nbaLeague(league)
                                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def Log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class Splits:
    def __init__(self, playerid, season='2014',seasontype=1, league='NBA',
        dateto='', datefrom='', gamesegment=1, lastngames=0, location=1, measuretype=1,
        month=0, opponentteamid=0, outcome=1, paceadjust=1, permode=1, period=0,
        plusminus=1, rank=1, seasonsegment=1, vsconf=1, vsdiv=1):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashboardbygeneralsplits?"
        self._api_param = {'PlayerID':playerid,
                           'SeasonType': _SeasonType(seasontype),
                           'Season': _nbaSeason(season),
                           'LeagueID': _nbaLeague(league),
                           'DateTo':dateto,
                           'DateFrom':datefrom,
                           'GameSegment':_GameSegment(gamesegment),
                           'LastNGames':lastngames,
                           'Location':_Location(location),
                           'MeasureType':_measureType(measuretype),
                           'Month':month,
                           'OpponentTeamID':opponentteamid,
                           'Outcome':_Outcome(outcome),
                           'PaceAdjust':_PaceAdjust(paceadjust),
                           'PerMode':_PerMode(permode),
                           'Period':period,
                           'PlusMinus':_PlusMinus(plusminus),
                           'Rank':_Rank(rank),
                           'SeasonSegment':_SeasonSegment(seasonsegment),
                           'VsConference':_VsConference(vsconf),
                           'VsDivision':_VsDivision(vsdiv)}
        self._pull = _requests.get(self._url, params = self._api_param)
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
    def __init__(self, playerid, league='NBA',permode=1):
        self._url = "http://stats.nba.com/stats/playercareerstats?"
        self._api_param = {'PlayerID':playerid,
                                                'LeagueID':_nbaLeague(league),
                                                'PerMode':_PerMode(permode)}
        self._pull = _requests.get(self._url, params = self._api_param)
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
        self._pull = _requests.get(self._url, params = self._api_param)
    def CommonPlayerInfo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class ShotChart:
    def __init__(self,playerid,leagueid='',season='2014', seasontype=1,teamid=0,
                             gameid='',outcome=1,location=1,month=0,seasonsegment=1,
                             datefrom='',dateto='',opponentteamid=0,vsconf=1,vsdiv=1,
                             position=1,period=0,lastngames=0,aheadbehind=1,
                             contextmeasure=1,clutchtime=7,rookieyear='', 
                             contextfilter='',startperiod='1',endperiod='10',startrange='0', 
                             endrange='28800', gamesegment=1, rangetype='2'):
        if not rookieyear == '':
            rookieyear = _nbaSeason(rookieyear)
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/shotchartdetail?"
        self._api_param = {'LeagueID': leagueid,
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'PlayerID' : playerid,
                           'GameID' : gameid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'Position' : _Position(position),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'AheadBehind' : _AheadBehind(aheadbehind),
                           'ContextMeasure' : _ContextMeasure(contextmeasure),
                           'ClutchTime' : _ClutchTime(clutchtime),
                           'RookieYear' : rookieyear,
                           'ContextFilter':contextfilter,
                           'StartPeriod':startperiod,
                           'EndPeriod':endperiod,
                           'StartRange':startrange,
                           'EndRange':endrange,
                           'RangeType':rangetype,
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def shotchart(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def leagueaverage(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class PlayerReboundLogSV:
    def __init__(self,playerid,league='NBA',season='2014',seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashptshotlog?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def PtRebLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class PlayerShotLogSV:
    def __init__(self,playerid,league='NBA',season='2014',seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashptshotlog?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def PtShotLog(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerShotDefSV:
    def __init__(self,playerid,league='NBA',season='2014', seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0,permode=1):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerMode(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def DefendingShot(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerPassingSV:
    def __init__(self,playerid,league='NBA',season='2014', seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0,permode=1):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerMode(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def PassesMade(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def PassesReceived(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayerReboundSV:
    def __init__(self,playerid,league='NBA',season='2014', seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0,permode=1):
        if not dateto == '':
            _valiDate(dateto)
        if not datefrom == '':
            _valiDate(datefrom)
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerMode(permode)
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

class PlayerShotSV:
    def __init__(self,playerid,league='NBA',season='2014', seasontype=1,teamid=0,
                             outcome=1,location=1,month=0,seasonsegment=1,datefrom='',
                             dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                             period=0,lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptshots?"
        self._api_param = {'PlayerID' : playerid,
                           'LeagueID': _nbaLeague(league),
                           'Season' :  _nbaSeason(season),
                           'SeasonType' : _SeasonType(seasontype),
                           'TeamID' : teamid,
                           'Outcome' : _Outcome(outcome),
                           'Location' : _Location(location),
                           'Month' : month,
                           'SeasonSegment' : _SeasonSegment(seasonsegment),
                           'DateFrom' :  datefrom,
                           'DateTo' : dateto,
                           'OpponentTeamID' : opponentteamid,
                           'VsConference' : _VsConference(vsconf),
                           'VsDivision' : _VsDivision(vsdiv),
                           'GameSegment' : _GameSegment(gamesegment),
                           'Period' :  period,
                           'LastNGames' : lastngames,
                           'PerMode' : _PerMode(permode)
                           }
            self._pull = _requests.get(self._url, params=self._api_param)
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

def PlayerList(season='2014', AllTime=False, league='NBA'):
    if AllTime:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"0",
                      'LeagueID':_nbaLeague(league),
                      'Season': "2014-15"}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    else:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason':"1",
                      'LeagueID': _nbaLeague(league),
                      'Season': _nbaSeason(season)}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ["PlayerShotSV", "PlayerReboundSV", "PlayerPassingSV", 
           "PlayerShotDefSV", "PlayerShotLogSV", "ShotChart",
           "Demo", "Career", "Splits", "GameLog", "PlayerReboundLogSV"]