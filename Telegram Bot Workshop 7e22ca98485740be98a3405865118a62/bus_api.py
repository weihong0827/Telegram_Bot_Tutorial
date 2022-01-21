import requests
import json
import time
import mpu

headers = {'AccountKey': 'sddcm97OSBWyyCWnAt+IoQ==',
           'accept': 'application/json'}
skip = 0
busStopList = []
busStopUrl = 'http://datamall2.mytransport.sg/ltaodataservice/BusStops'
response = requests.get(busStopUrl, headers=headers)
value = json.loads(response.content)['value']
while value:
    busStopList += value
    skip += 500
    busStopUrl = 'http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip={}'.format(
        skip)
    print(busStopUrl)
    response = requests.get(busStopUrl, headers=headers)
    print(response.content)
    value = json.loads(response.content)['value']
    time.sleep(1)


def get_bus_stops(my_cord):
    result = []
    for busStop in busStopList:

        distance = mpu.haversine_distance(
            my_cord, (busStop['Latitude'], busStop['Longitude']))
        if distance < 0.3:
            result.append(busStop)
    return result


def get_bus_arrival(busStopCode):
    url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={}'.format(
        busStopCode)
    response = requests.get(url, headers=headers)
    result = json.loads(response.content)['Services']
    return result
