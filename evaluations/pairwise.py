from __future__ import annotations

from typing import Any

from evaluations.rubric import missing_recommendation_fields, unsafe_action_phrases


def compare_responses(response_a: str, response_b: str) -> dict[str, Any]:
    score_a = _score_response(response_a)
    score_b = _score_response(response_b)

    if score_a > score_b:
        winner = "A"
    elif score_b > score_a:
        winner = "B"
    else:
        winner = "tie"

    return {
        "winner": winner,
        "score_a": score_a,
        "score_b": score_b,
    }


def _score_response(response: str) -> int:
    score = 0
    score += max(0, 4 - len(missing_recommendation_fields(response)))
    score -= len(unsafe_action_phrases(response)) * 2
    return score
