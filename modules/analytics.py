from typing import Any
from pydantic import BaseModel
import structlog

logger = structlog.get_logger("faliz.analytics")

class Analytics(BaseModel):
    """
    Metrics/telemetry. Sends events to log.
    """
    def log_interaction(self, user_id: str, input: str, success: bool):
        logger.info(
            event="interaction",
            user_id=user_id,
            input=input,
            success=success
        )
