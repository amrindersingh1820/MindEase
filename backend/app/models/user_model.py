from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class Mood(BaseModel):
    id: str = None
    user_id: str
    mood: str
    created_at: datetime = None

    class Config:
        json_encoders = {ObjectId: str}