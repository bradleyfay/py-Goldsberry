class ShotChart:
    def __init__(self,playerid,leagueid='',season='2013-14', seasontype='Regular Season',teamid=0,gameid='',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',position='',gamesegment='',
              period=0,lastngames=0,aheadbehind='',contextmeasure='FGM',clutchtime='',rookieyear=''):
        self._url = "http://stats.nba.com/stats/shotchartdetail?"
        self._api_param = {
             'LeagueID': leagueid,
             'Season' :  season,
             'SeasonType' : seasontype,
             'TeamID' : teamid,
             'PlayerID' : playerid,
             'GameID' : gameid,
             'Outcome' : outcome,
             'Location' : location,
             'Month' : month,
             'SeasonSegment' : seasonsegment,
             'DateFrom' :  datefrom,
             'DateTo' : dateto,
             'OpponentTeamID' : opponentteamid,
             'VsConference' : vsconf,
             'VsDivision' : vsdiv,
             'Position' : position,
             'GameSegment' : gamesegment,
             'Period' :  period,
             'LastNGames' : lastngames,
             'AheadBehind' : aheadbehind,
             'ContextMeasure' : contextmeasure,
             'ClutchTime' : clutchtime,
             'RookieYear' : rookieyear
             }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def shotchart(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']
    def leagueaverage(self):
        return self._x['resultSets'][1]['rowSet'],columns=self._x['resultSets'][1]['headers']

class BoxScore:
    def __init__(self, gameid, rangetype=0, startperiod=0, endperiod=0, startrange=0, endrange=0):
        self._url = "http://stats.nba.com/stats/boxscore?"
        self._api_param = {'GameID':gameid,
                     'RangeType':rangetype,
                     'StartPeriod':startperiod,
                     'EndPeriod':endperiod,
                     'StartRange':startrange,
                     'EndRange':endrange}
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def gamesummary(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']
    def linescore(self):
        return self._x['resultSets'][1]['rowSet'],columns=self._x['resultSets'][1]['headers']
    def seasonseries(self):
        return self._x['resultSets'][2]['rowSet'],columns=self._x['resultSets'][2]['headers']
    def lastmeeting(self):
        return self._x['resultSets'][3]['rowSet'],columns=self._x['resultSets'][3]['headers']
    def playerstats(self):
        return self._x['resultSets'][4]['rowSet'],columns=self._x['resultSets'][4]['headers']
    def teamstats(self):
        return self._x['resultSets'][5]['rowSet'],columns=self._x['resultSets'][5]['headers']
    def otherstats(self):
        return self._x['resultSets'][6]['rowSet'],columns=self._x['resultSets'][6]['headers']
    def officials(self):
        return self._x['resultSets'][7]['rowSet'],columns=self._x['resultSets'][7]['headers']
    def gameinfo(self):
        return self._x['resultSets'][8]['rowSet'],columns=self._x['resultSets'][8]['headers']
    def inactives(self):
        return self._x['resultSets'][9]['rowSet'],columns=self._x['resultSets'][9]['headers']
    def playertrack(self):
        return self._x['resultSets'][11]['rowSet'],columns=self._x['resultSets'][11]['headers']
    def teamtrack(self):
        return self._x['resultSets'][12]['rowSet'],columns=self._x['resultSets'][12]['headers']

class GameLog:
    def __init__(self, playerid, season='2013-14',seasontype='Regular Season', leagueid=''):
        self._url = "http://stats.nba.com/stats/playergamelog?"
        self._api_param = {'PlayerID':playerid,
                          'SeasonType': seasontype,
                          'Season': season,
                          'LeagueID': leagueid
                          }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def log(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']

class PlayByPlay:
    def __init__(self, gameid, startperiod=0, endperiod=0):
        self._url = "http://stats.nba.com/stats/playbyplay?"
        self._api_param = {'GameID':gameid,
                          'StartPeriod': startperiod,
                          'EndPeriod':endperiod,
                          }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def pbp(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']

class Lineups:
    def __init__(self, groupquantity=2, permode='Totals', seasontype='Regular Season', plusminus='Y',
                 paceadjust='Y', rank='Y', season='2013-14', outcome='', location='', month=0,
                 seasonsegment='', datefrom='', dateto='', opponentteamid=0, vsconf='', vsdiv='',
                 gamesegment='', period=0, lastngames=0, measuretype='Base'):
        self._url = "http://stats.nba.com/stats/leaguedashlineups?"
        self._api_param = {'GroupQuantity': groupquantity,
                          'PerMode':permode,
                          'SeasonType':seasontype,
                          'PlusMinus':plusminus,
                          'PaceAdjust':paceadjust,
                          'Rank':rank,
                          'Season':season,
                          'Outcome':outcome,
                          'Location':location,
                          'Month':month,
                          'SeasonSegment':seasonsegment,
                          'DateFrom':datefrom,
                          'DateTo':dateto,
                          'OpponentTeamID':opponentteamid,
                          'VsConference':vsconf,
                          'VsDivision':vsdiv,
                          'GameSegment':gamesegment,
                          'Period':period,
                          'LastNGames':lastngames,
                          'MeasureType':measuretype
                          }
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def line(self):
        return self._x['resultSets'][0]['rowSet'],columns=self._x['resultSets'][0]['headers']

class LeagueLeaders:
    def __init__(self, leagueid='00', permode='Per48',statcat='PTS',season='2013-14',seasontype='Regular Season',scope='S'):
        self._url = "http://stats.nba.com/stats/leagueleaders?"
        self._api_param = {'LeagueID':leagueid,
                          'PerMode':permode,
                          'StatCategory':statcat,
                          'Season':season,
                          'SeasonType':seasontype,
                          'Scope':scope,
             }
        self._season = season
        self._x = requests.get(self._url, params=self._api_param)
        self._x = self._x.json()
    def line(self):
        return self._x['resultSet']['rowSet'],columns=self._x['resultSet']['headers']
    def players(self):
        if self._season == 'All Time':
            return self.line().PLAYER_NAME.values,index=self.line().PLAYER_ID
        else:
            return self.line().PLAYER.values,index=self.line().PLAYER_ID
