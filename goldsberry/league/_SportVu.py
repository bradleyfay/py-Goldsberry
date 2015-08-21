import requests as _requests
from goldsberry._apiFunc import *

class catch_and_shoot:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/catchShootTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/catchShootData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class defense:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/defenseTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/defenseData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class drives:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/drivesTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/drivesData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class passing:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/passingTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/passingData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class touches:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/touchesTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/touchesData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class pull_up_shooting:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/pullUpShootTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/pullUpShootData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class rebounding:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/reboundingTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/reboundingData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class shooting:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/shootingTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/shootingData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']
class speed:
    def __init__(self, year=2014, team=False):
        if team:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/speedTeamData.json']
        else:
            self._url = ['http://stats.nba.com/js/data/sportvu/', str(year), '/speedData.json']
            self._url = "".join(self._url)
        self._pull = requests.get(self._url)
    def get_data(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def get_season(self):
        return self._pull.json()['parameters']['Season']

__all__ = ['catch_and_shoot', 'defense', 'drives', 'passing', 
    'touches', 'pull_up_shooting', 'rebounding', 'shooting', 
    'speed']