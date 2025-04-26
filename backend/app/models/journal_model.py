# backend/app/models/journal_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JournalBase(BaseModel):
    title: str
    content: str

class JournalCreate(JournalBase):
    pass

class Journal(JournalBase):
    id: Optional[str] = None
    user_id: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True