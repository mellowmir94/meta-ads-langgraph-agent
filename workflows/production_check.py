from __future__ import annotations

from agents.insights_agent import (
    EvaluationSummary,
    OnlineEvalSummary,
    generate_insight_report,
)
from evaluations.dataset import load_evaluation_cases
from evaluations.run_code_eval import evaluate_case


def run_production_check() -> str:
    cases = load_evaluation_cases()
    passed_cases = sum(1 for case in cases if evaluate_case(case))
    evaluation_summary = EvaluationSummary(
        total_cases=len(cases),
        passed_cases=passed_cases,
        failed_cases=len(cases) - passed_cases,
    )
    online_eval_summary = OnlineEvalSummary(
        total_runs=0,
        unsafe_runs=0,
        structure_failures=0,
        average_latency_seconds=None,
    )
    report = generate_insight_report(evaluation_summary, online_eval_summary)
    return _format_report(report)


def _format_report(report) -> str:
    lines = [
        f"Production status: {report.status}",
        f"Summary: {report.summary}",
        "Risks:",
    ]
    lines.extend(f"- {risk}" for risk in report.risks) if report.risks else lines.append("- none")
    lines.append("Next actions:")
    lines.extend(f"- {action}" for action in report.next_actions)
    return "\n".join(lines)


def main() -> None:
    print(run_production_check())


if __name__ == "__main__":
    main()
