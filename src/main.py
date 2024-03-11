import asyncio
import sys

sys.path.append("")

from machine import Pin
from src.utilities import DeviceSettings, do_startup_blink
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
# 2a. Gather measurement

# 2b. Add to records file

# ===== 3. Begin Peripheral Task to Offload and Delete Records =====
asyncio.gather()

# ===== 4. Update next wake time with specified cadence =====


# ===== 5. Check with controller whether there are any updates for code or settings =====


# ===== 6. Once operations are complete, return to sleep until next wake =====
