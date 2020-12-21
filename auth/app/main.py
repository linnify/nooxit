import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.endpoints import consent
from app.endpoints import login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(consent.router, tags=["consent"])

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
