
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from bson import ObjectId

from server.models.client import (
    Client,
    UpdateClient
)

from server.database import (
    clients
)

from server.app import app


# helpers
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
    
# routes
@app.get("/client")
async def read_clients():
    clients_data = await clients.find().to_list(1000)
    client_list = [client_helper(client) for client in clients_data]
    content = {
        "message": "List of clients",
        "clients": client_list
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

@app.get("/client/{client_id}")
async def read_client(client_id: str):
    client = await clients.find_one({"_id": ObjectId(client_id)})
    if client:
        content = {
            "message": "Client data",
            "client": client_helper(client)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})

@app.post("/client")
async def add_client(client: Client):
    client = jsonable_encoder(client)
    new_client = await clients.insert_one(client)
    id = new_client.inserted_id
    created_clinet = await clients.find_one({"_id": id})
    content = {
        "message": "Client created",
        "client": client_helper(created_clinet)
    }
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=content)

@app.put("/client/{client_id}")
async def update_client(client: UpdateClient, client_id: str):
    client = {k: v for k, v in client.dict().items() if v is not None}
    if len(client) >= 1:
        update_result = await clients.update_one({"_id": ObjectId(client_id)}, {"$set": client})
        updated_client = await clients.find_one({"_id": ObjectId(client_id)})
        if updated_client:
            content = {
                "message": "Client updated",
                "client": client_helper(updated_client)
            }
            return JSONResponse(status_code=status.HTTP_200_OK, content=content)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "No data to update"})

@app.delete("/client/{client_id}")
async def delete_client(client_id: str):
    res = await clients.delete_one({"_id": ObjectId(client_id)})
    if res.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client deleted successfully"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Client not found"})
