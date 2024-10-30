# Third Party Imports
from fastapi import APIRouter

# Local Imports
from app.apis.v1.endpoints import portrait

api_router = APIRouter()

api_router.include_router(portrait.router, prefix="/portrait", tags=["portrait"])
