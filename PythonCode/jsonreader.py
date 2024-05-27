import json
import os

#need to figure out file pathing and how to make it more dynamic.
file = os.path.join(os.getcwd(),"Configuration","BaseDBConfiguration.json")

try:
    with open(file) as f:
        json_file = json.load(f)
        print(json_file)
except FileNotFoundError:
    print(f"file {file} is not present.")