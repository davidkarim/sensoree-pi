#!/usr/bin/python

import requests
from datetime import datetime

import calendar
import time
import os

# epochtime = calendar.timegm(time.gmtime())
# print epochtime

count = 0

while (count < 20):
  timestamp = datetime.now()
  print timestamp

  # Send ping request to a host, this example uses sensoree
  hostname = "sensoree.net"
  response = os.popen("ping -c 1 " + hostname).read()

  # Parse data to retrieve response time in ms  
  ping_time = response.split("time=")[1].split(" ms")[0]
  print ping_time + " ms"

  headers = {'Content-type': 'multipart/form-data', 'Accept': 'application/json'}
  r = requests.post("http://www.sensoree.net/events/create", data={"api_key":"HVL9BWCA6KE06IMRGL21", "sensor_id": 9, "value":ping_time, "notified":"false", "capture_time":timestamp}, headers=headers)
  print(r.status_code, r.reason)
  print(r.text[:10000] + '...')

  count = count + 1
  time.sleep(40)

print "Finished"
