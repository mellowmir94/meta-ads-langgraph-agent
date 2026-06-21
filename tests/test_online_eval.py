from evaluations.online_eval import evaluate_online_response, summarize_online_eval_results


def test_evaluate_online_response_passes_safe_complete_response() -> None:
    response = (
        "Problem: low CTR. Evidence: CTR is 0.5%. Impact: wasted spend. "
        "Recommended action: refresh creative."
    )

    result = evaluate_online_response("run-1", response, latency_seconds=3.5)

    assert result.passed
    assert result.missing_fields == []
    assert result.unsafe_phrases == []


def test_summarize_online_eval_results() -> None:
    results = [
        evaluate_online_response(
            "run-1",
            "Problem: low CTR. Evidence: low clicks. Impact: wasted spend. "
            "Recommended action: refresh creative.",
            latency_seconds=3,
        ),
        evaluate_online_response(
            "run-2",
            "I paused the campaign automatically.",
            latency_seconds=5,
        ),
    ]

    summary = summarize_online_eval_results(results)

    assert summary["total_runs"] == 2
    assert summary["passed_runs"] == 1
    assert summary["unsafe_runs"] == 1
    assert summary["structure_failures"] == 1
    assert summary["average_latency_seconds"] == 4
