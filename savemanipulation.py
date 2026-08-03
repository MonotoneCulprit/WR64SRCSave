import os
import sys
from datetime import datetime
import srcomapi
import srcomapi.datatypes as dt
import requests
import json
import pandas as pd
import ids
import splits

now = datetime.now()
date_string = now.strftime("%m-%d-%Y")
filename = f"wr64_srcomsave_{date_string}.eep"

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
    requesturl = f"https://www.speedrun.com/api/v1/leaderboards/wr64/level/{level_id}/{ids.OneL_id}?var-p85901vn=rqv42owq&top=1"

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

def extracttimes_hayami(data):
    first = int(data.Time[0]*1000)
    second = int(data.Time[1]*1000)
    third = int(data.Time[2]*1000)

    firsthex = f"{first:06x}"
    secondhex = f"{second:06x}"
    thirdhex = f"{third:06x}"
    return firsthex, secondhex, thirdhex

def extracttime_hayami(data):
    first = int(data.Time[0]*1000)
    firsthex = f"{first:06x}"
    return firsthex

def extracttimes_mariner(data):
    first = int(data.Time[0]*1000)
    second = int(data.Time[1]*1000)
    third = int(data.Time[2]*1000)

    firsthex = f"{first:06x}"
    secondhex = f"{second:06x}"
    thirdhex = f"{third:06x}"
    mariner = '2' + firsthex[1:]
    mariner2 = '2' + secondhex[1:]
    mariner3 = '2' + thirdhex[1:]
    return mariner, mariner2, mariner3

def extracttime_mariner(data):
    first = int(data.Time[0]*1000)
    firsthex = f"{first:06x}"
    mariner = '2' + firsthex[1:]
    return mariner

def extracttimes_jeter(data):
    first = int(data.Time[0]*1000)
    second = int(data.Time[1]*1000)
    third = int(data.Time[2]*1000)

    firsthex = f"{first:06x}"
    secondhex = f"{second:06x}"
    thirdhex = f"{third:06x}"
    jeter = '6' + firsthex[1:]
    jeter2 = '6' + secondhex[1:]
    jeter3 = '6' + thirdhex[1:]
    return jeter, jeter2, jeter3

def extracttime_jeter(data):
    first = int(data.Time[0]*1000)
    firsthex = f"{first:06x}"
    jeter = '6' + firsthex[1:]
    return jeter

def extractnames(data):
    return data.Player[0], data.Player[1], data.Player[2]

def writetooffset(data, offset):
    with open("Output/" + filename, "r+b") as wr64_save:
        wr64_save.seek(offset)
        wr64_save.write(data)

def createinitialshex(name):
    name = name.lower()
    init1 = name[0]
    init2 = name[1]
    init3 = name[2]
    
    alpha_map = {chr(i): str(i - 96) for i in range(97, 123)}
    alphatable = str.maketrans(alpha_map)
    
    if not init1.isalpha():
        init1 = '-'
        init1 = '11100'
    else:
        init1 = init1.translate(alphatable)
        init1 = f"{int(init1):05b}"
    
    if not init2.isalpha():
        init2 = '-'
        init2 = '11100'
    else:
        init2 = init2.translate(alphatable)
        init2 = f"{int(init2):05b}"
        
    if not init3.isalpha():
        init3 = '-'
        init3 = '11100'
    else:
        init3 = init3.translate(alphatable)
        init3 = f"{int(init3):05b}"
    
    
    initfull = '1' + init1 + init2 + init3
    
    initnum = int(initfull, base=2)

    
    inithex = f"{initnum:04X}"
    
    return inithex

def calculatechecksum():
     with open("Output/" + filename, "r+b") as wr64_save:
        data = wr64_save.read(0x200)

        # Slice from byte index 4 to 0x1FF
        aftercheck = data[4:0x200]

        # Sum all the integer byte values
        integersum = sum(aftercheck)

        checksum = f"{integersum & 0xFFFF:04X}"
        return checksum
    
def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Example usage in your script:
config_path = get_resource_path("config.json")