# backend/app/models/session_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SessionBase(BaseModel):
    session_type: str  # e.g., "meditation", "counseling"
    duration: int  # in minutes
    notes: Optional[str] = None

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: Optional[str] = None
    user_id: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True