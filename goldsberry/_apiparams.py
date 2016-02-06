class param_base(object):
    api_params = {'LeagueID':'00', 'Season':'2015-16'}

class plyr_career(object):
    api_params = {'LeagueID':'00', 'Season':'2015-16', 'PerMode':'PerGame'}

class plyr_gamelogs(object):
    api_params = {'LeagueID':'00', 'Season':'2015-16', 'SeasonType':'Regualar Season'}

class player_list(object):
    _api_params = {'IsOnlyCurrentSeason':'1','LeagueID':'00','Season':'2015-16'}

class player_dashboard_params(object):
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

class game_id_params(object):
    api_params = {
    'LeagueID':'00',
    'Season':'2015-16',
    'PlayerOrTeam':'T',
    'Direction':'DESC',
    'SeasonType':'Regular Season',
    'Sorter':'FGM'}