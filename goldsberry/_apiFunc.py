def _nbaLeague(x):
    leagues = {"NBA":"00", "WNBA":"10", "NBADL":"20"}
    try:
        return leagues[x]
    except:
        raise Exception("Please use one of the following values for League: 'NBA', 'WNBA', 'NBADL'")

def _nbaSeason(x):
    if str(x) == "1999":
        return "1999-00"
    elif len(str(x)) == 4:
        try:
            return "-".join([str(x),str(int(x) % 100 + 1)])
        except ValueError: 
            raise Exception("Enter the four digit year for the first half of the desired season")
    else: raise Exception("Enter the four digit year for the first half of the desired season")

def _seasonID(x):
    if len(str(x)) == 4:
        try:
            return "".join(["2",str(x)])
        except ValueError:
            raise Exception("Enter the four digit year for the first half of the desired season")
    else: raise Exception("Enter the four digit year for the first half of the desired season")

# measuretype = "(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)"

def _measureType(x):
    measure = {1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"}
    try:
        return measure[x]
    except:
        raise EException("Please enter a number between 1 and "+str(len(measure)))

def _Scope(x):
    measure = {1:'',2:"RS",3:"S",4:"Rookies"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _PerMode(x):
    measure = {1:"Totals",2:"PerGame",3:"Per48"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _AheadBehind(x):
    measure = {1:"Ahead or Behind",2:"Behind or Tied",3:"Ahead or Tied"}
    try:
        return measure[x]
    except:
        raise Exception("Please enter a number between 1 and "+str(len(measure)))
def _ClutchTime(x):
    measure = {1:"Last 5 Minutes",2:"Last 4 Minutes",3:"Last 3 Minutes",3:"Last 2 Minutes",4:"Last 1 Minute",5:"Last 30 Seconds",6:"Last 10 Seconds"}
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
def _PerMode(x):
    measure = {1:"Totals",2:"PerGame",3:"MinutesPer",4:"Per48",5:"Per40",6:"Per36",7:"PerMinute", 8:"PerPossession", 9:"PerPlay", 10:"Per100Possessions", 11:"Per100Plays"}
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

# BoxScore -- RangeType must be between 0 and 2.

# All -- DateString validation