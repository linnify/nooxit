from typing import List

from pydantic import BaseModel


class AuthLogin(BaseModel):
    scope: List[str]
    redirect_page: str
