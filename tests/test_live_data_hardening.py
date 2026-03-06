from __future__ import annotations

import json
import os
import subprocess
from io import BytesIO
from urllib.error import HTTPError, URLError

import pytest

from tests.helpers import import_module_from_path, load_json


def run_cli(repo_root, args, env=None):
    return subprocess.run(
        args,
        cwd=repo_root,
        env=env,
        capture_output=True,
        text=True,
    )


class FakeResponse:
    def __init__(self, body: str):
        self.body = body.encode("utf-8")

    def read(self) -> bytes:
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def test_safe_json_request_wraps_http_errors(repo_root, monkeypatch):
    module = import_module_from_path("live_data_common_http", repo_root / "scripts/live_data_common.py")

    def fake_urlopen(*args, **kwargs):
        raise HTTPError(
            url="https://example.test",
            code=401,
            msg="Unauthorized",
            hdrs=None,
            fp=BytesIO(b"{}"),
        )

    monkeypatch.setattr(module, "urlopen", fake_urlopen)

    with pytest.raises(module.ProviderRuntimeError, match="HTTP 401"):
        module.safe_json_request("https://example.test", {}, provider_name="fmp")


def test_safe_json_request_wraps_network_errors(repo_root, monkeypatch):
    module = import_module_from_path("live_data_common_network", repo_root / "scripts/live_data_common.py")

    def fake_urlopen(*args, **kwargs):
        raise URLError("offline")

    monkeypatch.setattr(module, "urlopen", fake_urlopen)

    with pytest.raises(module.ProviderRuntimeError, match="Network error"):
        module.safe_json_request("https://example.test", {}, provider_name="fmp")


def test_safe_json_request_wraps_malformed_json(repo_root, monkeypatch):
    module = import_module_from_path("live_data_common_json", repo_root / "scripts/live_data_common.py")
    monkeypatch.setattr(module, "urlopen", lambda *args, **kwargs: FakeResponse("not-json"))

    with pytest.raises(module.ProviderRuntimeError, match="malformed JSON"):
        module.safe_json_request("https://example.test", {}, provider_name="fmp")


def test_economic_adapter_rejects_unexpected_payload_shape(repo_root):
    module = import_module_from_path(
        "economic_adapter_bad_shape",
        repo_root / "skills/economic-calendar/providers/fmp/adapter.py",
    )
    adapter = module.FMPEconomicCalendarAdapter()
    with pytest.raises(RuntimeError, match="unexpected payload shape"):
        adapter.normalize({"not": "a list"})


def test_earnings_adapter_rejects_unexpected_payload_shape(repo_root):
    module = import_module_from_path(
        "earnings_adapter_bad_shape",
        repo_root / "skills/earnings-calendar/providers/fmp/adapter.py",
    )
    adapter = module.FMPEarningsCalendarAdapter()
    with pytest.raises(RuntimeError, match="unexpected payload shape"):
        adapter.normalize({"not": "a list"})


def test_economic_degraded_payload_surfaces_warning(repo_root):
    adapter_module = import_module_from_path(
        "economic_adapter_degraded",
        repo_root / "skills/economic-calendar/providers/fmp/adapter.py",
    )
    script_module = import_module_from_path(
        "economic_fetch_script",
        repo_root / "skills/economic-calendar/scripts/fetch_calendar.py",
    )
    adapter = adapter_module.FMPEconomicCalendarAdapter()
    degraded = load_json(repo_root / "skills/economic-calendar/fixtures/degraded-provider-payload.json")

    normalized = adapter.normalize(degraded)
    analysis, coverage_warnings = script_module.analyze_events(normalized)

    assert normalized[0]["importance"] == "unknown"
    assert analysis["high_impact_count"] == 0
    assert coverage_warnings == ["Consensus missing for: US CPI YoY"]


def test_earnings_degraded_payload_surfaces_warning(repo_root):
    adapter_module = import_module_from_path(
        "earnings_adapter_degraded",
        repo_root / "skills/earnings-calendar/providers/fmp/adapter.py",
    )
    script_module = import_module_from_path(
        "earnings_fetch_script",
        repo_root / "skills/earnings-calendar/scripts/fetch_earnings.py",
    )
    adapter = adapter_module.FMPEarningsCalendarAdapter()
    degraded = load_json(repo_root / "skills/earnings-calendar/fixtures/degraded-provider-payload.json")

    normalized = adapter.normalize(degraded)
    analysis, coverage_warnings = script_module.analyze_events(normalized, [])

    assert normalized[0]["session"] == "unspecified"
    assert analysis["high_importance_count"] == 1
    assert coverage_warnings == ["Missing estimate fields for: ADBE"]


def test_economic_empty_result_behavior(repo_root):
    result = run_cli(
        repo_root,
        [
            "python3",
            "skills/economic-calendar/scripts/fetch_calendar.py",
            "--provider",
            "example",
            "--start-date",
            "2026-04-01",
            "--end-date",
            "2026-04-02",
            "--json",
        ],
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["event_count"] == 0
    assert payload["coverage_warnings"] == ["No events matched the requested window."]


def test_date_window_boundary_behavior(repo_root):
    result = run_cli(
        repo_root,
        [
            "python3",
            "skills/economic-calendar/scripts/fetch_calendar.py",
            "--provider",
            "example",
            "--start-date",
            "2026-03-12",
            "--end-date",
            "2026-03-12",
            "--json",
        ],
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["event_count"] == 1
    assert payload["events"][0]["event_name"] == "ECB Rate Decision"


def test_explicit_live_provider_missing_key_reports_clean_error(repo_root):
    env = dict(os.environ)
    env.pop("FMP_API_KEY", None)
    result = run_cli(
        repo_root,
        [
            "python3",
            "skills/economic-calendar/scripts/fetch_calendar.py",
            "--provider",
            "fmp",
            "--json",
        ],
        env=env,
    )
    assert result.returncode == 1
    assert "FMP_API_KEY" in result.stderr
    assert "Traceback" not in result.stderr


def test_live_only_mode_prevents_example_fallback(repo_root):
    env = dict(os.environ)
    env.pop("FMP_API_KEY", None)
    result = run_cli(
        repo_root,
        [
            "python3",
            "skills/earnings-calendar/scripts/fetch_earnings.py",
            "--provider",
            "auto",
            "--live-only",
            "--json",
        ],
        env=env,
    )
    assert result.returncode == 1
    assert "Live-only mode requested" in result.stderr
    assert "Traceback" not in result.stderr
