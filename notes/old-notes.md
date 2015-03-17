#NBAStats Python Package Updates

The NBA has updated their database to provide an increased amount of information. In doing so, the original packages for NBA Stats need to be updated to reflect the updates to the stats.nba.com website.  Here is a list of updates that need to be made.

##`BoxScore` Module
I need to add the loops for the following adjustments to the `_url` field 
- [ ] Change `boxscore` to `boxscoreusage`
- [ ] Add loop for `boxscoreadvancedv2`
- [ ] Add loop for `boxscorefourfactorsv2`
- [ ] Add loop for `boxscoremiscv2`
- [ ] Add loop for `boxscorescoringv2`
- [ ] Add loop for either `playbyplay` or `playbyplayv2` These dataframes need to be inspected for differences with the richer dataframe completed
- [ ] Add Module for SportVu Data
	- [ ] Shooting Dashboard `http://stats.nba.com/stats/playerdashptshots?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=`
	- [ ] Rebounding Dashboard ```http://stats.nba.com/stats/playerdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=```
	- [ ] Passing Dashboard `http://stats.nba.com/stats/playerdashptpass?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=`
	- [ ] Defensive Dashboard `http://stats.nba.com/stats/playerdashptshotdefend?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=PerGame&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=`
	- [ ] Player Shot Logs `http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=`
	- [ ] Player Rebound Logs `http://stats.nba.com/stats/playerdashptreboundlogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=201939&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=`
- [ ] Transition Stats `http://stats.nba.com/js/data/playtype/player_Transition.js`
- [ ] [Catch and Shoot data](http://stats.nba.com/tracking/#!/player/catchshoot/) `http://stats.nba.com/js/data/sportvu/2014/catchShootData.json` There is quite a bit more data available here. It will just take some time to search and code it up.
- [ ] Lineup Data `http://stats.nba.com/stats/teamdashlineups?DateFrom=&DateTo=&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612753&VsConference=&VsDivision=`
- [ ] Oncourt/Offcourt Team Data `http://stats.nba.com/stats/teamplayeronoffdetails?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Per48&Period=0&PlusMinus=N&Rank=N&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612753&VsConference=&VsDivision=`
- [ ] Clutch Stats `http://stats.nba.com/stats/leaguedashplayerclutch?AheadBehind=Ahead+or+Behind&ClutchTime=Last+5+Minutes&DateFrom=&DateTo=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&PointDiff=5&Rank=N&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&VsConference=&VsDivision=`
- [ ] SportVu Data `http://stats.nba.com/stats/locations_getmoments/?eventid=5&gameid=0021400001`


One thing to consider is to create two parent modules, `PlayerStats` and `GameStats`. These would either take a `playerid` or `gameid` variable and pipe that into a submodule that then makes the appropriate database call. Can add a `max` module that makes a call and pulls all the data that is associated with either a game or a player.

Another thing to look into is trying to backend into some sportVU data. Not sure if this is possible, but at this point, the data that is available is super rich and useful for analysis.

As with the last module, it would also be nice to build some pre-defined graphs into the module. Things such as shot charts and bar graphs. Anything that can be run on a single player/game. These graphs need to be subModules of their respective parent modules
