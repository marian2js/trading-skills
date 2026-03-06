"""Shared helpers for data-backed skills."""

from __future__ import annotations

import json
import socket
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class ProviderRuntimeError(RuntimeError):
    """User-facing provider or transport error."""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def coerce_utc_datetime(value, *, fallback_to_now: bool = False) -> str | None:
    if not value:
        return utc_now_iso() if fallback_to_now else None

    text = str(value).strip().replace(" ", "T")
    if text.endswith("Z"):
        return text
    if len(text) == 10:
        return f"{text}T00:00:00Z"
    if "+" not in text and text.count(":") >= 2:
        return f"{text}Z"
    return text


def within_date_window(timestamp: str, start_date: str | None, end_date: str | None) -> bool:
    date_part = timestamp[:10]
    if start_date and date_part < start_date:
        return False
    if end_date and date_part > end_date:
        return False
    return True


def safe_json_request(
    url: str,
    params: dict[str, str | None],
    *,
    timeout: float = 10.0,
    provider_name: str,
):
    query = urlencode({key: value for key, value in params.items() if value not in (None, "")})
    request = Request(
        f"{url}?{query}",
        headers={"User-Agent": "trading-skills/0.1"},
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            raw_body = response.read().decode("utf-8")
    except HTTPError as exc:
        raise ProviderRuntimeError(
            f"{provider_name} returned HTTP {exc.code}. Check credentials, provider status, and request parameters."
        ) from exc
    except URLError as exc:
        raise ProviderRuntimeError(
            f"Network error while contacting {provider_name}: {exc.reason}. Check your connection or try again later."
        ) from exc
    except socket.timeout as exc:
        raise ProviderRuntimeError(
            f"Request to {provider_name} timed out. Try again later or use example data."
        ) from exc

    try:
        return json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise ProviderRuntimeError(
            f"{provider_name} returned malformed JSON. Try again later or switch to example data."
        ) from exc


def ensure_list_payload(payload, *, provider_name: str, expected: str):
    if not isinstance(payload, list):
        raise ProviderRuntimeError(
            f"{provider_name} returned an unexpected payload shape. Expected a list of {expected}."
        )
    return payload


def select_adapter(
    *,
    provider: str,
    adapters: dict[str, object],
    primary_live_provider: str,
    example_provider: str,
    live_only: bool,
):
    if provider != "auto":
        adapter = adapters[provider]
        ok, reason = adapter.is_available()
        if not ok:
            raise ProviderRuntimeError(reason)
        return adapter, None, f"Explicit provider '{provider}' selected."

    live_adapter = adapters[primary_live_provider]
    ok, reason = live_adapter.is_available()
    if ok:
        return live_adapter, None, f"Auto-selected configured live provider '{primary_live_provider}'."

    if live_only:
        raise ProviderRuntimeError(
            f"Live-only mode requested, but the live provider is unavailable: {reason}"
        )

    example_adapter = adapters[example_provider]
    example_ok, example_reason = example_adapter.is_available()
    if not example_ok:
        raise ProviderRuntimeError(
            f"No usable provider is available. Live provider failed: {reason}. Example provider failed: {example_reason}"
        )

    return (
        example_adapter,
        reason,
        f"Live provider unavailable ({reason}); using example fixture data.",
    )


def output_envelope(
    *,
    provider: str,
    data_mode: str,
    selection_reason: str,
    fallback_reason: str | None,
    requested_window: dict[str, str | None],
    events: list[dict],
    analysis: dict,
    coverage_warnings: list[str],
):
    warnings = list(coverage_warnings)
    if not events:
        warnings.append("No events matched the requested window.")
    return {
        "data_mode": data_mode,
        "provider": provider,
        "selection_reason": selection_reason,
        "fallback_reason": fallback_reason,
        "requested_window": requested_window,
        "retrieved_at_utc": utc_now_iso(),
        "event_count": len(events),
        "coverage_warnings": warnings,
        "analysis": analysis,
        "events": events,
    }
