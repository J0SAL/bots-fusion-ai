
import motor.motor_asyncio
import os

from dotenv import load_dotenv
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.company

#collections
clients = db["clients"]
