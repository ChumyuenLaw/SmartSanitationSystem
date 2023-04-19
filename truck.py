import os
import requests
import json
import time
import numpy as np

# yG7QWdUFirLp9smggSpp truck 1
# qVq5MAEQGz4TdWuUKe3W truck 2

headers = {
    'Content-Type': 'application/json',
}

params = (
      ('clientKeys', 'fuel,longitude'),
      ('sharedKeys', 'shared1,shared2'),
      )

# 22.281843574803634 114.27959820739083 SENT Landfill

SENT_longitude = 114.27959820739083
SENT_latitude = 22.281843574803634

cityu_longitude = 114.173344
cityu_latitude = 22.335945

tst_longitude = 114.72344
tst_latitude = 22.297207

# truck 1 goes to cityu
range_longitude = np.linspace(SENT_longitude, cityu_longitude, 5)
range_latitude = np.linspace(SENT_latitude, cityu_latitude, 5)
os.system('curl -v -X POST --data "{"status": "Moving"}" https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes --header "Content-Type:application/json" ')
for i in range(5):
    data_telemetry = {"latitude": range_latitude[i], "longitude": range_longitude[i]} # initialization
    data_telemetry["latitude"] = range_latitude[i] # update
    data_telemetry["longitude"] = range_longitude[i] # update
    data_telemetry = json.dumps(data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/telemetry', headers=headers, data=data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes', headers=headers, data=data_telemetry)
    time.sleep(0.1)
os.system('curl -v -X POST --data "{"status": "Arrived"}" https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes --header "Content-Type:application/json" ')
time.sleep(1)
os.system('curl -v -X POST --data "{"status": "Collected"}" https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes --header "Content-Type:application/json" ')
time.sleep(1)
os.system('curl -v -X POST -d "{"weight": 0, "weightAlarmFlag": "false"}" https://thingsboard.cloud/api/v1/HJwEcNqs0ug0M2Zt4Io2/telemetry --header "Content-Type:application/json" ')

# truck 1 goes back to landfill
range_longitude = np.linspace(cityu_longitude, SENT_longitude + 0.01, 5)
range_latitude = np.linspace(cityu_latitude, SENT_latitude + 0.01, 5)
os.system('curl -v -X POST --data "{"status": "Moving"}" https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes --header "Content-Type:application/json" ')
for i in range(5):
    data_telemetry = {"latitude": range_latitude[i], "longitude": range_longitude[i]} # initialization
    data_telemetry["latitude"] = range_latitude[i] # update
    data_telemetry["longitude"] = range_longitude[i] # update
    data_telemetry = json.dumps(data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/telemetry', headers=headers, data=data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes', headers=headers, data=data_telemetry)
    time.sleep(0.1)
os.system('curl -v -X POST --data "{"status": "StandBy"}" https://thingsboard.cloud/api/v1/yG7QWdUFirLp9smggSpp/attributes --header "Content-Type:application/json" ')