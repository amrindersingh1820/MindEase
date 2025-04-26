# MindEase/backend/app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..controllers.auth_controller import authenticate_user, create_user, get_current_user  # Adjusted import
from ..models.user_model import UserCreate
from ..database import get_db
from datetime import timedelta
from ..config import JWT_SECRET, JWT_ALGORITHM
import jwt

router = APIRouter()

# ... rest of the code ...