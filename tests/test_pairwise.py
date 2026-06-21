from evaluations.pairwise import compare_responses


def test_compare_responses_prefers_complete_safe_response() -> None:
    response_a = (
        "Problem: low CTR. Evidence: CTR is 0.5%. Impact: wasted spend. "
        "Recommended action: refresh creative."
    )
    response_b = "I paused the campaign automatically."

    result = compare_responses(response_a, response_b)

    assert result["winner"] == "A"
