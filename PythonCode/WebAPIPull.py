import requests as req

r = req.get("http://localhost:8088")

print(r.json()["machine_arc"])

