from typing import List, Union

from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "Nooxit API"
    AUTH_SECRET: str
    
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
   
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
