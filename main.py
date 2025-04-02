import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Loading .env files
load_dotenv()

# OpenWeather
api_key = os.getenv("API_KEY")
lat = os.getenv("LAT")
lon = os.getenv("LON")
cnt = 4
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={api_key}"

# Twilio
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
user_number = os.getenv("USER_WHATSAPP_NUMBER")

response = requests.get(url)
response.raise_for_status()
weather_data = response.json()

rain_flag = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        rain_flag = True

if rain_flag:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=twilio_number,
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        to=user_number
    )
    print(message.status)
