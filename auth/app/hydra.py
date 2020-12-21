from ory_hydra_client import Configuration, ApiClient, AdminApi, LoginRequest, \
    CompletedRequest

from app.config import settings


class Hydra:
    
    def __init__(self):
        configuration = Configuration(host=settings.HYDRA_ADMIN_URL)
        client = ApiClient(configuration=configuration)
        self.client = AdminApi(api_client=client)
    
    def get_login_request(self, challenge) -> LoginRequest:
        return self.client.get_login_request(challenge)
    
    def get_redirect_url(self, challenge, subject) -> str:
        data: CompletedRequest = self.client.accept_login_request(challenge, subject=subject)
        return data.redirect_to
    
    def reject_login_request(self, challenge):
        body = {
            'error': 'access_denied',
            'error_description': 'The resource owner denied the request'
        }
        data: CompletedRequest = self.client.reject_login_request(challenge, body=body)
        return data.redirect_to
    
    def accept_login_request(self, challenge: str, email: str) -> str:
        
        login_request = self.get_login_request(challenge)
        acr_values = login_request.oidc_context.acr_values
        acr_values = acr_values[-1] if acr_values and len(acr_values) > 1 else '0'
        
        body = {
            'subject': email,
            'remember': True,
            'remember_for': 3600,
            'acr': '2'
        }
        data: CompletedRequest = self.client.accept_login_request(
            challenge,
            body=body
        )
        
        return data.redirect_to
