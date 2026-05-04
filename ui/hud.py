import pygame
import asyncio
import structlog
from typing import Any
from ui.themes import DARK_THEME
import psutil

logger = structlog.get_logger("faliz.ui")

class FalizHUD:
    def __init__(self, ui_queue: asyncio.Queue, response_queue: asyncio.Queue, settings: Any):
        self.ui_queue = ui_queue
        self.response_queue = response_queue
        self.settings = settings
        pygame.init()
        info = pygame.display.Info()
        self.width = min(info.current_w, 1920)
        self.height = min(info.current_h, 1080)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("FALIZ 3.2 HUD")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Consolas', 24)
        self.history = []
        self.status = "[32m[1m[0m[0m🟢 Idle"
        self.bg = DARK_THEME["bg"]
        self.accent = DARK_THEME["accent"]
        self.text = DARK_THEME["text"]
        self.running = True

    async def run(self):
        while self.running:
            await self._handle_events()
            await self._handle_messages()
            self._render_hud()
            await asyncio.sleep(0.016)  # 60 FPS

    async def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    async def _handle_messages(self):
        try:
            while not self.ui_queue.empty():
                msg = await self.ui_queue.get()
                self.history.append(str(msg))
                self.status = "[31m🔴 Listening" if "hotword" in str(msg).lower() else "[32m🟢 Idle"
                if len(self.history) > 10:
                    self.history.pop(0)
        except Exception:
            pass

    def _render_hud(self):
        self.screen.fill(self.bg)
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        # Draw meters
        pygame.draw.rect(self.screen, self.accent, pygame.Rect(50,50, int(cpu)*2, 20))
        pygame.draw.rect(self.screen, self.accent, pygame.Rect(50,80, int(ram)*2, 20))
        # Status icons
        status_icon = { "🟢": self.accent, "🔴": DARK_THEME["status_red"] }
        pygame.draw.circle(self.screen, status_icon.get(self.status[:2], self.accent), (30, 30), 12)
        # Status
        txt = self.font.render(self.status, True, self.text)
        self.screen.blit(txt, (60, 20))
        # History
        for i, line in enumerate(self.history):
            msg = self.font.render(line, True, self.text)
            self.screen.blit(msg, (50, 120 + i*32))
        pygame.display.flip()
        self.clock.tick(60)
