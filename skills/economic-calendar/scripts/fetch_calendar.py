#!/usr/bin/env python3
"""Fetch, normalize, and analyze economic calendar events."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))
SHARED_SCRIPTS_DIR = Path(__file__).resolve().parents[3] / "scripts"
if str(SHARED_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_SCRIPTS_DIR))

from live_data_common import ProviderRuntimeError, output_envelope, select_adapter
import json


def load_adapter_class(module_name: str, relative_path: str, class_name: str):
    module_path = SKILL_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load adapter module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)


ExampleEconomicCalendarAdapter = load_adapter_class(
    "economic_example_adapter",
    "providers/example/adapter.py",
    "ExampleEconomicCalendarAdapter",
)
FMPEconomicCalendarAdapter = load_adapter_class(
    "economic_fmp_adapter",
    "providers/fmp/adapter.py",
    "FMPEconomicCalendarAdapter",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch normalized economic calendar events."
    )
    parser.add_argument("--provider", default="auto", choices=["auto", "fmp", "example"])
    parser.add_argument("--start-date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--end-date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--country", default=None, help="Optional country code filter.")
    parser.add_argument(
        "--live-only",
        action="store_true",
        help="Fail if live data is unavailable instead of falling back to example fixtures.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def analyze_events(events: list[dict]) -> tuple[dict, list[str]]:
    high_impact = [event for event in events if event["importance"] == "high"]
    missing_consensus = [event["event_name"] for event in events if event.get("consensus") in (None, "", "null")]
    countries = sorted({event["country"] for event in events})
    warnings = (
        [f"Consensus missing for: {', '.join(missing_consensus[:3])}"]
        if missing_consensus
        else []
    )

    return (
        {
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
        },
        warnings,
    )


def main() -> int:
    args = parse_args()
    adapters = {
        "fmp": FMPEconomicCalendarAdapter(),
        "example": ExampleEconomicCalendarAdapter(),
    }

    try:
        adapter, fallback_reason, selection_reason = select_adapter(
            provider=args.provider,
            adapters=adapters,
            primary_live_provider="fmp",
            example_provider="example",
            live_only=args.live_only,
        )
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
        analysis, coverage_warnings = analyze_events(events)
    except ProviderRuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    payload = output_envelope(
        provider=adapter.provider_name,
        data_mode=adapter.data_mode,
        selection_reason=selection_reason,
        fallback_reason=fallback_reason,
        requested_window={
            "start_date": args.start_date,
            "end_date": args.end_date,
            "country": args.country,
        },
        events=events,
        analysis=analysis,
        coverage_warnings=coverage_warnings,
    )

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Data mode: {payload['data_mode']}")
    print(f"Provider: {payload['provider']}")
    print(f"Selection: {payload['selection_reason']}")
    print(f"Retrieved: {payload['retrieved_at_utc']}")
    print(f"Requested window: {payload['requested_window']}")
    print(f"Events: {payload['event_count']}")
    print(f"High-impact events: {payload['analysis']['high_impact_count']}")
    for event in events:
        print(
            f"- {event['scheduled_time_utc']} | {event['importance']} | "
            f"{event['country']} {event['event_name']} "
            f"(status={event['status']}, provider={event['provider']})"
        )
        print(f"  coverage: {event['coverage_notes']}")
    if payload["fallback_reason"]:
        print(f"Fallback: {payload['fallback_reason']}")
    for warning in payload["coverage_warnings"]:
        print(f"Warning: {warning}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
