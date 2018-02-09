#!/usr/bin/python3
#pip3 install requests --> package to download HTTP requests from the PyPI index

#step 1: get data from NASA site for meteor landings
#step 2: convert the data into a Python data structure
#step 3: calculate the distance between my location and the landing sites
#step 4: sort that data by distance
#step5: find the top 10 closest locations and print them

import requests #this is a package
import math
from math import radians, sin, cos, sqrt, asin #calculates disances on Earth
#step1:
resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
print (resp.status_code)
print (resp.text)
print (len(resp.text))

#step2:
meteor_data = resp.json()
print (type(meteor_data)) #indicates it is a list of dicts
print (meteor_data[0])

#step3:
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8 # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    return R * c

aaa = haversine(50.775000, 6.083330, 34.0549930, -84.2445950)
print (aaa)

myLocation = (34.0549930, -84.2445950)
myLat = myLocation[0]; print (myLat)
myLon = myLocation[1]; print (myLon)

for eachMeteor in meteor_data:
    #if 'reclat' not in eachMeteor or 'reclong' not in eachMeteor: #--> both the below statements are same
    if not('reclat' in eachMeteor and 'reclong' in eachMeteor): continue
    destLat = float(eachMeteor['reclat'])
    destLon = float(eachMeteor['reclong'])
    eachMeteor['distance'] = haversine(destLat, destLon, myLat, myLon)

#step4:
def get_dist(x):
    return x.get('distance', math.inf) #park all list entries w/o distance at the end

meteor_data.sort(key=get_dist) #get_dist func is being passed as a param VS being called

#step5:
print (meteor_data[0:10])
