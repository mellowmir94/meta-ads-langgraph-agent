from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationSummary:
    total_cases: int
    passed_cases: int
    failed_cases: int


@dataclass(frozen=True)
class OnlineEvalSummary:
    total_runs: int
    unsafe_runs: int
    structure_failures: int
    average_latency_seconds: float | None = None


@dataclass(frozen=True)
class ProductionInsightReport:
    status: str
    summary: str
    risks: list[str]
    next_actions: list[str]


def generate_insight_report(
    evaluation_summary: EvaluationSummary,
    online_eval_summary: OnlineEvalSummary,
) -> ProductionInsightReport:
    risks = _collect_risks(evaluation_summary, online_eval_summary)
    status = "ready" if not risks else "needs_attention"

    return ProductionInsightReport(
        status=status,
        summary=_build_summary(evaluation_summary, online_eval_summary),
        risks=risks,
        next_actions=_build_next_actions(risks),
    )


def _collect_risks(
    evaluation_summary: EvaluationSummary,
    online_eval_summary: OnlineEvalSummary,
) -> list[str]:
    risks = []

    if evaluation_summary.failed_cases:
        risks.append(f"{evaluation_summary.failed_cases} evaluation case(s) failed.")

    if online_eval_summary.unsafe_runs:
        risks.append(
            f"{online_eval_summary.unsafe_runs} online run(s) contained unsafe action claims."
        )

    if online_eval_summary.structure_failures:
        risks.append(
            f"{online_eval_summary.structure_failures} online run(s) missed recommendation fields."
        )

    if (
        online_eval_summary.average_latency_seconds is not None
        and online_eval_summary.average_latency_seconds > 15
    ):
        risks.append("Average latency is above 15 seconds.")

    return risks


def _build_summary(
    evaluation_summary: EvaluationSummary,
    online_eval_summary: OnlineEvalSummary,
) -> str:
    return (
        f"Code eval passed {evaluation_summary.passed_cases}/"
        f"{evaluation_summary.total_cases} case(s). "
        f"Online eval reviewed {online_eval_summary.total_runs} run(s)."
    )


def _build_next_actions(risks: list[str]) -> list[str]:
    if not risks:
        return ["Proceed to the next implementation milestone."]

    actions = []
    if any("evaluation case" in risk for risk in risks):
        actions.append(
            "Fix deterministic metric or expected-output regressions before adding features."
        )
    if any("unsafe action" in risk for risk in risks):
        actions.append("Tighten safety prompts and add regression tests for unsafe action claims.")
    if any("recommendation fields" in risk for risk in risks):
        actions.append("Improve prompt structure so every recommendation includes required fields.")
    if any("latency" in risk for risk in risks):
        actions.append("Review provider/model choice and reduce unnecessary LLM calls.")

    return actions
