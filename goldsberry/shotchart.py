class ShotChart:
    def __init__(self,playerid,leagueid='',season='2013-14', seasontype='Regular Season',teamid=0,gameid='',outcome='',location='',
              month=0,seasonsegment='',datefrom='',dateto='',opponentteamid=0,vsconf='',vsdiv='',position='',
              period=0,lastngames=0,aheadbehind='',contextmeasure='FGM',clutchtime='',rookieyear='', contextfilter='',
              startperiod='1',endperiod='10',startrange='0', endrange='28800', gamesegment='', rangetype='2'):
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
             'RookieYear' : rookieyear,
             'ContextFilter':contextfilter,
             'StartPeriod':startperiod,
             'EndPeriod':endperiod,
             'StartRange':startrange,
             'EndRange':endrange,
             'RangeType':rangetype,
             }
        self._pull = requests.get(self._url, params=self._api_param)
    def shotchart(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def leagueaverage(self):
        _headers = self._pull.json()['resultSets'][1]['headers']
        _values = self._pull.json()['resultSets'][1]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]