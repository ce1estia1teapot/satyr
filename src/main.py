import time
import network
import ujson as json
from machine import Pin, Timer
from utilities import do_startup_blink

networkPass = 'SevereNutAllergy0926'

# Declarations
led_pin = Pin('LED', Pin.OUT)

nic = network.WLAN()
nic.active(True)

# Blinking to indicate successful startup
do_startup_blink(led_pin)

# Creating WLAN object



# Saving sample data (Times are seconds since epoch, 1970-01-01 00:00 UTC)
test_data = {}
for i in range(0, 400):
    test_data[str(time.gmtime())] = f'Test Point {i+1}'
    time.sleep(1.1)
print(f'Test Data: \n{test_data}')
with open('test_data.json', 'w') as file:
    print('Writing to file...')
    json.dump(test_data, file)
    print('Write successful!')
