#!/usr/bin/python

import sys, os
import json
import subprocess
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
    sensorID = sensor["entity_id"]

    if sensorID == "sun.sun":
        sensorOID = "1.1.1.1.1.1.1.1.1.1"
    else:
        sensorOID = OIDPrefix+sensorID
    # Generate OID
    #extOID = subprocess.Popen(["snmpget", "", "-arg2"])



    # Save
    configFileObject.write("extend " + sensorOID + " " + sensorID + " python3 get-sensor-data.py")
    print("Added SNMP sensor "+sensorID+" with OID: "+sensorOID)


configFileObject.close()