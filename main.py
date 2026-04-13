import requests
import os
import json

WEBHOOK = os.environ["WEBHOOK"]
GROUP_ID = 15938842
STATE_FILE = "seen.json"

try:
    with open(STATE_FILE, "r") as f:
        seen = set(json.load(f))
except:
    seen = set()

url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&CreatorTargetId={GROUP_ID}&Limit=30"

res = requests.get(url, timeout=15).json()

new_seen = set(seen)

for item in res.get("data", []):
    item_id = str(item.get("id"))
    name = item.get("name", "New item")
    price_status = item.get("priceStatus")

    # ONLY send if it's actually for sale
    if price_status != "Off Sale":
        if item_id not in seen:
            link = f"https://www.roblox.com/catalog/{item_id}"

            requests.post(
                WEBHOOK,
                json={"content": f"NEW RELEASE: {name}\n{link}"},
                timeout=15
            )

            new_seen.add(item_id)

with open(STATE_FILE, "w") as f:
    json.dump(list(new_seen), f)
