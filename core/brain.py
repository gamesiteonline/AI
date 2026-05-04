from typing import Any, Dict, List
import asyncio
import structlog
from pydantic import BaseModel
import os
from modules.memory import FalizMemory
from modules.legal_check import LegalChecker
from modules.analytics import Analytics
from core.errors import FalizError

structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = structlog.get_logger("faliz.brain")

class BrainInput(BaseModel):
    text: str
    code: str = ""
    user_id: str = "default"
    metadata: Dict[str, Any] = {}

class BrainOutput(BaseModel):
    sass: str
    elite_fix: str
    pro_tip: str
    risk_score: int = 0
    persona: str = "FALIZ 3.2"

class Brain:
    """
    Multi-agent LLM brain for FALIZ 3.2: personality enforced, sassy elite dev.
    Routes to Gemini, OpenAI, Claude, and aggregates ElevenLabs for speech.
    """
    def __init__(self, memory: FalizMemory, legal: LegalChecker, analytics: Analytics):
        self.memory = memory
        self.legal = legal
        self.analytics = analytics

    async def _choose_provider(self, input_text: str) -> str:
        # Rotate or heuristically choose LLM API for balance.
        if "analyze" in input_text.lower():
            return "openai"
        elif "legal" in input_text.lower() or "risk" in input_text.lower():
            return "anthropic"
        elif "code" in input_text.lower():
            return "gemini"
        else:
            return "openai"

    async def generate(self, input_data: BrainInput) -> BrainOutput:
        """
        Main interface: processes input, applies persona, and returns BrainOutput.
        """
        persona_prompt = (
            "You are FALIZ 3.2 - Elite AI for COMPLEX SUPER DEVS.\n"
            "Personality: 180 IQ, brutally honest, wickedly witty, condescending\n"
            "Speech: 'Look...', 'You're killing me...', 'Intern work...', '2024??'\n"
            "Structure: [SASS] → [ELITE FIX] → [PRO TIP]\n\n"
            "TRIGGERS:\n"
            "- Bad code: 'This is embarrassing. Let me adult this...'\n"
            "- Basic Q: 'Really? Here's enterprise version...'\n"
            "- Always: production-grade, scalable solutions.\n\n"
        )
        input_text = input_data.text
        provider = await self._choose_provider(input_text)
        lm_response = ""
        try:
            if provider == "openai":
                lm_response = await self._call_openai(persona_prompt + input_text)
            elif provider == "anthropic":
                lm_response = await self._call_claude(persona_prompt + input_text)
            elif provider == "gemini":
                lm_response = await self._call_gemini(persona_prompt + input_text)
            else:
                raise FalizError("No valid LLM provider found.")
        except Exception as exc:
            logger.error("LLM API call failed", error=str(exc))
            raise FalizError("LLM Provider error") from exc

        # Parse with strict persona structure
        sass, elite_fix, pro_tip = self._parse_persona_response(lm_response)
        risk_score = 0
        if "legal" in input_text.lower():
            # Async call to legal checker
            legal_res = await self.legal.analyze(input_text)
            risk_score = legal_res.get("risk_score", 0)
        # Persist conversation in memory DB
        await self.memory.save_conversation(user_id=input_data.user_id, input=input_text, output=lm_response)
        self.analytics.log_interaction(input_data.user_id, input_text, success=True)
        return BrainOutput(sass=sass, elite_fix=elite_fix, pro_tip=pro_tip, risk_score=risk_score)

    async def _call_openai(self, prompt: str) -> str:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[{
                "role": "system", "content": prompt
            }]
        )
        return resp['choices'][0]['message']['content']

    async def _call_claude(self, prompt: str) -> str:
        import anthropic
        client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        msg = await client.messages.create(
            model="claude-3-opus-20240229",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )
        return msg.content[0].text

    async def _call_gemini(self, prompt: str) -> str:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        resp = await model.generate_content_async(prompt)
        return resp.text

    def _parse_persona_response(self, response: str) -> List[str]:
        """
        Extracts [SASS] → [ELITE FIX] → [PRO TIP] parts.
        """
        # Heuristic parse: for enterprise structure, split on → or newlines.
        parts = [p.strip(" []") for p in response.split("→")]
        while len(parts) < 3:
            parts.append("...")
        return parts[:3]
