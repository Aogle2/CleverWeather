from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Hello():
    data = {"message": "hello"}
    return data