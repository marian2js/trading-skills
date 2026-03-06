from __future__ import annotations

from tests.helpers import ECONOMIC_EVENT_REQUIRED_FIELDS, import_module_from_path, load_json


def test_economic_calendar_fixture_normalizes_to_expected_schema(repo_root):
    module = import_module_from_path(
        "economic_fmp_adapter",
        repo_root / "skills/economic-calendar/providers/fmp/adapter.py",
    )
    adapter = module.FMPEconomicCalendarAdapter()
    raw = load_json(repo_root / "skills/economic-calendar/fixtures/upcoming-week.json")
    expected = load_json(repo_root / "skills/economic-calendar/fixtures/normalized-events.json")

    actual = adapter.normalize(raw)
    assert actual == expected, "Economic calendar normalization should match the canonical fixture output"

    for event in actual:
        missing = ECONOMIC_EVENT_REQUIRED_FIELDS - set(event)
        assert not missing, f"Economic event is missing required fields: {sorted(missing)}"
