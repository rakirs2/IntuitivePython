import wikipedia

import json

file = open("nflteams.json")

allTeams = json.load(file)

wantedCity = input("Which city do you want?")

teams = []
for team in allTeams:
    if team["city"]==wantedCity:
        # print(team["city"])

        teams.append(team["city"]+ " " + team["name"])
        print(team["name"])
        # print(team["abr"])
        # print(team["conf"])
        # print(team["div"])


for i in range(len(teams)):
    print(str(teams[i]))
    print(wikipedia.summary(str(teams[i])))


# print(wikipedia.summary("Dallas Cowboys"))
# print(wikipedia.summary("Philadelphia Eagles"))
# print(wikipedia.summary("New York Giants"))
# print(wikipedia.summary("Washington Commanders"))