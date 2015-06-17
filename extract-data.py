from datetime import datetime
from itertools import chain
from urllib import urlopen
from geopy.geocoders import Nominatim

# Initialize nominatim geolocator API
geolocator = Nominatim()
for line in open('sample-data/MAGN_11.TXT','r'):
    if line <> "":
        data = line.split()
        # Process the coordinates
        lat = data[1] + data[2]
        lon = data[3] + data[4]
        # Reverse location lookup based on the coordinates
        location = geolocator.reverse(lat + ', ' + lon)
        # location.address contains the needed reverse address
