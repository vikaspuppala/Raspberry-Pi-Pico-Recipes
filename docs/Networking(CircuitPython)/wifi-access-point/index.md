# WiFi Access Point

Rather than connecting your Pico to you WiFi, have the Pico create its own WiFi network.

Instead of joining an existing network, you can make your Pico become a standalone Wireless Access Point! It won’t have access to the internet, but you can connect to it from other devices.

## Clear Your Settings File

Remove all contents from settings.toml, so that your Pico doesn't try to connect to an existing WiFi network.

Unplug your Pico from power and plug it back in for the settings to take effect.

## Add the Library

You need to add the network library. Copy **network.py** from the lib directory on github to the lib directory on the pico.

![Add library](add_lib.png)

## Code

Write this code and download to the Pico.

[See code on GitHub](https://github.com/lewfer/recipes-rpi-pico-circuitpython/blob/master/test_wifi.py)

```python id="6gbt9v"
# Test wifi access point
#
# Make sure your settings.toml is empty
#

import network

# Create a network object
net = network.Network()

# Create a wireless access point, providing the SSID and password
net.startWifiAccessPoint("mypico","hellothere")
```

Run the code. You should see a confirmation that the access point is created. You can then connect to your Pico from a phone or computer.

```
Access point created with SSID: mypico, password: hellothere
My MAC addr: ['0xe5', '0x5f', '0x3', '0xf0', '0x1c', '0xf9']
IP address is 192.168.4.1
```