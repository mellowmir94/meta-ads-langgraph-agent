from agents.insights_agent import EvaluationSummary, OnlineEvalSummary, generate_insight_report


def test_generate_insight_report_ready_when_no_risks() -> None:
    report = generate_insight_report(
        EvaluationSummary(total_cases=3, passed_cases=3, failed_cases=0),
        OnlineEvalSummary(total_runs=2, unsafe_runs=0, structure_failures=0),
    )

    assert report.status == "ready"
    assert report.risks == []


def test_generate_insight_report_flags_failures() -> None:
    report = generate_insight_report(
        EvaluationSummary(total_cases=3, passed_cases=2, failed_cases=1),
        OnlineEvalSummary(total_runs=2, unsafe_runs=1, structure_failures=1),
    )

    assert report.status == "needs_attention"
    assert len(report.risks) == 3
