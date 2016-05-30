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

  # Send ping request to a host, this example uses google
  hostname = "google.com"
  response = os.popen("ping -c 1 " + hostname).read()

  # Parse data to retrieve response time in ms  
  ping_time = response.split("time=")[1].split(" ms")[0]
  print ping_time + " ms"

  headers = {'Content-type': 'multipart/form-data', 'Accept': 'application/json'}
  r = requests.post("http://192.168.1.14:3000/events/create", data={"api_key":"NR71J65VHMH5WZ26A1K4", "sensor_id": 19, "value":ping_time, "notified":"false", "capture_time":timestamp}, headers=headers)
  print(r.status_code, r.reason)
  print(r.text[:10000] + '...')

  count = count + 1
  time.sleep(40)

print "Finished"
