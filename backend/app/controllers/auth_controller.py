from fastapi import HTTPException
from passlib.context import CryptContext
from app.models.user_model import User
from app.database import database

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user: User):
    user.hashed_password = pwd_context.hash(user.hashed_password)
    await database["users"].insert_one(user.dict())
    return user

async def get_user_by_email(email: str):
    user = await database["users"].find_one({"email": email})
    return user