from __future__ import print_function
import requests as _requests
import cgi
import copy
from contextlib import contextmanager

header_data = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 '
                  'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'',image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}


class ObjectManager(object):
    def __init__(self, url_modifier, default_params=None, **kwargs):
        if not default_params:
            default_params = {}
        self.api_params = {}
        self._url_modifier = url_modifier
        self.set_default_api_parameters(**default_params)
        self.set_default_api_parameters(**kwargs)
        self._set_class_data()

    def restore_class_dict(self, class_dict):
        self.__dict__.clear()
        self.__dict__.update(class_dict)

    def get_parameter_keys(self):
        return self.api_params.keys()

    def get_parameter_values(self):
        return self.api_params.values()

    def get_parameter_items(self):
        return self.api_params

    def _get_nba_data(self, api_params):
        base_url = 'http://stats.nba.com/stats/'
        pull_url = cgi.urllib.parse.urljoin(base_url, self._url_modifier)
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
            raise ValueError("Please use the set_default_api_parameters method to set the following paramters",
                             "\n".join(txt))

    @staticmethod
    def get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def _set_class_data(self):
        nba_data_response = self._get_nba_data(self.api_params)
        self.data_tables = nba_data_response

    def set_default_api_parameters(self, **kwargs):
        for k, v in kwargs.items():
            if v is not None:
                self.api_params[k] = v

    def _set_api_parameters(self, **kwargs):
        wrong_parameters_names = []
        for k, v in kwargs.items():
            if k not in self.api_params:
                wrong_parameters_names.append(k)
        if wrong_parameters_names:
            raise ValueError(
                'The following parameters:\n' +
                '\n'.join(wrong_parameters_names) +
                '\nDoes not exist for this class. Please set only existing parameters')
        else:
            self.api_params.update(kwargs)

    @contextmanager
    def reinitialize_data_with_new_parameters(self, **kwargs):
        original_dict = copy.deepcopy(self.__dict__)
        try:
            self._set_api_parameters(**kwargs)
            self._set_class_data()
        except ValueError as e:
            self.restore_class_dict(original_dict)
            raise e
        yield
        self.restore_class_dict(original_dict)


class NbaDataProvider(object):
    def __init__(self, url_modifier, default_params=None, **kwargs):
        self.object_manager = ObjectManager(url_modifier, default_params, **kwargs)


class PlayTypeProvider(object):
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
            self._datatables = self._response.json()
        else:
            # Change this to Exception
            txt = self._response.text.split(';')
            txt = [x.replace(' property', '') for x in txt]
            txt = [x.replace('The ', '') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            print("Please use the set_default_api_parameters method to set the following paramters", "\n".join(txt))

    @staticmethod
    def _get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def offensive(self):
        return self._get_table_from_data(self._datatables, 0)

    def defensive(self):
        return self._get_table_from_data(self._datatables, 1)

    def season(self):
        return self._datatables['parameters']['Season']


class SportVuProvider(object):
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
            self._datatables = self._response.json()
        else:
            # Change this to Exception
            txt = self._response.text.split(';')
            txt = [x.replace(' property', '') for x in txt]
            txt = [x.replace('The ', '') for x in txt]
            txt = [x.split(' is')[0] for x in txt]
            txt = [x.lstrip() for x in txt]
            print("Please use the set_default_api_parameters method to set the following paramters", "\n".join(txt))

    @staticmethod
    def _get_table_from_data(nba_table, table_id):
        headers = nba_table['resultSets'][table_id]['headers']
        values = nba_table['resultSets'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def data(self):
        return self._get_table_from_data(self._datatables, 0)

    def season(self):
        return self._datatables['parameters']['Season']

    def GET_raw_data(self):
        self._get_nba_data(self._url_modifier, self.year)

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
