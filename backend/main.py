# Third Party Imports
from fastapi import FastAPI

# Local Imports
from api.v1.router import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "Running"}


app.include_router(api_router, prefix="/api/v1")
