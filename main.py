from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, K3s from FastAPI!"}


@app.get("/ping")
def read_root():
    return {"message": "ok"}
