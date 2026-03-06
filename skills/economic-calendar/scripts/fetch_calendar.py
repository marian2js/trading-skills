#!/usr/bin/env python3
"""Fetch, normalize, and analyze economic calendar events."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from providers.example.adapter import ExampleEconomicCalendarAdapter
from providers.fmp.adapter import FMPEconomicCalendarAdapter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch normalized economic calendar events."
    )
    parser.add_argument("--provider", default="auto", choices=["auto", "fmp", "example"])
    parser.add_argument("--start-date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--end-date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--country", default=None, help="Optional country code filter.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def choose_adapter(provider: str):
    adapters = {
        "fmp": FMPEconomicCalendarAdapter(),
        "example": ExampleEconomicCalendarAdapter(),
    }
    if provider != "auto":
        adapter = adapters[provider]
        ok, reason = adapter.is_available()
        if not ok:
            raise RuntimeError(reason)
        return adapter, f"Explicit provider '{provider}' selected."

    live = adapters["fmp"]
    ok, reason = live.is_available()
    if ok:
        return live, "Auto-selected configured live provider 'fmp'."
    return adapters["example"], f"Live provider unavailable ({reason}); using example fixture data."


def analyze_events(events: list[dict]) -> dict:
    high_impact = [event for event in events if event["importance"] == "high"]
    missing_consensus = [event["event_name"] for event in events if event.get("consensus") in (None, "", "null")]
    countries = sorted({event["country"] for event in events})

    return {
        "high_impact_count": len(high_impact),
        "high_impact_events": [
            {
                "event_name": event["event_name"],
                "country": event["country"],
                "scheduled_time_utc": event["scheduled_time_utc"],
            }
            for event in high_impact[:5]
        ],
        "countries_covered": countries,
        "coverage_warnings": (
            [f"Consensus missing for: {', '.join(missing_consensus[:3])}"]
            if missing_consensus
            else []
        ),
    }


def main() -> int:
    args = parse_args()

    try:
        adapter, selection_reason = choose_adapter(args.provider)
        raw = adapter.fetch_raw(
            start_date=args.start_date,
            end_date=args.end_date,
            country=args.country,
        )
        events = adapter.normalize(
            raw,
            start_date=args.start_date,
            end_date=args.end_date,
            country=args.country,
        )
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    payload = {
        "provider": adapter.provider_name,
        "selection_reason": selection_reason,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "event_count": len(events),
        "analysis": analyze_events(events),
        "events": events,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Provider: {payload['provider']}")
    print(f"Selection: {payload['selection_reason']}")
    print(f"Retrieved: {payload['retrieved_at_utc']}")
    print(f"Events: {payload['event_count']}")
    print(f"High-impact events: {payload['analysis']['high_impact_count']}")
    for event in events:
        print(
            f"- {event['scheduled_time_utc']} | {event['importance']} | "
            f"{event['country']} {event['event_name']} "
            f"(status={event['status']}, provider={event['provider']})"
        )
        print(f"  coverage: {event['coverage_notes']}")
    for warning in payload["analysis"]["coverage_warnings"]:
        print(f"Warning: {warning}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
