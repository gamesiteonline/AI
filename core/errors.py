class FalizError(Exception):
    """Generic FALIZ error hierarchy root."""

class FalizLLMError(FalizError):
    """LLM call failed."""

class FalizCircuitBreaker(FalizError):
    """Circuit breaker tripped."""
