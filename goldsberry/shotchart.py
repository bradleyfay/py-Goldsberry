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
