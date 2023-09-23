from weather_api import get_weather, get_weather_details, Weather
import matplotlib.pyplot as plt
import numpy as np


def get_fmt_date(item):
    return f'{item.date:%d-%m-%y}'


def print_plot(weather_details: list[Weather], current_weather: dict):
    city: dict = current_weather.get('city')
    lines: list = []
    legends: list[str] = []

    days: list[str] = sorted(
        {get_fmt_date(date) for date in weather_details})

    for day in days:
        grouped: list[Weather] = [
            current for current in weather_details if get_fmt_date(current) == day]

        x = np.array([item.date.hour for item in grouped])
        y = np.array([item.temp for item in grouped])

        legends.append(day)
        lines.extend([x, y])

    plt.title(f'{city.get("name")}, {city.get("country")}')
    plt.xlabel("Година")
    plt.ylabel("Температура, C°")

    plt.plot(*lines)
    plt.legend(legends)
    plt.grid()
    plt.show()


def print_details(weather_details: list[Weather]):
    # Get the current days
    days: list[str] = sorted(
        {get_fmt_date(date) for date in weather_details})

    for day in days:
        print(day)
        print('---')

        # Group the weather data by date to make it easier to read
        grouped: list[Weather] = [
            current for current in weather_details if get_fmt_date(current) == day]

        for element in grouped:
            print(element)

        print()  # An empty line


def main():
    # Ask the user for their city
    user_city: str = input('Вкажіть місто: ')

    # Get the current weather details
    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)

    print_details(weather_details)

    print_plot(weather_details, current_weather)


if __name__ == '__main__':
    main()
