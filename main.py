from typing import Optional
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel
from bson import ObjectId

import motor.motor_asyncio
import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#database
db = client.company

#Models 
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

#helpers
def client_helper(client) -> dict:
    return {
        "id": str(client["_id"]),
        "name": client["name"],
        "email": client["email"],
        "mobile": client["mobile"],
        "dob": client["dob"],
        "city": client["city"],
        "gender": client["gender"]
    }

@app.get("/")
def read_clients():
    return {"Hello": []}

@app.get("/client/{client_id}")
def read_client(client_id: int):
    return {"client": clients[client_id]}

@app.post("/")
async def add_client(client: Client):
    client = jsonable_encoder(client)
    new_client = await db["clients"].insert_one(client)
    id = new_client.inserted_id
    created_clinet = await db["clients"].find_one({"_id": id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=client_helper(created_clinet))

@app.put("/client/{client_id}")
def update_client(client: Client, client_id: int):
    return {"Put": client}

@app.delete("/client/{client_id}")
def delete_client(client_id: int):
    return {"Delete": clients[client_id]}