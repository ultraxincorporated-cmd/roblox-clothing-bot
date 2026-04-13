import requests
import os

WEBHOOK = os.environ["WEBHOOK"]
GROUP_ID = 15938842

url = f"https://catalog.roblox.com/v1/search/items?category=Clothing&creatorTargetId={GROUP_ID}&creatorType=Group&limit=10"

res = requests.get(url).json()

for item in res["data"]:
    if item["price"] > 0:
        link = f"https://www.roblox.com/catalog/{item['id']}"
        requests.post(WEBHOOK, json={
            "content": f"New item: {item['name']}\n{link}"
        })
