import requests as _requests
from goldsberry.apiconvertor import *

class daily_scoreboard:
    def __init__(self, date, league="NBA", dayoffset=0):
        valid_date(date)
        self._url = "http://stats.nba.com/stats/scoreboardV2?"
        self._api_param = {
                "gameDate":valid_date(date),
                "LeagueID":nba_league(league),
                "DayOffset":dayoffset
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def game_header(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def linescore(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def series_standings(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def last_meeting(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def eastern_conference_standings(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def western_conference_standings(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def available(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def team_leaders(self):
        _headers = self._pull.json()['resultSets'][7]['headers']
        _values = self._pull.json()['resultSets'][7]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def _ticket_links(self):
        _headers = self._pull.json()['resultSets'][8]['headers']
        _values = self._pull.json()['resultSets'][8]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def win_probability(self):
        _headers = self._pull.json()['resultSets'][9]['headers']
        _values = self._pull.json()['resultSets'][9]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class transactions:
    """
    """
    def __init__(self):
        self._url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
        self._pull = _requests.get(self._url)
    def transactions(self):
        return self._pull.json()['ListItems']
class franchise_history:
    """
    """
    def __init__(self, league="NBA"):
        self._url = "http://stats.nba.com/stats/franchisehistory?"
        self._api_param = {'LeagueID':nba_league(league)}
        self._pull = _requests.get(self._url, params=self._api_param)
    def current_teams(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defunct_teams(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class playoff_picture:
    """
    """
    def __init__(self, league='NBA', season=2015):
        self._url = "http://stats.nba.com/stats/playoffpicture?"
        self._api_param = {'LeagueID':nba_league(league),
                             'SeasonID':season_id(season)
                             }
        self._pull = _requests.get(self._url, params=self._api_param)
    def eastern_conf_playoff_picture(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def western_confe_playoff_picture(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def eastern_conf_standing(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def western_conf_standing(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def eastern_conf_remaining_games(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def western_conf_remaining_games(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class league_leaders:
    def __init__(self, AllTime = False, league='NBA', permode=2, scope=1, season='2015',
        seasontype=1, statcategory=1):
        self._url = "http://stats.nba.com/stats/leagueleaders?"
        if not AllTime:
            self._api_param = {'LeagueID':nba_league(league),
                                'Scope':scope(scope),
                                'PerMode':per_mode_small_48(permode),
                                'Season':nba_season(season),
                                'SeasonType':season_type(seasontype),
                                'StatCategory':stat_category(statcategory)
                                }
        else:
            self._api_param = {'LeagueID':nba_league(league),
                                'Scope':scope(scope),
                                'PerMode':per_mode_small_48(permode),
                                'Season':"All Time",
                                'SeasonType':season_type(seasontype),
                                'StatCategory':stat_category(statcategory)
                                }
        #Scope: (RS)|(S)|(Rookies) one of these options
        self._pull = _requests.get(self._url, params=self._api_param)
    def leaders(self):
        _headers = self._pull.json()['resultSet']['headers']
        _values = self._pull.json()['resultSet']['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class classic_stats:
    def __init__(self,stattype="Team",datefrom='', dateto='', gamescope=1,
        gamesegment=1, lastngames='0', league='NBA', location=1,
        measuretype=1, month='0', opponentteamid='0', outcome=1, paceadjust=1,
        permode=1, period='0', playerexperience=1, playerposition=1, plusminus=1,
        rank=1,season='2015',seasonsegment=1, seasontype=1, starterbench=1,vsconf=1,
        vsdiv=1):
        if stattype.lower() == "team":
            self._url = "http://stats.nba.com/stats/leaguedashteamstats?"
        else: self._url = "http://stats.nba.com/stats/leaguedashplayerstats?"
        self._api_param = {
            'DateFrom' : valid_date(datefrom),
            'DateTo' : valid_date(dateto),
            'GameScope' : game_scope(gamescope),
            'GameSegment' : game_segment(gamesegment),
            'LastNGames' : lastngames,
            'LeagueID' : nba_league(league),
            'Location' : location(location),
            'MeasureType' : measure_type(measuretype),
            'Month' : month,
            'OpponentTeamID' : opponentteamid,
            'Outcome' : outcome(outcome),
            'PaceAdjust' : pace_adjust(paceadjust),
            'PerMode' : per_mode_large(permode),
            'Period' : period,
            'PlayerExperience' : player_experience(playerexperience),
            'PlayerPosition' : player_position(playerposition),
            'PlusMinus' : plus_minus(plusminus),
            'Rank' : rank(rank),
            'Season' : nba_season(season),
            'SeasonSegment' : season_segment(seasonsegment),
            'SeasonType' : season_type(seasontype),
            'StarterBench' : starter_bench(starterbench),
            'VsConference' : vs_conference(vsconf),
            'VsDivision' : vs_division(vsdiv)
            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class clutch_stats:
    def __init__(self, Team=True, aheadbehind=1, clutchtime=1, datefrom='',
        dateto='', gamescope=1, gamesegment=1, lastngames='0', league='NBA', location=1,
        measuretype=1, month='0', opponentteamid='0', outcome=1, paceadjust=1,
        permode=1, period='0', playerexperience=1, playerposition=1, plusminus=1,
        rank=1,season='2015',seasonsegment=1, seasontype=1, starterbench=1,vsconf=1,
        vsdiv=1):
        if Team:
            self._url = "http://stats.nba.com/stats/leaguedashteamclutch?"
        else: self._url = "http://stats.nba.com/stats/leaguedashplayerclutch?"
        self._api_param = {
            'AheadBehind' : ahead_behind(aheadbehind),
            'ClutchTime' : clutch_time(clutchtime),
            'DateFrom' : valid_date(datefrom),
            'DateTo' : valid_date(dateto),
            'GameScope' : game_scope(gamescope),
            'GameSegment' : game_segment(gamesegment),
            'LastNGames' : lastngames,
            'LeagueID' : nba_league(league),
            'Location' : location(location),
            'MeasureType' : measure_type(measuretype),
            'Month' : month,
            'OpponentTeamID' : opponentteamid,
            'Outcome' : outcome(outcome),
            'PaceAdjust' : pace_adjust(paceadjust),
            'PerMode' : per_mode_large(permode),
            'Period' : period,
            'PlayerExperience' : player_experience(playerexperience),
            'PlayerPosition' : player_position(playerposition),
            'PlusMinus' : plus_minus(plusminus),
            'PointDiff' : pointdiff,
            'Rank' : rank(rank),
            'Season' : nba_season(season),
            'SeasonSegment' : season_segment(seasonsegment),
            'SeasonType' : season_type(seasontype),
            'StarterBench' : starter_bench(starterbench),
            'VsConference' : vs_conference(vsconf),
            'VsDivision' : vs_division(vsdiv)
            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def clutch(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class lineups:
    def __init__(self, groupsize=5, gameid='',season=2015, league="NBA", datefrom='', dateto='',
    measure=1, month=0, opponentteamid=0, paceadjust=1, permode=1, period=0, plusminus=1, rank=1,
    seasonsegment=1, seasontype=1, vsconf=1, vsdiv=1, lastngames=0, location=1, outcome=1):
        self._url = "http://stats.nba.com/stats/leaguedashlineups?"
        self._api_param = {
            'DateFrom':valid_date(datefrom),
            'DateTo':valid_date(dateto),
            'GameID':gameid,
            'GameSegment':game_segment(gamesegment),
            'GroupQuantity':groupsize,
            'LastNGames':lastngames,
            'LeagueID':nba_league(league),
            'Location':location(location),
            'MeasureType':measure_type(measure),
            'Month':month,
            'OpponentTeamID':opponentteamid,
            'Outcome':outcome(outcome),
            'PaceAdjust':pace_adjust(paceadjust),
            'PerMode':per_mode_large(permode),
            'Period':period,
            'PlusMinus':plus_minus(plusminus),
            'Rank':rank(rank),
            'Season':nba_season(season),
            'SeasonSegment':season_segment(seasonsegment),
            'SeasonType':season_type(seasontype),
            'VsConference':vs_conference(vsconf),
            'VsDivision':vs_division(vsdiv)
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def lineups(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ['daily_scoreboard', 'transactions', 'franchise_history',
            'playoff_picture', 'league_leaders', 'classic_stats',
            'clutch_stats', 'lineups', 'shooting']

## Shooting class needs some further study of the data because it classifies shots in two levels. This class will be used for Player & Team as well as Self & Opponent

class shooting:
    def __init__(self,team=False, measure=1, season=2015, datefrom='', dateto='',distancerange=1,
    gamescope=1, gamesegment=1, lastngames=0, league="NBA", location=1, month=0, opponentteamid=0,
    outcome=1, paceadjust=1, permode=1, period=0, playerexperience=1, playerposition=1, plusminus=1,
    rank=1, seasonsegment=1, seasontype=1, starterbench=1, vsconference=1, vsdivision=1):
        if team:
            self._url = "http://stats.nba.com/stats/leaguedashteamshotlocations?"
        else: self._url = "http://stats.nba.com/stats/leaguedashplayershotlocations?"
        if measure == 2:
            measure="Opponent"
        else: measure='Base'
        self._api_param = {
            'DateFrom':datefrom,
            'DateTo':dateto,
            'DistanceRange':distance_range(distancerange),
            'GameScope':game_scope(gamescope),
            'GameSegment':game_segment(gamesegment),
            'LastNGames':lastngames,
            'LeagueID':nba_league(league),
            'Location':location(location),
            'MeasureType':measure,
            'Month':month,
            'OpponentTeamID':opponentteamid,
            'Outcome':outcome(outcome),
            'PaceAdjust':pace_adjust(paceadjust),
            'PerMode':per_mode_large(permode),
            'Period':period,
            'PlayerExperience':player_experience(playerexperience),
            'PlayerPosition':player_position(playerposition),
            'PlusMinus':plus_minus(plusminus),
            'Rank':rank(rank),
            'Season':nba_season(season),
            'SeasonSegment':season_segment(seasonsegment),
            'SeasonType':season_type(seasontype),
            'StarterBench':starter_bench(starterbench),
            'VsConference':vs_conference(vsconference),
            'VsDivision':vs_division(vsdivision)
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def headers(self):
        _skip = self._pull.json()['resultSets']['headers'][0]['columnsToSkip']
        _span = self._pull.json()['resultSets']['headers'][0]['columnSpan']
        _headers = []
        for i in self._pull.json()['resultSets']['headers'][0]['columnNames']:
            for j in self._pull.json()['resultSets']['headers'][1]['columnNames'][_skip:_skip+_span]:
                _headers.append(j + " " + i)
        _headers = self._pull.json()['resultSets']['headers'][1]['columnNames'][:_skip] + _headers
        return _headers
    def shooting(self):
        _headers = self.headers()
        _values = self._pull.json()['resultSets']['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
