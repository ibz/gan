# gan

Temperature sensor to be run on a simple Raspberry Pi OS-based machine (usually a Raspberry Pi Zero).

## Usage

* Use [`gan-gen`](https://github.com/ibz/gan-gen) to generate a minimal OS image you can use to run `gan` on.
* Flash the image to a Micro SD card:
  * On Linux you can use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (`rpi-imager`).
  * On Mac you can use [balenaEtcher](https://www.balena.io/etcher/).
* Boot your Pi Zero (with attached sensors - hot-plugging USB devices [might not always work](https://forums.raspberrypi.com/viewtopic.php?t=23205#p217196)!).
* SSH into the Pi.
* Generate a config file for digitemp. For example, if you have a single USB sensor, you can run `digitemp_DS9097 -i -s /dev/ttyUSB0`
* Download `gan`: `curl -sSL -o gan.zip https://github.com/ibz/gan/archive/refs/heads/master.zip && unzip gan.zip && rm gan.zip && mv gan-master gan`
* Set up a cronjob that reads the sensors. The data will be saved locally.
* You will need [`stasi`](https://github.com/ibz/stasi) to collect data from multiple `gan` sensors and generate graphs.
  * `mkdir ~/.ssh && chmod 700 ~/.ssh` then add the public key of the machine running `stasi` to `~/.ssh/authorized_keys`

## Supported sensors

* **USB-attached DS18B20 sensors**. These are nice because they don't require you messing with wires and (some) are waterproof. You can find them on eBay. The downside is they only measure temperature.
* [**BME280 Breakout**](https://shop.pimoroni.com/products/bme280-breakout) can measure temperature, humidity and pressure. You can buy it directly from Pimoroni.

## TODO

I use this system for my own home monitoring setup and it works fine, but it might not work for everyone nor is it easy enough to install for everyone.
