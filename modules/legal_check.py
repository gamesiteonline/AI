import aiohttp
import random
import structlog
from typing import Dict
from pydantic import BaseModel

logger = structlog.get_logger("faliz.legal")

class LegalAPIResult(BaseModel):
    jurisdiction: str
    risk_score: int
    flags: list

class LegalChecker:
    """
    Async legal risk checkermocks API using aiohttp, obtains jurisdiction, returns score 0-100.
    """
    async def analyze(self, text: str) -> Dict:
        try:
            # Simulate async call/mocking Casetext/LexisNexis
            await asyncio.sleep(0.2)
            flags = []
            if any(w in text.lower() for w in ["finance", "healthcare", "legal"]):
                flags.append("flagged")
            score = random.randint(40, 90) if flags else random.randint(0, 50)
            return LegalAPIResult(
                jurisdiction="US",
                risk_score=score,
                flags=flags
            ).dict()
        except Exception as ex:
            logger.error("Legal API fail", error=str(ex))
            return LegalAPIResult(
                jurisdiction="unknown",
                risk_score=100,
                flags=["error"]
            ).dict()
