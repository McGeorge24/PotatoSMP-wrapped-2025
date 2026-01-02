import json
import os

STATS_DIR = "stats/"

total_deaths = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    deaths = data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:deaths", {}) if data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:deaths", {}) else 0
    # print(f"{playername}:{deaths}")
    all_players[playername] = deaths
    total_deaths += deaths

print("Total deaths on server:", total_deaths)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
