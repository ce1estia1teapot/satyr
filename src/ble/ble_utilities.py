import sys

sys.path.append("")

from micropython import const
import uasyncio as asyncio
import aioble
import bluetooth

import random
import struct

# Randomly generated UUIDs.
_FILE_SERVICE_UUID = bluetooth.UUID("0492fcec-7194-11eb-9439-0242ac130002")
_CONTROL_CHARACTERISTIC_UUID = bluetooth.UUID("0492fcec-7194-11eb-9439-0242ac130003")

# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000

def setup_ble():
    # 1. Create ENV_SENSE service
    env_sense_service = aioble.Service(_ENV_SENSE_UUID)

    # 2. Create ENV_SENSE_TEMP characteristic for service
    env_temp_sense_char = aioble.Characteristic(env_sense_service, _ENV_SENSE_TEMP_UUID, read=True, notify=True)

    # 3. Register service
    aioble.register_services(env_sense_service)