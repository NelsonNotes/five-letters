from fastapi import APIRouter

from app.api.api_v1.endpoints import login, user, word, attempt

api_router_v1 = APIRouter()
PREFIX_V1: str = "/api/v1"
api_router_v1.include_router(login.router, prefix="/login", tags=["login"])
api_router_v1.include_router(user.router, prefix="/user", tags=["user"])
api_router_v1.include_router(word.router, prefix="/word", tags=["word"])
api_router_v1.include_router(
    attempt.router, prefix="/attempt", tags=["attempt"])
