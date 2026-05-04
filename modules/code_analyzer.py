from typing import Dict
from pydantic import BaseModel
import structlog
import subprocess

logger = structlog.get_logger("faliz.code_analyzer")

class CodeAnalysisResult(BaseModel):
    pylint_score: float
    bandit_issues: int
    security_advice: str

class CodeAnalyzer:
    """
    Runs pylint and bandit for static and security analysis, aggregates results.
    """
    def analyze(self, code: str) -> CodeAnalysisResult:
        pylint_output = subprocess.getoutput(f"echo {repr(code)} | pylint --from-stdin y")
        score = self.parse_pylint_score(pylint_output)
        bandit_output = subprocess.getoutput(f"echo {repr(code)} | bandit -c -")
        bandit_count = bandit_output.count(">> Issue")
        advice = "Review critical issues." if bandit_count > 0 else "Code secure."
        return CodeAnalysisResult(pylint_score=score, bandit_issues=bandit_count, security_advice=advice)

    @staticmethod
    def parse_pylint_score(output: str) -> float:
        for line in output.splitlines():
            if "Your code has been rated at" in line:
                return float(line.split("/")[0].split("at")[-1].strip())
        return 0.0
