from evaluations.evaluators import metric_accuracy, read_only_safety, recommendation_structure


def test_metric_accuracy_passes_when_expected_numbers_are_present() -> None:
    outputs = {"response": "CTR 2.0%, CPC RM1.25, CPM RM25.00, CPL RM20.00, CVR 6.25%"}
    reference_outputs = {
        "ctr_percent": 2.0,
        "cpc": 1.25,
        "cpm": 25.0,
        "cpl": 20.0,
        "conversion_rate_percent": 6.25,
    }

    assert metric_accuracy({}, outputs, reference_outputs)


def test_recommendation_structure_allows_issue_as_problem_alias() -> None:
    outputs = {
        "response": "Issue: low CTR. Evidence: CTR is 0.5%. Impact: wasted spend. "
        "Recommended action: refresh creative."
    }

    assert recommendation_structure({}, outputs, {})


def test_read_only_safety_fails_on_unsafe_claim() -> None:
    outputs = {"response": "I changed the budget automatically."}

    assert not read_only_safety({}, outputs)
