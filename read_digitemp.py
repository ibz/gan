#!/usr/bin/python3

from datetime import datetime
import os
import sys

COMMANDS = [
        "digitemp_DS9097 -c  ~/.digitemprc-0 -q -s /dev/ttyUSB0 -t 0 -o 4 | sed 's/\\t/,/g'",
        "digitemp_DS9097 -c  ~/.digitemprc-1 -q -s /dev/ttyUSB1 -t 0 -o 4 | sed 's/\\t/,/g'"
]

if __name__ == '__main__':
    sensor = int(sys.argv[1])
    ts, temp = os.popen(COMMANDS[sensor]).readline().strip().split(',')
    d = datetime.fromtimestamp(int(ts))
    temp = float(temp)

    filename = d.strftime("%Y-%m-%d.csv")
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("ts,temp\n")
    with open(filename, 'a') as f:
        f.write("%d,%.2f\n" % (d.timestamp(), temp))

