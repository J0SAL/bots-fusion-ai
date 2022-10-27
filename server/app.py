from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

from server.routes.client import *
# app.include_router(client.router)
