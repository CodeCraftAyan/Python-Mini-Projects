import requests
from datetime import *

now = datetime.today()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
day = now.strftime("%A")

def get_weather_data():
    latitude = 22.5726  # Use Latitute and Longtitude base on your area (you can Google it)
    longitude = 88.3639
    api_key = "####################" # Use OpenWeather or Other Website's your API Key 
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        country = data["sys"]["country"]
        city = data["name"]
        weatherDesc = data["weather"][0]["description"]
        temp = data["main"]["temp"] / 10
        humidity = data["main"]["humidity"]

        print(f"\n-- {day}'s Weather --\n\nDate : {date}\nCurrent Time : {time} \n\nCountry : {country}\nLocation : {city}\nWeather Description : {weatherDesc}\nTemperature : {round(temp, 2)} °C\nHumidity : {round(humidity, 2)}%\n")

    except requests.exceptions.HTTPError as httpError :
        print(f"Http Error occurred : {httpError}")
    except Exception as error:
        print(f"Error occurred : {error}")

get_weather_data()