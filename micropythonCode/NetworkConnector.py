#Just getting things setup and orgainized.

import network as nw


class NewConnection:
    def __init__(self,ssid,password):
        self.wifiname = ssid
        self.wifipass = password

    def ConnectNow(self):
        wlan = nw.WLAN(nw.STA_IF)
        wlan.active(True)
        wlan.connect(self.wifiname,self.wifipass)


            