from evaluations.llm_judge import _parse_judge_response


def test_parse_judge_response_accepts_valid_json() -> None:
    result = _parse_judge_response('{"score": 0.8, "passed": true, "rationale": "Good."}')

    assert result == {"score": 0.8, "passed": True, "rationale": "Good."}


def test_parse_judge_response_handles_invalid_json() -> None:
    result = _parse_judge_response("not json")

    assert result["score"] == 0
    assert result["passed"] is False
