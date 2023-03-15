import requests
import location
import datetime

condition_dict = {
    200: {'main': 'Thunderstorm', 'description': 'thunderstorm with light rain', 'icon': '11d'},
    201: {'main': 'Thunderstorm', 'description': 'thunderstorm with rain', 'icon': '11d'},
    202: {'main': 'Thunderstorm', 'description': 'thunderstorm with heavy rain', 'icon': '11d'},
    210: {'main': 'Thunderstorm', 'description': 'light thunderstorm', 'icon': '11d'},
    211: {'main': 'Thunderstorm', 'description': 'thunderstorm', 'icon': '11d'},
    212: {'main': 'Thunderstorm', 'description': 'heavy thunderstorm', 'icon': '11d'},
    221: {'main': 'Thunderstorm', 'description': 'ragged thunderstorm', 'icon': '11d'},
    230: {'main': 'Thunderstorm', 'description': 'thunderstorm with light drizzle', 'icon': '11d'},
    231: {'main': 'Thunderstorm', 'description': 'thunderstorm with drizzle', 'icon': '11d'},
    232: {'main': 'Thunderstorm', 'description': 'thunderstorm with heavy drizzle', 'icon': '11d'},

    300: {'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'},
    301: {'main': 'Drizzle', 'description': 'drizzle', 'icon': '09d'},
    302: {'main': 'Drizzle', 'description': 'heavy intensity drizzle', 'icon': '09d'},
    310: {'main': 'Drizzle', 'description': 'light intensity drizzle rain', 'icon': '09d'},
    311: {'main': 'Drizzle', 'description': 'drizzle rain', 'icon': '09d'},
    312: {'main': 'Drizzle', 'description': 'heavy intensity drizzle rain', 'icon': '09d'},
    313: {'main': 'Drizzle', 'description': 'shower rain and drizzle', 'icon': '09d'},
    314: {'main': 'Drizzle', 'description': 'heavy shower rain and drizzle', 'icon': '09d'},
    321: {'main': 'Drizzle', 'description': 'shower drizzle', 'icon': '09d'},

    500: {'main': 'Rain', 'description': 'light rain', 'icon': '10d'},
    501: {'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'},
    502: {'main': 'Rain', 'description': 'heavy intensity rain', 'icon': '10d'},
    503: {'main': 'Rain', 'description': 'very heavy rain', 'icon': '10d'},
    504: {'main': 'Rain', 'description': 'extreme rain', 'icon': '10d'},
    511: {'main': 'Rain', 'description': 'freezing rain', 'icon': '13d'},
    520: {'main': 'Rain', 'description': 'light intensity shower rain', 'icon': '09d'},
    521: {'main': 'Rain', 'description': 'shower rain', 'icon': '09d'},
    522: {'main': 'Rain', 'description': 'heavy intensity shower rain', 'icon': '09d'},
    531: {'main': 'Rain', 'description': 'ragged shower rain', 'icon': '09d'},

    600: {'main': 'Snow', 'description': 'light snow', 'icon': '13d'},
    601: {'main': 'Snow', 'description': 'snow', 'icon': '13d'},
    602: {'main': 'Snow', 'description': 'heavy snow', 'icon': '13d'},
    611: {'main': 'Snow', 'description': 'sleet', 'icon': '13d'},
    612: {'main': 'Snow', 'description': 'light shower sleet', 'icon': '13d'},
    613: {'main': 'Snow', 'description': 'shower sleet', 'icon': '13d'},
    615: {'main': 'Snow', 'description': 'light rain and snow', 'icon': '13d'},
    616: {'main': 'Snow', 'description': 'rain and snow', 'icon': '13d'},
    620: {'main': 'Snow', 'description': 'light shower snow', 'icon': '13d'},
    621: {'main': 'Snow', 'description': 'shower snow', 'icon': '13d'},
    622: {'main': 'Snow', 'description': 'heavy shower snow', 'icon': '13d'},

    701: {'main': 'Mist', 'description': 'mist', 'icon': '50d'},
    711: {'main': 'Smoke', 'description': 'smoke', 'icon': '50d'},
    721: {'main': 'Haze', 'description': 'haze', 'icon': '50d'},
    731: {'main': 'Dust', 'description': 'sand/dust whirls', 'icon': '50d'},
    741: {'main': 'Fog', 'description': 'fog', 'icon': '50d'},
    751: {'main': 'Sand', 'description': 'sand', 'icon': '50d'},
    761: {'main': 'Dust', 'description': 'dust', 'icon': '50d'},
    762: {'main': 'Ash', 'description': 'volcanic ash', 'icon': '50d'},
    771: {'main': 'Squall', 'description': 'squalls', 'icon': '50d'},
    781: {'main': 'Tornado', 'description': 'tornado', 'icon': '50d'},

    800: {'main': 'Clear', 'description': 'clear sky', 'icon': '01d'},

    801: {'main': 'Clouds', 'description': 'few clouds: 11-25%', 'icon': '02d'},
    802: {'main': 'Clouds', 'description': 'scattered clouds: 25-50%', 'icon': '03d'},
    803: {'main': 'Clouds', 'description': 'broken clouds: 51-84%', 'icon': '04d'},
    804: {'main': 'Clouds', 'description': 'overcast clouds: 85-100%', 'icon': '04d'},
}

'''
{
    'coord': {
        'lon': -117.6031, 
        'lat': 33.6409
    }, 
    'weather': [
        {
            'id': 804, 
            'main': 'Clouds', 
            'description': 'overcast clouds', 
            'icon': '04d'
        }
    ], 
    'base': 'stations', 
    'main': {
        'temp': 56.59, 
        'feels_like': 56.26, 
        'temp_min': 54.57, 
        'temp_max': 58.8, 
        'pressure': 1016, 
        'humidity': 92
    }, 
    'visibility': 10000, 
    'wind': {
        'speed': 8.01, 
        'deg': 114, 
        'gust': 11.99
    }, 
    'clouds': {
        'all': 100
    }, 
    'dt': 1678836568, 
    'sys': {
        'type': 2, 
        'id': 2079737, 
        'country': 'US', 
        'sunrise': 1678802546, 
        'sunset': 1678845419
    }, 
    'timezone': -25200, 
    'id': 5386082, 
    'name': 'Rancho Santa Margarita', 
    'cod': 200
}
'''

def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = 'cfe3a601fe0d5d42fdd017500bcef2df'
    lat, lon = location.get_location()

    params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': api_key}
    response = requests.get(url, params=params)

    data = response.json()

    return data['dt'], data['weather']
    

if __name__ == '__main__':
    time, weather = get_weather()
    date_time = datetime.datetime.fromtimestamp(time)
    print(date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print(weather)