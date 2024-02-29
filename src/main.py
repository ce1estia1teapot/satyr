import sys
sys.path.append("")

import aioble
import uasyncio as asyncio
import bluetooth
import ujson as json
import mip
import network
import random
import struct
import time

from machine import Pin, Timer
from micropython import const
from utilities import do_startup_blink, network_scan_for_ssid, network_connect_by_ssid

# Load secrets
with open("secrets.json", 'r') as file:
    secrets = json.load(file)

# Defining LED Pin and setting to off
led_pin = Pin("LED", Pin.OUT)
led_pin.off()

# Defining Network
nic = network.WLAN(network.STA_IF)
nic.active(True)

# Connect to Network and turn on LED if connected
found_ssid: str = network_scan_for_ssid(nic, 'cheese')[0]
is_connected_wifi: bool = network_connect_by_ssid(p_network=nic, p_ssid=found_ssid, p_pass=secrets['network_password'])
if not is_connected_wifi:
    print('Not connected to wifi')
    sys.exit()



