from fastapi import FastAPI
import json
import os
import random

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()

with open(os.path.join(DIRECTORY, "api.json")) as API:
    JSON = json.loads(API.read())

@app.get("/")
def info() -> str:
    return "wholesomeBot API is working"

@app.get("/quotes")
def quote() -> str:

    random.seed(a = None)
    return random.choice(JSON["quotes"])

@app.get("/ily")
def ily() -> str:

    random.seed(a = None)
    return random.choice(JSON["ily"])

@app.get("/pickuplines")
def pickup() -> str:

    random.seed(a = None)
    return random.choice(JSON["pickuplines"])

@app.get("/info")
def info() -> str:

    information = {
        "Author": "Devansh Singh",
        "GitHub": "https://github.com/Devansh3712",
        "Source Code": "https://github.com/Devansh3712/wholesomeBot-API",
        "Bot": "https://top.gg/bot/753959496937898095",
        "Socials": [
            "https://instagram.com/whodevansh",
            "https://fiverr.com/devansh3712",
            "https://stackoverflow.com/users/13722027/devansh-singh",
            "https://www.linkedin.com/in/devanshsingh3/",
            "https://www.hackerrank.com/devanshamity"
        ],
        "Last Updated": "31-05-2021"
    }
    return information
