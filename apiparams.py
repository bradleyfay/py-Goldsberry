default_league_id = '00'
default_season = '2015-16'
default_season_id = '22015'
default_season_type = 'Regular Season'
default_pace_adjust = 'N'
default_plus_minus = 'N'
default_ahead_or_behind = 'Ahead or Behind'
default_clutch_time = 'Last 5 Minutes'
default_points_diff = 5
default_team_id = 0
default_player_id = 0
default_game_id = 0


p_player_common = {
    'PlayerID': default_player_id
}

p_team_base = {
    'LeagueID': default_league_id,
    'Season': default_season,
    'TeamID': default_team_id
}

p_ply_career = {
    'PerMode': 'Totals',
    'PlayerID': default_player_id
}

p_team_year_by_year = {
    'LeagueID': default_league_id,
    'SeasonType': default_season_type,
    'TeamID': default_team_id,
    'PerMode': 'Totals'
}

p_ply_gamelogs = {
    'PlayerID': default_player_id,
    'Season': default_season,
    'SeasonType': default_season_type
}

p_ply_dashboard = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'Location': '',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'Period': 0,
    'PerMode': 'Totals',
    'PlayerID': default_player_id,
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': '',
    'LeagueID': default_league_id
}

p_ply_list = {
    'IsOnlyCurrentSeason': '1',
    'LeagueID': default_league_id,
    'PlayerID': default_player_id,
    'Season': default_season
}

p_ply_shotchart = {
    'ContextMeasure': 'FGM',
    'DateFrom': '',
    'DateTo': '',
    'GameID': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'Period': 0,
    'PlayerID': default_player_id,
    'Position': '',
    'RookieYear': '',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''
}

p_game_ids = {
    'LeagueID': default_league_id,
    'Season': default_season,
    'PlayerOrTeam': 'T',
    'Direction': 'DESC',
    'SeasonType': default_season_type,
    'Sorter': 'FGM'
}

p_team_lineups = {
    'DateFrom': '',
    'DateTo': '',
    'GameID': '',
    'GameSegment': '',
    'GroupQuantity': 5,
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Advanced',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''}

p_team_onoff = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Advanced',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''}

p_team_dashbd = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'Period': 0,
    'PerMode': 'Totals',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''
}

p_team_gamelogs = {
    'LeagueID': default_league_id,
    'Season': default_season,
    'SeasonType': default_season_type,
    'TeamID': default_team_id
}

p_team_season = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''}

p_team_shooting = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''}

p_team_split = {
    'DateFrom': '',
    'DateTo': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Advanced',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''}

p_team_info = {
    'LeagueID': default_league_id,
    'Season': default_season,
    'SeasonType': default_season_type,
    'TeamID': default_team_id
}

p_game_bs = {
    'GameID': default_game_id,
    'EndPeriod': 0,
    'EndRange': 0,
    'RangeType': 0,
    'StartPeriod': 0,
    'StartRange': 0}

p_game_pbp = {'GameID': default_game_id, 'EndPeriod': 0, 'StartPeriod': 0}

p_league_sb = {'DayOffset': '0', 'LeagueID': default_league_id}

p_league_history = {'LeagueID': default_league_id}

p_league_leaders = {
    'LeagueID': default_league_id,
    'PerMode': 'PerGame',
    'Scope': 'RS',
    'Season': default_season,
    'SeasonType': default_season_type,
    'StatCategory': 'PTS'}

p_league_lineups = {
    'Conference': '',
    'DateFrom': '',
    'DateTo': '',
    'Division': '',
    'GameSegment': '',
    'GroupQuantity': 5,
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Advanced',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': ''
}

p_playoff_picture = {
    'LeagueID': default_league_id,
    'SeasonID': default_season_id
}

p_league_classic = {
    'College': '',
    'Conference': '',
    'Country': '',
    'DateFrom': '',
    'DateTo': '',
    'Division': '',
    'DraftPick': '',
    'DraftYear': '',
    'GameScope': '',
    'GameSegment': '',
    'Height': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PORound': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlayerExperience': '',
    'PlayerPosition': '',
    'PlusMinus': default_plus_minus,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'ShotClockRange': '',
    'StarterBench': '',
    'TeamID': default_team_id,
    'VsConference': '',
    'VsDivision': '',
    'Weight': ''
}

p_league_team_clutch = {
    'AheadBehind': default_ahead_or_behind,
    'ClutchTime': default_clutch_time,
    'DateFrom': '',
    'DateTo': '',
    'Direction': 'DESC',
    'GameScope': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Advanced',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Totals',
    'Period': 0,
    'PlayerExperience': '',
    'PlayerOrTeam': 'T',
    'PlayerPosition': '',
    'PlusMinus': default_plus_minus,
    'PointDiff': default_points_diff,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'Sorter': 'FGM',
    'StarterBench': '',
    'VsConference': '',
    'VsDivision': ''
}

p_league_player_clutch = {
    'AheadBehind': default_ahead_or_behind,
    'ClutchTime': default_clutch_time,
    'DateFrom': '',
    'DateTo': '',
    'Direction': 'DESC',
    'GameScope': '',
    'GameSegment': '',
    'LastNGames': 0,
    'LeagueID': default_league_id,
    'Location': '',
    'MeasureType': 'Base',
    'Month': 0,
    'OpponentTeamID': 0,
    'Outcome': '',
    'PaceAdjust': default_pace_adjust,
    'PerMode': 'Per36',
    'Period': 0,
    'PlayerExperience': '',
    'PlayerOrTeam': 'P',
    'PlayerPosition': '',
    'PlusMinus': default_plus_minus,
    'PointDiff': default_points_diff,
    'Rank': 'Y',
    'Season': default_season,
    'SeasonSegment': '',
    'SeasonType': default_season_type,
    'Sorter': 'FGM',
    'StarterBench': '',
    'VsConference': '',
    'VsDivision': ''
}

p_draft = {'LeagueID': default_league_id, 'SeasonYear': default_season}
