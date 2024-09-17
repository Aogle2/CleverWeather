from machine import Pin
import dht


# Class that reads the sensor and then returns two outputs, the temp an humidity)_

class TempHumiditySensor:
    # Configure the pin on this constructure as this is the first thing to do.
    def __init__(self, pin):
        self.gppin = Pin(pin, Pin.IN)
        self.sensor = dht.DHT11(self.gppin)

    # Read all of the sensor and return temp and humidity.
    def ReadSensorOverall(self):
        self.sensor.measure()
        temp = self.sensor.temperature()
        humidity = self.sensor.humidity()

        return temp, humidity

