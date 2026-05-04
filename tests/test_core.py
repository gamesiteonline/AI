import pytest
from core.brain import Brain, BrainInput

@pytest.mark.asyncio
async def test_brain_generate():
    brain = Brain(memory=None, legal=None, analytics=None)
    bi = BrainInput(text="How do I write a list comprehension in python?")
    output = await brain.generate(bi)
    assert hasattr(output, "sass")
    assert hasattr(output, "elite_fix")
    assert hasattr(output, "pro_tip")

def test_dummy():
    assert True
