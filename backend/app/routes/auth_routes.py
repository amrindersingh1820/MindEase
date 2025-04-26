from fastapi import APIRouter
from app.controllers.auth_controller import create_user

router = APIRouter()

@router.post("/register")
async def register(user: User):
    return await create_user(user)