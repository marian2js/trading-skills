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
    assert payload["analysis"]["high_impact_count"] == 2, "Expected two high-impact demo macro events"


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
    assert payload["events"][0]["session"] == "after-close", "Example earnings output should expose canonical session fields"


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


def test_position_sizing_script_smoke(repo_root):
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/position-sizing/scripts/calculate_position_size.py",
            "--account-size",
            "150000",
            "--risk-percent",
            "0.4",
            "--entry",
            "84.2",
            "--stop",
            "81.9",
            "--slippage",
            "0.1",
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload["position_size"] == 250, "Position sizing smoke test should match the fixture arithmetic"
    assert payload["total_risk"] == 600.0, "Position sizing smoke test should report total dollar risk"


def test_risk_reward_script_smoke(repo_root):
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/risk-reward-sanity-check/scripts/check_trade_structure.py",
            "--direction",
            "long",
            "--entry",
            "58.2",
            "--stop",
            "55.9",
            "--target",
            "65.5",
            "--thesis",
            "Breakout continuation if software leadership holds.",
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload["risk_reward_ratio"] > 3.0, "Risk-reward smoke test should show strong asymmetry for the demo case"
    assert payload["asymmetry"] == "strong", "Risk-reward smoke test should classify the demo case as strong asymmetry"
