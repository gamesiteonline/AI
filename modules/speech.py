import os
from typing import Optional
import aiohttp
import structlog
from pydantic import BaseModel

logger = structlog.get_logger("faliz.speech")

class TextToSpeechRequest(BaseModel):
    text: str
    voice: Optional[str] = "Rachel"
    output_format: Optional[str] = "mp3"

class SpeechSynthesizer:
    """
    Uses ElevenLabs TTS API to synthesize human-like speech.
    """
    API_URL = "https://api.elevenlabs.io/v1/text-to-speech/"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = "21m00Tcm4TlvDq8ikWAM" # Rachel
        assert self.api_key, "No ElevenLabs API key set"

    async def synthesize(self, req: TextToSpeechRequest) -> bytes:
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "text": req.text,
            "voice_settings": {"stability": 0.75, "similarity_boost": 0.5},
            "model_id": "eleven_multilingual_v2"
        }
        url = f"{self.API_URL}{self.voice_id}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status != 200:
                    logger.error("TTS API error", status=response.status)
                    raise Exception(f"TTS err {response.status}")
                return await response.read()
