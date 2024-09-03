import requests as req
import json
import os

r = req.get("http://localhost:8088/cpu")

print(r.__sizeof__())

for x,v in r.json().items():
    print(f"{x}:{v}")

if "machine_cpu" in r.json():
    print("This has the correct key")

if "python_version" in r.json():
    print("This has the needed key")
jsonfile = r.json()
print(jsonfile['machine_cpu'][0]['arch'])


