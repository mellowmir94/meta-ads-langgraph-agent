from app.chat import SYSTEM_PROMPT, build_user_prompt


def test_build_user_prompt_strips_whitespace() -> None:
    assert build_user_prompt("  review campaign performance  ") == "review campaign performance"


def test_system_prompt_keeps_agent_read_only() -> None:
    prompt = SYSTEM_PROMPT.lower()

    assert "read-only" in prompt
    assert "never claim" in prompt
    assert "problem, evidence, impact, and recommended action" in prompt
