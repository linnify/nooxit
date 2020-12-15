from fastapi import FastAPI, APIRouter, Depends
from fastapi.openapi.models import OAuthFlows, OAuthFlowAuthorizationCode
from fastapi.security import OAuth2, OpenIdConnect
from starlette.middleware.cors import CORSMiddleware

from app.config import settings
from app.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)

oauth2_scheme = OAuth2(
    flows=OAuthFlows(
        authorizationCode=OAuthFlowAuthorizationCode(
            authorizationUrl=settings.AUTHORIZATION_URL,
            tokenUrl=settings.AUTHORIZATION_TOKEN_URL,
            scopes={
                'openid': 'OpenID',
                'email': 'Email',
                'profile': 'Profile',
                'offline_access': 'Offline Access',
            }
        ),
        
    )

)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    print(token)

    return {"message": "Ok"}
