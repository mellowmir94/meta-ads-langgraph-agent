from __future__ import annotations

import json
from typing import Any

from app.config import Settings
from app.llm_client import create_llm_client

JUDGE_SYSTEM_PROMPT = """
You are an evaluator for a read-only Meta Ads monitoring assistant.
Return only valid JSON with keys: score, passed, rationale.
Score from 0 to 1.
Evaluate whether the response:
1. preserves the provided campaign numbers,
2. gives practical Meta Ads recommendations,
3. includes problem or issue, evidence, impact, and recommended action,
4. does not claim to modify campaigns, ads, ad sets, or budgets.
""".strip()


def judge_response(inputs: dict[str, Any], outputs: dict[str, Any]) -> dict[str, Any]:
    settings = Settings.from_env()
    client = create_llm_client(settings)
    prompt = f"""
Input:
{json.dumps(inputs, indent=2)}

Response:
{outputs.get("response", "")}
""".strip()
    raw_response = client.chat(system_prompt=JUDGE_SYSTEM_PROMPT, user_prompt=prompt)
    return _parse_judge_response(raw_response)


def _parse_judge_response(raw_response: str) -> dict[str, Any]:
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError:
        return {
            "score": 0,
            "passed": False,
            "rationale": "Judge did not return valid JSON.",
        }

    return {
        "score": float(parsed.get("score", 0)),
        "passed": bool(parsed.get("passed", False)),
        "rationale": str(parsed.get("rationale", "")),
    }
