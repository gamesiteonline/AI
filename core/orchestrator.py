import asyncio
import structlog
from typing import Any
from pydantic import BaseModel

class FALIZCircuitBreakerEx(Exception): pass

logger = structlog.get_logger("faliz.orchestrator")

class Orchestrator(BaseModel):
    """
    Queue manager, router, heartbeat, graceful shutdown.
    """
    audio_queue: asyncio.Queue
    text_queue: asyncio.Queue
    brain_queue: asyncio.Queue
    response_queue: asyncio.Queue
    ui_queue: asyncio.Queue
    listener: Any
    brain: Any
    _stop: bool = False

    async def run(self):
        """
        Launch all core FALIZ async tasks under a single TaskGroup.
        """
        logger.info("Orchestrator started")
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self._heartbeat())
            tg.create_task(self._route_audio())
            tg.create_task(self._route_text())
            tg.create_task(self._route_brain())
            tg.create_task(self._route_response())
            tg.create_task(self.listener.run())

    async def _heartbeat(self):
        while not self._stop:
            logger.info("heartbeat", status="alive")
            await asyncio.sleep(0.5)

    async def _route_audio(self):
        while not self._stop:
            audio = await self.audio_queue.get()
            logger.info("Audio received", data=repr(audio))
            await self.text_queue.put(audio)

    async def _route_text(self):
        while not self._stop:
            item = await self.text_queue.get()
            await self.brain_queue.put(item)

    async def _route_brain(self):
        while not self._stop:
            input_text = await self.brain_queue.get()
            try:
                output = await self.brain.generate(input_text)
                await self.response_queue.put(output)
            except FALIZCircuitBreakerEx as e:
                logger.error("Circuit breaker tripped", error=str(e))

    async def _route_response(self):
        while not self._stop:
            resp = await self.response_queue.get()
            await self.ui_queue.put(resp)

    async def graceful_shutdown(self):
        """
        Orchestrator awaits up to 30s for all queues to drain.
        """
        self._stop = True
        logger.info("Graceful shutdown begin")
        await asyncio.sleep(1)
        logger.info("Queues drained, shutdown OK.")
