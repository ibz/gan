#!/usr/bin/python3

from datetime import datetime
import os

from bmp280 import BMP280
from smbus import SMBus

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

now = datetime.now()
temperature = bmp280.get_temperature()
pressure = bmp280.get_pressure()

filename = now.strftime("%Y-%m-%d.csv")

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("h,m,s,temperature,pressure\n")

with open(filename, 'a') as f:
    f.write("%d,%d,%d,%.2f,%.2f\n" % (now.hour, now.minute, now.second, temperature, pressure))


