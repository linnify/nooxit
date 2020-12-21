from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse

from app.hydra import Hydra
from db import find_by_email_and_password

router = APIRouter()
templates = Jinja2Templates("app/templates")
hydra = Hydra()


@router.get("/login", response_class=HTMLResponse)
def login(login_challenge: str, request: Request):
    if login_challenge is None:
        return
    
    data = hydra.get_login_request(login_challenge)
    if data.skip:
        # Hydra already authenticate the user, skip the login
        return RedirectResponse(hydra.get_redirect_url(login_challenge, data.subject))
    
    # If the authentication can be skipped we MUST show the UI login
    
    return templates.TemplateResponse('login.html', {
        'request': request,
        'challenge': login_challenge,
        'hint': data.oidc_context.login_hint or '',
    })


@router.post('/login', response_class=HTMLResponse)
def handle_login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    challenge: str = Form(...),
    submit: str = Form(...)
):
    
    if submit == 'cancel':
        # User denied the login
        redirect_login = hydra.reject_login_request(challenge)
        return RedirectResponse(redirect_login, status_code=status.HTTP_303_SEE_OTHER)
    
    user = find_by_email_and_password(email, password)
    
    if not user:
        return templates.TemplateResponse('login.html', {
            'request': request,
            'challenge': challenge,
            'error': 'The email / password combination is not correct'
        })
    
    redirect_url = hydra.accept_login_request(challenge, email)
    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
