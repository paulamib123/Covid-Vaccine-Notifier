from flask.json import jsonify
import requests
import json


def getResponseFromDistrictID(districtID, date):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    parameters = {
        'district_id' : districtID,
        'date': date
    }
    return requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict", headers=headers, params=parameters)


def convertResponseToDict(districtID, date):
    response = getResponseFromDistrictID(districtID, date)
    return json.loads(response.text)


def createDataDictionary(session):
    if session["available_capacity"] <= 0:
        return {}

    return {"name" : session["name"], 
    "address": session["address"], 
    "date": session["date"], 
    "available_capacity_dose1": session["available_capacity_dose1"], 
    "available_capacity_dose2": session["available_capacity_dose2"], 
    "available_capacity": session["available_capacity"],
    "min_age_limit": session["min_age_limit"],
    "vaccine": session["vaccine"], 
    "slots": session["slots"]}
    

def getData(n, data):
    if data == {}:
        return

    result = str(n) + ". "

    for key, value in data.items():
        result += key.capitalize() + " : " + str(value) + "\n"
    
    return result + "\n"


def parseResponse(districtID, date):
    num = 1
    result = ""
    response = convertResponseToDict(districtID, date)
    for session in response["sessions"]:
        dataDict = createDataDictionary(session)
        if dataDict == {}:
            continue
        result += getData(num, dataDict)
        num += 1
    
    return result

    
