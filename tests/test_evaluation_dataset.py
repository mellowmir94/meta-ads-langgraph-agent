from evaluations.dataset import load_evaluation_cases


def test_load_evaluation_cases() -> None:
    cases = load_evaluation_cases()

    assert len(cases) == 3
    assert cases[0].case_id == "baseline_lead_gen"
    assert cases[0].campaign_metrics.spend == 100
    assert cases[0].expected_metrics.ctr_percent == 2.0
