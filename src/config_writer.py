import ujson as json
import time

tempConfig = {
    'network_ssid': '',
    'test_string': 'this is a test string'
    }

try:
    with open('config.json', 'w') as file:
        json.dump(tempConfig, file)
except e:
    print(f'Failed to open config file: {e}')