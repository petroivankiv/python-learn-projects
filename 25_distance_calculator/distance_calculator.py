from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from fake_useragent import UserAgent


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    """Creates a geolocator that returns coordinates for the given address."""

    geolocator = Nominatim(user_agent=UserAgent().chrome)
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    """Calculates the distance in km for the home coordinates and the target coordinates."""

    if home and target:
        return geodesic(home.coordinates(), target.coordinates()).kilometers


def get_distance_km(home: str, target: str) -> float | None:
    """Gets the distance and returns it as a float."""

    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home} -> {target}: {distance:.2f} кілометрів')
        return distance
    else:
        print('Failed to calculate the distance.')


def main():
    # home_address: str = 'Helsinkigade 10, Copenhagen 2150, Denmark'
    home_address: str = input('Початкова адреса: ')
    target_address: str = input('Кінцева адреса: ')
    
    print('Calculating...')
    
    get_distance_km(home_address, target=target_address)


if __name__ == '__main__':
    main()
