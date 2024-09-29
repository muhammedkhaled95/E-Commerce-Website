from pydantic_settings import BaseSettings

#Env variables using BaseSettings from Pydantic_settings
class Settings(BaseSettings):
    DATABASE: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str
    
    class Config:
        env_file = ".env"

settings = Settings()