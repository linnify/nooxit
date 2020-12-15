from fastapi import APIRouter

router = APIRouter()


@router.get("/auth/login")
async def auth():
    print('Generate OAuth Redirect link')
    
    return {
        "redirect_link": "http://....."
    }


@router.get("/auth/callback")
async def auth_callback():
    
    print('Auth Callback auth flow')
    return {}
