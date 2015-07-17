import requests as _requests
from goldsberry._apiFunc import _nbaSeason, _nbaLeague, _measureType, _seasonID, _DistanceRange, _GameScope, _GameSegment, _Location, _Outcome, _PaceAdjust, _PerMode
from goldsberry._apiFunc import _PlayerExperience, _PlayerPosition, _PlusMinus, _Rank, _SeasonSegment, _StarterBench, _VsConference, _VsDivision

class Transactions:
    """
    """
    def __init__(self):
        self._url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
        self._pull = _requests.get(self._url)
    def Transactions(self):
        return self._pull.json()['ListItems']

class DailyStandings:
    """
    """
    def __init__(self, date, league = "NBA", offset = 0):
        self.url = "http://stats.nba.com/stats/scoreboard?"
        # Add Logic to test if date matches patter mm-dd-yyyy
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'gameDate':date,
                           'DayOffset':offset
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def GameHeader(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LineScore(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeriesStandings(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LastMeeting(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfStandingsByDay(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfStandingsByDay(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Available(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class FranchiseHistory:
    """
    """
    def __init__(self, league="NBA"):
        self._url = "http://stats.nba.com/stats/franchisehistory?"
        self._api_param = {'LeagueID':_nbaLeague(league)}
        self._pull = _requests.get(self._url, params=self._api_param)
    def FranchiseHistory(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def DefunctTeams(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class PlayoffPicture:
    """
    """
    def __init__(self, league='NBA', season=2014):
        self._url = "http://stats.nba.com/stats/playoffpicture?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonID':_seasonID(season)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)
    def EastConfPlayoffPicture(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfPlayoffPicture(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfStandings(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfStandings(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def EastConfRemainingGames(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def WestConfRemainingGames(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class LeagueLeaders:
    def __init__(self, league='NBA', permode='PerGame', scope='S', season='2014',
        seasontype='Regular Season', statcategory='PTS', AllTime = False):
        self._url = "http://stats.nba.com/stats/leagueleaders?"
        if not AllTime:
            self._api_param = {'LeagueID':_nbaLeague(league), 
                                'Scope':scope,
                                'PerMode':permode,
                                'Season':_nbaSeason(season),
                                'SeasonType':seasontype,
                                'StatCategory':statcategory
                                }
        else: 
            self._api_param = {'LeagueID':_nbaLeague(league), 
                                'Scope':scope,
                                'PerMode':permode,
                                'Season':"All Time",
                                'SeasonType':seasontype,
                                'StatCategory':statcategory
                                }
        #Scope: (RS)|(S)|(Rookies) one of these options
        self._pull = _requests.get(self._url, params=self._api_param)
    def Leaders(self):
        _headers = self._pull.json()['resultSet']['headers']
        _values = self._pull.json()['resultSet']['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class ClassicStats:
    def __init__(self,stattype="Team",datefrom = '',dateto = '',gamescope = '',
        gamesegment = '',lastngames = '0',league = 'NBA',location = '',
        measuretype = 1,month = '0',opponentteamid = '0',
        outcome = '',paceadjust = 'N',permode = 'PerGame',period = '0',
        playerexperience = '',playerposition = '',plusminus = 'N',
        rank = 'N',season = '2014',seasonsegment = '',
        seasontype = 'Regular Season',starterbench = '',vsconference = '',
        vsdivision = ''):
        if stattype.lower() == "team":
            self._url = "http://stats.nba.com/stats/leaguedashteamstats?"
        else: self._url = "http://stats.nba.com/stats/leaguedashplayerstats?"
        self._api_param = {
            'DateFrom' : datefrom,
            'DateTo' : dateto,
            'GameScope' : gamescope,
            'GameSegment' : gamesegment,
            'LastNGames' : lastngames,
            'LeagueID' : _nbaLeague(league),
            'Location' : location,
            'MeasureType' : _measureType(measuretype),
            'Month' : month,
            'OpponentTeamID' : opponentteamid,
            'Outcome' : outcome,
            'PaceAdjust' : paceadjust,
            'PerMode' : permode,
            'Period' : period,
            'PlayerExperience' : playerexperience,
            'PlayerPosition' : playerposition,
            'PlusMinus' : plusminus,
            'Rank' : rank,
            'Season' : _nbaSeason(season),
            'SeasonSegment' : seasonsegment,
            'SeasonType' : seasontype,
            'StarterBench' : starterbench,
            'VsConference' : vsconference,
            'VsDivision' : vsdivision
            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def Stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
 
class ClutchStats:
    def __init__(self, stattype="Team", aheadbehind='Ahead or Behind', 
      clutchtime = 'Last 5 Minutes', datefrom='', dateto='', 
      gamescope='', gamesegment='', lastngames = '0', league = 'NBA', 
      location='', measuretype = 1, month = '0', 
      opponentteamid = '0', outcome='', paceadjust = 'N', 
      permode = 'PerGame', period = '0', playerexperience='', 
      playerposition='', plusminus = 'N', pointdiff = '5', rank = 'N', 
      season = '2014', seasonsegment='', seasontype = 'Regular Season', 
      starterbench='', vsconference='', vsdivision=''):
        if stattype.lower()=="team":
            self._url = "http://stats.nba.com/stats/leaguedashteamclutch?"
        else: self._url = "http://stats.nba.com/stats/leaguedashplayerclutch?"
        self._api_param = {
            'AheadBehind' : aheadbehind,
            'ClutchTime' : clutchtime,
            'DateFrom' : datefrom,
            'DateTo' : dateto,
            'GameScope' : gamescope,
            'GameSegment' : gamesegment,
            'LastNGames' : lastngames,
            'LeagueID' : _nbaLeague(league),
            'Location' : location,
            'MeasureType' : _measureType(measuretype),
            'Month' : month,
            'OpponentTeamID' : opponentteamid,
            'Outcome' : outcome,
            'PaceAdjust' : paceadjust,
            'PerMode' : permode,
            'Period' : period,
            'PlayerExperience' : playerexperience,
            'PlayerPosition' : playerposition,
            'PlusMinus' : plusminus,
            'PointDiff' : pointdiff,
            'Rank' : rank,
            'Season' : _nbaSeason(season),
            'SeasonSegment' : seasonsegment,
            'SeasonType' : seasontype,
            'StarterBench' : starterbench,
            'VsConference' : vsconference,
            'VsDivision' : vsdivision
            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def Clutch(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]            

## Shooting class needs some further study of the data because it classifies shots in two levels. This class will be used for Player & Team as well as Self & Opponent

## class Shooting:
##     def __init__(self,stattype="team", measure=["Base","Opponent"], season=2014, datefrom='', dateto='',distancerange=1,
##     gamescope=1, gamesegment=1, lastngames=0, league="NBA", location=1, month=0, opponentteamid=0,
##     outcome=1, paceadjust=1, permode=1, period=0, playerexperience=1, playerposition=1, plusminus=1,
##     rank=1, seasonsegment=1, seasontype=1, starterbench=1, vsconference=1, vsdivision=1):
##         if stattype.tolower() == "team":
##             self._url = "http://stats.nba.com/stats/leaguedashteamshotlocations?"
##         else: self._url = "http://stats.nba.com/stats/leaguedashplayershotlocations?"
##         self._api_param = {
##             'DateFrom':datefrom,
##             'DateTo':dateto,
##             'DistanceRange':_DistanceRange(distancerange),
##             'GameScope':_GameScope(gamescope),
##             'GameSegment':_GameSegment(gamesegment),
##             'LastNGames':lastngames,
##             'LeagueID':_nbaLeague(league),
##             'Location':_Location(location),
##             'MeasureType':measure,
##             'Month':month=0,
##             'OpponentTeamID':opponentteamid=0,
##             'Outcome':_Outcome(outcome),
##             'PaceAdjust':_PaceAdjust(paceadjust),
##             'PerMode':_PerMode(permode),
##             'Period':period=0,
##             'PlayerExperience':_PlayerExperience(playerexperience),
##             'PlayerPosition':_PlayerPosition(playerposition),
##             'PlusMinus':_PlusMinus(plusminus),
##             'Rank':_Rank(rank),
##             'Season':_nbaSeason(season),
##             'SeasonSegment':_SeasonSegment(seasonsegment),
##             'SeasonType':_SeasonType(seasontype),
##             'StarterBench':_StarterBench(starterbench),
##             'VsConference':_VsConference(vsconference),
##             'VsDivision':_VsDivision(vsdivision)
##         }
##         self._pull = _requests.get(self._url, params=self._api_param)
##     def Shooting(self):
##         _headers = self._pull.json()['resultSets'][0]['headers']
##         _values = self._pull.json()['resultSets'][0]['rowSet']
##         return [dict(zip(_headers, value)) for value in _values]

class Lineups:
  def __init__(self, groupsize=5, gameid='',season=2014, league="NBA", datefrom='', dateto='',  
    measure=1, month=0, opponentteamid=0, paceadjust=1, permode=1, period=0, plusminus=1, rank=1,
    seasonsegment=1, seasontype=1, vsconf=1, vsdiv=1, lastngames=0, location=1, outcome=1):
    self._url = "http://stats.nba.com/stats/leaguedashlineups?"
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
        'VsConference':_VsConference(vsconf),
        'VsDivision':_VsDivision(vsdiv)
    }
    self._pull = _requests.get(self._url, params=self._api_param)
    def Lineups(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    


__all__ = ['Transactions', 'DailyStandings', 'FranchiseHistory',
            'PlayoffPicture', 'LeagueLeaders', 'PlayerClutchStats',
            'PlayerStats']