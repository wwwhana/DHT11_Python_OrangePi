# DHT11 Python library (for Orange Pi WiringPi)

This simple class can be used for reading temperature and humidity values from DHT11 sensor on Orange pi SBCs.

Based on [szazo/DHT11_Python](https://github.com/szazo/DHT11_Python), and referenced from [somnisomni/DHT11_Python_Odroid](https://github.com/somnisomni/DHT11_Python_Odroid).

Tested on Orange pi zero 2w.

require [wiringOP-Python](https://github.com/orangepi-xunlong/wiringOP-Python)


# Installation

To install, clone this repository and setup:

```sh
$ git clone https://github.com/wwwhana/DHT11_Python_OP
$ cd DHT11_Python_OP
$ pip3 install .  # or with `sudo`
```

# Usage

1. Instantiate the `DHT11` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code.

For example:

```python
import wiringpi
import dht11

# initialize WiringPi
wiringpi.wiringPiSetup()

# read data using pin 4
instance = dht11.DHT11(pin = 4)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `example.py` (you probably need to adjust pin for your configuration)

# License

This project is licensed under the terms of the MIT license.
