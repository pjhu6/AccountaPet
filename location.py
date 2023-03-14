# pip install geopy

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        # Get current location using geolocation service
        location = geolocator.geocode("me", timeout=10)
        return location.latitude, location.longitude
    except GeocoderTimedOut as e:
        print("Error: geocode service is not available at the moment.")
        return None

if __name__ == '__main__':
    latitude, longitude = get_location()
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")