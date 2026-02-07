from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Lihabesha API"
    api_prefix: str = "/api"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/lihabesha"

settings = Settings()
