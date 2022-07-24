#!/usr/bin/python3

from datetime import datetime
import os

import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

now = datetime.now()
temperature = dht_device.temperature
humidity = dht_device.humidity

filename = now.strftime("%Y-%m-%d.csv")

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("ts,temp,humid\n")

with open(filename, 'a') as f:
    f.write("%d,%.2f,%.2f\n" % (now.timestamp(), temperature, humidity))

