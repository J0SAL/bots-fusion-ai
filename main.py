from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId

import motor.motor_asyncio
import os

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.college


class Client(BaseModel):
    name: str
    email: str
    mobile: str
    dob: str
    city: str
    gender: str

class UpdateClient(BaseModel):
    name: Optional[str]
    email: Optional[str]
    mobile: Optional[str]
    dob: Optional[str]
    city: Optional[str]
    gender: Optional[str]

@app.get("/")
def read_clients():
    return {"Hello": []}

@app.get("/client/{client_id}")
def read_client(client_id: int):
    return {"client": clients[client_id]}

@app.post("/")
def add_client(client: Client):
    return {"Hello": client}

@app.put("/client/{client_id}")
def update_client(client: Client, client_id: int):
    return {"Put": client}

@app.delete("/client/{client_id}")
def delete_client(client_id: int):
    return {"Delete": clients[client_id]}