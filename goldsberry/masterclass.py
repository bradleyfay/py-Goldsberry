from __future__ import print_function

import requests as _requests
import copy
from contextlib import contextmanager
import retrying

from future.standard_library import install_aliases

install_aliases()
# This library is different between python 2 and 3. This negates the difference
# noinspection PyCompatibility
from urllib.parse import urljoin

header_data = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
                  'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'',image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

class ObjectManager(object):
    def __init__(self, base_url, url_modifier, default_params=None, **kwargs):
        if not default_params:
            default_params = {}
        self.base_url = base_url
        self.api_params = {}
        self._url_modifier = url_modifier
        self.set_default_api_parameters(**default_params)
        self.set_api_parameters(**kwargs)
        self._set_class_data()

    @property
    def target_url(self):
        return urljoin(self.base_url, self._url_modifier)

    def get_parameter_keys(self):
        return self.api_params.keys()

    def get_parameter_values(self):
        return self.api_params.values()

    def get_parameter_items(self):
        '''Return a dict of paramters and values used in query'''
        return self.api_params

    @retrying.retry(stop_max_attempt_number=3, wait_fixed=1000,
                    retry_on_exception=lambda exception: isinstance(exception, _requests.ConnectionError))
    def _get_nba_data(self, api_params):
        pull_url = self.target_url
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
        try:
            headers = nba_table['resultSets'][table_id]['headers']
            values = nba_table['resultSets'][table_id]['rowSet']
        except:
            headers = nba_table['resultSet'][table_id]['headers']
            values = nba_table['resultSet'][table_id]['rowSet']
        return [dict(zip(headers, value)) for value in values]

    def _set_class_data(self):
        nba_data_response = self._get_nba_data(self.api_params)
        self._data_tables = nba_data_response

    def set_api_parameters(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.api_params:
                raise Exception("Bad param '%s'" % k)
            else:
                if v is not None:
                    self.api_params[k] = v

    def set_default_api_parameters(self, **kwargs):
        for k, v in kwargs.items():
            if v is not None:
                self.api_params[k] = v

    def _update_api_parameters(self, **kwargs):
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

    def restore_class_dict(self, class_dict):
        self.__dict__.clear()
        self.__dict__.update(class_dict)

    @contextmanager
    def reinitialize_data_with_new_parameters(self, **kwargs):
        original_dict = copy.deepcopy(self.__dict__)
        try:
            self._update_api_parameters(**kwargs)
            self._set_class_data()
            yield
        except Exception as e:
            raise e
        finally:
            self.restore_class_dict(original_dict)


class ObjectManagerForPlayType(ObjectManager):
    def __init__(self, base_url, url_modifier, year, team, default_params=None, **kwargs):
        self.scope = 'team_' if team else 'player_'
        self.year = int(year[:4])
        if not self.year == 2015:
            raise ValueError('Playtype data stats only available for 2015')
        ObjectManager.__init__(self, base_url, url_modifier, default_params, **kwargs)

    @property
    def target_url(self):
        return urljoin(self.base_url,
                       "{scope}{url_modifier}.js".format(scope=self.scope, url_modifier=self._url_modifier))


class ObjectManagerForSportVu(ObjectManager):
    def __init__(self, base_url, url_modifier, year, team, default_params=None, **kwargs):
        self.scope = 'Team' if team else ''
        self.year = int(year[:4])
        if not 2013 <= self.year <= 2015:
            raise ValueError('SportVU data stats only available for 2013-2015')
        ObjectManager.__init__(self, base_url, url_modifier, default_params, **kwargs)

    @property
    def target_url(self):
        return urljoin(urljoin(self.base_url, "%s/" % self.year),
                       "{url_modifier}{scope}Data.json".format(url_modifier=self._url_modifier, scope=self.scope))


class NbaDataProvider(object):
    def __init__(self, url_modifier, default_params=None, **kwargs):
        base_url = 'http://stats.nba.com/stats/'
        self.object_manager = ObjectManager(base_url, url_modifier, default_params, **kwargs)


class NbaDataProviderPlayType(object):
    def __init__(self, url_modifier, year, team=False, default_params=None, **kwargs):
        base_url = "http://stats.nba.com/js/data/playtype/"
        self.object_manager = ObjectManagerForPlayType(base_url, url_modifier, year, team, default_params, **kwargs)

    def offensive(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    def defensive(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 1)

    @property
    def season(self):
        return self.object_manager.data_tables['parameters']['Season']


class NbaDataProviderSportVu(object):
    def __init__(self, url_modifier, year, team=False, default_params=None, **kwargs):
        base_url = 'http://stats.nba.com/js/data/sportvu/'
        self.object_manager = ObjectManagerForSportVu(base_url, url_modifier, year, team, default_params, **kwargs)

    def data(self):
        return self.object_manager.get_table_from_data(self.object_manager.data_tables, 0)

    @property
    def season(self):
        return self.object_manager.data_tables['parameters']['Season']
