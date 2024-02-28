from fastapi import FastAPI, HTTPException
from model import User
from database import(
    fetch_one_user,
    fetch_all_users,
    create_user,
    update_user,
    remove_user
)

from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{user_id}", response_model=User)
async def get_user_by_user_id(user_id: int):
    user = await fetch_one_user(user_id)
    if user:
        return user
    raise HTTPException(404, f"User {user_id} not found")

@app.get("/users", response_model=list[User])
async def get_all_users():
    users = await fetch_all_users()
    return users

@app.post("/users", response_model=User)
async def post_user(user: User):
    if not user.user_id:
        raise HTTPException(400, "The user_id is required")
    existing_user = await fetch_one_user(user.user_id)
    if existing_user:
        raise HTTPException(400, f"User with user_id {user.user_id} already exists")


    response = await create_user(user.dict()) 
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/users/{user_id}", response_model=User)
async def put_user(user_id: int, user: User):
    response = await update_user(user_id, user)
    if response:
        return response
    raise HTTPException(404, f"User {user_id} not found")

@app.delete("/users/{user_id}")

async def delete_user(user_id: int):
    response = await remove_user(user_id)
    if response:
        return "Successfully deleted user"
    raise HTTPException(404, f"User {user_id} not found")