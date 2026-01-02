import json
import os

STATS_DIR = "stats/"

total_deaths = 0
all_blocks: dict[str, int] = {}

for file in os.listdir(STATS_DIR):
    if not file.endswith(".json"):
        continue

    with open(os.path.join(STATS_DIR, file)) as f:
        data = json.load(f)

    mined = data.get("stats", {}).get("minecraft:mined", {})
    for block, amount in mined.items():
        all_blocks[block] = all_blocks.get(block, 0) + amount


for playername, playerstat in sorted(all_blocks.items(), key=lambda x: x[1], reverse=True):
    print(f"{playername}:{playerstat}")
