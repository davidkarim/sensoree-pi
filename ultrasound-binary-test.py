#!/usr/bin/env python

import requests
from datetime import datetime
import calendar
import RPi.GPIO as GPIO
import time

# These are the Pi header pin numbers; they correspond to GPIO 17 and 18
TRIG = 11
ECHO = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	counter = 60
	while True:
		counter = counter - 1
		timestamp = datetime.now()
		dis = distance()
		if dis > 200:
			dis = 1
		else:
			dis = 0
		print dis
		print ''
		time.sleep(0.5)
		if counter == 0:
			print timestamp
			counter = 60
			headers = {'Content-type': 'multipart/form-data', 'Accept': 'application/json'}
			r = requests.post("http://192.168.1.5:3000/events/create", data={"api_key":"NR71J65VHMH5WZ26A1K4", "sensor_id": 2, "value":dis, "notified":"false", "capture_time":timestamp}, headers=headers)
			print(r.status_code, r.reason)
  			print(r.text[:10000] + '...')

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
