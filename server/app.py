from fastapi import FastAPI
app = FastAPI()

from server.routes.client import router as ClientRouter

app.include_router(ClientRouter, tags=["Client"], prefix="/client")


@app.get("/", tags=["Home"])
def home():
    messgae = {
        "greetings": "Welcome to the Bots Fusion AI Assesment",
        "author": "Joy Almeida",
        "comment": "please visit https://joy-bots-fusion-ai.herokuapp.com/docs or https://github.com/J0SAL/bots-fusion-ai/blob/main/README.md"
    }
    return messgae

