# gan

`gan` includes some very simple scripts that read data from temperature sensors and save this data locally in CSV files. It is intended to be run on simple Raspberry Pi OS-based machines (usually Raspberry Pi Zero) with attached sensors.

[`stasi`](https://github.com/ibz/stasi) will be used to centralize data from multiple `gan` sensors and generate graphs.

## Supported sensors

* **USB-attached DS18B20 sensors**. These are nice because they don't require you messing with wires and (some) are waterproof. You can find them on eBay. The downside is they only measure temperature.
* [**BME280 Breakout**](https://shop.pimoroni.com/products/bme280-breakout) can measure temperature, humidity and pressure. You can buy it directly from Pimoroni.

## Usage

* Use [`gan-gen`](https://github.com/ibz/gan-gen) to generate a minimal OS image which includes `gan`.
* Flash the image to a Micro SD card:
  * On Linux you can use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (`rpi-imager`).
  * On Mac you can use [balenaEtcher](https://www.balena.io/etcher/).
* Boot your Pi Zero (with attached sensors - hot-plugging USB devices [might not always work](https://forums.raspberrypi.com/viewtopic.php?t=23205#p217196)!).
* SSH into the Pi.
* If using the DS18B20 USB sensor, you will be using `digitemp` to read the data. `digitemp` is already installed on the SD card from `gan-gen`, but it needs a config file.
  * Generate a config file for digitemp. For example, if you have a single USB sensor, you can run `digitemp_DS9097 -i -s /dev/ttyUSB0 && mv ~/.digitemprc ~/.digitemprc-0`
* Create a directory to store the data files: `mkdir -p /home/gan/data/<SENSOR_NAME>`.
* Set up a cronjob that reads the sensors. The data will be saved locally.
  * For example: `* * * * * cd /home/gan/data/<SENSOR_NAME> && python3 /home/gan/gan/read_digitemp.py 0`
* You will need [`stasi`](https://github.com/ibz/stasi) to collect data from multiple `gan` sensors and generate graphs.
  * `mkdir ~/.ssh && chmod 700 ~/.ssh` then add the public key of the machine running `stasi` to `~/.ssh/authorized_keys`

## TODO

I use this system for my own home monitoring setup and it works fine, but it might not work for everyone nor is it easy enough to install for everyone.
