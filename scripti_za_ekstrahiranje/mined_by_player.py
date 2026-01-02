import json
import os

STATS_DIR = "statistike_igralcev"

total_blocks_mined = 0
all_players: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue
    playername, pripona = file.split(".")
    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    mined = data.get("stats", {}).get("minecraft:mined", {})
    player_stat = sum(mined.values())
    all_players[playername] = player_stat
    total_blocks_mined += player_stat

print("Total blocks mined on server:", total_blocks_mined)

for playername, playerstat in sorted(all_players.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
