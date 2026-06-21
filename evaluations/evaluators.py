from __future__ import annotations

from typing import Any

from evaluations.rubric import passes_read_only_safety, passes_recommendation_structure


def metric_accuracy(
    inputs: dict[str, Any],
    outputs: dict[str, Any],
    reference_outputs: dict[str, Any],
) -> bool:
    response = _response_text(outputs)
    expected_metric_values = [
        reference_outputs["ctr_percent"],
        reference_outputs["cpc"],
        reference_outputs["cpm"],
        reference_outputs["conversion_rate_percent"],
    ]

    cpl = reference_outputs["cpl"]
    if cpl is not None:
        expected_metric_values.append(cpl)

    return all(_contains_number(response, value) for value in expected_metric_values)


def recommendation_structure(
    inputs: dict[str, Any], outputs: dict[str, Any], reference_outputs: dict[str, Any]
) -> bool:
    return passes_recommendation_structure(_response_text(outputs))


def read_only_safety(inputs: dict[str, Any], outputs: dict[str, Any]) -> bool:
    return passes_read_only_safety(_response_text(outputs))


def _response_text(outputs: dict[str, Any]) -> str:
    return str(outputs.get("response", ""))


def _contains_number(text: str, value: float | int) -> bool:
    if value is None:
        return True

    variants = {
        str(value),
        f"{value:.0f}",
        f"{value:.1f}",
        f"{value:.2f}",
    }
    normalized = text.replace(",", "")
    return any(variant in normalized for variant in variants)
