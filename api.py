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
    return JSON["information"]
