import urequests as requests
from machine import Pin
from time import sleep
import dht 
 
sensor = dht.DHT11(Pin(13))
 
while True:
  try:
    sleep(5)
    sensor.measure()
    temp= sensor.temperature()
    hum = sensor.humidity()
    
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    requests.get(url=f'https://hellvin.com.tr/eslamibots/nsm.php?temp={temp}')
    requests.get(url=f'https://hellvin.com.tr/eslamibots/nsm.php?temp={hum}')
   
    
  except OSError as e:
    print('Failed to read sensor.')