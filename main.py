import requests
import os

WEBHOOK = os.environ["WEBHOOK"]
GROUP_ID = 15938842

url = f"https://catalog.roblox.com/v1/search/items?category=Clothing&creatorTargetId={GROUP_ID}&creatorType=Group&limit=10"

res = requests.get(url, timeout=15).json()

for item in res.get("data", []):
    item_id = item.get("id")
    name = item.get("name", "New item")

    price = item.get("price")
    if price is None:
        price = item.get("lowestPrice", 0)

    if item_id and price and price > 0:
        link = f"https://www.roblox.com/catalog/{item_id}"
        requests.post(
            WEBHOOK,
            json={"content": f"New item: {name}\n{link}"},
            timeout=15
        )
