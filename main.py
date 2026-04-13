import requests
import os

WEBHOOK = os.environ["WEBHOOK"]
GROUP_ID = 15938842

url = f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&CreatorTargetId={GROUP_ID}&Limit=30"

res = requests.get(url, timeout=15)
data = res.json()

for item in data.get("data", []):
    item_id = item.get("id")
    name = item.get("name", "New item")
    price = item.get("priceStatus")

    if item_id and price == "Off Sale":
        continue

    if item_id:
        link = f"https://www.roblox.com/catalog/{item_id}"
        requests.post(
            WEBHOOK,
            json={"content": f"New item: {name}\n{link}"},
            timeout=15
        )
