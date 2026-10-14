# Connect to WiFi

Connecting your Pico to WiFi opens up all sorts of possibilities for networked applications.

The Pico W is WiFi enabled, so you can make networked and internet-connected projects!

## Add Your WiFi Credentials

Add your WiFi details to your settings.toml file, e.g:

```toml
CIRCUITPY_WIFI_SSID="YOURWIFISSID"
CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
```

Unplug your Pico from power and plug it back in for the settings to take effect.

## Add the Library

You need to add the network library. Copy **network.py** from the lib directory on github to the lib directory on the pico.

![Add library](add_lib.png)

## Code

Write this code and download to the Pico.

[See code on GitHub](https://github.com/lewfer/recipes-rpi-pico-circuitpython/blob/master/test_wifi.py)

```python
# Test wifi
#
# Make sure your wifi credentials are set up in settings.toml:
#
# CIRCUITPY_WIFI_SSID="YOURWIFISSID"
# CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
#

import network

# Create a network object
net = network.Network()

# Connect to the wifi
net.connectWifi()

#  Test network by pinging Google
ipv4 = network.ipaddress.ip_address("8.8.4.4")
pingTime = network.wifi.radio.ping(ipv4)
if pingTime!=None:
    print("Ping google.com: %f ms" % (pingTime*1000))
else:
    print("Could not ping Google")
```

Run the code. You should see a confirmation that the Pico is connected to your Wifi. You will also see some details of your device. The MAC address is the globally unique device ID for your Pico. The IP address is your Pico's address on the local network.

You will also see the time it takes to ping (i.e. send and receive a short message) to google.com. This just confirms your internet connection is working.

```
Connected to WiFi...
My MAC addr: ['0xe5', '0x5f', '0x3', '0xf0', '0x1c', '0xf9']
My IP address is 192.168.1.101
Ping google.com: 9.000000 ms
```