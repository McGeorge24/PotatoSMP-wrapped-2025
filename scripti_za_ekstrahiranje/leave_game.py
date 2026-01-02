import json
import os

STATS_DIR = "statistike_igralcev"

total_times_left = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    times_left = data.get("stats", {}).get(
        "minecraft:custom", {}).get("minecraft:leave_game", {})
    # print(f"{playername}:{times_slept}")
    total_times_left += times_left
    all_players[playername] = times_left

print("Total times players left server:", total_times_left)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
