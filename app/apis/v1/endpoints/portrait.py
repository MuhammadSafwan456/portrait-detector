# Third Party Imports
from fastapi import APIRouter

router = APIRouter()


@router.get("/upload/")
async def upload():
    return {"app": "Portrait API", "status": "Running"}
