from app.models.mood_model import Mood
from app.database import database

async def create_mood(mood: Mood):
    mood.created_at = datetime.utcnow()
    await database["moods"].insert_one(mood.dict())
    return mood