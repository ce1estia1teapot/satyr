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
from ble.ble_utilities import setup_connection_demo_ble, peripheral_task

# Load secrets
with open("secrets.json", 'r') as file:
    secrets = json.load(file)

# Load

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

# ===== BLUETOOTH SECTION =====
# 1. Setup BLE
setup_connection_demo_ble()

# 2. Run peripheral task
asyncio.run(peripheral_task())