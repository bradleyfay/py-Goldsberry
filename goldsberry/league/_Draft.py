import requests as _requests
from goldsberry._apiFunc import *

class Anthro:
    def __init__(self, season='2014', league='NBA'):
        self._url = "http://stats.nba.com/stats/draftcombineplayeranthro?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonYear':_nbaSeason(season),
        }
        self._pull = _requests.get(self._url, params=self._api_param)
    def data(self):
        """Returns list of dicts with anthropometric data

        For best results, wrap this in pandas.DataFrame()

        Return values:
            PLAYER_ID -
            TEMP_PLAYER_ID -
            PLAYER_NAME -
            FIRST_NAME -
            LAST_NAME -
            POSITION - Projected Position of the Prospect
            BODY_FAT_PCT - Body Fat Percentage
            HAND_LENGTH - Length of the Prospect's hand
                in inches. The measurement is taken from the bottom of the
                player's palm to the tip of his middle finger.
            HAND_WIDTH - Width of the Prospects hand in
                inches. The measurement is taken from the player's outstretched
                hand from the tip of the thumb to tip of the pinky finger.
            HEIGHT_WO_SHOES_FT_IN - Height of the player
                without wearing shoes.
            HEIGHT_WO_SHOES -
            HEIGHT_W_SHOES_FT_IN - Height of the player
                while in shoes.
            HEIGHT_W_SHOES -
            STANDING_REACH_FT_IN - The reach in inches
                of the player while standing still. The player reaches straight
                up to his highest point.
            STANDING_REACH -
            WEIGHT - The weight of the player in pounds.
            WINGSPAN_FT_IN - The player stretches his arms
                horizontally and a measure is made from the tip of his left hand
                to the tip of his right hand.
            WINGSPAN -
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class Agility:
    def __init__(self, season='2014', league='NBA'):
        self._url = "http://stats.nba.com/stats/draftcombinedrillresults?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonYear':_nbaSeason(season)
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def data(self):
        """Returns list of dicts with anthropometric data

        For best results, wrap this in pandas.DataFrame()

        Return values:
            PLAYER_ID --
            TEMP_PLAYER_ID --
            PLAYER_NAME --
            FIRST_NAME --
            LAST_NAME --
            POSITION -- Projected Position of the Prospect
            LANE_AGILITY_TIME -- Lane Agility (seconds) - This drill measures
                lateral quickness and the player's agility.
            MODIFIED_LANE_AGILITY_TIME -- Shuttle Run (seconds) - This measures a
                player's agility and ability to change directions.
            THREE_QUARTER_SPRINT -- Three Quarter Sprint (seconds) - A player is
                timed in a sprint from the baseline to 3/4th the length of the
                court.
            STANDING_VERTICAL_LEAP -- Standing (inches) - The vertical leap of a
                player with no running start.
            MAX_VERTICAL_LEAP -- Max Vertical Leap (inches) - The vertical leap
                of a player with a few steps to start and gather his leap.
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class NonStationaryShooting:
    def __init__(self, season='2014', league='NBA'):
        self._url = "http://stats.nba.com/stats/draftcombinenonstationaryshooting?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonYear':_nbaSeason(season)
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def data(self):
        """Returns list of dicts with anthropometric data

        For best results, wrap this in pandas.DataFrame()

        Return values:
            PLAYER_ID --
            TEMP_PLAYER_ID --
            PLAYER_NAME --
            FIRST_NAME --
            LAST_NAME --
            POSITION -- Projected Position of the Prospect
            OFF_DRIB_COLLEGE_BREAK_LEFT_MADE --
            OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT --
            OFF_DRIB_COLLEGE_BREAK_LEFT_PCT -- Off Dribble College Break Left - A player takes six
                shots coming off the dribble from the left break area of the court. The shot is from
                about the distance of a college three pointer (20 ft. 9 in.).
            OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE --
            OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT --
            OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT -- Off Dribble College Break Right - A player takes six
                shots coming off the dribble from the right break area of the court. The shot is from
                about the distance of a college three pointer (20 ft. 9 in.).
            OFF_DRIB_COLLEGE_TOP_KEY_MADE --
            OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT --
            OFF_DRIB_COLLEGE_TOP_KEY_PCT -- Off Dribble College Top Key - A player takes six shots
                coming off the dribble from the top of the key. The shot is from about the distance
                of a college three pointer (20 ft. 9 in.).
            OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE --
            OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT --
            OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT -- Off Dribble Fifteen Break Left - A player takes six
                shots coming off the dribble from 15 feet away from the basket on the left break
                area of the court.
            OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE --
            OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT --
            OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT -- Off Dribble Fifteen Break Right - A player takes six
            shots coming off the dribble from 15 feet away from the basket on the right break area
                of the court.
            OFF_DRIB_FIFTEEN_TOP_KEY_MADE --
            OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT --
            OFF_DRIB_FIFTEEN_TOP_KEY_PCT -- Off Dribble Fifteen Top Key - A player takes six shots
                coming off the dribble from 15 feet out at the top of the key.
            ON_MOVE_COLLEGE_MADE --
            ON_MOVE_COLLEGE_ATTEMPT --
            ON_MOVE_COLLEGE_PCT -- On the Move College - 35 seconds to attempt as many shots as time
                allows from college 3-pt range (20 ft. 9 in.) while moving between spots (corners
                and elbows from both sides).
            ON_MOVE_FIFTEEN_MADE --
            ON_MOVE_FIFTEEN_ATTEMPT --
            ON_MOVE_FIFTEEN_PCT -- On the Move Fifteen - 35 seconds to attempt as many shots as time
                allows from 15 feet while moving between spots (corners and elbows from both sides).
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class SpotUpShooting:
    def __init__(self, season='2014', league='NBA'):
        self._url = "http://stats.nba.com/stats/draftcombinespotshooting?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonYear':_nbaSeason(season)
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def data(self):
        """Returns list of dicts with anthropometric data

        For best results, wrap this in pandas.DataFrame()

        Return values:
            PLAYER_ID --
            TEMP_PLAYER_ID --
            PLAYER_NAME --
            FIRST_NAME --
            LAST_NAME --
            POSITION -- Projected Position of the Prospect
            NBA_BREAK_LEFT_MADE --
            NBA_BREAK_LEFT_ATTEMPT --
            NBA_BREAK_LEFT_PCT -- NBA Break Left - A player takes five shots
                from the left break area of the court. The shot is from the
                distance of an NBA three pointer (23 ft. 9 in.)
            NBA_BREAK_RIGHT_MADE --
            NBA_BREAK_RIGHT_ATTEMPT --
            NBA_BREAK_RIGHT_PCT -- NBA Break Right - A player takes five shots
                from the right break area of the court. The shot is from the
                distance of an NBA three pointer (23 ft. 9 in.)
            NBA_CORNER_LEFT_MADE --
            NBA_CORNER_LEFT_ATTEMPT --
            NBA_CORNER_LEFT_PCT -- NBA Corner Left - A player takes five shots
                from the left corner area of the court. The shot is from the
                distance of an NBA three pointer (23 ft. 9 in.)
            NBA_CORNER_RIGHT_MADE --
            NBA_CORNER_RIGHT_ATTEMPT --
            NBA_CORNER_RIGHT_PCT -- NBA Corner Right - A player takes five
                shots from the right corner area of the court. The shot is from
                the distance of an NBA three pointer (23 ft. 9 in.)
            NBA_TOP_KEY_MADE --
            NBA_TOP_KEY_ATTEMPT --
            NBA_TOP_KEY_PCT -- NBA Top Key - A player takes five shots from top
                of the key. The shot is from the distance of an NBA three
                pointer (23 ft. 9 in.)
            COLLEGE_BREAK_LEFT_MADE --
            COLLEGE_BREAK_LEFT_ATTEMPT --
            COLLEGE_BREAK_LEFT_PCT -- College Break Left - A player takes five
                shots from the left break area of the court. The shot is from
                the distance of a college three pointer (20 ft. 9 in.).
            COLLEGE_BREAK_RIGHT_MADE --
            COLLEGE_BREAK_RIGHT_ATTEMPT --
            COLLEGE_BREAK_RIGHT_PCT -- College Break Right - A player takes
                five shots from the right break area of the court. The shot is
                from the distance of a college three pointer (20 ft. 9 in.).
            COLLEGE_CORNER_LEFT_MADE --
            COLLEGE_CORNER_LEFT_ATTEMPT --
            COLLEGE_CORNER_LEFT_PCT -- College Corner Left - A player takes
                five shots from the left corner area of the court. The shot is
                from the distance of a college three pointer (20 ft. 9 in.).
            COLLEGE_CORNER_RIGHT_MADE --
            COLLEGE_CORNER_RIGHT_ATTEMPT --
            COLLEGE_CORNER_RIGHT_PCT -- College Corner Right - A player takes
                five shots from the right corner area of the court. The shot is
                from the distance of a college three pointer (20 ft. 9 in.).
            COLLEGE_TOP_KEY_MADE --
            COLLEGE_TOP_KEY_ATTEMPT --
            COLLEGE_TOP_KEY_PCT -- College Top Key - A player takes five shots
                from the top of the key. The shot is from the distance of a
                college three pointer (20 ft. 9 in.).
            FIFTEEN_BREAK_LEFT_MADE --
            FIFTEEN_BREAK_LEFT_ATTEMPT --
            FIFTEEN_BREAK_LEFT_PCT -- Fifteen Break Left - A player takes five
                shots from the left break and 15 feet away from the basket.
            FIFTEEN_BREAK_RIGHT_MADE --
            FIFTEEN_BREAK_RIGHT_ATTEMPT --
            FIFTEEN_BREAK_RIGHT_PCT -- Fifteen Break Right - A player takes
                five shots from the right break and 15 feet away from the
                basket.
            FIFTEEN_CORNER_LEFT_MADE --
            FIFTEEN_CORNER_LEFT_ATTEMPT --
            FIFTEEN_CORNER_LEFT_PCT -- Fifteen Corner Left - A player takes
                five shots from the left baseline and 15 feet away from the
                basket.
            FIFTEEN_CORNER_RIGHT_MADE --
            FIFTEEN_CORNER_RIGHT_ATTEMPT --
            FIFTEEN_CORNER_RIGHT_PCT -- Fifteen Corner Right - A player takes
                five shots from the right baseline and 15 feet away from the
                basket.
            FIFTEEN_TOP_KEY_MADE --
            FIFTEEN_TOP_KEY_ATTEMPT --
            FIFTEEN_TOP_KEY_PCT -- Fifteen Top Key - A player takes five shots
                from the top of the key and 15 feet away from the basket.
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
class Combine:
    def __init__(self, season='2014', league='NBA'):
        self._url = "http://stats.nba.com/stats/draftcombinestats?"
        self._api_param = {'LeagueID':_nbaLeague(league),
                           'SeasonYear':_nbaSeason(season)
        }
        self._pull = requests.get(self._url, params=self._api_param)
    def data(self):
        """Returns list of dicts with anthropometric data

        For best results, wrap this in pandas.DataFrame()

        Return values:
            SEASON --
            PLAYER_ID -- 
            FIRST_NAME --
            LAST_NAME --
            PLAYER_NAME --
            POSITION --
            HEIGHT_WO_SHOES --
            HEIGHT_WO_SHOES_FT_IN --
            HEIGHT_W_SHOES --
            HEIGHT_W_SHOES_FT_IN --
            WEIGHT --
            WINGSPAN --
            WINGSPAN_FT_IN --
            STANDING_REACH --
            STANDING_REACH_FT_IN --
            BODY_FAT_PCT --
            HAND_LENGTH --
            HAND_WIDTH --
            STANDING_VERTICAL_LEAP --
            MAX_VERTICAL_LEAP --
            LANE_AGILITY_TIME --
            MODIFIED_LANE_AGILITY_TIME --
            THREE_QUARTER_SPRINT --
            SPOT_FIFTEEN_CORNER_LEFT --
            SPOT_FIFTEEN_BREAK_LEFT --
            SPOT_FIFTEEN_TOP_KEY --
            SPOT_FIFTEEN_BREAK_RIGHT --
            SPOT_FIFTEEN_CORNER_RIGHT --
            SPOT_COLLEGE_CORNER_LEFT --
            SPOT_COLLEGE_BREAK_LEFT --
            SPOT_COLLEGE_TOP_KEY --
            SPOT_COLLEGE_BREAK_RIGHT --
            SPOT_COLLEGE_CORNER_RIGHT --
            SPOT_NBA_CORNER_LEFT --
            SPOT_NBA_BREAK_LEFT --
            SPOT_NBA_TOP_KEY --
            SPOT_NBA_BREAK_RIGHT --
            SPOT_NBA_CORNER_RIGHT --
            OFF_DRIB_FIFTEEN_BREAK_LEFT --
            OFF_DRIB_FIFTEEN_TOP_KEY --
            OFF_DRIB_FIFTEEN_BREAK_RIGHT --
            OFF_DRIB_COLLEGE_BREAK_LEFT --
            OFF_DRIB_COLLEGE_TOP_KEY --
            OFF_DRIB_COLLEGE_BREAK_RIGHT --
            ON_MOVE_FIFTEEN --
            ON_MOVE_COLLEGE --
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]

__all__ = ['Anthro', 'Agility', 'NonStationaryShooting', 'SpotUpShooting', 'Combine']