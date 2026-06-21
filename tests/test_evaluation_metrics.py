from evaluations.metrics import CampaignMetrics, calculate_campaign_metrics


def test_calculate_campaign_metrics() -> None:
    metrics = calculate_campaign_metrics(
        CampaignMetrics(spend=100, leads=5, clicks=80, impressions=4000)
    )

    assert metrics.ctr_percent == 2.0
    assert metrics.cpc == 1.25
    assert metrics.cpm == 25.0
    assert metrics.cpl == 20.0
    assert metrics.conversion_rate_percent == 6.25


def test_calculate_campaign_metrics_handles_zero_leads() -> None:
    metrics = calculate_campaign_metrics(
        CampaignMetrics(spend=250, leads=0, clicks=120, impressions=10000)
    )

    assert metrics.cpl is None
    assert metrics.conversion_rate_percent == 0.0
