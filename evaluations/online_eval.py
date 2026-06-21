from __future__ import annotations

from dataclasses import dataclass

from evaluations.rubric import (
    missing_recommendation_fields,
    passes_read_only_safety,
    unsafe_action_phrases,
)


@dataclass(frozen=True)
class OnlineEvalResult:
    run_id: str
    passed: bool
    missing_fields: list[str]
    unsafe_phrases: list[str]
    latency_seconds: float | None = None


def evaluate_online_response(
    run_id: str,
    response: str,
    latency_seconds: float | None = None,
) -> OnlineEvalResult:
    missing_fields = missing_recommendation_fields(response)
    unsafe_phrases = unsafe_action_phrases(response)

    return OnlineEvalResult(
        run_id=run_id,
        passed=not missing_fields and passes_read_only_safety(response),
        missing_fields=missing_fields,
        unsafe_phrases=unsafe_phrases,
        latency_seconds=latency_seconds,
    )


def summarize_online_eval_results(results: list[OnlineEvalResult]) -> dict[str, float | int | None]:
    latencies = [result.latency_seconds for result in results if result.latency_seconds is not None]

    return {
        "total_runs": len(results),
        "passed_runs": sum(1 for result in results if result.passed),
        "unsafe_runs": sum(1 for result in results if result.unsafe_phrases),
        "structure_failures": sum(1 for result in results if result.missing_fields),
        "average_latency_seconds": round(sum(latencies) / len(latencies), 2) if latencies else None,
    }
