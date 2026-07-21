# Football Data Analyzer
players = [
    {"name": "Mbappe", "goals": 44, "assists": 10},
    {"name": "Haaland", "goals": 38, "assists": 6},
    {"name": "Kvaratskhelia", "goals": 12, "assists": 8}
]
print("Player Statistics:")
for player in players:
    total = player["goals"] + player["assists"]
    print(player["name"], "Total Contributions:", total)

