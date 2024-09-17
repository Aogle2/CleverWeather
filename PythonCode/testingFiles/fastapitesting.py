from fastapi import FastAPI
import uvicorn as uc
app = FastAPI()

@app.get("/")
def Hello():
    data = {"message": "hello"}
    return data

#https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d

uc.run(
    "fastapitesting:app",
    host="0.0.0.0",
    reload=True

)
