from fastapi import FastAPI
from .database import get_db
from .routes import auth_routes, mood_routes, meditation_routes, counseling_routes


app = FastAPI(title="MindEase Backend")

# Include routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Auth"])
app.include_router(mood_routes.router, prefix="/api", tags=["Moods"])
app.include_router(meditation_routes.router, prefix="/api", tags=["Meditations"])
app.include_router(counseling_routes.router, prefix="/api", tags=["Counseling"])

@app.get("/")
async def root():
    return {"message": "Welcome to MindEase Backend"}

@app.get("/health")
async def health_check():
    try:
        db = get_db()
        await db.list_collection_names()
        return {"status": "MongoDB Atlas connection successful"}
    except Exception as e:
        return {"status": "MongoDB Atlas connection failed", "error": str(e)}