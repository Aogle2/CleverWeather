import network as nw


class Connection():
    def __init__(self, ssid, password):
        self.wifiName = ssid
        self.wifipass = password
        print(f"{self.wifiName} will be connected to...")

    def ConnectNow(self):
        wlan = nw.WLAN(nw.STA_IF)
        wlan.active(True)
        wlan.connect(self.wifiName, self.wifipass)






