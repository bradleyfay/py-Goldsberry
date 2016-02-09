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

p_ply_shotchart = {
    'ContextMeasure': 'FGM',
    'DateFrom': '',
    'DateTo': '',
    'GameID': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': '',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'Period': 0,
    'Position': '',
    'RookieYear': '',
    'Season': '2015-16',
    'SeasonSegment': '',
    'SeasonType': 'Regular Season',
    'TeamID': 0,
    'VsConference': '',
    'VsDivision': ''
    }

p_game_ids = {
    'LeagueID':'00',
    'Season':'2015-16',
    'PlayerOrTeam':'T',
    'Direction':'DESC',
    'SeasonType':'Regular Season',
    'Sorter':'FGM'
}

p_team_lineups = {
    'DateFrom': None,
    'DateTo': None,
    'GameID': None,
    'GameSegment': None,
    'GroupQuantity': 5,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PORound': None,
    'PaceAdjust': 'Y',
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': 'Y',
    'Rank': 'Y',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'ShotClockRange': None,
    'VsConference': None,
    'VsDivision': None}

p_team_onoff = {
    'DateFrom': None,
    'DateTo': None,
    'GameSegment': None,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PaceAdjust': 'Y',
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': 'Y',
    'Rank': 'Y',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'VsConference': None,
    'VsDivision': None}

p_team_dashbd = {
    'DateFrom': None,
    'DateTo': None,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PerMode': 'Totals',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'VsConference': None,
    'VsDivision': None
    }

p_team_season = {
    'DateFrom': None,
    'DateTo': None,
    'GameSegment': None,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PORound': None,
    'PaceAdjust': 'Y',
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': 'Y',
    'Rank': 'Y',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'ShotClockRange': None,
    'TeamID': 1610612758,
    'VsConference': None,
    'VsDivision': None}

p_team_shooting = {
    'DateFrom': None,
    'DateTo': None,
    'GameSegment': None,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PORound': None,
    'PaceAdjust': 'Y',
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': 'Y',
    'Rank': 'Y',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'ShotClockRange': None,
    'VsConference': None,
    'VsDivision': None}

p_team_split = {
    'DateFrom': None,
    'DateTo': None,
    'GameSegment': None,
    'LastNGames': 0,
    'LeagueID': '00',
    'Location': None,
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': None,
    'PORound': None,
    'PaceAdjust': 'Y',
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': 'Y',
    'Rank': 'Y',
    'Season': '2015-16',
    'SeasonSegment': None,
    'SeasonType': 'Regular Season',
    'ShotClockRange': None,
    'VsConference': None,
    'VsDivision': None}

p_team_info = {
    'LeagueID':'00',
    'Season': '2015-16',
    'SeasonType': 'Pre Season'
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
