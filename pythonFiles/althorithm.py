import pandas as pd
from teamStats import teamStats
import math
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

teamA_abbr = input("Enter the first team abbreviation: ")
teamA_year = input("Enter the first team year: ")

teamB_abbr = input("Enter the second team abbreviation: ")
teamB_year = input("Enter the second team year: ")

avgA_stats = []
avgB_stats = []

teamA = teamStats(teamA_abbr, teamA_year)

teamB = teamStats(teamB_abbr, teamB_year)

avgA_stats = teamA.returnValue()

avgB_stats = teamB.returnValue()

coefficients = [0.16118265, -0.05958713, 0.07061777, 0.03267933, 0.17885523, -0.33924331]

x = 0;
i = 0;

while i <= 5:
	x+= (avgA_stats[i]-avgB_stats[i]) * coefficients[i]
	i+=1

sigmoid = 1 / (1 + math.exp(-x));
if sigmoid > 0.5:
	print(teamA_abbr + ' Wins!')
else:
	print(teamB_abbr + ' Wins!')
