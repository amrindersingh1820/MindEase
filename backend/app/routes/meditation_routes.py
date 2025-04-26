# backend/app/routes/meditation_routes.py
from fastapi import APIRouter, Depends
from app.models.session_model import SessionCreate, Session
from app.controllers.counseling_controller import create_session
from app.middlewares.auth_middleware import get_current_user

router = APIRouter()

@router.post("/meditations", response_model=Session)
async def create_meditation(session: SessionCreate, user_id: str = Depends(get_current_user)):
    session.session_type = "meditation"
    return await create_session(session, user_id)