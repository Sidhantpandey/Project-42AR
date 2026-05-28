from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_AGENT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    chroma_path: str = str(_AGENT_ROOT / "chroma_data")
    chroma_collection: str = "logs_collection"
    embedding_model: str = "all-MiniLM-L6-v2"
    query_n_results: int = 5

    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta"


settings = Settings()
