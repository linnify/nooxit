import json
from typing import Optional

from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse

from app.config import settings
from app.models import AuthLogin

router = APIRouter()


@router.post("/auth/login")
async def auth(data: AuthLogin, request: Request):
    """
    Redirect the user to the SSO Page
    """
    state = json.dumps({'success_url': data.redirect_page})
    
    authorize_url = f'{settings.AUTHORIZATION_URL}?response_type=code&response_mode=query&scope=openid'  # noqa
    authorize_url += f'&client_id={settings.CLIENT_ID}'
    authorize_url += f'&redirect_uri={request.base_url}auth/callback'
    authorize_url += f'&scope=${data.scope}'
    authorize_url += f'&state={state}'

    return {
        'authorization_url': authorize_url
    }


@router.get("/auth/callback")
async def auth_callback(code: Optional[str], state: Optional[str], error: Optional[str], error_description: Optional[str]):
    data = json.loads(state)
    redirect_url = data.get('success_url') # TODO Vlad Should we set the success_url the web default one
    
    if error:
        redirect_url += f"?error={error}&error_description={error_description}"
        return RedirectResponse(redirect_url)
    
    # TODO Parse the Code and get the user info and token

    user = {
        'email': "razvan.bretoiu@linnify.com",
        'token': 'asaxasasa'
    }
    redirect_url += f'?user={json.dumps(user)}'
    return RedirectResponse(redirect_url)
