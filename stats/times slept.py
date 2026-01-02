import json
import os

STATS_DIR = "stats/"

total_times_slept = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    times_slept = data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:sleep_in_bed", {}) if data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:sleep_in_bed", {}) else 0
    # print(f"{playername}:{times_slept}")
    all_players[playername] = times_slept
    total_times_slept += times_slept

print("Total times slept on server:", total_times_slept)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
