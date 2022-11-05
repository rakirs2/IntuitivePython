import json

file = open("nflteams.json")

teams = json.load(file)

for team in teams:
    print(team["city"])
    print(team["name"])
    print(team["abr"])
    print(team["conf"])
    print(team["div"])




## exercises

## get all teams in a division

## get all teams in a city

## get all teams in a conference

## get all teams in a division


class nflteam:
    def __init__(self, city, name, abr, conf, div):
        self.city = city
        self.name = name
        self.abbreviation = abr
        self.conference = conf
        self.division = div