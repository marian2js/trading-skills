from __future__ import annotations

import json
import subprocess

from tests.helpers import load_json


def run_command(repo_root, args):
    result = subprocess.run(
        args,
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def test_economic_calendar_example_script_smoke(repo_root):
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/economic-calendar/scripts/fetch_calendar.py",
            "--provider",
            "example",
            "--start-date",
            "2026-03-12",
            "--end-date",
            "2026-03-13",
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload["provider"] == "example", "Economic calendar smoke test should use the example adapter"
    assert payload["event_count"] == 3, "Economic calendar example should return three events in the demo window"


def test_earnings_calendar_example_script_smoke(repo_root):
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/earnings-calendar/scripts/fetch_earnings.py",
            "--provider",
            "example",
            "--start-date",
            "2026-03-12",
            "--end-date",
            "2026-05-30",
            "--symbols",
            "NVDA",
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload["provider"] == "example", "Earnings calendar smoke test should use the example adapter"
    assert payload["events"][0]["symbol"] == "NVDA", "Requested symbol should be boosted to the top of the example output"


def test_market_regime_script_smoke(repo_root):
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/market-regime-detector/scripts/assess_regime.py",
            "--trend",
            "up",
            "--volatility",
            "elevated",
            "--breadth",
            "narrow",
            "--event-backdrop",
            "heavy",
            "--json",
        ],
    )
    payload = json.loads(output)
    fixture = load_json(repo_root / "skills/market-regime-detector/fixtures/basic-observation-set.json")
    assert (
        payload["regime"] == fixture["expected_regime"]
    ), f"Expected regime {fixture['expected_regime']}, got {payload['regime']}"
