from fastapi import FastAPI
app = FastAPI()

from server.routes.client import router as ClientRouter

app.include_router(ClientRouter, tags=["Client"], prefix="/client")


@app.get("/", tags=["Home"])
def home():
    return {"message": "Bots Fusion AI"}

# app.include_router(client.router)
