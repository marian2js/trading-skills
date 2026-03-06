# Architecture

## Core idea

This repository is designed around user-facing capabilities, not raw integrations.

That means:

- `economic-calendar` is a public skill
- `earnings-calendar` is a public skill
- provider adapters such as `fmp` are implementation details inside those skills

This is the default because users think in terms of a job to be done, not in terms of vendor topology.

The same principle applies to scope boundaries: broker execution is not part of v1. Decision support comes first, while brokerage workflows remain explicitly out of scope.

## Skill != API

A skill is a repeatable decision-support capability. It may use:

- no external data at all
- one external source
- several sources normalized into a common representation
- user-provided observations or files

An API is only one possible dependency.

Treating "skill" and "API integration" as the same concept causes predictable product problems:

- the install surface becomes cluttered with vendor names
- users must understand internal implementation choices
- swapping providers becomes a packaging problem instead of an internal change
- the capability becomes harder to trust because the design reflects engineering internals more than the user workflow

## Capability-first vs provider-first

Capability-first design produces cleaner public UX:

- one public skill per user job
- stable naming over time
- room to evolve internals without breaking the public mental model

Provider-first design tends to create unnecessary fragmentation:

- `fmp-earnings-calendar`
- `fred-economic-calendar`
- `alpaca-market-regime`

Those names may describe implementation, but they are usually poor product defaults.

Provider-specific public skills should be rare and justified by user-facing differences, not engineering convenience.

## Internal adapter pattern

Data-backed skills use a simple internal adapter pattern:

1. Check whether a provider is available
2. Fetch raw provider data
3. Normalize it into a canonical schema
4. Run the analysis logic on the normalized schema
5. Disclose provider, freshness, and limitations in output

This gives the repo a stable internal seam:

- new providers can be added without changing the public skill name
- normalized data becomes easier to test
- ranking and analysis code can be reused across providers
- provider quirks stay out of the user-facing reasoning layer

## v1 approach

The repository is intentionally pragmatic in v1:

- one primary provider per capability is acceptable
- a mock or example provider is required where practical
- the internal contract should be explicit even if only one live adapter exists today

This keeps the codebase future-proof without turning v1 into a framework project.

## Static, data-optional, and data-required skills

The repository documents dependency classes clearly because users need to know setup cost before installing:

- `static`: works immediately
- `data-optional`: useful without live data, better with additional inputs
- `data-required`: needs external data to be fully useful
- `broker-required`: reserved for future execution workflows

The dependency class is part of the trust model. It helps users understand what the skill can and cannot do in a fresh install.
