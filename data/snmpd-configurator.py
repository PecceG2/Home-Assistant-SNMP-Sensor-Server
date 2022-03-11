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

print("Generated SNMP OIDs:")
for sensor in ha_sensors:
    sensorID = sensor["entity_id"]

    # Generate OID
    sensorOID = subprocess.check_output('snmptranslate -On NET-SNMP-EXTEND-MIB::nsExtendOutput1Line.\\\"' + sensorID + '\\\"', shell=True, stderr=subprocess.STDOUT, text=True)

    # Save
    configFileObject.write("extend " + sensorID + " get-sensor-data-pyconvert.sh " + sensorID + '\n')
    print("Added SNMP sensor "+sensorID+" with OID: "+sensorOID)


configFileObject.close()