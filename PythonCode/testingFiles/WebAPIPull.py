import requests as req
import json
import os


def checkwebserver(server):
    r = req.get("http://"+server+":8088")
    if r.status_code == 200:
        print(f"{server} is up and able to be read.")

checkwebserver("localhost")


r = req.get("http://localhost:8088/cpu")
print(r.status_code)
print(r.encoding)
print(r.headers)

print(r.__sizeof__())
print(r)
#for x,v in r.json().items():
#    print(f"{x}:{v}")
#
#if "machine_cpu" in r.json():
#    print("This has the correct key")
#
#if "python_version" in r.json():
#    print("This has the needed key")
#jsonfile = r.json()
#print(jsonfile['machine_cpu'][0]['arch'])
#
#
