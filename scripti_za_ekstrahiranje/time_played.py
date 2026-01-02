import json
import os

STATS_DIR = "statistike_igralcev"

total_time_played = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    time_played = data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:play_time", {}) / 72000
    all_players[playername] = time_played
    total_time_played += time_played

print("Total time played on server:", total_time_played)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
