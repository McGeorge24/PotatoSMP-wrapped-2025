import json
import os

STATS_DIR = "statistike_igralcev"

total = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    interactions = data.get("stats", {}).get(
        "minecraft:used", {}).get("minecraft:potato", {}) if data.get("stats", {}).get(
        "minecraft:used", {}).get("minecraft:potato", {}) else 0
    # print(f"{playername}:{deaths}")
    all_players[playername] = interactions
    total += interactions

print("Total potato uses on server:", total)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
