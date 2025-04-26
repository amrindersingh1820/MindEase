from fastapi import APIRouter, HTTPException, Depends
from app.models.mood_model import Mood
from app.controllers.mood_controller import create_mood, get_moods_by_user
from app.middlewares.auth_middleware import get_current_user

router = APIRouter()

@router.post("/moods", response_model=Mood)
async def add_mood(mood: Mood, current_user: str = Depends(get_current_user)):
    mood.user_id = current_user  # Associate the mood with the current user
    return await create_mood(mood)

@router.get("/moods", response_model=list[Mood])
async def list_moods(current_user: str = Depends(get_current_user)):
    moods = await get_moods_by_user(current_user)
    return moods