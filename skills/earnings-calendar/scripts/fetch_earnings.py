#!/usr/bin/env python3
"""Fetch and normalize earnings calendar events."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILL_ROOT))

from providers.example.adapter import ExampleEarningsCalendarAdapter
from providers.fmp.adapter import FMPEarningsCalendarAdapter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch normalized earnings calendar events."
    )
    parser.add_argument("--provider", default="auto", choices=["auto", "fmp", "example"])
    parser.add_argument("--start-date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--end-date", default=None, help="YYYY-MM-DD")
    parser.add_argument(
        "--symbols",
        default="",
        help="Comma-separated symbol filter for relevance boosting.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    return parser.parse_args()


def choose_adapter(provider: str):
    adapters = {
        "fmp": FMPEarningsCalendarAdapter(),
        "example": ExampleEarningsCalendarAdapter(),
    }
    if provider != "auto":
        adapter = adapters[provider]
        ok, reason = adapter.is_available()
        if not ok:
            raise RuntimeError(reason)
        return adapter

    live = adapters["fmp"]
    ok, _ = live.is_available()
    if ok:
        return live
    return adapters["example"]


def main() -> int:
    args = parse_args()
    watchlist = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]

    try:
        adapter = choose_adapter(args.provider)
        raw = adapter.fetch_raw(start_date=args.start_date, end_date=args.end_date)
        events = adapter.normalize(raw, start_date=args.start_date, end_date=args.end_date, watchlist=watchlist)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    payload = {
        "provider": adapter.provider_name,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "event_count": len(events),
        "events": events,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Provider: {payload['provider']}")
    print(f"Retrieved: {payload['retrieved_at_utc']}")
    print(f"Events: {payload['event_count']}")
    for event in events:
        print(
            f"- {event['scheduled_time_utc']} | {event['symbol']} | score={event['relevance_score']} | "
            f"{event['company_name']} ({event['report_timing']})"
        )
        print(f"  rationale: {event['relevance_notes']}")
        print(f"  coverage: {event['coverage_notes']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
