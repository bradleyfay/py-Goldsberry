import requests as _requests
from goldsberry.apiconvertor import *

class team_info:
    def __init__(self, teamid, season='2015',league='NBA', seasontype=1):
        self._url = "http://stats.nba.com/stats/teaminfocommon?"
        self._api_param = {'TeamID':teamid,
                            'LeagueID': nba_league(league),
                            'SeasonType':season_type(seasontype),
                            'Season': nba_season(season)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def info(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season_ranks(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class roster:
    def __init__(self, teamid, season='2015',league='NBA'):
        self._url = "http://stats.nba.com/stats/commonteamroster?"
        self._api_param = {'TeamID':teamid,
                            'Season': nba_season(season),
                            'LeagueID': nba_league(league)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def players(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def coaches(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class history:
    def __init__(self, teamid):
        self._url = "".join(["http://stats.nba.com/feeds/teams/profile/",str(teamid),"_TeamProfile.js"])
        self._pull = _requests.get(self._url)
    def details(self):
        return self._pull.json()['TeamDetails'][0]['Details']
    def history(self):
        return self._pull.json()['TeamDetails'][1]['History']
    def social_sites(self):
        return self._pull.json()['TeamDetails'][2]['SocialSites']
    def championships(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][0]['Championships']
    def conference_titles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles'] == []:
            return ["None"]
        else: return self._pull.json()['TeamDetails'][3]['Awards'][1]['ConferenceTitles']
    def divisional_titles(self):
        if self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles'] == []:
            return ['None']
        else: return self._pull.json()['TeamDetails'][3]['Awards'][2]['DivitionalTitles']
    def hof_inductees(self):
        return self._pull.json()['TeamDetails'][4]['HallOfFameInductees']
    def retired_members(self):
        return self._pull.json()['TeamDetails'][5]['RetiredMembers']
class splits:
    def __init__(self, teamid, season='2015',league='NBA', datefrom='',
        dateto='', gamesegment=1, lastngames='0', location=1, measuretype=1,
        month='0', opponentteamid='0', outcome=1, paceadjust=1, permode=1,
        period='0', plusminus=1, seasonsegment=1, seasontype=1,
        vsconf=1, vsdiv=1, rank=1):
        self._url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?"
        self._api_param = {'TeamID':teamid,
                            'Season': nba_season(season),
                            'LeagueID': nba_league(league),
                            'DateFrom':valid_date(datefrom),
                            'DateTo':valid_date(dateto),
                            'GameSegment':game_segment(gamesegment),
                            'LastNGames':lastngames,
                            'Location':location(location),
                            'MeasureType': measure_type(measuretype),
                            'Month':month,
                            'OpponentTeamID':opponentteamid,
                            'Outcome':outcome(outcome),
                            'PaceAdjust':pace_adjust(paceadjust),
                            'PerMode':per_mode_large(permode),
                            'Period':period,
                            'PlusMinus':plus_minus(plusminus),
                            'Rank':rank(rank),
                            'SeasonSegment':season_segment(seasonsegment),
                            'SeasonType':season_type(seasontype),
                            'VsConference':vs_conference(vsconf),
                            'VsDivision':vs_division(vsdiv)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def location(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def wins_losses(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def month(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def pre_post_allstar(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def days_rest(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class season_stats:
    def __init__(self, teamid, season='2015',league='NBA', datefrom='',
        dateto='', gamesegment=1, lastngames='0', location=1, measuretype=1,
        month='0', opponentteamid='0', outcome=1, paceadjust=1, permode=1,
        period='0', plusminus=1, seasonsegment=1, seasontype=1,
        vsconf=1, vsdiv=1, rank=1):
        self._url = "http://stats.nba.com/stats/teamplayerdashboard?"
        self._api_param = {'TeamID':teamid,
                            'Season': nba_season(season),
                            'LeagueID': nba_league(league),
                            'DateFrom': valid_date(datefrom),
                            'DateTo': valid_date(dateto),
                            'GameSegment': game_segment(gamesegment),
                            'LastNGames': lastngames,
                            'Location': location(location),
                            'MeasureType': measure_type(measuretype),
                            'Month': month,
                            'OpponentTeamID': opponentteamid,
                            'Outcome': outcome(outcome),
                            'PaceAdjust': pace_adjust(paceadjust),
                            'PerMode': per_mode_large(permode),
                            'Period': period,
                            'PlusMinus': plus_minus(plusminus),
                            'Rank': rank(rank),
                            'SeasonSegment': season_segment(seasonsegment),
                            'SeasonType': season_type(seasontype),
                            'VsConference': vs_conference(vsconf),
                            'VsDivision': vs_division(vsdiv)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def player_totals(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class on_off_court:
    def __init__(self, teamid, season='2015',league='NBA', datefrom='',
        dateto='', gamesegment=1, lastngames='0', location=1, measuretype=1,
        month='0', opponentteamid='0', outcome=1, paceadjust=1, permode=1,
        period='0', plusminus=1, seasonsegment=1, seasontype=1,
        vsconf=1, vsdiv=1, rank='N'):
        self._url = "http://stats.nba.com/stats/teamplayeronoffdetails?"
        self._api_param = {'TeamID':teamid,
                            'Season': nba_season(season),
                            'LeagueID': nba_league(league),
                            'DateFrom': valid_date(datefrom),
                            'DateTo': valid_date(dateto),
                            'GameSegment':game_segment(gamesegment),
                            'LastNGames':lastngames,
                            'Location':location(location),
                            'MeasureType': measure_type(measuretype),
                            'Month':month,
                            'OpponentTeamID':opponentteamid,
                            'Outcome':outcome(outcome),
                            'PaceAdjust':pace_adjust(paceadjust),
                            'PerMode':per_mode_large(permode),
                            'Period':period,
                            'PlusMinus':plus_minus(plusminus),
                            'Rank':rank(rank),
                            'SeasonSegment':season_segment(seasonsegment),
                            'SeasonType':season_type(seasontype),
                            'VsConference':vs_conference(vsconf),
                            'VsDivision':vs_division(vsdiv)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
        self._url2 = "http://stats.nba.com/stats/teamdashboardbyshootingsplits?"
        self._pull2 = _requests.get(self._url2, params=self._api_param)

    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def on_court(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def off_court(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def overall_summary(self):
        _headers = self._pull2.json()['resultSets'][0]['headers']
        _values = self._pull2.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def on_court_summary(self):
        _headers = self._pull2.json()['resultSets'][1]['headers']
        _values = self._pull2.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def off_court_summary(self):
        _headers = self._pull2.json()['resultSets'][2]['headers']
        _values = self._pull2.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class on_off_court:
    def __init__(self, teamid, permode=1,league='NBA', seasontype=1):
        self._url = "http://stats.nba.com/stats/teamyearbyyearstats?"
        self._api_param = {'TeamID':teamid,
                            'PerMode': per_mode_mini(permode),
                            'LeagueID': nba_league(league),
                            'SeasonType':season_type(seasontype)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def team_stats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class game_logs:
    def __init__(self, teamid, season='2015',seasontype=1):
        self._url = "http://stats.nba.com/stats/teamgamelog?"
        self._api_param = {'TeamID':teamid,
                            'SeasonType':season_type(seasontype),
                            'Season': nba_season(season)
                            }
        self._pull = _requests.get(self._url, params=self._api_param)
    def logs(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class lineups:
    def __init__(self, teamid, groupsize=5, measure=1, gameid='',season=2015, league="NBA", datefrom='',   
        dateto='', month=0, opponentteamid=0, paceadjust=1, permode=1, period=0, plusminus=1, rank=1,
        seasonsegment=1, seasontype=1, vsconf=1, vsdiv=1, lastngames=0, location=1, outcome=1):
        self._url = "http://stats.nba.com/stats/teamdashlineups?"
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
                'TeamID':teamid,
                'VsConference':vs_conference(vsconf),
                'VsDivision':vs_division(vsdiv)
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def lineups(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class shooting_splits:
    def __init__(self, teamid, measure=1, season=2015, league="NBA", datefrom='',   
        dateto='', month=0, opponentteamid=0, paceadjust=1, permode=1, period=0, plusminus=1, rank=1,
        seasonsegment=1, seasontype=1, vsconf=1, vsdiv=1, lastngames=0, location=1, outcome=1):
        self._url = "http://stats.nba.com/stats/teamdashboardbyshootingsplits?"
        self._api_param = {
                'DateFrom':valid_date(datefrom),
                'DateTo':valid_date(dateto),
                'GameSegment':game_segment(gamesegment),
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
                'TeamID':teamid,
                'VsConference':vs_conference(vsconf),
                'VsDivision':vs_division(vsdiv)
        }
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_5ft(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_8ft(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_area(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def assisted_shot(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_type(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def assisted_by(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class passing_dashboard:
    def __init__(self,teamid,league='NBA',season='2015', seasontype=1,outcome=1,location=1,month=0,
                seasonsegment=1,datefrom='',dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                period=0,lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/teamdashptpass?"
        self._api_param = {
                        'TeamID' : teamid,
                        'LeagueID': nba_league(league),
                        'Season' :  nba_season(season),
                        'SeasonType' : season_type(seasontype),
                        'Outcome' : outcome(outcome),
                        'Location' : location(location),
                        'Month' : month,
                        'SeasonSegment' : season_segment(seasonsegment),
                        'DateFrom' :  valid_date(datefrom),
                        'DateTo' : valid_date(dateto),
                        'OpponentTeamID' : opponentteamid,
                        'VsConference' : vs_conference(vsconf),
                        'VsDivision' : vs_division(vsdiv),
                        'GameSegment' : game_segment(gamesegment),
                        'Period' :  period,
                        'LastNGames' : lastngames,
                        'PerMode' : per_mode_mini(permode)
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
class rebound_dashboard:
    def __init__(self,teamid,league='NBA',season='2015', seasontype=1,outcome=1,location=1,month=0,
                seasonsegment=1,datefrom='',dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,
                period=0,lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/teamdashptreb?"
        self._api_param = {
                        'TeamID' : teamid,
                        'LeagueID': nba_league(league),
                        'Season' :  nba_season(season),
                        'SeasonType' : season_type(seasontype),
                        'Outcome' : outcome(outcome),
                        'Location' : location(location),
                        'Month' : month,
                        'SeasonSegment' : season_segment(seasonsegment),
                        'DateFrom' :  valid_date(datefrom),
                        'DateTo' : valid_date(dateto),
                        'OpponentTeamID' : opponentteamid,
                        'VsConference' : vs_conference(vsconf),
                        'VsDivision' : vs_division(vsdiv),
                        'GameSegment' : game_segment(gamesegment),
                        'Period' :  period,
                        'LastNGames' : lastngames,
                        'PerMode' : per_mode_mini(permode)
                        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_type(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def contesting_rebounders(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_distance(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def rebound_distance(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class shot_dashboard:
    def __init__(self,teamid,league='NBA',season='2015', seasontype=1,outcome=1,location=1,month=0,
        seasonsegment=1,datefrom='',dateto='',opponentteamid=0,vsconf=1,vsdiv=1,gamesegment=1,period=0,
        lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/teamdashptshots?"
        self._api_param = {
                        'TeamID' : teamid,
                        'LeagueID': nba_league(league),
                        'Season' :  nba_season(season),
                        'SeasonType' : season_type(seasontype),
                        'Outcome' : outcome(outcome),
                        'Location' : location(location),
                        'Month' : month,
                        'SeasonSegment' : season_segment(seasonsegment),
                        'DateFrom' :  valid_date(datefrom),
                        'DateTo' : valid_date(dateto),
                        'OpponentTeamID' : opponentteamid,
                        'VsConference' : vs_conference(vsconf),
                        'VsDivision' : vs_division(vsdiv),
                        'GameSegment' : game_segment(gamesegment),
                        'Period' : period,
                        'LastNGames' : lastngames,
                        'PerMode' : per_mode_mini(permode)
                        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def general(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def shot_clock(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def dribble(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def closest_defender(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def closest_defender_10ft(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def touch_time(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ['team_info', 'roster', 'history', 'splits','season_stats', 'on_off_court', 
           'on_off_court', 'game_logs', 'lineups', 'shooting_splits', 'passing_dashboard',
           'passing_dashboard', 'shot_dashboard']
