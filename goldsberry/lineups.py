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
