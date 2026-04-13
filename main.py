import requests
import os

WEBHOOK = os.environ["WEBHOOK"]

requests.post(
    WEBHOOK,
    json={"content": "test message from github bot"},
    timeout=15
)
