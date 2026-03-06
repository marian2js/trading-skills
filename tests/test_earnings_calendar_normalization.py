from __future__ import annotations

from tests.helpers import EARNINGS_EVENT_REQUIRED_FIELDS, import_module_from_path, load_json


def test_earnings_calendar_fixture_normalizes_to_expected_schema(repo_root):
    module = import_module_from_path(
        "earnings_fmp_adapter",
        repo_root / "skills/earnings-calendar/providers/fmp/adapter.py",
    )
    adapter = module.FMPEarningsCalendarAdapter()
    raw = load_json(repo_root / "skills/earnings-calendar/fixtures/upcoming-week.json")
    expected = load_json(repo_root / "skills/earnings-calendar/fixtures/normalized-events.json")

    actual = adapter.normalize(raw)
    assert actual == expected, "Earnings calendar normalization should match the canonical fixture output"

    for event in actual:
        missing = EARNINGS_EVENT_REQUIRED_FIELDS - set(event)
        assert not missing, f"Earnings event is missing required fields: {sorted(missing)}"
