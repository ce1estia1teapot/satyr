import sys

sys.path.append("")

from micropython import const
import uasyncio as asyncio
import aioble
import bluetooth

import random
import struct


# org.bluetooth.service.environmental_sensing
_ENV_SENSE_UUID = bluetooth.UUID(0x181A)
# org.bluetooth.characteristic.temperature
_ENV_SENSE_TEMP_UUID = bluetooth.UUID(0x2A6E)
# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_ENV_SENSOR = const(5696)

# Randomly generated UUIDs.
_FILE_SERVICE_UUID = bluetooth.UUID("0492fcec-7194-11eb-9439-0242ac130002")
_CONTROL_CHARACTERISTIC_UUID = bluetooth.UUID("0492fcec-7194-11eb-9439-0242ac130003")

# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000

def setup_connection_demo_ble():
    # 1. Create ENV_SENSE service
    env_sense_service = aioble.Service(_ENV_SENSE_UUID)

    # 2. Create ENV_SENSE_TEMP characteristic for service
    env_temp_sense_char = aioble.Characteristic(env_sense_service, _ENV_SENSE_TEMP_UUID, read=True, notify=True)

    # 3. Register service
    aioble.register_services(env_sense_service)


def setup_ble():
    print('Setting up BLE...')

    # 1. Create ENV_SENSE service
    file_service = aioble.Service(_FILE_SERVICE_UUID)

    # 2. Create ENV_SENSE_TEMP characteristic for service
    control_char = aioble.Characteristic(file_service, _CONTROL_CHARACTERISTIC_UUID, read=True, notify=True)

    # 3. Register service
    aioble.register_services(control_char)


# Serially wait for connections. Don't advertise while a central is
# connected.
async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_MS,
            name="Satyr Test",
            services=[_ENV_SENSE_UUID],
            appearance=_ADV_APPEARANCE_GENERIC_ENV_SENSOR,
        ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected()

