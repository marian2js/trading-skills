from __future__ import annotations

from pathlib import Path

from tests.helpers import import_module_from_path


ADAPTER_CASES = [
    (
        "economic_fmp",
        Path("skills/macro-event-analysis/providers/fmp/adapter.py"),
        "FMPEconomicCalendarAdapter",
    ),
    (
        "economic_example",
        Path("skills/macro-event-analysis/providers/example/adapter.py"),
        "ExampleEconomicCalendarAdapter",
    ),
    (
        "earnings_fmp",
        Path("skills/earnings-preview/providers/fmp/adapter.py"),
        "FMPEarningsCalendarAdapter",
    ),
    (
        "earnings_example",
        Path("skills/earnings-preview/providers/example/adapter.py"),
        "ExampleEarningsCalendarAdapter",
    ),
]


def test_provider_adapters_follow_internal_contract(repo_root):
    for module_name, relative_path, class_name in ADAPTER_CASES:
        module = import_module_from_path(module_name, repo_root / relative_path)
        adapter_cls = getattr(module, class_name)
        adapter = adapter_cls()

        assert hasattr(adapter, "provider_name"), f"{class_name} should define provider_name"
        assert hasattr(adapter, "data_mode"), f"{class_name} should define data_mode"
        assert callable(getattr(adapter, "is_available", None)), f"{class_name} should implement is_available()"
        assert callable(getattr(adapter, "fetch_raw", None)), f"{class_name} should implement fetch_raw()"
        assert callable(getattr(adapter, "normalize", None)), f"{class_name} should implement normalize()"

        availability = adapter.is_available()
        assert isinstance(availability, tuple), f"{class_name}.is_available() should return a tuple"
        assert len(availability) == 2, f"{class_name}.is_available() should return (bool, reason)"
        assert isinstance(availability[0], bool), f"{class_name}.is_available()[0] should be a bool"
        assert isinstance(availability[1], str), f"{class_name}.is_available()[1] should be a string reason"
