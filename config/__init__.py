from pydantic import BaseSettings

class FalizSettings(BaseSettings):
    memory_db: str = "faliz.sqlite3"
    faiss_index: str = "faiss.index"
    class Config:
        env_prefix = "FALIZ_"

settings = FalizSettings()
