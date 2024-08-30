#Used to incorporate the sensors that are to be used on teh Pi Pico and make things easier?


#DHT code to get started with, Pins are confusing on these things https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi-pico/#:~:text=Before%20starting%20to%20connect%20components%20to%20the%20GPIO,of%20the%20sensor%20to%203V3%20%28OUT%29%20%28red%20wire%29

#Function to start with:

#need to do a few things, error catching and a bit more explanation of how this works and why.
from machine import Pin
from time import sleep
import dht

dht_pin = Pin(2, Pin.IN)
sensor = dht.DHT11(dht_pin)


sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()
print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))

def get_temp(pin):
    sensor = dht.DHT11(Pin(pin,Pin.IN))

    def convert_to_fahrenheit(celsius):
        return (celsius * 9/5) +32

    sensor.measure()




