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

from sportsreference.nba.schedule import Schedule
from sportsreference.nba.boxscore import Boxscore

team_abbr = input("Enter the team abbreviation: ")
team_year = input("Enter the team year: ")
team_schedule = Schedule(team_abbr, team_year)
list_points = []

#Lists for stats
list_location = []
list_efg = []
list_or = []
list_to = []
list_ft = []
list_ora = []
list_dra = []

for game in team_schedule:
 	game_data = Boxscore(game.boxscore_index)
 	team_to_use = ''
 	if game_data.away_points > game_data.home_points and game_data.winning_abbr == team_abbr:
 		# print(game_data.winning_name)
 		# print(game_data.losing_name)
 		# print(game_data.away_points)
 		# print("Away")
 		# print("break")
 		#list_points.append(game_data.away_points)
 		list_efg.append(game_data.away_effective_field_goal_percentage)
 		list_location.append('Away')
 		list_or.append(game_data.away_offensive_rebound_percentage)
 		list_to.append(game_data.away_turnover_percentage)
 		list_ft.append(game_data.away_free_throw_percentage)
 		list_ora.append(game_data.away_offensive_rating)
 		list_dra.append(game_data.away_defensive_rating)

 	elif game_data.away_points > game_data.home_points and game_data.losing_abbr == team_abbr:
 		# print(game_data.winning_name)
 		# print(game_data.losing_name)
 		# print(game_data.home_points)
 		# print("Home")
 		# print("break")
 		#list_points.append(game_data.home_points)
 		list_efg.append(game_data.home_effective_field_goal_percentage)
 		list_location.append('Home')
 		list_or.append(game_data.home_offensive_rebound_percentage)
 		list_to.append(game_data.home_turnover_percentage)
 		list_ft.append(game_data.home_free_throw_percentage)
 		list_ora.append(game_data.home_offensive_rating)
 		list_dra.append(game_data.home_defensive_rating)

data = {'Location':list_location, 
		'Effective Field Goals':list_efg, 
		'Offensive Rebounds':list_or, 
		'Turnovers':list_to,
		'Freethrows':list_ft,
		'Offensive Rating':list_ora,
		'Defensive Rating':list_dra}

df = pd.DataFrame(data)

print(df)


    
