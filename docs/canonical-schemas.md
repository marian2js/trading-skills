# Canonical Schemas

The v1 data-backed skills normalize provider payloads into explicit, versioned canonical schemas before analysis.

Schema version for both definitions in this document: `1`

## Economic calendar event

Required or strongly recommended fields:

- `schema_version`
- `event_id`
- `provider`
- `event_name`
- `country`
- `currency`
- `scheduled_time_utc`
- `importance`
- `status`
- `source_url`
- `last_updated_utc`
- `coverage_notes`

Optional fields:

- `actual`
- `consensus`
- `previous`
- `unit`
- `category`

Example:

```json
{
  "schema_version": 1,
  "event_id": "fmp-us-cpi-2026-03-12T13:30:00Z",
  "provider": "fmp",
  "event_name": "US CPI YoY",
  "country": "US",
  "currency": "USD",
  "scheduled_time_utc": "2026-03-12T13:30:00Z",
  "importance": "high",
  "category": "inflation",
  "previous": "3.0",
  "consensus": "2.9",
  "actual": null,
  "unit": "%",
  "status": "scheduled",
  "source_url": "https://site.example/economic-calendar/us-cpi",
  "last_updated_utc": "2026-03-06T09:15:00Z",
  "coverage_notes": "Provider may omit revisions and secondary release notes."
}
```

## Earnings event

Required or strongly recommended fields:

- `schema_version`
- `event_id`
- `provider`
- `company_name`
- `symbol`
- `scheduled_time_utc`
- `report_timing`
- `status`
- `source_url`
- `last_updated_utc`
- `coverage_notes`

Optional fields:

- `exchange`
- `sector`
- `estimated_eps`
- `estimated_revenue`
- `market_cap_bucket`
- `relevance_score`
- `relevance_notes`

Example:

```json
{
  "schema_version": 1,
  "event_id": "fmp-nvda-2026-05-27",
  "provider": "fmp",
  "company_name": "NVIDIA Corporation",
  "symbol": "NVDA",
  "exchange": "NASDAQ",
  "sector": "Semiconductors",
  "scheduled_time_utc": "2026-05-27T20:15:00Z",
  "report_timing": "after-close",
  "estimated_eps": "7.12",
  "estimated_revenue": "43.8B",
  "market_cap_bucket": "mega-cap",
  "relevance_score": 95,
  "relevance_notes": "Benchmark component with sector read-through and index weight impact.",
  "status": "scheduled",
  "source_url": "https://site.example/earnings/nvda",
  "last_updated_utc": "2026-03-06T08:50:00Z",
  "coverage_notes": "Timing can shift close to the event date; confirm with investor relations when critical."
}
```

## Normalization rules

- Use UTC timestamps in ISO 8601 format when possible.
- Preserve the provider name in every record.
- Prefer `null` over invented values when the provider omits a field.
- Put provider-specific caveats in `coverage_notes`.
- Keep raw payload quirks out of the analysis layer.
