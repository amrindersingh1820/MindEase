# backend/app/controllers/counseling_controller.py
from app.models.session_model import SessionCreate, Session
from app.database import get_db
from datetime import datetime

async def create_session(session: SessionCreate, user_id: str):
    db = get_db()
    session_dict = session.dict()
    session_dict["user_id"] = user_id
    session_dict["created_at"] = datetime.utcnow()
    result = await db.sessions.insert_one(session_dict)
    return {"id": str(result.inserted_id), **session_dict}