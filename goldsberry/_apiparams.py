class param_base(object):
    _api_params = {}

class player_list(param_base):
    def __init__(self):
        self._api_params.update({
        'IsOnlyCurrentSeason':'1',
        'LeagueID':'00',
        'Season':'2015-16'
            })

class player_dashboard_params(param_base):
    def __init__(self):
        self._api_params.update({
            'DateFrom':'',
            'DateTo':'',
            'GameSegment':'',
            'LastNGames':0,
            'Location':'',
            'Month':0,
            'OpponentTeamID':0,
            'Outcome':'',
            'Period':0,
            'PerMode':'PerGame',
            'Season':'2015-16',
            'SeasonSegment':'',
            'SeasonType':'Regular Season',
            'TeamID':0,
            'VsConference':'',
            'VsDivision':'',
            'LeagueID': '00'
            })

class default_params(param_base):
    def __init__(self):
        self._api_params.update({
        'PerMode':'Totals'
            })

class default_parameters(object):
    _api_params = {}



# DateFrom=
# DateTo=
# GameSegment=
# LastNGames=0
# Location=
# Month=0
# OpponentTeamID=0
# Outcome=
# Period=0
# PerMode=PerGame
# Season=2015-16
# SeasonSegment=
# SeasonType=Regular+Season
# TeamID=0
# LeagueID=00
# PlayerID=202326
# VsConference=
# VsDivision=