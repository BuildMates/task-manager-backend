import os


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Task Manager Backend")
    ENV: str = os.getenv("ENV", "development")
    PORT: int = int(os.getenv("PORT", "8000"))


settings = Settings()