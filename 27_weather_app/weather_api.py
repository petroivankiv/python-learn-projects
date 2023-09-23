from model import Weather, dt
import json
import requests
from typing import Final
from os import getenv
from dotenv import load_dotenv, find_dotenv

# find the .env file and load it
load_dotenv(find_dotenv())


# Constants
API_KEY: Final[str] = getenv("WEATHER_API_KEY")
BASE_URL: Final[str] = getenv("WEATHER_API_URL")


def get_weather(city_name: str, mock: bool = False) -> dict:
    """Gets the current weather from the weather api"""

    # Return dummy data for testing
    if mock:
        print('Using mock data...')

        with open('27_weather_app/dummy_data.json') as file:
            return json.load(file)

    # Request live data
    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    """Takes the weather json and turns it into a nice list of Weather objects"""

    days: list[dict] = weather.get('list')

    # If there is no data for days, no point in continuing
    if not days:
        raise Exception(f'Problem with json: {weather}')

    # Try to add the info we want to our list_of_weather
    list_of_weather: list[Weather] = []

    for day in days:
        details: dict = day.get('main')
        weather: dict = day.get('weather')
        wind: dict = day.get('wind')
        windSpeed: float = round(wind.get('speed') * 0.51444444, 2)

        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             temp=details.get('temp'),
                             humidity=details.get('humidity'),
                             description=weather[0].get('description'),
                             wind_speed=windSpeed)
        
        list_of_weather.append(w)

    return list_of_weather
