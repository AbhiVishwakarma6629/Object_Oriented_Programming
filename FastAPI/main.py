from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

app = FastAPI()

client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.user_database
collection = db.users


class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user.get("age")
    }


@app.post("/users/", response_model=User)
async def create_user(user: User):
    user_dict = user.dict()
    result = await collection.insert_one(user_dict)
    new_user = await collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)


@app.get("/users/", response_model=List[User])
async def list_users():
    users = []
    async for user in collection.find():
        users.append(user_helper(user))
    return users


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, updated_user: User):
    result = await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": updated_user.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    user = await collection.find_one({
        "_id": ObjectId(user_id)
    })
    return user_helper(user)
