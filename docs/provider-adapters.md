# Provider Adapters

## Purpose

Provider adapters let a public capability use one or more data sources without exposing provider complexity as a public packaging problem.

Users install `economic-calendar`, not `fmp-economic-calendar`.

## Adapter contract

Each adapter should expose three concerns:

1. Availability or config check
2. Raw fetch
3. Canonical normalization

A minimal Python interface can look like this:

```python
class ProviderAdapter:
    provider_name = "example"

    def is_available(self) -> tuple[bool, str]:
        ...

    def fetch_raw(self, **kwargs) -> object:
        ...

    def normalize(self, raw: object, **kwargs) -> list[dict]:
        ...
```

The exact method signatures can vary by skill, but those three responsibilities should stay explicit.

## Selection strategy

v1 uses a pragmatic selection order:

1. Use an explicitly requested provider if available
2. Otherwise use the primary live provider if configured
3. Otherwise fall back to an example adapter if the skill supports one
4. Otherwise return a clear setup message

This keeps the public skill usable without forcing every contributor to solve provider orchestration upfront.

## Fallback behavior

A fallback should be intentional and visible:

- identify the provider used
- identify whether it is live or example data
- include timestamp and coverage notes when possible
- never silently present example data as current market data

## Adding a new provider

To add a provider to an existing skill:

1. Create `skills/<capability>/providers/<provider>/`
2. Implement availability, fetch, and normalize
3. Normalize into the documented canonical schema
4. Add tests or fixtures when practical
5. Update any selection logic in `scripts/`
6. Keep user-facing instructions capability-first

## Why provider-specific public skills are usually the wrong default

Public provider-specific skills:

- make installation more confusing
- create duplicate user journeys
- push vendor choices onto users who do not care
- make migration between providers a breaking packaging change

The default should be one public skill per capability, with provider-specific internals hidden behind a documented adapter seam.
