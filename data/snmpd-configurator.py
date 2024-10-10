#!/usr/bin/python

import sys, os
import json
import subprocess
from requests import get
import time

configFile = sys.argv[1]
OIDPrefix = sys.argv[2]
SupervisorToken = os.environ["SUPERVISOR_TOKEN"]

configFileObject = open(configFile, 'a')

url = "http://supervisor/core/api/states"
headers = {
    "Authorization": "Bearer "+SupervisorToken,
    "content-type": "application/json",
}


while True:
    ha_sensors_request = get(url, headers=headers)

    status_code = ha_sensors_request.status_code
    content_type = ha_sensors_request.headers.get('Content-Type', '')
    
    print(f"Response HTTP status code: {status_code}, Content-Type: {content_type}")
    
    if status_code == 200 and content_type.startswith('application/json'):
        try:
            ha_sensors = ha_sensors_request.json()
            break  # Exit if json decoded correctly
        except json.JSONDecodeError as e:
            print(f"Error ocurred trying decode JSON response: {e}")
    else:
        print("The supervisor has returned invalid information, waiting 5 seconds to retry...")

    time.sleep(5)

print("Generated SNMP OIDs:")
for sensor in ha_sensors:
    sensorID = sensor["entity_id"]

    # Generate OID
    sensorOID = subprocess.check_output('snmptranslate -On NET-SNMP-EXTEND-MIB::nsExtendOutput1Line.\\\"' + sensorID + '\\\"', shell=True, stderr=subprocess.STDOUT, text=True)

    # Save
    configFileObject.write("extend " + sensorID + " get-sensor-data-pyconvert.sh " + sensorID + '\n')
    print("Added SNMP sensor "+sensorID+" with OID: "+sensorOID)


configFileObject.close()