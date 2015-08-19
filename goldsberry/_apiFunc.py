from dateutil.parser import parse as _parse

def _nbaLeague(x):
    """Takes in initials of league and returns numeric API Code

    Input Values: "NBA", "WNBA", or "NBADL"

    Used in: _Draft.Anthro(), _Draft.Agility(), _Draft.NonStationaryShooting(), 
    _Draft.SpotUpShooting(), _Draft.Combine()

    """
    leagues = {"NBA":"00", "WNBA":"10", "NBADL":"20"}
    try:
        return leagues[x.upper()]
    except:
        raise Exception("Please use one of the following values for League: 'NBA', 'WNBA', 'NBADL'")
def _nbaSeason(x):
    """Takes in 4-digit year for first half of season and returns API appropriate formatted code

    Input Values: YYYY 

    Used in: _Draft.Anthro(), _Draft.Agility(), _Draft.NonStationaryShooting(), 
    _Draft.SpotUpShooting(), _Draft.Combine()

    """
    if str(x) == "1999":
        return "1999-00"
    elif len(str(x)) == 4:
        try:
            return "-".join([str(x),str(int(x) % 100 + 1)])
        except ValueError: 
            raise Exception("Enter the four digit year for the first half of the desired season")
    else: raise Exception("Enter the four digit year for the first half of the desired season")
def _seasonID(x):
    """takes in 4-digit years and returns API formatted seasonID

    Input Values: YYYY 

    Used in:

    """
    if len(str(x)) == 4:
        try:
            return "".join(["2",str(x)])
        except ValueError:
            raise Exception("Enter the four digit year for the first half of the desired season")
    else: raise Exception("Enter the four digit year for the first half of the desired season")
def _measureType(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"

    Used in:

    """
    measure = {1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _Scope(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"", 2:"RS", 3:"S", 4:"Rookies"
    Used in:

    """
    measure = {1:'',2:"RS",3:"S",4:"Rookies"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PerModeSmall48(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"

    Used in:

    """
    measure = {1:"Totals",2:"PerGame",3:"Per48"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PerModeSmall36(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"

    Used in:

    """
    measure = {1:"Totals",2:"PerGame",3:"Per36"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PerModeMini(x):
    """Takes Numeric Code and returns String API code

    Input Values: 1:"Totals", 2:"PerGame"

    Used in:

    """
    measure = {1:"Totals",2:"PerGame"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PerModeLarge(x):
    measure = {1:"Totals",2:"PerGame",3:"MinutesPer",4:"Per48",5:"Per40",
               6:"Per36",7:"PerMinute", 8:"PerPossession", 9:"PerPlay", 
               10:"Per100Possessions", 11:"Per100Plays"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _AheadBehind(x):
    measure = {1:"Ahead or Behind",2:"Behind or Tied",3:"Ahead or Tied"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _ClutchTime(x):
    measure = {1:"Last 5 Minutes",2:"Last 4 Minutes",3:"Last 3 Minutes",
               4:"Last 2 Minutes",5:"Last 1 Minute",6:"Last 30 Seconds",
               7:"Last 10 Seconds", 8:''}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _GameScope(x):
    measure = {1:'', 2:"Yesterday", 3:"Last 10"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PlayerExperience(x):
    measure = {1:'', 2:"Rookie",3:"Sophomore",4:"Veteran"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PlayerPosition(x):
    measure = {1:'',2:"F", 3:"C", 4:"G", 5:"C-F", 6:"F-C", 7:"F-G", 8:"G-F"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _StarterBench(x):
    measure = {1:'', 2:"Starters", 3:"Bench"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PlusMinus(x):
    measure = {2:"Y",1:"N"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PaceAdjust(x):
    measure = {2:"Y",1:"N"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _Rank(x):
    measure = {2:"Y",1:"N"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _SeasonType(x):
    measure = {1:"Regular Season",2:"Playoffs",3:"All Star"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _SeasonType4(x):
    measure = {1:"Regular Season",2:"Playoffs",3:"All Star",4:"Pre Season"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _Outcome(x):
    measure = {1:'',2:"W",3:"L"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _Location(x):
    measure = {1:'', 2:"Home",3:"Road"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _SeasonSegment(x):
    measure = {1:'', 2:"Post All-Star",3:"Pre All-Star"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _VsConference(x):
    measure = {1:'',2:"East",3:"West"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _VsDivision(x):
    measure = {1:'',2:"Atlantic",3:"Central",4:"Northwest",5:"Pacific",6:"Southeast",7:"Southwest",8:"East",9:"West"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _GameSegment(x):
    measure = {1:'',2:"First Half",3:"Overtime",2:"Second Half"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _DistanceRange(x):
    measure = {1:"5ft Range",2:"8ft Range",3:"By Zone"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _valiDate(date_text):
    if not date_text == '':
        try:
            date = _parse(date_text)
            return str(date.date())
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD or MM-DD-YYYY")
    else: pass
def _ContextMeasure(x):
    measure = { 1:'FGM',2:'FGA',3:"FG_PCT",4:'FG3M',5:'FG3A',6:'FG3_PCT',8:'PF',
                9:'EFG_PCT',10:'TS_PCT',11:'PTS_FB',12:'PTS_OFF_TOV',
                13:'PTS_2ND_CHANCE',14:'PF'}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _Position(x):
    measure = {1:'',2:'Guard',3:'Center',4:'Forward'}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _StatCategory(x):
    measure = {1:"MIN",2:"FGM",3:"FGA",4:"FG_PCT",5:"FG3M",6:"FG3A",7:"FG3_PCT",
    8:"FTM",9:"FTA",10:"FT_PCT",11:"OREB",12:"DREB",13:"REB",14:"AST",15:"STL",
    16:"BLK",17:"TOV",18:"PTS",19:"EFF"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
# BoxScore -- RangeType must be between 0 and 2.
__all__ = ['_Position', '_ContextMeasure', '_valiDate', '_DistanceRange',
           '_GameSegment', '_VsDivision', '_VsConference', '_SeasonSegment'
           '_Location', '_Outcome', '_SeasonType', '_Rank', '_PaceAdjust',
           '_PlusMinus', '_PerModeSmall48', '_StarterBench', '_PlayerPosition',
           '_PlayerExperience', '_GameScope', '_ClutchTime', '_AheadBehind',
           '_PerModeLarge', '_Scope', '_measureType', '_seasonID', '_nbaSeason',
           '_nbaLeague','_PerModeSmall36', '_PerModeMini']