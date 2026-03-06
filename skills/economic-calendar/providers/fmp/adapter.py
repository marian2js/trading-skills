"""FMP adapter for normalized economic calendar events."""

from __future__ import annotations

import json
import os
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen


class FMPEconomicCalendarAdapter:
    provider_name = "fmp"
    endpoint = "https://financialmodelingprep.com/stable/economic-calendar"

    def is_available(self) -> tuple[bool, str]:
        if os.getenv("FMP_API_KEY"):
            return True, "FMP_API_KEY found."
        return False, "FMP_API_KEY is not set. Use --provider example for demo data."

    def fetch_raw(self, start_date=None, end_date=None, country=None):
        api_key = os.getenv("FMP_API_KEY")
        params = {"apikey": api_key}
        # FMP calendar endpoints commonly accept from/to date windows.
        if start_date:
            params["from"] = start_date
        if end_date:
            params["to"] = end_date
        if country:
            params["country"] = country

        with urlopen(f"{self.endpoint}?{urlencode(params)}") as response:
            return json.loads(response.read().decode("utf-8"))

    def normalize(self, raw, start_date=None, end_date=None, country=None):
        normalized = []
        for item in raw:
            scheduled = item.get("date") or item.get("scheduledTime") or item.get("timestamp")
            scheduled_time_utc = _coerce_datetime(scheduled)
            record_country = item.get("country") or item.get("countryCode") or "unknown"
            if country and record_country.lower() != country.lower():
                continue

            event_name = item.get("event") or item.get("name") or "Unnamed economic event"
            event_id = f"fmp-{record_country.lower()}-{slugify(event_name)}-{scheduled_time_utc}"
            normalized.append(
                {
                    "schema_version": 1,
                    "event_id": event_id,
                    "provider": self.provider_name,
                    "event_name": event_name,
                    "country": record_country,
                    "currency": item.get("currency") or "unknown",
                    "scheduled_time_utc": scheduled_time_utc,
                    "importance": normalize_importance(item.get("impact") or item.get("importance")),
                    "category": item.get("category") or "macro",
                    "previous": stringify(item.get("previous")),
                    "consensus": stringify(item.get("estimate") or item.get("consensus")),
                    "actual": stringify(item.get("actual")),
                    "unit": item.get("unit"),
                    "status": normalize_status(item.get("actual")),
                    "source_url": self.endpoint,
                    "last_updated_utc": _coerce_datetime(item.get("lastUpdated") or scheduled),
                    "coverage_notes": (
                        "Normalized from FMP economic calendar data. Importance and category "
                        "can be provider-specific, and some releases may omit estimates or revisions."
                    ),
                }
            )
        filtered = [
            event
            for event in normalized
            if _within_date_window(event["scheduled_time_utc"], start_date, end_date)
        ]
        return sorted(filtered, key=lambda event: event["scheduled_time_utc"])


def stringify(value):
    if value is None:
        return None
    return str(value)


def normalize_importance(value):
    if value is None:
        return "unknown"
    lowered = str(value).strip().lower()
    if lowered in {"high", "3", "3.0"}:
        return "high"
    if lowered in {"medium", "2", "2.0"}:
        return "medium"
    if lowered in {"low", "1", "1.0"}:
        return "low"
    return lowered


def normalize_status(actual):
    return "released" if actual not in (None, "", "null") else "scheduled"


def slugify(value):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def _coerce_datetime(value):
    if not value:
        return datetime.utcnow().isoformat(timespec="seconds") + "Z"

    text = str(value).strip().replace(" ", "T")
    if text.endswith("Z"):
        return text
    if len(text) == 10:
        return f"{text}T00:00:00Z"
    if "+" not in text and text.count(":") == 2:
        return f"{text}Z"
    return text


def _within_date_window(timestamp, start_date, end_date):
    date_part = timestamp[:10]
    if start_date and date_part < start_date:
        return False
    if end_date and date_part > end_date:
        return False
    return True
