import os
import time
import requests

data = {
    # 'Pittsburgh(100)': [40.0, 40.5, -80.0, -79.5],
    'Pittsburgh(16)': [40.3, 40.5, -80.0, -79.8],
    'Pittsburgh(4)': [40.4, 40.5, -80.0, -79.9],
    'Pittsburgh(1)': [40.45, 40.5, -80.0, -79.95],
    # 'New York(100)': [40.5, 41.0, -74.2, -73.7],
    'New York(16)': [40.6, 40.8, -74.1, -73.9],
    'New York(4)': [40.7, 40.8, -74.0, -73.9],
    'New York(1)': [40.7, 40.75, -74.0, -73.95],
    # 'San Francisco(100)': [37.1, 37.6, -122.22, -121.72],
    'San Francisco(16)': [37.25, 37.45, -122.07, -121.87],
    'San Francisco(4)': [37.3, 37.4, -122.02, -121.92],
    'San Francisco(1)': [37.3, 37.35, -122.02, -121.97],
}

# OSM_URL = "https://overpass-api.de/api/map?bbox=-80.0441,40.2400,-79.2957,40.6309"
OSM_URL = "https://overpass-api.de/api/map?bbox={2},{0},{3},{1}"


def getOSMData(coordinate):
    before = time.time()
    r = requests.get(OSM_URL.format(*coordinate), stream=True)
    after = time.time()
    with open("./map.txt", 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    size = os.path.getsize('./map.txt') / 1000000.
    os.remove('./map.txt')

    return after - before, size

if __name__ == '__main__':
    for k, v in data.items():
        t, size = getOSMData(v)
        print("{0}, time:{1} seconds, size:{2} MB".format(k, t, size))
