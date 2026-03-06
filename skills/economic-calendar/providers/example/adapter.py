"""Example adapter for normalized economic calendar events."""

from __future__ import annotations

import json
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[2] / "fixtures" / "normalized-events.json"


class ExampleEconomicCalendarAdapter:
    provider_name = "example"

    def is_available(self) -> tuple[bool, str]:
        return True, "Example fixture is always available."

    def fetch_raw(self, start_date=None, end_date=None, country=None):
        return json.loads(FIXTURE.read_text(encoding="utf-8"))

    def normalize(self, raw, start_date=None, end_date=None, country=None):
        events = []
        for item in raw:
            if country and item["country"].lower() != country.lower():
                continue
            if not _within_date_window(item["scheduled_time_utc"], start_date, end_date):
                continue
            events.append(item)
        return sorted(events, key=lambda event: event["scheduled_time_utc"])


def _within_date_window(timestamp, start_date, end_date):
    date_part = timestamp[:10]
    if start_date and date_part < start_date:
        return False
    if end_date and date_part > end_date:
        return False
    return True
