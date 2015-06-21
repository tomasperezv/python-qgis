#!/usr/bin/env python
"""
 extract-data.py
 @author tom@0x101.com
"""
from datetime import datetime
from itertools import chain
from urllib import urlopen
from geopy.geocoders import Nominatim
import ping

# Initialize nominatim geolocator API
geolocator = Nominatim()

# Compute the timeout delay to the Nominatim API
# @see http://wiki.openstreetmap.org/wiki/Nominatim
try:
    delay = ping.do_one('nominatim.openstreetmap.org', 500, 64)
except RuntimeError:
    pass

for line in open('sample-data/MAGN_11.TXT','r'):
    if line <> "":
        data = line.split()
        # Process the coordinates
        lat = data[1] + data[2]
        lon = data[3] + data[4]

        # Reverse location lookup based on the coordinates
        location = geolocator.reverse(lat + ', ' + lon, True)
        # location.address contains the needed reverse address
        if location <> None:
            try:
                location = geolocator.reverse(lat + ', ' + lon)
                # location.address contains the needed reverse address
                if location <> None:
                    pass
            except (RuntimeError, TypeError, NameError):
                pass
