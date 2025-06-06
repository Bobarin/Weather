import requests
import json
import sqlite3
import datetime
import logging

logging.basicConfig(filename='weather.log', level=logging.INFO)
headers = {"User-Agent": "weather-cli-app"}

#city = input('Enter your city:')

while True:
    city = input('Enter your city:').strip()
    location = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={city}", headers=headers)
    data_coord = location.json()
    if data_coord != [] :
        logging.info(f"Chepuh at {datetime.datetime.now().isoformat()} | City: {city}")
        break 
    else:
        print("chepuh vvedi Gorod")
        logging.error(f"Chepuh oshibsa {datetime.datetime.now().isoformat()} | City: {city}")

#current_time = datetime.datetime.now().time()       


#city = "Berlin"
#location = requests.get("https://nominatim.openstreetmap.org/search?format=json&q={'Berlin'}", headers=headers)

#print(data_coord)
def longito(data_coord):
    longit = float(data_coord[0]["lon"])
    print(longit)
    return longit

def latito(data_coord):
    lat = float(data_coord[0]["lat"])
    print(lat)
    return lat

#print(data_weath,temp)                      

#logging.basicConfig(filename='conversion.log', level=logging.INFO)
def weather_fun(longit,lat):
    weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}2&longitude={longit}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data_weath = weather.json()["current"]
    temp = data_weath["temperature_2m"]
    return temp

Summary_weather = weather_fun(longito(data_coord),latito(data_coord))
print(Summary_weather)

#weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}2&longitude={longit}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
#data_weath = weather.json()["current"]
#temp = data_weath["temperature_2m"]
#print(temp) 