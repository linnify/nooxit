from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.config import settings
from app.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])

app = FastAPI(
    title=settings.PROJECT_NAME
)
app.include_router(api_router)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
async def root():
    return {"message": "Ok"}
