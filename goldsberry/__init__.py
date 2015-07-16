__author__ = 'Bradley Fay'
__email__ = 'bradley.fay@gmail.com'
__version__ = '0.3.2'

import requests as _requests
import goldsberry.game
import goldsberry.league
import goldsberry.player
import goldsberry.team

def PlayerList(CurrentSeason='1', LeagueID='00', Season='2014-15'):
    _url = "http://stats.nba.com/stats/commonallplayers?"
    _api_param = {'IsOnlyCurrentSeason':CurrentSeason,
                  'LeagueID':LeagueID,
                  'Season': Season
                  }
    _pull = _requests.get(_url, params=_api_param)
    _headers = _pull.json()['resultSets'][0]['headers']
    _values = _pull.json()['resultSets'][0]['rowSet']
    return [dict(zip(_headers, value)) for value in _values]

#CurrentNBA = _df(PlayerList())
#AllTimeNBA = _df(PlayerList(0))
