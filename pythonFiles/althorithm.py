import pandas as pd

#effective field goal perentage difference: 0.16118265
#turnover percentage difference: -0.05958713
#offensive rebound percentage difference: 0.07061777
#free throws to field goals attempts difference: 0.03267933
#offensive rating difference: 0.17885523
#defensive rating difference: -0.33924331

#effective field goal perentage difference (court): 0.10808104
#turnover percentage difference (court):  -0.09548481
#offensive rebound percentage difference (court):   0.07055131
#free throws to field goals attempts difference (court): 0.0748545
#offensive rating difference (court): 0.14822224
#defensive rating difference (court): -0.21756487

#court means: considering court situation means:
#if team A is the host and team B is the visitor,
#effective field goal percentage is A efgp home - B efgp road

# from datetime import datetime
# from sportsreference.nba.boxscore import Boxscores
# from sportsreference.nba.boxscore import Boxscore
# # Pulls all games between and including January 1, 2018 and January 5, 2018
# gamesSet = Boxscores(datetime(2018, 1, 1), datetime(2018, 1, 5))
# # Prints a dictionary of all results from January 1, 2018 and January 5,
# # 2018
# #print(gamesSet.games)
# for x in gamesSet.games:
# 	print(x)

from sportsreference.nba.schedule import Schedule
from sportsreference.nba.boxscore import Boxscore

team_abbr = input("Enter the team abbreviation: ")
team_year = input("Enter the team year: ")
team_schedule = Schedule(team_abbr, team_year)
list_points = []
for game in team_schedule:
 	game_data = Boxscore(game.boxscore_index)
 	team_to_use = ''
 	if game_data.away_points > game_data.home_points and game_data.winning_abbr == team_abbr:
 		# print(game_data.winning_name)
 		# print(game_data.losing_name)
 		# print(game_data.away_points)
 		# print("Away")
 		# print("weeee")
 		list_points.append(game_data.away_points)
 	elif game_data.away_points > game_data.home_points and game_data.losing_abbr == team_abbr:
 		# print(game_data.winning_name)
 		# print(game_data.losing_name)
 		# print(game_data.home_points)
 		# print("Home")
 		# print("weeee")
 		list_points.append(game_data.home_points)
# 	if game_data.away_abbr == 'HOU':
# 		list.append(game_data.away_points)
# 	else: 
# 		list.append(game_data.home_points)

data = {'Points':list_points}
df = pd.DataFrame(data)

print(df)
