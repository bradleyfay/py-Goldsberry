import requests as _requests
from goldsberry.apiconvertor import *


class Demographics:
    def __init__(self, player_id):
        self._url = 'http://stats.nba.com/stats/commonplayerinfo?'
        self._api_param = {'PlayerID': player_id}
        self._pull = _requests.get(self._url, params=self._api_param)

    def player_info(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def headline_stats(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class CareerStats:
    def __init__(self, playerid, league='NBA', permode=1):
        self._url = "http://stats.nba.com/stats/playerprofilev2?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'PerMode': per_mode_small_36(permode)}
        self._pull = _requests.get(self._url, params=self._api_param)

    def season_totals_regular(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def career_totals_regular(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_totals_post(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def career_totals_post(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_totals_allstar(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def career_totals_allstar(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_totals_college(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def career_totals_college(self):
        _headers = self._pull.json()['resultSets'][7]['headers']
        _values = self._pull.json()['resultSets'][7]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_rankings_regular(self):
        _headers = self._pull.json()['resultSets'][8]['headers']
        _values = self._pull.json()['resultSets'][8]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_rankings_post(self):
        _headers = self._pull.json()['resultSets'][9]['headers']
        _values = self._pull.json()['resultSets'][9]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def season_high(self):
        _headers = self._pull.json()['resultSets'][10]['headers']
        _values = self._pull.json()['resultSets'][10]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def career_high(self):
        _headers = self._pull.json()['resultSets'][11]['headers']
        _values = self._pull.json()['resultSets'][11]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def next_game(self):
        _headers = self._pull.json()['resultSets'][12]['headers']
        _values = self._pull.json()['resultSets'][12]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class general_splits:
    def __init__(self, playerid, season='2015', seasontype=1, league='NBA',
                 dateto='', datefrom='', gamesegment=1, lastngames=0, location=1, measuretype=1,
                 month=0, opponentteamid=0, outcome=1, paceadjust=1, permode=1, period=0,
                 plusminus=1, rank=1, seasonsegment=1, vsconf=1, vsdiv=1):
        self._url = "http://stats.nba.com/stats/playerdashboardbygeneralsplits?"
        self._api_param = {'PlayerID': playerid,
                           'SeasonType': season_type(seasontype),
                           'Season': nba_season(season),
                           'LeagueID': nba_league(league),
                           'DateTo': valid_date(dateto),
                           'DateFrom': valid_date(datefrom),
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
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv)}
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

    def starting_position(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def days_rest(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class game_logs:
    def __init__(self, playerid, season='2015', seasontype=1, league='NBA'):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID': playerid,
                           'SeasonType': season_type(seasontype),
                           'Season': nba_season(season),
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def logs(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class ShotDashboard:
    def __init__(self, playerid, league='NBA', season='2015', seasontype=1, teamid=0,
                 outcome=1, location=1, month=0, seasonsegment=1, datefrom='',
                 dateto='', opponentteamid=0, vsconf=1, vsdiv=1, gamesegment=1,
                 period=0, lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptshots?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames,
                           'PerMode': per_mode_mini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def overall(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def general(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def shot_clock(self):
        _headers = self._pull.json()['resultSets'][2]['headers']
        _values = self._pull.json()['resultSets'][2]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def dribble(self):
        _headers = self._pull.json()['resultSets'][3]['headers']
        _values = self._pull.json()['resultSets'][3]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def closest_defender(self):
        _headers = self._pull.json()['resultSets'][4]['headers']
        _values = self._pull.json()['resultSets'][4]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def closest_defender_10ft(self):
        _headers = self._pull.json()['resultSets'][5]['headers']
        _values = self._pull.json()['resultSets'][5]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def touch_time(self):
        _headers = self._pull.json()['resultSets'][6]['headers']
        _values = self._pull.json()['resultSets'][6]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class ReboundDashboard:
    def __init__(self, player_id, league='NBA', season='2015', season_type=1, team_id=0,
                 outcome=1, location=1, month=0, season_segment=1, date_from='',
                 date_to='', opponent_team_id=0, vs_conf=1, vs_div=1, game_segment=1,
                 period=0, last_n_games=0, per_mode=1):
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID': player_id,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(season_type),
                           'TeamID': team_id,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(season_segment),
                           'DateFrom': valid_date(date_from),
                           'DateTo': valid_date(date_to),
                           'OpponentTeamID': opponent_team_id,
                           'VsConference': vs_conference(vs_conf),
                           'VsDivision': vs_division(vs_div),
                           'GameSegment': game_segment(game_segment),
                           'Period': period,
                           'LastNGames': last_n_games,
                           'PerMode': per_mode_mini(per_mode)
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


class passing_dashboard:
    def __init__(self, playerid, league='NBA', season='2015', seasontype=1, teamid=0,
                 outcome=1, location=1, month=0, seasonsegment=1, datefrom='',
                 dateto='', opponentteamid=0, vsconf=1, vsdiv=1, gamesegment=1,
                 period=0, lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptpass?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames,
                           'PerMode': per_mode_mini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def passes_made(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def passes_received(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class defense_dashboard:
    def __init__(self, playerid, league='NBA', season='2015', seasontype=1, teamid=0,
                 outcome=1, location=1, month=0, seasonsegment=1, datefrom='',
                 dateto='', opponentteamid=0, vsconf=1, vsdiv=1, gamesegment=1,
                 period=0, lastngames=0, permode=1):
        self._url = "http://stats.nba.com/stats/playerdashptreb?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames,
                           'PerMode': per_mode_mini(permode)
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def defending_shot(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class shot_log:
    def __init__(self, playerid, league='NBA', season='2015', seasontype=1, teamid=0,
                 outcome=1, location=1, month=0, seasonsegment=1, datefrom='',
                 dateto='', opponentteamid=0, vsconf=1, vsdiv=1, gamesegment=1,
                 period=0, lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptshotlog?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class rebound_log:
    def __init__(self, playerid, league='NBA', season='2015', seasontype=1, teamid=0,
                 outcome=1, location=1, month=0, seasonsegment=1, datefrom='',
                 dateto='', opponentteamid=0, vsconf=1, vsdiv=1, gamesegment=1,
                 period=0, lastngames=0):
        self._url = "http://stats.nba.com/stats/playerdashptreboundlogs?"
        self._api_param = {'PlayerID': playerid,
                           'LeagueID': nba_league(league),
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def log(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


class shot_chart:
    def __init__(self, playerid, leagueid='', season='2015', seasontype=1, teamid=0,
                 gameid='', outcome=1, location=1, month=0, seasonsegment=1,
                 datefrom='', dateto='', opponentteamid=0, vsconf=1, vsdiv=1,
                 position=1, period=0, lastngames=0, aheadbehind=1,
                 contextmeasure=1, clutchtime=7, rookieyear='',
                 contextfilter='', startperiod='1', endperiod='10', startrange='0',
                 endrange='28800', gamesegment=1, rangetype='2'):
        if not rookieyear == '':
            rookieyear = nba_season(rookieyear)
        self._url = "http://stats.nba.com/stats/shotchartdetail?"
        self._api_param = {'LeagueID': leagueid,
                           'Season': nba_season(season),
                           'SeasonType': season_type(seasontype),
                           'TeamID': teamid,
                           'PlayerID': playerid,
                           'GameID': gameid,
                           'Outcome': outcome(outcome),
                           'Location': location(location),
                           'Month': month,
                           'SeasonSegment': season_segment(seasonsegment),
                           'DateFrom': valid_date(datefrom),
                           'DateTo': valid_date(dateto),
                           'OpponentTeamID': opponentteamid,
                           'VsConference': vs_conference(vsconf),
                           'VsDivision': vs_division(vsdiv),
                           'Position': position(position),
                           'GameSegment': game_segment(gamesegment),
                           'Period': period,
                           'LastNGames': lastngames,
                           'AheadBehind': ahead_behind(aheadbehind),
                           'ContextMeasure': context_measure(contextmeasure),
                           'ClutchTime': clutch_time(clutchtime),
                           'RookieYear': rookieyear,
                           'ContextFilter': contextfilter,
                           'StartPeriod': startperiod,
                           'EndPeriod': endperiod,
                           'StartRange': startrange,
                           'EndRange': endrange,
                           'RangeType': rangetype,
                           }
        self._pull = _requests.get(self._url, params=self._api_param)

    def chart(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

    def leagueaverage(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


def PlayerList(season='2015', AllTime=False, league='NBA'):
    if AllTime:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason': "0",
                      'LeagueID': nba_league(league),
                      'Season': "2015-15"}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    else:
        _url = "http://stats.nba.com/stats/commonallplayers?"
        _api_param = {'IsOnlyCurrentSeason': "1",
                      'LeagueID': nba_league(league),
                      'Season': nba_season(season)}
        _pull = _requests.get(_url, params=_api_param)
        _headers = _pull.json()['resultSets'][0]['headers']
        _values = _pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]


__all__ = ["Demographics", "CareerStats", "general_splits",
           "game_logs", "ShotDashboard", "ReboundDashboard",
           "passing_dashboard", "defense_dashboard", "shot_log",
           "rebound_log", "shot_chart"]
