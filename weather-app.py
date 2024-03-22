import requests
from datetime import datetime

api_key = '<api-key-here>'
location = input("Enter city name: ")

formatted_api_link = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

api_link = requests.get(formatted_api_link)
api_data = api_link.json()

kelvin_base = 273.15
city_temperature = ((api_data['main']['temp']) - kelvin_base)
weather_desc = api_data['weather'][0]['description']
humidity_ = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print(f"Weather Stats for - {location.upper()}  || {date_time}")
print("-------------------------------------------------------------")

print(f"Current temperature is: {city_temperature:.2f} deg C")
print(f"Current weather desc  : {weather_desc}")
print(f"Current Humidity      : {humidity_} {%}")
print(f"Current wind speed    : {wind_speed} km/h")

with open('Weather.txt' ,'wb') as f:
    f.write(api_link.content)
