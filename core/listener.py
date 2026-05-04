import asyncio
import structlog
import webrtcvad
import whisper
import sounddevice as sd
import numpy as np
from typing import Any
from pydantic import BaseModel
from pynput import keyboard
from core.errors import FalizError

logger = structlog.get_logger("faliz.listener")

class Listener(BaseModel):
    """
    Listener for hotword, speech (STT), and keyboard Ctrl+Space.
    """
    audio_queue: asyncio.Queue
    text_queue: asyncio.Queue
    hotword: str = "Hey FALIZ"

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.__vad = webrtcvad.Vad(1)
        self.__asr = whisper.load_model("base")

    async def run(self):
        """
        Main listener loop using asyncio and keyboard listener.
        """
        task_audio = asyncio.create_task(self._audio_listener_loop())
        task_keyboard = asyncio.create_task(self._keyboard_listener_loop())
        await asyncio.gather(task_audio, task_keyboard)

    async def _audio_listener_loop(self):
        logger.info("Audio listener started.")
        while True:
            try:
                frames = await self._record_audio()
                if self._detect_hotword(frames):
                    await self.text_queue.put(await self._transcribe(frames))
            except Exception as e:
                logger.error("Audio listen failed", error=str(e))
                continue

    async def _keyboard_listener_loop(self):
        def on_press(key):
            if key == keyboard.Key.space and keyboard.Controller().pressed(keyboard.Key.ctrl):
                logger.info("Keyboard hotkey detected", event="Ctrl+Space")
                asyncio.create_task(self.text_queue.put("Hotkey activated"))
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    async def _record_audio(self, seconds=4, fs=16000):
        try:
            rec = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()
            arr = np.squeeze(rec)
            return arr
        except Exception as ex:
            logger.error("Sounddevice record failed", error=str(ex))
            raise FalizError("Audio record fail") from ex

    def _detect_hotword(self, audio_frames):
        # Simple RMS threshold VAD, then Whisper fallback for "Hey FALIZ"
        if np.abs(audio_frames).mean() < 1e-3:
            return False
        # Use Whisper to get text
        try:
            text = self.__asr.transcribe(audio_frames, fp16=False)["text"]
            return self.hotword.lower() in text.lower()
        except Exception:
            return False

    async def _transcribe(self, audio_frames):
        # Use whisper for STT
        result = self.__asr.transcribe(audio_frames, fp16=False)
        return result["text"]
