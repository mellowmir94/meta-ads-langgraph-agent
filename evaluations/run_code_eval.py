from __future__ import annotations

from dataclasses import astuple

from evaluations.dataset import EvaluationCase, load_evaluation_cases
from evaluations.metrics import calculate_campaign_metrics


def evaluate_case(case: EvaluationCase) -> bool:
    actual = calculate_campaign_metrics(case.campaign_metrics)
    return astuple(actual) == astuple(case.expected_metrics)


def main() -> None:
    cases = load_evaluation_cases()
    results = [(case.case_id, evaluate_case(case)) for case in cases]
    passed = sum(1 for _, result in results if result)

    print(f"Code eval results: {passed}/{len(results)} passed")
    for case_id, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{status} {case_id}")

    if passed != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
