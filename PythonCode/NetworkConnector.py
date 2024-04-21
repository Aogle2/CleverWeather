#Just getting things setup and orgainized.

import network as nw

def ConnectWIFI(ssid,password): #Yes, I know this may not be PEP8 ready, I just want to get my thoughts on here first.
    wlan = nw.WLAN(nw.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    counter = 0

    while not wlan.isconnected():
        if counter > 0:
            print(f"Trying to connect to: {ssid}\r")

        else:
            counter += 1


            