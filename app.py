-----------------------------------------------
import logging
from fastapi import FastAPI
from backend.config import Config

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app: FastAPI = FastAPI()

@app.on_event("startup")
def startup_event() -> None:
    logger.info("Starting up the application")
    # Load configuration
    Config.load()

@app.on_event("shutdown")
def shutdown_event() -> None:
    logger.info("Shutting down the application")

@app.get("/")
def read_root() -> dict:
    logger.info("Root endpoint called")
    return {"message": "Welcome to the API"}

# Import routers
from backend.controllers.users.user_controller import router as user_router
from backend.controllers.auth.auth_controller import router as auth_router

# Include routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])