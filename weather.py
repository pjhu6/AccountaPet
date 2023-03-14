import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'cfe3a601fe0d5d42fdd017500bcef2df'

params = {'q': 'New York', 'units': 'imperial', 'appid': api_key}

response = requests.get(url, params=params)

data = response.json()
print(data)