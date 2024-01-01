from time import sleep
from machine import Pin
import onewire, ds18x20

import network

ssid = 'POCO F5'
password = '62741290'




station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

