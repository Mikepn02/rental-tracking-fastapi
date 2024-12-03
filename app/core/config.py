from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    PROJECT_NAME: str = "Rental Management System"
    
    class Config:
        env_file = ".env"

settings = Settings()

print("DATABASE_URL:", settings.DATABASE_URL)