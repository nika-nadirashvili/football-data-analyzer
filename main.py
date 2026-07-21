# Football Data Analyzer
import csv
players = []
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        players.append(row)
print("Player Statistics:")
for player in players:
    contribution = int(player["Goals"]) + int(player["Assists"])
    print(
        player["Name"],
        "- Goal Contributions:",
        contribution
    )

