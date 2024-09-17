import network as nw
import machine


class Connection():
    def __init__(self, ssid, password):
        self.wifiName = ssid
        self.wifipass = password
        print(f"{self.wifiName} will be connected to...")

    def ConnectNow(self):
        wlan = nw.WLAN(nw.STA_IF)
        wlan.active(True)
        wlan.connect(self.wifiName, self.wifipass)

        while wlan.isconnected():




#implement part of this here: https://programmingdigest.com/getting-started-with-raspberry-pi-pico-w-built-in-wifi/#:~:text=If%20the%20Pico%20W%20is%20not%20connected%20to,status%20messages%2C%20will%20be%20displayed%20on%20the%20console.



