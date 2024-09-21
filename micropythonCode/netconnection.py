import network as nw
import machine
import errno
from time import sleep
import _thread as thread


class Connection():
    def __init__(self, ssid, password):
        self.wifiName = ssid
        self.wifipass = password
        self.OnboardLED = machine.Pin("LED", machine.Pin.OUT)
        print(f"{self.wifiName} will be connected to...")

    async def ToggleLED(self):
        self.OnboardLED.toggle()

    async def BlinkLED(self):
        pass

    def ConnectNow(self):
        wlan = nw.WLAN(nw.STA_IF)
        wlan.active(True)
        wlan.connect(self.wifiName, self.wifipass)

        if wlan.status() == 1:
            print(f"Incorrect Password for {self.wifiName}")
            self.BlinkLED()

        if wlan.status() == 3:
            print(f"Device is connected ")

        if wlan.isconnected():
            self.ToggleLED()

# implement part of this here: https://programmingdigest.com/getting-started-with-raspberry-pi-pico-w-built-in-wifi/#:~:text=If%20the%20Pico%20W%20is%20not%20connected%20to,status%20messages%2C%20will%20be%20displayed%20on%20the%20console.





