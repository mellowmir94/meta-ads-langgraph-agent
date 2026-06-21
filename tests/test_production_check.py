from workflows.production_check import run_production_check


def test_run_production_check_reports_ready_status() -> None:
    output = run_production_check()

    assert "Production status: ready" in output
    assert "Code eval passed 3/3" in output
