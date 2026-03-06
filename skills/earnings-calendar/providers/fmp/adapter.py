"""FMP adapter for normalized earnings calendar events."""

from __future__ import annotations

import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen


class FMPEarningsCalendarAdapter:
    provider_name = "fmp"
    endpoint = "https://financialmodelingprep.com/stable/earnings-calendar"

    def is_available(self) -> tuple[bool, str]:
        if os.getenv("FMP_API_KEY"):
            return True, "FMP_API_KEY found."
        return False, "FMP_API_KEY is not set. Use --provider example for demo data."

    def fetch_raw(self, start_date=None, end_date=None):
        api_key = os.getenv("FMP_API_KEY")
        params = {"apikey": api_key}
        if start_date:
            params["from"] = start_date
        if end_date:
            params["to"] = end_date

        with urlopen(f"{self.endpoint}?{urlencode(params)}") as response:
            return json.loads(response.read().decode("utf-8"))

    def normalize(self, raw, start_date=None, end_date=None, watchlist=None):
        watchlist = set(watchlist or [])
        normalized = []
        for item in raw:
            symbol = (item.get("symbol") or "").upper()
            company_name = item.get("name") or symbol or "Unknown company"
            relevance_score, relevance_notes = score_relevance(
                symbol=symbol,
                sector=item.get("sector"),
                market_cap=item.get("marketCap"),
                watchlist=watchlist,
            )
            importance = classify_importance(item.get("marketCap"), symbol in watchlist)
            normalized.append(
                {
                    "schema_version": 1,
                    "event_id": f"fmp-{symbol.lower()}-{item.get('date', 'unknown')}",
                    "provider": self.provider_name,
                    "company_name": company_name,
                    "symbol": symbol,
                    "exchange": item.get("exchangeShortName"),
                    "sector": item.get("sector"),
                    "scheduled_time_utc": coerce_earnings_datetime(item.get("date"), item.get("time")),
                    "session": normalize_session(item.get("time")),
                    "estimate_eps": stringify(item.get("epsEstimated")),
                    "actual_eps": stringify(item.get("epsActual")),
                    "estimate_revenue": stringify(item.get("revenueEstimated")),
                    "actual_revenue": stringify(item.get("revenueActual")),
                    "importance": importance,
                    "market_cap_bucket": bucket_market_cap(item.get("marketCap")),
                    "relevance_score": relevance_score,
                    "relevance_notes": relevance_notes,
                    "status": "released" if item.get("epsActual") is not None else "scheduled",
                    "source_url": self.endpoint,
                    "last_updated_utc": coerce_timestamp(item.get("lastUpdated")) or coerce_earnings_datetime(item.get("date"), item.get("time")),
                    "coverage_notes": (
                        "Normalized from FMP earnings calendar data. Timing, sector fields, "
                        "and revenue estimates may be incomplete or shift near the report date."
                    ),
                }
            )
        filtered = [
            event
            for event in normalized
            if within_date_window(event["scheduled_time_utc"], start_date, end_date)
        ]
        return sorted(filtered, key=lambda event: (-event["relevance_score"], event["scheduled_time_utc"]))


def stringify(value):
    if value is None:
        return None
    return str(value)


def normalize_session(value):
    lowered = str(value or "").strip().lower()
    if lowered in {"amc", "after-close", "after market close"}:
        return "after-close"
    if lowered in {"bmo", "before-open", "before market open"}:
        return "before-open"
    return "unspecified"


def coerce_earnings_datetime(date_value, time_value):
    if not date_value:
        return "1970-01-01T00:00:00Z"
    if "T" in str(date_value):
        return coerce_timestamp(date_value)
    timing = normalize_session(time_value)
    if timing == "after-close":
        return f"{date_value}T20:15:00Z"
    if timing == "before-open":
        return f"{date_value}T11:30:00Z"
    return f"{date_value}T00:00:00Z"


def coerce_timestamp(value):
    if not value:
        return None
    text = str(value).strip().replace(" ", "T")
    if text.endswith("Z"):
        return text
    if len(text) == 10:
        return f"{text}T00:00:00Z"
    if "+" not in text and text.count(":") >= 2:
        return f"{text}Z"
    return text


def bucket_market_cap(value):
    try:
        market_cap = float(value)
    except (TypeError, ValueError):
        return "unknown"
    if market_cap >= 200_000_000_000:
        return "mega-cap"
    if market_cap >= 10_000_000_000:
        return "large-cap"
    if market_cap >= 2_000_000_000:
        return "mid-cap"
    return "small-cap"


def score_relevance(symbol, sector, market_cap, watchlist):
    score = 40
    notes = []

    if symbol in watchlist:
        score += 35
        notes.append("Directly requested symbol.")

    bucket = bucket_market_cap(market_cap)
    if bucket == "mega-cap":
        score += 25
        notes.append("Mega-cap benchmark with index sensitivity.")
    elif bucket == "large-cap":
        score += 15
        notes.append("Large-cap name with broader market visibility.")

    if sector and str(sector).lower() in {"technology", "semiconductors", "financials", "energy"}:
        score += 10
        notes.append("Sector has meaningful read-through potential.")

    if not notes:
        notes.append("Relevant event, but broad market read-through appears limited.")

    return min(score, 100), " ".join(notes)


def classify_importance(market_cap, in_watchlist):
    bucket = bucket_market_cap(market_cap)
    if in_watchlist or bucket == "mega-cap":
        return "high"
    if bucket == "large-cap":
        return "medium"
    return "low"


def within_date_window(timestamp, start_date, end_date):
    date_part = timestamp[:10]
    if start_date and date_part < start_date:
        return False
    if end_date and date_part > end_date:
        return False
    return True
