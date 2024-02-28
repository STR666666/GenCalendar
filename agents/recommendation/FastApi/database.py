import motor.motor_asyncio
from model import User
from collections.abc import MutableMapping

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database=client.User
collection=database.user_preference

async def fetch_one_user(user_id: int):
    document = await collection.find_one({"user_id": user_id})
    return document

async def fetch_all_users():
    users = []
    async for document in collection.find({}):
        users.append(User(**document))
    return users

async def create_user(user: User):
    document = user
    await collection.insert_one(document)
    return document

async def update_user(user_id: int, user: User):
    await collection.update_one({"user_id": user_id}, {"$set": user.dict()})
    document = await collection.find_one({"user_id": user_id})
    return document

async def remove_user(user_id: int):
    await collection.delete_one({"user_id": user_id})
    return True
