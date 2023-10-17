import time
import network
from machine import Pin, Timer

networkPass = 'SevereNutAllergy0926'

# Declaring the LED Pin
led_pin = Pin('LED', Pin.OUT)

# Blinking to indicate successful startup
i=0
led_pin.value(0)
while i<3:
    i+=1
    led_pin.value(1)
    time.sleep(0.2)
    led_pin.value(0)
    time.sleep(0.2)

# Creating WLAN object
nic = network.WLAN()
nic.active(True)

# Scanning for WiFi networks
scan_results = nic.scan()
for net in scan_results:
    print(f'SSID: {net[0]}')

# Searching scan results for my network
good_network: Tuple = None
for temp_net in scan_results:
    ssid, bssid, channel, RSSI, security, hidden = temp_net
    if 'cheese' in str(ssid):
        good_network = temp_net
if good_network is None:
    print('Network not found')
    exit

# Attempting Connection...
print(f'Connecting to: {good_network[0]}...')
nic.connect(ssid=good_network[0], key=networkPass)
while not nic.isconnected():
    print('...')
    time.sleep(0.3)
if nic.isconnected():
    print(f'Successfully connected')
    print(f'Network information: {nic.ifconfig()}')
    led_pin.value(1)