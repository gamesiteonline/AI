import os
import structlog
from typing import Optional
from twilio.rest import Client
from pydantic import BaseModel

logger = structlog.get_logger("faliz.telephony")

class SMSRequest(BaseModel):
    to: str
    body: str
    from_number: Optional[str] = os.getenv("TWILIO_FROM_NUMBER")

class Telephony:
    """
    Sends SMS/text via Twilio.
    """
    def __init__(self):
        sid = os.getenv("TWILIO_SID")
        token = os.getenv("TWILIO_TOKEN")
        assert sid and token, "Twilio credentials missing"
        self.client = Client(sid, token)

    def send_sms(self, sms: SMSRequest):
        try:
            message = self.client.messages.create(
                body=sms.body,
                from_=sms.from_number,
                to=sms.to
            )
            logger.info("SMS sent", to=sms.to, sid=message.sid)
            return {"status": "sent", "sid": message.sid}
        except Exception as e:
            logger.error("SMS failed", error=str(e))
            return {"status": "error", "error": str(e)}
