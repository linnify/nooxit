import json
from typing import Optional

from fastapi import APIRouter, Request, Depends
from requests_oauthlib import OAuth2Session
from starlette.responses import RedirectResponse

from app.config import settings
from app.helpers.deps import get_current_user
from app.models import AuthLogin

router = APIRouter()


@router.post("/auth/login")
async def auth(data: AuthLogin, request: Request):
    """
    Return SSO Page URL
    """
    state = json.dumps({'success_url': data.redirect_page})
    scopes = " ".join(data.scope)
    
    authorize_url = f'{settings.AUTHORIZATION_URL}?response_type=code&response_mode=query'  # noqa
    authorize_url += f'&client_id={settings.CLIENT_ID}'
    authorize_url += f'&redirect_uri={settings.AUTHORIZATION_REDIRECT_URI}'
    authorize_url += f'&state={state}'
    authorize_url += f'&scope=openid email profile groups'

    return {
        'authorization_url': authorize_url
    }


@router.get("/auth/callback")
async def auth_callback(state: Optional[str], code: Optional[str] = None, error: Optional[str] = None, error_description: Optional[str] = None):
    data = json.loads(state)
    redirect_url = data.get('success_url')
    
    if error:
        redirect_url += f"?error={error}&error_description={error_description}"
        return RedirectResponse(redirect_url)
    
    oauth2 = OAuth2Session(
        settings.CLIENT_ID,
        redirect_uri=settings.AUTHORIZATION_REDIRECT_URI,
        state=state
    )
    token = oauth2.fetch_token(
        settings.AUTHORIZATION_TOKEN_URL,
        code=code,
        client_secret=settings.CLIENT_SECRET,
    )
    
    access_token = token.get('access_token')
    redirect_url += f'?token={access_token}'
    
    return RedirectResponse(redirect_url)


@router.get('/auth/profile')
def auth_profile(user=Depends(get_current_user)):
    return user
