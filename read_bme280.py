#!/usr/bin/python3

from datetime import datetime
import os

from bme280 import BME280
from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

bme280.setup(mode="forced")

now = datetime.now()
temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()

filename = now.strftime("%Y-%m-%d.csv")

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("ts,temperature,pressure,humidity\n")

with open(filename, 'a') as f:
    f.write("%d,%.2f,%.2f,%.2f\n" % (now.timestamp(), temperature, pressure, humidity))

