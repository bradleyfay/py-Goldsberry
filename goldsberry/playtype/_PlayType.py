import requests as _requests
from goldsberry.apiconvertor import *

class transition:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Transition.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Transition.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']

class isolation:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Isolation.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Isolation.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']

class pick_and_roll_ball_handler:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_PRBallHandler.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_PRBallHandler.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class pick_and_roll_roll_man:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_PRRollMan.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_PRRollMan.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class postup:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Postup.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Postup.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class spotup:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Spotup.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Spotup.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class handoff:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_handoff.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_cut.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class cut:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Cut.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Cut.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class offscreen:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_OffScreen.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_OffScreen.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class offrebound:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_OffRebound.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_OffRebound.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']
class misc:
    def __init__(self, team=False):
        if team:
            self._url = "http://stats.nba.com/js/data/playtype/team_Misc.js"
        else:
            self._url = "http://stats.nba.com/js/data/playtype/player_Misc.js"
        self._pull = requests.get(self._url)
    def offensive(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def defensive(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def season(self):
        return self._pull.json()['parameters']['Season']

__all__ = ['transition', 'isolation', 'pick_and_roll_ball_handler', 
'pick_and_roll_roll_man', 'postup', 'spotup', 'handoff', 'cut', 
'offscreen', 'offrebound', 'misc']