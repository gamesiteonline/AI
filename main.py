import asyncio
import os
import signal
import sys
from typing import Optional
import typer
import uvicorn
from fastapi import FastAPI
import structlog
import psutil

from config import settings as faliz_settings
from core.orchestrator import Orchestrator
from core.listener import Listener
from core.brain import Brain
from modules.legal_check import LegalChecker
from modules.memory import FalizMemory
from modules.analytics import Analytics
from ui.hud import FalizHUD

app = FastAPI()
cli = typer.Typer()
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger("faliz")


def validate_config():
    """
    Validate required config values and environment.
    """
    faliz_settings.validate()
    logger.info("Config validated", config=faliz_settings.dict())


@app.get("/health")
async def health():
    # Simple health endpoint for readiness checks.
    return {"status": "healthy"}


async def shutdown_signal_handler(orchestrator: Orchestrator):
    logger.info("Shutdown requested.")
    await orchestrator.graceful_shutdown()  # Custom graceful shutdown with timeout


async def main_async():
    validate_config()
    # All asyncio queues for orchestrator:
    audio_queue = asyncio.Queue()
    text_queue = asyncio.Queue()
    brain_queue = asyncio.Queue()
    response_queue = asyncio.Queue()
    ui_queue = asyncio.Queue()
    # subsystems (inject queues as needed)
    memory = FalizMemory(faliz_settings.memory_db, faliz_settings.faiss_index)
    legal = LegalChecker()
    analytics = Analytics()
    brain = Brain(memory=memory, legal=legal, analytics=analytics)
    listener = Listener(
        audio_queue=audio_queue,
        text_queue=text_queue,
        hotword="Hey FALIZ"
    )
    orchestrator = Orchestrator(
        audio_queue=audio_queue,
        text_queue=text_queue,
        brain_queue=brain_queue,
        response_queue=response_queue,
        ui_queue=ui_queue,
        listener=listener,
        brain=brain,
    )
    hud = FalizHUD(ui_queue, response_queue, faliz_settings)
    # Setup graceful shutdown handlers
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown_signal_handler(orchestrator)))
    # Run orchestrator + HUD + FastAPI in parallel under TaskGroup
    async with asyncio.TaskGroup() as tg:
        tg.create_task(orchestrator.run())
        tg.create_task(hud.run())
        tg.create_task(uvicorn.run(app, host='0.0.0.0', port=8080))
    await orchestrator.graceful_shutdown()
    logger.info("Shutdown complete")


@cli.command()
def run(
    debug: bool = typer.Option(False, "--debug", "-d"),
    reload: bool = typer.Option(True, "--reload", "-r"),
):
    """
    Launch FALIZ 3.2 Enterprise.
    """
    try:
        if debug:
            logger.warning("Debug mode enabled.")
        asyncio.run(main_async())
    except Exception as e:
        logger.error("Fatal error", error=str(e))
        raise e


@cli.command()
def healthcheck():
    """
    Print healthcheck result manually.
    """
    import requests
    try:
        r = requests.get("http://localhost:8080/health")
        typer.echo(str(r.json()))
    except Exception as e:
        typer.echo(f"Health check failed: {e}")


@cli.command()
def info():
    """
    Show FALIZ info and system resource usage.
    """
    mem = psutil.virtual_memory()
    typer.echo(f"FALIZ 3.2 — Enterprise SuperDev Assistant")
    typer.echo(f"CPU: {psutil.cpu_percent()}%  RAM: {mem.used/1024/1024:.2f}MB/{mem.total/1024/1024:.2f}MB")


if __name__ == "__main__":
    cli()
