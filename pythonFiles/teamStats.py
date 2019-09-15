import pandas as pd
from sportsreference.nba.schedule import Schedule
from sportsreference.nba.boxscore import Boxscore

class teamStats:
	def __init__(self, teamA_abbr, teamA_year):
		self.teamA_abbr = teamA_abbr
		self.teamA_year = teamA_year

	def returnValue(self):
		teamA_schedule = Schedule(self.teamA_abbr, self.teamA_year)

		#Lists for stats
		listA_location = []
		listA_efg = []
		listA_or = []
		listA_to = []
		listA_ft = []
		listA_ora = []
		listA_dra = []

		for game in teamA_schedule:
 			game_data = Boxscore(game.boxscore_index)
 			if game_data.away_points > game_data.home_points and game_data.winning_abbr == self.teamA_abbr:
 				listA_efg.append(game_data.away_effective_field_goal_percentage)
 				listA_location.append('Away')
 				listA_or.append(game_data.away_offensive_rebound_percentage)
 				listA_to.append(game_data.away_turnover_percentage)
 				listA_ft.append(game_data.away_free_throw_percentage)
 				listA_ora.append(game_data.away_offensive_rating)
 				listA_dra.append(game_data.away_defensive_rating)

 			elif game_data.away_points > game_data.home_points and game_data.losing_abbr == self.teamA_abbr:
 				listA_efg.append(game_data.home_effective_field_goal_percentage)
 				listA_location.append('Home')
 				listA_or.append(game_data.home_offensive_rebound_percentage)
 				listA_to.append(game_data.home_turnover_percentage)
 				listA_ft.append(game_data.home_free_throw_percentage)
 				listA_ora.append(game_data.home_offensive_rating)
 				listA_dra.append(game_data.home_defensive_rating)


		dataA = {'Location':listA_location, 
			'EffectiveFieldGoals':listA_efg, 
			'OffensiveRebounds':listA_or, 
			'Turnovers':listA_to,
			'Freethrows':listA_ft,
			'OffensiveRating':listA_ora,
			'DefensiveRating':listA_dra}

		dfA = pd.DataFrame(dataA)
		avgStatsA = [dfA.EffectiveFieldGoals.mean(), 
			dfA.OffensiveRebounds.mean(),
			dfA.Turnovers.mean(),
			dfA.Freethrows.mean(),
			dfA.OffensiveRating.mean(),
			dfA.DefensiveRating.mean()]

		return avgStatsA


