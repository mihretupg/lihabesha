from fastapi import APIRouter
from app.api.routes import auth, housing, jobs, travel, community, moderation, admin

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(housing.router)
api_router.include_router(jobs.router)
api_router.include_router(travel.router)
api_router.include_router(community.router)
api_router.include_router(moderation.router)
api_router.include_router(admin.router)
