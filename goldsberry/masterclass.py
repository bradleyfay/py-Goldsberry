from __future__ import print_function
import cgi
import requests as _requests


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


class NbaDataProvider(object):
    """Primary Class"""
    def __init__(self, url_modifier, default_params=None, **kwargs):
        if not default_params:
            default_params = {}
        self._response = None
        self.api_params = {}
        self._url_modifier = url_modifier
        self._set_api_parameters(**default_params)
        self._set_api_parameters(**kwargs)
        self._set_class_data()


    def get_parameter_items(self):
        '''Return a dict of paramters and values used in query'''
        return self.api_params

    def _get_nba_data(self, api_params):
        '''Execute request to nba website and returns json formatted data'''
        base_url = 'http://stats.nba.com/stats/'
        pull_url = cgi.urlparse.urljoin(base_url, self._url_modifier)
        self._response = _requests.get(pull_url, params=api_params,
                                       headers=header_data)

        if self._response.status_code == 200:
            return self._response.json()
        else:
            # Change this to Exception
            txt = self._response.text.split(';')
            txt = [x.replace(' property', '') for x in txt]
            txt = [x.replace('The ', '') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            raise ValueError("Please use the set_api_parameters method to set the following parameters",
                             "\n".join(txt))

    @staticmethod
    def _get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def _set_class_data(self):
        nba_data_response = self._get_nba_data(self.api_params)
        self._data_tables = nba_data_response

    def _set_api_parameters(self, **kwargs):
        for k, v in kwargs.items():
            self.api_params[k] = v

    def _update_api_parameters(self, **kwargs):
        wrong_parameters_names = []
        for k, _ in kwargs.items():
            if not self.api_params.has_key(k):
                wrong_parameters_names.append(k)
        if wrong_parameters_names:
            raise ValueError(
                'The following parameters:\n' +
                '\n'.join(wrong_parameters_names) +
                '\nDoes not exist for this class. Please set only existing parameters')
        else:
            self.api_params.update(kwargs)

    def get_new_data(self, **kwargs):
        '''Re-runs query to NBA site with new kwarg parameters'''
        original_api_params = self.api_params
        try:
            self._update_api_parameters(**kwargs)
            self._set_class_data()
        except ValueError:
            print("There was an error in your parameter update. No new data was collected")
            self.api_params = original_api_params

class PlayTypeProvider(object):
    """Class specific settings to query play type data"""
    def __init__(self, url_modifier, team=False):
        self._url_modifier = url_modifier
        self._get_nba_data(url_modifier, team)

    def _get_nba_data(self, url_modifier, team):
        base_url = "http://stats.nba.com/js/data/playtype/"
        if team:
            scope = 'team_'
        else:
            scope = 'player_'
        pull_url = "{0}{1}{2}.js".format(base_url, scope, url_modifier)
        self._response = _requests.get(pull_url,
                                       headers=header_data)

        if self._response.status_code == 200:
            self._data_tables = self._response.json()
        else:
            # Change this to Exception
            txt = self._response.text.split(';')
            txt = [x.replace(' property', '') for x in txt]
            txt = [x.replace('The ', '') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            print("Please use the set_api_parameters method to set the following paramters",
                  "\n".join(txt))

    @staticmethod
    def _get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def offensive(self):
        '''Return Offensive data'''
        return self._get_table_from_data(self._data_tables, 0)

    def defensive(self):
        '''Return Defensive data'''
        return self._get_table_from_data(self._data_tables, 1)

    def season(self):
        '''Return Season Summary data'''
        return self._data_tables['parameters']['Season']

class SportVuProvider(object):
    """Class specific settings to query sportvu data"""
    def __init__(self, url_modifier, year=2015, team=False):
        self.year = year
        self.team = team
        self._url_modifier = url_modifier
        self._get_nba_data(url_modifier, self.year, self.team)

    def _get_nba_data(self, url_modifier, year, team):
        base_url = 'http://stats.nba.com/js/data/sportvu/'
        if team:
            team = 'Team'
        else:
            team = ''
        pull_url = "{0}{1}/{2}{3}Data.json".format(base_url,
                                                   year, url_modifier, team)
        self._response = _requests.get(pull_url,
                                       headers=header_data)
        if self._response.status_code == 200:
            self._data_tables = self._response.json()
        else:
            # Change this to Exception
            txt = self._response.text.split(';')
            txt = [x.replace(' property', '') for x in txt]
            txt = [x.replace('The ', '') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            print("Please use the set_api_parameters method to set the following paramters", "\n".join(txt))

    @staticmethod
    def _get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def data(self):
        '''Return SportVU data'''
        return self._get_table_from_data(self._data_tables, 0)

    def season(self):
        '''Return Season Summary SportVu Data'''
        return self._data_tables['parameters']['Season']