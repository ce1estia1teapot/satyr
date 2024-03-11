import asyncio
import json
import random
import sys

import machine

sys.path.append("")

from datetime import datetime as DateTime
from machine import Pin
from src.utilities import DeviceSettings, do_startup_blink, format_measurement
from src.ble import file_server_ble_utilities

# ===== 1. Boot =====
# Defining LED Pin
led_pin = Pin("LED", Pin.OUT)
led_pin.off()
do_startup_blink(led_pin)

# Load settings and secrets
device_settings = DeviceSettings.initialize_from_files(p_config_fp="src/device_settings.json",
                                                       p_secrets_fp="src/secrets.json")
file_server_ble_utilities.set_device_settings(p_dev_settings=device_settings)

# ===== 2. Record a measurement from the sensor =====
async def main():
    # 2a. Gather measurement
    measured_value = random.randint(0, 10)
    creation_time = DateTime.now()

    measurement_dict = format_measurement(p_measurement=measured_value, p_device_settings=device_settings,
                                          p_creation_time=creation_time)

    # 2b. Add to records file
    try:
        with open(f'data/{creation_time.timestamp()}', 'a') as file:
            if file.writable():
                json.dump(measurement_dict)
    except OSError as e:
        print(e)
        pass

    # ===== 3. Begin Peripheral Task to Offload and Delete Records =====
    await file_server_ble_utilities.peripheral_task()


# ===== 4. Check with controller whether there are any updates for code or settings =====
asyncio.run(main(), debug=True)

# ===== 5. Once operations are complete, return to sleep until next wake =====
machine.deepsleep(device_settings.sleep_duration_s * 1000)
