import requests as _requests

class NBA_datapull():
    # Set QueryString Parameters
    #_api_params = {}
    def SET_parameters(self, param, value):
        self._api_params[param] = value

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
        self._url = response.url
        self._headers = response.request.headers
        if response.status_code == 200:
            self._datatables = response.json()
        else:
            # Change this to Exception
            print 'HTTP Response {0}: {1}'.format(response.status_code,
                                                   response.reason)
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
        self._get_nba_data(self._url_modifier,self._api_params)

class TEAM(NBA_datapull):
    def __init__(self, teamid, **kwargs):
        self.SET_parameters('TeamID', teamid)
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self._api_params)

class GAME(NBA_datapull):
    def __init__(self, gameid, **kwargs):
        self.SET_parameters('GameID', gameid)
        for k,v in kwargs:
            self.SET_parameters(k,v)
        self.GET_raw_data()
    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier,self._api_params)