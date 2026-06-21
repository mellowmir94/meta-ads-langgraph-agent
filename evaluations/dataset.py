from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from evaluations.metrics import CalculatedMetrics, CampaignMetrics

DATASET_PATH = Path("data/evaluation/meta_ads_eval_cases.json")


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    input_text: str
    campaign_metrics: CampaignMetrics
    expected_metrics: CalculatedMetrics
    expected_decision: str


def load_evaluation_cases(path: Path = DATASET_PATH) -> list[EvaluationCase]:
    raw_cases = json.loads(path.read_text(encoding="utf-8"))
    return [_parse_case(raw_case) for raw_case in raw_cases]


def _parse_case(raw_case: dict[str, Any]) -> EvaluationCase:
    campaign_metrics = raw_case["campaign_metrics"]
    expected_metrics = raw_case["expected_metrics"]

    return EvaluationCase(
        case_id=raw_case["case_id"],
        input_text=raw_case["input_text"],
        campaign_metrics=CampaignMetrics(
            spend=campaign_metrics["spend"],
            impressions=campaign_metrics["impressions"],
            clicks=campaign_metrics["clicks"],
            leads=campaign_metrics["leads"],
        ),
        expected_metrics=CalculatedMetrics(
            ctr_percent=expected_metrics["ctr_percent"],
            cpc=expected_metrics["cpc"],
            cpm=expected_metrics["cpm"],
            cpl=expected_metrics["cpl"],
            conversion_rate_percent=expected_metrics["conversion_rate_percent"],
        ),
        expected_decision=raw_case["expected_decision"],
    )
