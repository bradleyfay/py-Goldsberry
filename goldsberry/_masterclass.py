from __future__ import print_function
import requests as _requests

class NBA_datapull(object):
    # Set QueryString Parameters
    #api_params = {}
    def SET_parameters(self, param, value):
        self.api_params[param] = value

    def _get_nba_data(self, url_modifier, api_params):
        base_url = 'http://stats.nba.com/stats/'
        pull_url = "{0}{1}?".format(base_url, url_modifier)
        header_data = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'\
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 '\
            'Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'\
            ',image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
        response = _requests.get(pull_url, params = api_params,
                                headers = header_data)

        if response.status_code == 200:
            self._datatables = response.json()
        else:
            # Change this to Exception
            txt = response.text.split(';')
            txt = [x.replace(' property','') for x in txt]
            txt = [x.replace('The ','') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            print("Please use the SET_parameters method to set the following paramters", "\n".join(txt))

    def _get_table_from_data(self, nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values  = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

class PLAYER(NBA_datapull):
    def __init__(self, playerid, **kwargs):
        self.SET_parameters('PlayerID', playerid)
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)

class TEAM(NBA_datapull):
    def __init__(self, teamid, **kwargs):
        self.SET_parameters('TeamID', teamid)
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)

class GAME(NBA_datapull):
    def __init__(self, gameid, **kwargs):
        self.SET_parameters('GameID', gameid)
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)

class DAILY(NBA_datapull):
    def __init__(self, date, **kwargs):
        self.SET_parameters('gameDate', date) # Needs format validation
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)

class LEAGUE(NBA_datapull):
    def __init__(self, **kwargs):
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.api_params)

class PLAYTYPE(object):
    def __init__(self, team=False):
        self._get_nba_data(self._url_modifier, team)

    def _get_nba_data(self, url_modifier, team):
        header_data = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'\
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 '\
            'Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'\
            ',image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
        base_url = "http://stats.nba.com/js/data/playtype/"
        if team:
            scope = 'team_'
        else: scope = 'player_'
        pull_url = "{0}{1}{2}.js".format(base_url, scope, url_modifier)
        response = _requests.get(pull_url, headers = header_data)
        self._url = response.url
        self._headers = response.request.headers
        if response.status_code == 200:
            self._datatables = response.json()
        else:
            # Change this to Exception
            print('HTTP Response {0}: {1}'.format(response.status_code,
                                                   response.reason))
    def _get_table_from_data(self, nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values  = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def offensive(self):
        return self._get_table_from_data(self._datatables, 0)
    def defensive(self):
        return self._get_table_from_data(self._datatables, 1)
    def season(self):
        return self._datatables['parameters']['Season']

class BASE(NBA_datapull):
    _junk = ''

class SPORTVU(object):
    def __init__(self, year=2015, team=False):
        self.year = year
        self.team = team
        self._get_nba_data(self._url_modifier, self.year, self.team)

    def _get_nba_data(self, url_modifier, year, team) :
        header_data = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'\
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 '\
            'Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'\
            ',image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
        base_url = 'http://stats.nba.com/js/data/sportvu/'
        if team:
            team = 'Team'
        else: team = ''
        pull_url = "{0}{1}/{2}{3}Data.json".format(base_url, 
                                                year, url_modifier,team)
        response = _requests.get(pull_url, headers = header_data)
        self._url = response.url
        self._headers = response.request.headers
        if response.status_code == 200:
            self._datatables = response.json()
        else:
            # Change this to Exception
            print('HTTP Response {0}: {1}'.format(response.status_code,
                                                   response.reason))
    def _get_table_from_data(self, nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values  = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def data(self):
        return self._get_table_from_data(self._datatables, 0)
    def season(self):
        return self._datatables['parameters']['Season']
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self.year)
    def SET_parameters(self, **kwargs):
        if kwargs.has_key('year'):
            self.year = kwargs['year']
        elif kwargs.has_key('team'):
            if isinstance(kwargs['team'], (bool)):
                self.team = kwargs['team']
            else: 
                self.team = False
                print('Please use True/False for team parameter')
        else:
            pass