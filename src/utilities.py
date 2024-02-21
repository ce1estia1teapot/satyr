import time
import network
import ujson as json

from machine import Pin, Timer
from network import WLAN

def do_startup_blink(p_pin):
    i=0
    p_pin.value(0)
    while i<3:
        i+=1
        p_pin.value(1)
        time.sleep(0.2)
        p_pin.value(0)
        time.sleep(0.2)

def network_scan_for_ssid(p_network=None, p_ssid=None):
    """
    Scans for available networks whose SSID match the provided SSID
    
    p_network: a WLAN object from Network library. Used for scanning
    p_ssid: str SSID of the desired network
    
    returns: bool representing whether the provided SSID represents a valid network
    """
    
    # Scanning for WiFi networks
    scan_results = p_network.scan()
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
    

def network_connect_by_ssid(p_network=None, p_ssid=None, p_pass=None, p_numAttempts=10):
    """
    p_network: a WLAN object from Network library
    p_ssid: A str representing the SSID of the desired network
    p_numAttempts: An int number of times to attempt connection before reporting failure
    
    returns:
    """
    if p_network is None:
        return None
    if p_ssid is None:
        return None
    if p_pass is None:
        return None
    
    # Attempting Connection...
    print(f'Connecting to: {good_network[0]}...')
    p_network.connect(ssid=good_network[0], key=networkPass)
    while not nic.isconnected():
        print('...')
        time.sleep(0.3)
    if p_network.isconnected():
        print(f'Successfully connected')
        print(f'Network information: {p_network.ifconfig()}')
