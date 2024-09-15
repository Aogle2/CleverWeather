from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Hello():
    data = {"message": "hello"}
    return data

#https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d