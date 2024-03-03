## this file is used to make changes to the user_preference collection 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from model import User




cred = credentials.Certificate('../gencalendar-9a8b4-firebase-adminsdk-tmzfi-82ec806343.json')
firebase_admin.initialize_app(cred)

# Get a reference to Firestore
db = firestore.client()
collection = db.collection('users')


async def fetch_one_user(user_id: int):
    document = await collection.where("user_id", "==", user_id).get()
    return document

async def fetch_all_users():
    users = []
    async for user in collection.stream():
        users.append(user.to_dict())
    return users

async def create_user(user: User):
    document = user
    await collection.add(document.dict())
    return document

async def update_user(user_id: int, user: User):
    await collection.where('user_id', '==', user_id).update(user.dict())
    document = await collection.where('user_id', '==', user_id).get()
    return document

async def remove_user(user_id: int):
    await collection.where('user_id', '==', user_id).delete()
    return True
