#!/usr/bin/env python3
# Creating a Wave Race 64 Save using the current top 3 times for each track.

import os
import sys
import srcomapi
import srcomapi.datatypes as dt
import requests
import json
import pandas as pd

api = srcomapi.SpeedrunCom()

SB_id = "ldypjjd3"
SBAY_id = "gdrqg89z"
DL_id = "nwl7np9v"
MF_id = "ywe8nqwl"
PB_id = "69z4x6w1"
TC_id = "r9g3rqw2"
GC_id = "o9xlk69l"
SI_id = "4958y29p"

ThreeL_id = "02qpq7dy"
OneL_id = "ndx7yo2q"
Reverse_id = "w20v0jkn"

def gettopthree (level_id, category_id):
    requesturl = f"https://www.speedrun.com/api/v1/leaderboards/wr64/level/{level_id}/{category_id}?var-p85901vn=rqv42owq&top=3"

    response = requests.get(requesturl).json()["data"]["runs"]
    data = response
    keys = "place", "id", "primary_t"

    data = filterleaderboard(data, keys)

    data = pd.json_normalize(data)
    data = filterleaderboard(data, keys)
    del data["run.id"]
    del data["run.videos.links"]
    data['run.players'] = data['run.players'].apply(
        lambda x: x[0]['id'] if isinstance(x, list) and len(x) > 0 else x
    )

    data = data.rename(
        columns={
            "run.times.primary_t": "Time",
            "run.players": "Player",
            "place": "Place"
            })
    
    for i in range(3):
        data.at[i, "Player"] = getplayername(data.at[i, "Player"])
        
    return data

def gettoprun (level_id):
    requesturl = f"https://www.speedrun.com/api/v1/leaderboards/wr64/level/{level_id}/{OneL_id}?var-p85901vn=rqv42owq&top=1"

    response = requests.get(requesturl).json()["data"]["runs"]
    data = response
    keys = "place", "id", "primary_t"

    data = filterleaderboard(data, keys)

    data = pd.json_normalize(data)
    data = filterleaderboard(data, keys)
    del data["run.id"]
    del data["run.videos.links"]
    data['run.players'] = data['run.players'].apply(
        lambda x: x[0]['id'] if isinstance(x, list) and len(x) > 0 else x
    )
    

    data = data.rename(
        columns={
            "run.times.primary_t": "Time",
            "run.players": "Player",
            "place": "Place"
            })
    
    data.at[0, "Player"] = getplayername(data.at[0, "Player"])
    
    return data

def getplayername (player_id):
    url = f"https://www.speedrun.com/api/v1/users/{player_id}"
    
    response = requests.get(url)
    data = response.json()
    username = data["data"]["names"]["international"]
    return username

def filterleaderboard(data, keep_keys):
    if isinstance(data, dict):
        # Filter the dictionary keys and recursively filter their values
        return {
            key: filterleaderboard(value, keep_keys)
            for key, value in data.items()
            if key in keep_keys or isinstance(value, (dict, list))
        }
    elif isinstance(data, list):
        # Recursively filter each item in the list
        return [filterleaderboard(item, keep_keys) for item in data]
    else:
        # Return primitive values (strings, numbers, booleans, None) as-is
        return data
    
    
SB3data = gettopthree(SB_id, ThreeL_id)
SBAY3data = gettopthree(SBAY_id, ThreeL_id)
DL3data = gettopthree(DL_id, ThreeL_id)
MF3data = gettopthree(MF_id, ThreeL_id)
PB3data = gettopthree(PB_id, ThreeL_id)
TC3data = gettopthree(TC_id, ThreeL_id)
GC3data = gettopthree(GC_id, ThreeL_id)
SI3data = gettopthree(SI_id, ThreeL_id)

SB1data = gettoprun(SB_id)
SBAY1data = gettoprun(SBAY_id)
DL1data = gettoprun(DL_id)
MF1data = gettoprun(MF_id)
PB1data = gettoprun(PB_id)
TC1data = gettoprun(TC_id)
GC1data = gettoprun(GC_id)
SI1data = gettoprun(SI_id)

SBRdata = gettopthree(SB_id, Reverse_id)
SBAYRdata = gettopthree(SBAY_id, Reverse_id)
DLRdata = gettopthree(DL_id, Reverse_id)
MFRdata = gettopthree(MF_id, Reverse_id)
PBRdata = gettopthree(PB_id, Reverse_id)
TCRdata = gettopthree(TC_id, Reverse_id)
GCRdata = gettopthree(GC_id, Reverse_id)
SIRdata = gettopthree(SI_id, Reverse_id)