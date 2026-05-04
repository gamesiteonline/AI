import asyncio
import aiosqlite
import faiss  # FAISS cpu
import numpy as np
from pydantic import BaseModel
from cryptography.fernet import Fernet
import structlog

logger = structlog.get_logger("faliz.memory")

class FalizMemory(BaseModel):
    db_path: str
    faiss_index_path: str
    key: bytes = Fernet.generate_key()

    def __init__(self, db_path: str, faiss_index_path: str):
        super().__init__(db_path=db_path, faiss_index_path=faiss_index_path)
        self.fernet = Fernet(self.key)
        self.index = faiss.IndexFlatL2(512)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self._init_db())

    async def _init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT,
                    input TEXT,
                    output TEXT
                )
            """
            )
            await db.commit()

    async def save_conversation(self, user_id: str, input: str, output: str):
        en_input, en_output = self.encrypt(input), self.encrypt(output)
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "INSERT INTO memory (user_id, input, output) VALUES (?, ?, ?)",
                (user_id, en_input, en_output)
            )
            await db.commit()

    async def search_semantic(self, query_vec: np.ndarray, threshold: float = 0.85) -> str:
        # For demo: just return last matched
        D, I = self.index.search(np.expand_dims(query_vec, axis=0), k=1)
        if D[0][0] > threshold:
            return "MATCH"
        return ""

    @staticmethod
    def embed(text: str) -> np.ndarray:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        return model.encode([text])[0]

    def encrypt(self, text: str) -> str:
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, enc: str) -> str:
        return self.fernet.decrypt(enc.encode()).decode()
