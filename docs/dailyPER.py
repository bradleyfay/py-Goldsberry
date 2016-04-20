from __future__ import division
import subprocess

import goldsberry
import pandas as pd


class DailyPER(object):
    
    def __init__(self):
        per_data = compute_daily_per()
        per_data.to_csv('data/cardinal_PER.csv')
        subprocess.check_call(['aws','s3','sync','~/data/','s3://cardinal-advising/paul-robbins'])
    
    def compute_daily_per():
        games = compute_cum_team_totals(get_games())
        players = get_players()
        game_logs = get_player_game_logs(players.PERSON_ID.tolist())
        per_data = merge_game_and_player_logs(games, game_logs)
        return compute_PER(per_data)

    def get_games():
        games_json = goldsberry.GameIDs()
        df_games = pd.DataFrame(games_json.game_list())
        df_games.sort_values('GAME_ID', inplace=True)
        df_games.reset_index(drop=True, inplace=True)
        return df_games
    
    def compute_cum_team_totals(games):
        t = games.groupby(['TEAM_ID', 'GAME_DATE'])['AST', 'FGA', 'FGM', 'PTS'].cumsum()
        games = games.merge(t, left_index=True, right_index=True, suffixes=('', '_CUM_TOTALS'))
        games['GAME_NUMBER'] = games.groupby(['TEAM_ID', 'GAME_DATE']).cumcount()+1
        games = games.merge(
                    (games
                         .groupby(['GAME_DATE'])['AST', 'FGA', 'FGM', 
                                                 'REB', 'OREB', 'TOV', 
                                                 'FTA', 'FTM', 'PF', 'PTS']
                         .sum()),
                    left_on='GAME_DATE', right_index=True,
                    suffixes=('', '_LEAGUE'))
        g = games.groupby('GAME_DATE')['TEAM_ID'].nunique()
        g.name = 'NUM_TEAMS'
        games = games.join(g, on='GAME_DATE')
        cum_cols = ['AST_LEAGUE', 'FGA_LEAGUE', 'FGM_LEAGUE', 'REB_LEAGUE', 
                    'OREB_LEAGUE', 'TOV_LEAGUE', 'FTA_LEAGUE', 'FTM_LEAGUE', 
                    'PF_LEAGUE', 'PTS_LEAGUE', 'NUM_TEAMS']

        d = df_games.merge(df_games.groupby('GAME_DATE')[cum_cols].cumsum(), 
                       left_index=True, right_index=True,
                       suffixes = ('', '_CUM'))
        
        d = d.join(d.groupby('GAME_ID')['PTS'].sum(), on='GAME_ID', rsuffix='_GAMETOTAL')
        
        def compute_FTM_PF(row):
            return row['FTM_LEAGUE_CUM']/row['PF_LEAGUE_CUM']

        def compute_FTA_PF(row):
            return row['FTA_LEAGUE_CUM']/row['PF_LEAGUE_CUM']
        
        def compute_factor(row):
            return (2/3) - (.5*row['AST_LEAGUE_CUM']/row['FGM_LEAGUE_CUM']/(2*row['FGM_LEAGUE_CUM']/row['FTM_LEAGUE_CUM']))
        
        def compute_DRB(row):
            return (row['REB_LEAGUE_CUM']-row['OREB_LEAGUE_CUM'])/row['REB_LEAGUE_CUM']
        
        d['FACTOR'] = d.apply(compute_factor, axis = 1)
        d['VOP'] = d.apply(compute_VOP, axis = 1)
        d['DRB_PCT'] = d.apply(compute_DRB, axis = 1)
        d['FTM_PF'] = d.apply(compute_FTM_PF, axis = 1)
        d['FTA_PF'] = d.apply(compute_FTA_PF, axis = 1)
        d['PACE_ADJUST'] = (2*d.PTS_LEAGUE_CUM/d.NUM_TEAMS_CUM)/d.PTS_GAMETOTAL
        d.rename(columns={'AST':'AST_TEAM_DAILY', 'FGM':'FGM_TEAM_DAILY'}, inplace=True)
        return d[['GAME_ID', 'MATCHUP','VOP', 'FACTOR', 'DRB_PCT', 'FTM_PF', 'FTA_PF', 
                  'PACE_ADJUST','AST_TEAM_DAILY', 'FGM_TEAM_DAILY']]
        
    
    def get_players():
        players_json = goldsberry.PlayerList()
        players_df = pd.DataFrame(players_json.players())
        df_players.rename(columns={'DISPLAY_FIRST_LAST':'PLAYER_NAME'}, inplace=True)
        return player_df[['PLAYER_NAME', 'PERSON_ID']]
    
    
    def get_player_game_logs(id_list):
        league_logs = []
        for pid in id_list:
            player_log = goldsberry.player.game_logs(pid)
            league_logs[0:0] = player_log.logs()
            
        game_logs = pd.DataFrame(league_logs)
        return game_logs[['Player_ID', 'DISPLAY_FIRST_LAST', 'Game_ID', 'MATCHUP', 'GAME_DATE',
                            'MIN', 'FG3M', 'AST', 'FGM', 'FTM',
                            'TOV', 'FGA', 'FTA', 'FTM', 'REB', 
                            'OREB', 'STL', 'BLK', 'PF']]
    
    def merge_game_and_player_logs(game_logs, player_logs):
        return player_logs.merge(game_logs, left_on=['Game_ID', 'MATCHUP'], right_on=['GAME_ID', 'MATCHUP'])
    
    def uPER(row):
        def line_1(row):
            return 1/row['MIN']

        def line_2(row):
            return row['FG3M']

        def line_3(row):
            return 2/3*row['AST']

        def line_4(row):
            return (2 - row['FACTOR'] * compute_assisted_FG(row)) * row['FGM']

        def line_5a(row):
            return row['FTM']*.5

        def line_5b(row):
            return 1 + (1 - compute_assisted_FG(row))

        def line_5c(row):
            return 2/3*compute_assisted_FG(row)

        def line_5(row):
            return line_5a(row)*line_5b(row) + line_5c(row)

        def line_6(row):
            return row['VOP']*row['TOV']

        def line_7(row):
            return row['VOP']*row['DRB_PCT']*(row['FGA'] - row['FGM'])

        def line_8(row):
            return row['VOP']*.44*(.44 + (.56*row['DRB_PCT']))*(row['FTA']-row['FTM'])

        def line_9(row):
            return row['VOP']*(1 - row['DRB_PCT'])*(row['REB']-row['OREB'])

        def line_10(row):
            return row['VOP']*row['DRB_PCT']*row['OREB']

        def line_11(row):
            return row['VOP']*row['STL']

        def line_12(row):
            return row['VOP']*row['DRB_PCT']*row['BLK']

        def line_13(row):
            return row['PF']*(row['FTM_PF'] - .44*row['FTA_PF']*row['VOP'])
        
        uPER = (line_2(row) + 
            line_3(row) + 
            line_4(row) + 
            line_5(row) -
            line_6(row) -
            line_7(row) -
            line_8(row) +
            line_9(row) +
            line_10(row)+
            line_11(row)+
            line_12(row)-
            line_13(row))
        return uPER[0]
    
    def compute_PER(df):
        df['uPER'] = df.apply(uPER, axis = 1)
        df['aPER'] = df.uPER*df.PACE_ADJUST
        df['PER'] = 0
        df.loc[df.MIN > 0, 'PER'] = df.loc[df.MIN > 0, 'aPER']/df.loc[df.MIN > 0, 'MIN']
        df_min_filter = df.loc[df.MIN >=8].drop(['PER_CUM_SUM', 'PER_CUM_COUNT'], axis=1)
        df_min_filter = (df_min_filter
            .join(df_min_filter.sort_values('GAME_DATE').groupby('GAME_DATE').PER.sum().cumsum(), on='GAME_DATE', rsuffix='_CUM_SUM')
            .join(df_min_filter.sort_values('GAME_DATE').groupby('GAME_DATE').PER.count().cumsum(), on='GAME_DATE', rsuffix='_CUM_COUNT'))
        
        df_min_filter['AVG_PER'] = df_min_filter['PER_CUM_SUM']/df_min_filter['PER_CUM_COUNT']
        df_min_filter['HollingerPER'] = df_min_filter['PER']*(15/df_min_filter['AVG_PER'])
        return df_min_filter
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                    

