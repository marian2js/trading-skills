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
    expected = load_json(repo_root / "skills/economic-calendar/fixtures/interpreted-summary.json")
    assert payload["provider"] == "example", "Economic calendar smoke test should use the example adapter"
    assert payload["data_mode"] == expected["data_mode"], "Economic calendar output should label example mode explicitly"
    assert payload["requested_window"] == expected["requested_window"], "Economic calendar output should echo the requested window"
    assert payload["fallback_reason"] == expected["fallback_reason"], "Explicit example mode should not report a fallback reason"
    assert isinstance(payload["retrieved_at_utc"], str) and payload["retrieved_at_utc"].endswith("Z")
    assert payload["coverage_warnings"] == expected["coverage_warnings"], "Economic calendar coverage warnings should match the fixture"
    assert payload["event_count"] == 3, "Economic calendar example should return three events in the demo window"
    assert payload["analysis"] == expected["analysis"], "Economic calendar analysis should match the interpreted fixture"


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
    expected = load_json(repo_root / "skills/earnings-calendar/fixtures/interpreted-summary.json")
    assert payload["provider"] == "example", "Earnings calendar smoke test should use the example adapter"
    assert payload["data_mode"] == expected["data_mode"], "Earnings calendar output should label example mode explicitly"
    assert payload["requested_window"] == expected["requested_window"], "Earnings calendar output should echo the requested window"
    assert payload["fallback_reason"] == expected["fallback_reason"], "Explicit example mode should not report a fallback reason"
    assert isinstance(payload["retrieved_at_utc"], str) and payload["retrieved_at_utc"].endswith("Z")
    assert payload["coverage_warnings"] == expected["coverage_warnings"], "Earnings calendar coverage warnings should match the fixture"
    assert payload["events"][0]["symbol"] == "NVDA", "Requested symbol should be boosted to the top of the example output"
    assert payload["events"][0]["session"] == "after-close", "Example earnings output should expose canonical session fields"
    assert payload["analysis"] == expected["analysis"], "Earnings calendar analysis should match the interpreted fixture"


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
    expected = load_json(repo_root / "skills/market-regime-detector/fixtures/expected-output.json")
    assert payload == expected, "Market regime smoke test should match the expected fixture output"


def test_position_sizing_script_smoke(repo_root):
    fixture_input = load_json(repo_root / "skills/position-sizing/fixtures/example-input.json")
    expected = load_json(repo_root / "skills/position-sizing/fixtures/expected-output.json")
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/position-sizing/scripts/calculate_position_size.py",
            "--account-size",
            str(fixture_input["account_size"]),
            "--risk-percent",
            str(fixture_input["risk_percent"]),
            "--entry",
            str(fixture_input["entry"]),
            "--stop",
            str(fixture_input["stop"]),
            "--slippage",
            str(fixture_input["slippage"]),
            "--fee-per-unit",
            str(fixture_input["fee_per_unit"]),
            "--contract-multiplier",
            str(fixture_input["contract_multiplier"]),
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload == expected, "Position sizing smoke test should match the expected fixture output"


def test_risk_reward_script_smoke(repo_root):
    fixture_input = load_json(repo_root / "skills/risk-reward-sanity-check/fixtures/example-input.json")
    expected = load_json(repo_root / "skills/risk-reward-sanity-check/fixtures/expected-output.json")
    output = run_command(
        repo_root,
        [
            "python3",
            "skills/risk-reward-sanity-check/scripts/check_trade_structure.py",
            "--direction",
            fixture_input["direction"],
            "--entry",
            str(fixture_input["entry"]),
            "--stop",
            str(fixture_input["stop"]),
            "--target",
            str(fixture_input["target"]),
            "--thesis",
            fixture_input["thesis"],
            "--time-horizon",
            fixture_input["time_horizon"],
            "--event-risk",
            fixture_input["event_risk"],
            "--json",
        ],
    )
    payload = json.loads(output)
    assert payload == expected, "Risk-reward smoke test should match the expected fixture output"
