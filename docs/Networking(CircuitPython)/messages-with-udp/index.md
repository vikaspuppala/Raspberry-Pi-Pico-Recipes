# Send Messages with UDP

You can use UDP to send messages to of from another networked device, including another Pico.

UDP is a protocol from transmitting messages between networked devices. UDP is 'connectionless' which means that messages might not be received at the other end! But the protocol is fast. Compare this with TCP, where messages are reliably sent and received, but the messaging is slower. UDP can be used for remote control, e.g. for a robot. In this example, we see how to send messages between two Picos.

## Add Your WiFi Credentials

Add your WiFi details to your settings.toml file, e.g:

```toml id="h4n8vx"
CIRCUITPY_WIFI_SSID="YOURWIFISSID"
CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
```

Unplug your Pico from power and plug it back in for the settings to take effect.

## Add the Library

You need to add the network library. Copy **network.py** from the lib directory on github to the lib directory on the pico.

![Add library](add_lib.png)

## Code on the Sender Pico

```python id="y3kp8w"
# Test UDP send
#

import network
import time

print()
print("Connecting to WiFi")

# Edit host and port to match server
HOST = "192.168.1.150"
PORT = 5000
TIMEOUT = 5

# Connect to WIFI
net = network.Network()
net.connectWifi()

# Create sender to send messages
net.createSender(HOST, PORT)

net.sendMessage("Hello there")
time.sleep(0.1)
net.sendMessage("from another Pico!")
time.sleep(0.1)
net.sendMessage("stop")


net.closeSocket()
```

Change the IP address to match the IP address of the receiver Pico.

## Code on the Receiver Pico

```python id="p7b2mq"
# Test UDP receive
#

import network

PORT = 5000

# Connect to WIFI
net = network.Network()
net.connectWifi()

# Create receiver to listen for messages
net.createReceiver(PORT)

# Receive messages
message = ""
while message!="stop":
    message = net.receiveMessage()
    print("Received", message)

net.closeSocket()
```