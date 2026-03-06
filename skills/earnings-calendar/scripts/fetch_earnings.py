#!/usr/bin/env python3
"""Fetch, normalize, and analyze earnings calendar events."""

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
        return adapter, f"Explicit provider '{provider}' selected."

    live = adapters["fmp"]
    ok, reason = live.is_available()
    if ok:
        return live, "Auto-selected configured live provider 'fmp'."
    return adapters["example"], f"Live provider unavailable ({reason}); using example fixture data."


def analyze_events(events: list[dict], watchlist: list[str]) -> dict:
    high_importance = [event for event in events if event["importance"] == "high"]
    direct_hits = [event["symbol"] for event in events if event["symbol"] in set(watchlist)]
    missing_estimates = [
        event["symbol"]
        for event in events
        if event.get("estimate_eps") in (None, "", "null")
        or event.get("estimate_revenue") in (None, "", "null")
    ]
    return {
        "high_importance_count": len(high_importance),
        "direct_watchlist_hits": direct_hits,
        "coverage_warnings": (
            [f"Missing estimate fields for: {', '.join(missing_estimates[:3])}"]
            if missing_estimates
            else []
        ),
    }


def main() -> int:
    args = parse_args()
    watchlist = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]

    try:
        adapter, selection_reason = choose_adapter(args.provider)
        raw = adapter.fetch_raw(start_date=args.start_date, end_date=args.end_date)
        events = adapter.normalize(raw, start_date=args.start_date, end_date=args.end_date, watchlist=watchlist)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    payload = {
        "provider": adapter.provider_name,
        "selection_reason": selection_reason,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "event_count": len(events),
        "analysis": analyze_events(events, watchlist),
        "events": events,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Provider: {payload['provider']}")
    print(f"Selection: {payload['selection_reason']}")
    print(f"Retrieved: {payload['retrieved_at_utc']}")
    print(f"Events: {payload['event_count']}")
    for event in events:
        print(
            f"- {event['scheduled_time_utc']} | {event['symbol']} | score={event['relevance_score']} | "
            f"{event['company_name']} ({event['session']})"
        )
        print(f"  rationale: {event['relevance_notes']}")
        print(f"  coverage: {event['coverage_notes']}")
    for warning in payload["analysis"]["coverage_warnings"]:
        print(f"Warning: {warning}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
