"""Application configuration."""
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
STORAGE_DIR = BASE_DIR / "storage"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "NewsScript AI Video"
    API_PREFIX: str = "/api"
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/app.db"
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]

    # ---- External providers (all optional) ----
    MOCK_MODE: bool = True                       # force mock even with keys
    LLM_BASE_URL: str = "https://api.openai.com/v1"
    LLM_API_KEY: str = ""
    LLM_MODEL: str = "gpt-4o-mini"

    TTS_BASE_URL: str = "https://api.openai.com/v1"
    TTS_API_KEY: str = ""
    TTS_MODEL: str = "tts-1"
    TTS_VOICE: str = "alloy"

    PEXELS_API_KEY: str = ""

settings = Settings()

for sub in ("audio", "footage", "subtitles", "videos", "thumbnails", "temp"):
    (STORAGE_DIR / sub).mkdir(parents=True, exist_ok=True)