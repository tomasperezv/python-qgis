#!/usr/bin/env python
"""
 geoip.py
 @author tom@0x101.com
"""
from geoip import geolite2

def geoip(ipAddress):
    result = ''
    locate = geolite2.lookup(ipAddress)
    if locate is not None:
        result = locate.country
    return result
