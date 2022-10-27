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
async def read_clients():
    clients_data = await db["clients"].find().to_list(1000)
    clients = [client_helper(client) for client in clients_data]
    return JSONResponse(status_code=status.HTTP_200_OK, content=clients)

@app.get("/client/{client_id}")
async def read_client(client_id: str):
    client = await db["clients"].find_one({"_id": ObjectId(client_id)})
    return JSONResponse(status_code=status.HTTP_200_OK, content=client_helper(client))

@app.post("/")
async def add_client(client: Client):
    client = jsonable_encoder(client)
    new_client = await db["clients"].insert_one(client)
    id = new_client.inserted_id
    created_clinet = await db["clients"].find_one({"_id": id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=client_helper(created_clinet))

@app.put("/client/{client_id}")
async def update_client(client: UpdateClient, client_id: str):
    client = {k: v for k, v in client.dict().items() if v is not None}
    if len(client) >= 1:
        update_result = await db["clients"].update_one({"_id": ObjectId(client_id)}, {"$set": client})
        updated_client = await db["clients"].find_one({"_id": ObjectId(client_id)})
        return JSONResponse(status_code=status.HTTP_200_OK, content=client_helper(updated_client))
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "No data to update"})

@app.delete("/client/{client_id}")
async def delete_client(client_id: str):
    res = await db["clients"].delete_one({"_id": ObjectId(client_id)})
    if res.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client deleted successfully"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Client not found"})