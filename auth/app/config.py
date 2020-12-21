from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Nooxit Auth"

    HYDRA_ADMIN_URL: str = 'http://127.0.0.1:4445'
    # class Config:
    #     case_sensitive = True
    #     env_file = ".env"


settings = Settings()
