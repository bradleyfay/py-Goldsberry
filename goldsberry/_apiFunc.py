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
    measuretypes = {1:"Base", 2:"Advanced", 3:"Misc", 4:"Four Factors", 5:"Scoring", 6:"Opponent", 7:"Usage"}
    try:
        return measuretypes[x]
    except:
        raise Exception("Please enter a number from 1 to 7")

#The field Scope must match the regular expression '^(RS)|(S)|(Rookies)$'

#The field PerMode must match the regular expression '^(Totals)|(PerGame)|(Per48)$'.