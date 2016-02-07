p_base = {
    'LeagueID':'00',
    'Season':'2015-16'
}

p_ply_career = {
    'LeagueID':'00',
    'Season':'2015-16',
    'PerMode':'PerGame'
}

p_ply_gamelogs = {
    'LeagueID':'00',
    'Season':'2015-16',
    'SeasonType':'Regular Season'
}

p_ply_dashboard = {
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

p_ply_list = {
    'IsOnlyCurrentSeason':'1',
    'LeagueID':'00',
    'Season':'2015-16'
}

class default_parameters(object):
    def __init__(self):
        pass

class param_base(object):
    def __init__(self):
        # NBA_datapull.__init__(self)
        self.SET_parameters(**{
            'LeagueID':'00',
            'Season':'2015-16'
            })

class plyr_career(object):
    def __init__(self):
        self.SET_parameters(**{
            'LeagueID':'00',
            'Season':'2015-16'
            })

class plyr_gamelogs(object):
    def __init__(self):
        self.SET_parameters(**{
            'LeagueID':'00',
            'Season':'2015-16',
            'SeasonType':'Regualar Season'
            })

class player_list(object):
    def __init__(self):
        self.SET_parameters(**{
            'IsOnlyCurrentSeason':'1',
            'LeagueID':'00',
            'Season':'2015-16'
            })

class player_dashboard_params(object):
    def __init__(self):
        self.SET_parameters(**{
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
            })

class game_id_params(object):
    def __init__(self):
        self.SET_parameters(**{
            'LeagueID':'00',
            'Season':'2015-16',
            'PlayerOrTeam':'T',
            'Direction':'DESC',
            'SeasonType':'Regular Season',
            'Sorter':'FGM'
            })