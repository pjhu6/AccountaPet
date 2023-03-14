# pip install geocoder

import geocoder

def get_location():
    g = geocoder.ip('me')
    return g.latlng

if __name__ == '__main__':
    latitude, longitude = get_location()
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")