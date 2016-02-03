class param_base(object):
    api_params = {'LeagueID':'00', 'Season':'2015-16'}

class player_list(param_base):
    _api_params = {'IsOnlyCurrentSeason':'1','LeagueID':'00','Season':'2015-16'}

class player_dashboard_params(param_base):
    api_params = {
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
        'LeagueID':'00'
        }

class default_parameters(object):
    api_params = {}