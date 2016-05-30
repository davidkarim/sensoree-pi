#!/usr/bin/python

import requests
from datetime import datetime

import calendar
import time

# epochtime = calendar.timegm(time.gmtime())
# print epochtime

count = 0

while (count < 20):
  timestamp = datetime.now()
  print timestamp

  # Take temperature reading
  with open('/sys/bus/w1/devices/28-041623a757ff/w1_slave', 'r') as myfile:
    data=myfile.read().replace('\n', '')

  # Parse data and convert to Celsius
  temp = float(data.split("t=")[1]) / 1000
  temp_f = temp * 9 / 5 + 32
  print temp_f

  headers = {'Content-type': 'multipart/form-data', 'Accept': 'application/json'}
  r = requests.post("http://192.168.1.4:3000/events/create", data={"api_key":"NR71J65VHMH5WZ26A1K4", "sensor_id": 1, "value":temp_f, "notified":"false", "capture_time":timestamp}, headers=headers)
  print(r.status_code, r.reason)
  print(r.text[:10000] + '...')

  count = count + 1
  time.sleep(40)

print "Finished"
