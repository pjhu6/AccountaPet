import requests
import location

def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = 'cfe3a601fe0d5d42fdd017500bcef2df'
    lat, lon = location.get_location()

    params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': api_key}
    response = requests.get(url, params=params)

    data = response.json()
    print(data)

if __name__ == '__main__':
    get_weather()