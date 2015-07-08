import requests
from . import Game
from . import League
from . import Draft
from . import Player
from . import Team

def PlayerList(CurrentSeason='1', LeagueID='00', Season='2014-15'):
    _url = "http://stats.nba.com/stats/commonallplayers?"
    _api_param = {'IsOnlyCurrentSeason':CurrentSeason,
                  'LeagueID':LeagueID,
                  'Season': Season
                  }
    _pull = requests.get(_url, params=_api_param)
    _headers = _pull.json()['resultSets'][0]['headers']
    _values = _pull.json()['resultSets'][0]['rowSet']
    return [dict(zip(_headers, value)) for value in _values]

playersCurrent = PlayerList()
playersAllTime = PlayerList(0)