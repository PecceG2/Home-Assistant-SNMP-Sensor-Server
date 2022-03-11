
import sys, os
import json
from requests import get

sensorID = sys.argv[1]
SupervisorToken = os.environ["SUPERVISOR_TOKEN"]


url = "http://supervisor/core/api/states/"+sensorID
headers = {
    "Authorization": "Bearer "+SupervisorToken,
    "content-type": "application/json",
}

ha_sensor_data_request = get(url, headers=headers)
ha_sensor = json.loads(ha_sensor_data_request.text)

# Sensor state output
print(ha_sensor["state"])