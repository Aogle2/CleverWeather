import requests as req
import json
import os

r = req.get("http://localhost:8088/time")

print(r.__sizeof__())

for x,v in r.json().items():
    print(f"{x}:{v}")

if "machine_arc" in r.json():
    print("This has the correct key")


