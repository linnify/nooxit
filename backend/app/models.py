from pydantic import BaseModel


class AuthLogin(BaseModel):
    scope: str
    redirect_page: str
