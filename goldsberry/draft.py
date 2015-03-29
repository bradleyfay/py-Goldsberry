class Anthro:
    """Retrieves anthropometric data collected during draft combine

    Keyword arguments:
    Season -- What season the data returned is associated with.
        Default value is 2014-15
        Takes values going back to 2000-01
    LeagueID -- Unique ID Associated with various leagues owned by NBA
        Default value = 00 (NBA)
        Possible values = 00 (NBA), 10(NBADL), 20(WNBA) <- Double Check These
    """

    def __init__(self, Season='2014-15', LeagueID='00'):
        self._url = "http://stats.nba.com/stats/draftcombineplayeranthro?"
        self._api_param = {'LeagueID':LeagueID,
                           'SeasonYear':Season,
        }
        self._pull = requests.get(self._url, params=self._api_param)
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
    """Retrieves speed and agility data collected during draft combine

    Keyword arguments:
    Season -- What season the data returned is associated with.
        Default value is 2014-15
        Takes values going back to 2000-01
    LeagueID -- Unique ID Associated with various leagues owned by NBA
        Default value = 00 (NBA)
        Possible values = 00 (NBA), 10(NBADL), 20(WNBA) <- Double Check These
    """

    def __init__(self, Season='2014-15', LeagueID='00'):
        self._url = "http://stats.nba.com/stats/draftcombinedrillresults?"
        self._api_param = {'LeagueID':LeagueID,
                           'SeasonYear':Season,
        }
        self._pull = requests.get(self._url, params=self._api_param)
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
            LANE_AGILITY_TIME - Lane Agility (seconds) - This drill measures
                lateral quickness and the player's agility.
            MODIFIED_LANE_AGILITY_TIME - Shuttle Run (seconds) - This measures a
                player's agility and ability to change directions.
            THREE_QUARTER_SPRINT - Three Quarter Sprint (seconds) - A player is
                timed in a sprint from the baseline to 3/4th the length of the
                court.
            STANDING_VERTICAL_LEAP - Standing (inches) - The vertical leap of a
                player with no running start.
            MAX_VERTICAL_LEAP - Max Vertical Leap (inches) - The vertical leap
                of a player with a few steps to start and gather his leap.
        """
        _headers = self._pull.json()['resultSets'][0]['headers']
        _values = self._pull.json()['resultSets'][0]['rowSet']
        return [dict(zip(_headers, value)) for value in _values]
