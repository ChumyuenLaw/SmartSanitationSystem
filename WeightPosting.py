import os
import requests
import json
import time
import random

headers = {
    'Content-Type': 'application/json',
}

# access token
# HJwEcNqs0ug0M2Zt4Io2 CityU
# bF1QWEhwdjqTPYstGaV5 Tsim Sha Tsui
# B4tAmO4IAAokfUmkpk9x Mong Kok
# qb92jB8fGh4f8LPZw4sl Sham Shui Po

##Telemetry upload
weight = 0
for i in range(100):
    data_telemetry = {"weight": weight}  # initialization
    weight += random.randint(1, 20)
    data_telemetry["weight"] = weight # update
    data_telemetry = json.dumps(data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/HJwEcNqs0ug0M2Zt4Io2/telemetry', headers=headers, data=data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/bF1QWEhwdjqTPYstGaV5/telemetry', headers=headers, data=data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/B4tAmO4IAAokfUmkpk9x/telemetry', headers=headers, data=data_telemetry)
    requests.post('https://thingsboard.cloud/api/v1/qb92jB8fGh4f8LPZw4sl/telemetry', headers=headers, data=data_telemetry)
    time.sleep(0.1)