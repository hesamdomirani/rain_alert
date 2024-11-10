import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
LATITUDE = 50.316540
LONGITUDE = 11.913620

parameters = {"lat": LATITUDE ,
              "lon":LONGITUDE ,
              "appid": api_key,
              "cnt":4 } 

response = requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data_total = response.json()
weather_for_12_hours = weather_data_total["list"]
code_status = [item["weather"][0]["id"] for item in weather_for_12_hours]
will_rain = False
for code in code_status:
    if code < 700:
        will_rain=True
if will_rain:
    print("Bring your Umbrella!!")
      