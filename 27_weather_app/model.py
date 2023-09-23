from datetime import datetime as dt
from dataclasses import dataclass


@dataclass
class Weather:
    date: dt
    temp: str
    humidity: str
    description: str
    wind_speed: str

    def __str__(self):
        return f'[{self.date:%H:%M}] {self.temp}C° {self.humidity}% {self.wind_speed} m/s ({self.description})'
