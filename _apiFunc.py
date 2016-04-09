import dateutil.parser


def _nba_league(x):
    """Takes in initials of league and returns numeric API Code

    Input Values: "NBA", "WNBA", or "NBADL"

    Used in: _Draft.Anthro(), _Draft.Agility(), _Draft.NonStationaryShooting(), 
    _Draft.SpotUpShooting(), _Draft.Combine()

    """
    leagues = {"NBA": "00", "WNBA": "10", "NBADL": "20"}
    try:
        return leagues[x.upper()]
    except:
        raise ValueError("Please use one of the following values for League: 'NBA', 'WNBA', 'NBADL'")


def _nba_season(x):
    """Takes in 4-digit year for first half of season and returns API appropriate formatted code

    Input Values: YYYY 

    Used in: _Draft.Anthro(), _Draft.Agility(), _Draft.NonStationaryShooting(), 
    _Draft.SpotUpShooting(), _Draft.Combine()

    """
    if len(str(x)) == 4:
        try:
            return '{0}-{1}'.format(x, str(int(x) % 100 + 1)[-2:].zfill(2))
        except ValueError:
            raise ValueError("Enter the four digit year for the first half of the desired season")
    else:
        raise ValueError("Enter the four digit year for the first half of the desired season")


def _season_id(x):
    """takes in 4-digit years and returns API formatted seasonID

    Input Values: YYYY 

    Used in:

    """
    if len(str(x)) == 4:
        try:
            return "".join(["2", str(x)])
        except ValueError:
            raise ValueError("Enter the four digit year for the first half of the desired season")
    else:
        raise ValueError("Enter the four digit year for the first half of the desired season")


def _measure_type(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"

    Used in:

    """
    measure = {1: "Base", 2: "Advanced", 3: "Misc", 4: "Four Factors", 5: "Scoring", 6: "Opponent", 7: "Usage"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _scope(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"", 2:"RS", 3:"S", 4:"Rookies"
    Used in:

    """
    measure = {1: '', 2: "RS", 3: "S", 4: "Rookies"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _per_mode_small_48(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Totals", 2:"PerGame", 3:"Per48"

    Used in:

    """
    measure = {1: "Totals", 2: "PerGame", 3: "Per48"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _per_mode_small_36(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Totals", 2:"PerGame", 3:"Per36"

    Used in:

    """
    measure = {1: "Totals", 2: "PerGame", 3: "Per36"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _per_mode_mini(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Totals", 2:"PerGame"

    Used in:

    """
    measure = {1: "Totals", 2: "PerGame"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _per_mode_large(x):
    measure = {1: "Totals", 2: "PerGame", 3: "MinutesPer", 4: "Per48", 5: "Per40",
               6: "Per36", 7: "PerMinute", 8: "PerPossession", 9: "PerPlay",
               10: "Per100Possessions", 11: "Per100Plays"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _ahead_behind(x):
    measure = {1: "Ahead or Behind", 2: "Behind or Tied", 3: "Ahead or Tied"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _clutch_time(x):
    measure = {1: "Last 5 Minutes", 2: "Last 4 Minutes", 3: "Last 3 Minutes",
               4: "Last 2 Minutes", 5: "Last 1 Minute", 6: "Last 30 Seconds",
               7: "Last 10 Seconds", 8: ''}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _game_scope(x):
    measure = {1: '', 2: "Yesterday", 3: "Last 10"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _player_experience(x):
    measure = {1: '', 2: "Rookie", 3: "Sophomore", 4: "Veteran"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _player_position(x):
    measure = {1: '', 2: "F", 3: "C", 4: "G", 5: "C-F", 6: "F-C", 7: "F-G", 8: "G-F"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _starter_bench(x):
    measure = {1: '', 2: "Starters", 3: "Bench"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _plus_minus(x):
    measure = {2: "Y", 1: "N"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _pace_adjust(x):
    measure = {2: "Y", 1: "N"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _rank(x):
    measure = {2: "Y", 1: "N"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _season_type(x):
    measure = {1: "Regular Season", 2: "Playoffs", 3: "All Star", 4: "Pre Season"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _outcome(x):
    measure = {1: '', 2: "W", 3: "L"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _location(x):
    measure = {1: '', 2: "Home", 3: "Road"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _season_segment(x):
    measure = {1: '', 2: "Post All-Star", 3: "Pre All-Star"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _vs_conference(x):
    measure = {1: '', 2: "East", 3: "West"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _vs_division(x):
    measure = {1: '', 2: "Atlantic", 3: "Central", 4: "Northwest", 5: "Pacific", 6: "Southeast", 7: "Southwest",
               8: "East", 9: "West"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _game_segment(x):
    measure = {1: '', 2: "First Half", 3: "Second Half", 4: "Overtime"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _distance_range(x):
    measure = {1: "5ft Range", 2: "8ft Range", 3: "By Zone"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _valid_date(date_text):
    if date_text == '':
        return date_text
    else:
        try:
            date = dateutil.parser.parse(date_text)
            return str(date.date())
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD or MM-DD-YYYY")


def _context_measure(x):
    measure = {1: 'FGM', 2: 'FGA', 3: "FG_PCT", 4: 'FG3M', 5: 'FG3A', 6: 'FG3_PCT', 8: 'PF',
               9: 'EFG_PCT', 10: 'TS_PCT', 11: 'PTS_FB', 12: 'PTS_OFF_TOV',
               13: 'PTS_2ND_CHANCE', 14: 'PF'}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _position(x):
    measure = {1: '', 2: 'Guard', 3: 'Center', 4: 'Forward'}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


def _stat_category(x):
    measure = {1: "MIN", 2: "FGM", 3: "FGA", 4: "FG_PCT", 5: "FG3M", 6: "FG3A", 7: "FG3_PCT",
               8: "FTM", 9: "FTA", 10: "FT_PCT", 11: "OREB", 12: "DREB", 13: "REB", 14: "AST", 15: "STL",
               16: "BLK", 17: "TOV", 18: "PTS", 19: "EFF"}
    try:
        return measure[x]
    except:
        raise ValueError("Please enter a number between 1 and " + str(len(measure)))


# BoxScore -- RangeType must be between 0 and 2.
__all__ = ['_nba_league', '_nba_season', '_season_id', '_measure_type',
           '_scope', '_per_mode_small_48', '_per_mode_small_36', '_per_mode_mini',
           '_per_mode_large', '_ahead_behind', '_clutch_time', '_game_scope',
           '_player_experience', '_player_position', '_starter_bench',
           '_plus_minus', '_pace_adjust', '_rank', '_season_type', '_SeasonType4',
           '_outcome', '_location', '_season_segment', '_vs_conference',
           '_vs_division', '_game_segment', '_distance_range', '_valid_date',
           '_context_measure', '_position', '_stat_category']
