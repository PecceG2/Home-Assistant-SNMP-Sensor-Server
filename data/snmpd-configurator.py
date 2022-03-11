#!/usr/bin/python

import sys, os
import json
from requests import get


configFile = sys.argv[1]
OIDPrefix = sys.argv[2]
SupervisorToken = os.environ["SUPERVISOR_TOKEN"]

configFileObject = open(configFile, 'a')

url = "http://supervisor/core/api/states"
headers = {
    "Authorization": "Bearer "+SupervisorToken,
    "content-type": "application/json",
}

ha_sensors_request = get(url, headers=headers)
ha_sensors = json.loads(ha_sensors_request.text)

for sensor in ha_sensors:
    sensorOID = OIDPrefix + sensor["entity_id"]
    configFileObject.write("extend " + sensorOID + " " + sensor["entity_id"] + " python3 get-sensor-data.py")
    print("Added SNMP sensor with OID: "+sensorOID)


configFileObject.close()