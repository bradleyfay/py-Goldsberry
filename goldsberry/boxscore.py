class Summary:
    """
    """
    def __init__(self, gameid):
        self._url = "http://stats.nba.com/stats/boxscoresummaryv2?"
        self._api_param = {'GameID':gameid}
        self._pull = requests.get(self._url, params=self._api_param)
    def GameSummary(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def OtherStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Officials(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def Inactives(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def GameInfo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LineScore(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def LastMeeting(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def SeasonSeries(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def AvailableVideo(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Traditional:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoretraditionalv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayerStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Advanced:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoreadvancedv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayerStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamStats(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Miscellaneous:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoremiscv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayersMisc(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamMisc(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Scoring:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscorescoringv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayersScoring(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamScoring(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class FourFactors:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscorefourfactorsv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayersFourFactors(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamFourFactors(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

class Usage:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoreusagev2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayersUsage(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamUsage(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
        
class Tracking:
    """
    """
    def __init__(self, gameid, season='2014-15', seasontype='Regular Season',
                 startperiod=1, endperiod=10, startrange=0, endrange=28800,
                 rangetype=2):
        self._url = "http://stats.nba.com/stats/boxscoreplayertrackv2?"
        self._api_param = {'EndPeriod':endperiod,
                           'EndRange':endrange,
                           'GameID':gameid,
                           'RangeType':rangetype,
                           'Season':season,
                           'SeasonType':seasontype,
                           'StartPeriod':startperiod,
                           'StartRange':startrange
                           }
        self._pull = requests.get(self._url, params=self._api_param)
    def PlayersTrack(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
    def TeamTrack(self):
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]