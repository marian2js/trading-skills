"""FMP adapter for normalized economic calendar events."""

from __future__ import annotations

import os
import sys
from pathlib import Path


SHARED_SCRIPTS_DIR = Path(__file__).resolve().parents[4] / "scripts"
if str(SHARED_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_SCRIPTS_DIR))

from live_data_common import (
    ProviderRuntimeError,
    coerce_utc_datetime,
    ensure_list_payload,
    safe_json_request,
    within_date_window,
)


class FMPEconomicCalendarAdapter:
    provider_name = "fmp"
    data_mode = "live"
    endpoint = "https://financialmodelingprep.com/stable/economic-calendar"

    def is_available(self) -> tuple[bool, str]:
        if os.getenv("FMP_API_KEY"):
            return True, "FMP_API_KEY found."
        return False, "FMP_API_KEY is not set. Use --provider example for demo data."

    def fetch_raw(self, start_date=None, end_date=None, country=None):
        api_key = os.getenv("FMP_API_KEY")
        params = {"apikey": api_key}
        if start_date:
            params["from"] = start_date
        if end_date:
            params["to"] = end_date
        if country:
            params["country"] = country
        payload = safe_json_request(
            self.endpoint,
            params,
            provider_name=self.provider_name,
        )
        return ensure_list_payload(
            payload,
            provider_name=self.provider_name,
            expected="economic calendar events",
        )

    def normalize(self, raw, start_date=None, end_date=None, country=None):
        ensure_list_payload(raw, provider_name=self.provider_name, expected="economic calendar events")
        normalized = []
        for item in raw:
            if not isinstance(item, dict):
                raise ProviderRuntimeError(
                    f"{self.provider_name} returned a malformed event item; expected an object per row."
                )
            scheduled = item.get("date") or item.get("scheduledTime") or item.get("timestamp")
            scheduled_time_utc = coerce_utc_datetime(scheduled, fallback_to_now=True)
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
                    "last_updated_utc": coerce_utc_datetime(item.get("lastUpdated") or scheduled, fallback_to_now=True),
                    "coverage_notes": (
                        "Normalized from FMP economic calendar data. Importance and category "
                        "can be provider-specific, and some releases may omit estimates or revisions."
                    ),
                }
            )
        filtered = [
            event
            for event in normalized
            if within_date_window(event["scheduled_time_utc"], start_date, end_date)
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
