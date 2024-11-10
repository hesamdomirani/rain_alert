import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
api_key = os.getenv('API_KEY')
auth_token = os.getenv("AuthToken")
account_sid= os.getenv("Account_Sid")

OWM_Endpoint = os.getenv("OWM_Endpoint")
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
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=os.getenv("MY_VIRTUELL_NUMBER"),
    body='It will be Rainy,Bring Your Umbrella!!!',
    to= os.getenv("MY_ACTUELL_NUMBER")
)
    print(message.sid)