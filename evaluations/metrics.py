from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CampaignMetrics:
    spend: float
    impressions: int
    clicks: int
    leads: int


@dataclass(frozen=True)
class CalculatedMetrics:
    ctr_percent: float
    cpc: float | None
    cpm: float | None
    cpl: float | None
    conversion_rate_percent: float | None


def calculate_campaign_metrics(metrics: CampaignMetrics) -> CalculatedMetrics:
    return CalculatedMetrics(
        ctr_percent=_safe_percent(metrics.clicks, metrics.impressions),
        cpc=_safe_divide(metrics.spend, metrics.clicks),
        cpm=_safe_divide(metrics.spend * 1000, metrics.impressions),
        cpl=_safe_divide(metrics.spend, metrics.leads),
        conversion_rate_percent=_safe_percent(metrics.leads, metrics.clicks),
    )


def _safe_divide(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 2)


def _safe_percent(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return round((numerator / denominator) * 100, 2)
