import os

headers = {
    'Content-Type': 'application/json',
}

# access token
# HJwEcNqs0ug0M2Zt4Io2 CityU
# bF1QWEhwdjqTPYstGaV5 Tsim Sha Tsui
# B4tAmO4IAAokfUmkpk9x Mong Kok
# qb92jB8fGh4f8LPZw4sl Sham Shui Po

##Telemetry upload
os.system('curl -v -X POST -d "{"weight": 900, "weightAlarmFlag": "true"}" https://thingsboard.cloud/api/v1/HJwEcNqs0ug0M2Zt4Io2/telemetry --header "Content-Type:application/json" ')
os.system('curl -v -X POST -d "{"weight": 1100, "weightAlarmFlag": "true"}" https://thingsboard.cloud/api/v1/bF1QWEhwdjqTPYstGaV5/telemetry --header "Content-Type:application/json" ')
os.system('curl -v -X POST -d "{"weight": 300, "weightAlarmFlag": "false"}" https://thingsboard.cloud/api/v1/B4tAmO4IAAokfUmkpk9x/telemetry --header "Content-Type:application/json" ')
os.system('curl -v -X POST -d "{"weight": 200, "weightAlarmFlag": "false"}" https://thingsboard.cloud/api/v1/qb92jB8fGh4f8LPZw4sl/telemetry --header "Content-Type:application/json" ')
