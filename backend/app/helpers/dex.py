import requests

from app.config import settings


class Dex:
    
    def __init__(
        self,
        token_type='bearer',
    ):
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET
        self.token_type = token_type
        
        super().__init__()
    
    def exchange(self, code: str):
        
        pass
    
    def user_profile(self, token: str):
        headers = {'Authorization': f'{self.token_type} {token}'}
        response = requests.get(settings.AUTHORIZATION_USER_INFO_URL, headers=headers)
        response.raise_for_status()
        
        return response.json()

