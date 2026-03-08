# trading-skills

[![CI](https://github.com/marian2js/trading-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/marian2js/trading-skills/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

`trading-skills` is a portable, capability-first collection of trading and investing skills for agent tools that support `SKILL.md`-style packages.

The goal is not to generate magic signals. The goal is to improve decision quality, risk management, execution planning, and review discipline with transparent, auditable workflows.

Broker integrations are explicitly out of scope for v1. This repo does not ship order execution, portfolio syncing, account management, or brokerage adapters.

## Why this repo exists

Most users think in terms of jobs to be done:

- `earnings-preview`
- `macro-event-analysis`
- `position-sizing`
- `market-regime-analysis`

They do not want to think in terms of vendor internals such as `fmp-earnings-preview` or `fred-macro-event-analysis`.

This repository keeps the public UX capability-first:

- A skill is a user-facing capability.
- A provider is an internal implementation detail in most cases.
- Data-backed skills disclose the source, freshness, and limitations of their output.
- Public skills are analyst workflows, not raw data wrappers.

The repository also ships a small machine-readable [catalog.json](catalog.json) so browsing, docs generation, and validation can rely on one simple index.

`trading-skills` is preferred over `trading-agent-skills` because it is cleaner, easier to remember, and centered on the user job rather than the implementation medium.

Current release candidate version: `0.1.0-rc.1` in [VERSION](VERSION).

## Quick links

- [Examples](docs/examples/README.md)
- [Optional provider support](docs/optional-provider-support.md)
- [Compatibility and install](docs/compatibility-and-install.md)
- [Composing skills](docs/composing-skills.md)
- [Contributing](CONTRIBUTING.md)
- [Versioning and releases](docs/versioning-and-releases.md)
- [Changelog](CHANGELOG.md)

## Installation model

The intended UX is simple and capability-first:

```bash
npx skills add marian2js/trading-skills@position-sizing
npx skills add marian2js/trading-skills@macro-event-analysis
npx skills add marian2js/trading-skills@earnings-preview
```

## Quickstart

Use the static skills immediately:

- `pre-trade-check`
- `earnings-trade-prep`
- `watchlist-review`
- `catalyst-map`
- `evidence-gap-check`
- `thesis-validation`
- `position-management`
- `journal-pattern-analyzer`
- `execution-plan-check`
- `portfolio-concentration`
- `position-sizing`
- `risk-reward-sanity-check`
- `post-trade-review`

Use the analysis-first, data-aware skills with the material you already have:

- `macro-event-analysis`
- `earnings-preview`
- `market-regime-analysis`

Only if critical information is missing should these skills consult optional provider support.

See [docs/optional-provider-support.md](docs/optional-provider-support.md) for the provider fallback pattern.

Example walkthroughs for evaluating the current skills live in [docs/examples/](docs/examples/).

Example prompts after installation:

- "Use `position-sizing` for a $125,000 account risking 0.5% with entry 412.30 and stop 406.80."
- "Use `pre-trade-check` on this swing idea and tell me if it is actually ready."
- "Use `earnings-trade-prep` on NVDA for next week and tell me whether this is prep-only, pre-event tradeable, or a hold-through candidate."
- "Use `watchlist-review` on these semis for next week and tell me which names actually deserve active attention."
- "Use `catalyst-map` on my semis watchlist for the next three weeks and show me which events actually matter."
- "Use `evidence-gap-check` on this swing idea and tell me what I still need to know before it deserves deeper work."
- "Use `thesis-validation` on my semis swing thesis and tell me what evidence is real, what is assumption, and what would invalidate it."
- "Use `position-management` on this open long and tell me whether to hold, trim, tighten risk, or exit."
- "Use `journal-pattern-analyzer` on my last 25 trades and tell me what mistake keeps repeating."
- "Use `execution-plan-check` on my plan to buy a niche ETF at the open and tell me whether the order logic is actually executable."
- "Use `portfolio-concentration` on my book before I add to NVDA and tell me if I already have too much semis overlap."
- "Use `risk-reward-sanity-check` on a swing long with entry 58.20, stop 55.90, and target 65.50."
- "Use `macro-event-analysis` to summarize macro event risk for the next 48 hours."
- "Use `earnings-preview` for NVDA, AMD, and the semiconductor group heading into the next earnings-heavy week."
- "Use `market-regime-analysis` to classify current context from my observations without pretending to forecast."
- "Use `post-trade-review` to review a trade where I respected the thesis but violated my stop."

## User Data First

This repo prefers the user's material first:

- pasted notes
- watchlists
- transcripts
- screenshots
- schedules already in context
- estimate tables already in context

Only if critical information is missing should a skill consult optional provider support.

If the user already named a supported provider or already shared usable access details, the skill should use that provider path directly. Otherwise it should ask which supported provider to use.

## Trust model

High-trust output is a product requirement, not a nice-to-have. Skills that use provider-based data should always disclose:

- source or provider used
- freshness or timestamp when available
- coverage gaps and missing fields
- caveats about assumptions, ranking logic, or incomplete visibility

The repo avoids hype, fake precision, and guaranteed-outcome language.

## Initial skills

The current library stays intentionally small and capability-first:

<!-- SKILL_INDEX_START -->
| Skill | Summary | Guide |
| --- | --- | --- |
| `pre-trade-check` | Orchestrate a disciplined pre-trade workflow by routing a watchlist or trade idea through the minimum set of underlying skills needed to decide whether the trade is ready, not ready, or should be resized or reworked first. | [guide](docs/examples/pre-trade-check-walkthrough.md) |
| `earnings-trade-prep` | Orchestrate a disciplined earnings-event workflow by deciding which names deserve prep, mapping the key debates and read-through paths, pressure-testing the thesis and structure, and ending with a clear pre-earnings hold, avoid, or trade decision. | [guide](docs/examples/earnings-trade-prep-walkthrough.md) |
| `watchlist-review` | Review a watchlist and rank which names deserve active attention, background monitoring, or removal based on catalysts, tradability, redundancy, and evidence quality for the user's style and timeframe. | [guide](docs/examples/watchlist-review-walkthrough.md) |
| `catalyst-map` | Build a ranked map of the catalysts that could move a watchlist, theme, or portfolio by showing what matters, when it matters, and how those events could transmit across related names or exposures. | [guide](docs/examples/catalyst-map-walkthrough.md) |
| `evidence-gap-check` | Identify the most important missing facts, assumptions, and unresolved questions that should be answered before a trade or investment idea is trusted, sized, or acted on. | [guide](docs/examples/evidence-gap-check-walkthrough.md) |
| `thesis-validation` | Pressure-test a trade or investment thesis by clarifying the core claim, evidence, invalidation, timeframe, and dependency chain before the user turns it into an entry, stop, or size. | [guide](docs/examples/thesis-validation-walkthrough.md) |
| `position-management` | Review an open position and decide whether to hold, trim, tighten risk, close, or wait by comparing current behavior against the original thesis, invalidation logic, catalyst calendar, and execution constraints. | [guide](docs/examples/position-management-walkthrough.md) |
| `journal-pattern-analyzer` | Analyze a trade journal or trade log to find repeated strengths, mistakes, environment-dependent patterns, and process changes that could improve future decisions without turning the review into hindsight theater. | [guide](docs/examples/journal-pattern-analyzer-walkthrough.md) |
| `execution-plan-check` | Review whether a trade plan is operationally executable by checking order type logic, liquidity and spread risk, event timing, stop realism, and whether the user can actually implement the plan cleanly. | [guide](docs/examples/execution-plan-check-walkthrough.md) |
| `portfolio-concentration` | Evaluate whether a portfolio, account, or planned position is too dependent on a small number of issuers, sectors, themes, or correlated exposures before the user adds or holds more risk. | [guide](docs/examples/portfolio-concentration-walkthrough.md) |
| `position-sizing` | Compute a conservative position size from account equity, risk budget, entry, stop, and trading friction so the user can inspect exposure before entering a trade. | [guide](docs/examples/position-sizing-walkthrough.md) |
| `risk-reward-sanity-check` | Analyze whether a proposed entry, stop, and target structure is coherent, asymmetric enough, and vulnerable to obvious failure modes before the trade is placed. | [guide](docs/examples/risk-reward-sanity-check-walkthrough.md) |
| `post-trade-review` | Guide a disciplined post-trade review across thesis quality, setup quality, execution, adherence, mistakes, and lessons without turning the result into hindsight theater. | [guide](docs/examples/post-trade-review-walkthrough.md) |
| `macro-event-analysis` | Prepare for upcoming macro catalysts by identifying the events that matter, mapping the likely transmission channels, and surfacing timing risk for the user's markets or positions. | [guide](docs/examples/macro-event-analysis-example-mode.md) |
| `earnings-preview` | Prepare for an upcoming earnings report or earnings week by identifying the reports that matter, framing the key debates, and surfacing the read-through risk that could affect the user's watchlist or positions. | [guide](docs/examples/earnings-preview-live-mode.md) |
| `market-regime-analysis` | Analyze current market context through trend, volatility, breadth, and event backdrop so the user can choose tactics that fit the environment without relying on black-box regime claims. | [guide](docs/examples/market-regime-analysis-walkthrough.md) |

<!-- SKILL_INDEX_END -->

## What v1 does not include

- broker-required skills
- order execution
- portfolio syncing
- trade placement
- account management
- provider-specific public skill packages

## Repository layout

```text
trading-skills/
  README.md
  CONTRIBUTING.md
  LICENSE
  Makefile
  docs/
  scripts/
  skills/
```

Each public skill lives in `skills/<capability>/` and centers around a `SKILL.md` file. Long notes, methodology, assets, and provider references stay in adjacent folders so the skill body stays readable.

## Architecture in one page

- Public packages are capability-first.
- Public skills are analytical capabilities.
- User-provided context comes first.
- Optional provider support is markdown-based and used only when needed.

The repo now contains two useful layers:

- atomic skills: narrow, reusable capabilities such as `thesis-validation` or `position-sizing`
- workflow skills: wrappers such as `pre-trade-check` that run the minimum necessary chain of atomic skills

## Agent Integration Patterns

For agent systems, the cleanest pattern is:

1. gather user context first
2. run the smallest number of skills needed
3. carry forward a compact markdown trade context instead of raw transcript state
4. disclose any provider-based data that was used
5. keep execution and broker actions outside this repo

Recommended composition:

- use `pre-trade-check` when the user wants one readiness verdict instead of manually running each check
- use `earnings-trade-prep` when the main question is how to prepare for or trade around an upcoming report
- use `watchlist-review` when the user starts with too many names and needs triage first
- use `catalyst-map` when the user needs one event map across names, sectors, or themes
- use `evidence-gap-check` when the idea is interesting but the missing information is not yet prioritized
- use `macro-event-analysis` or `earnings-preview` to frame event risk
- use `market-regime-analysis` to classify the broader environment
- use `thesis-validation` to pressure-test the claim before turning it into structure
- use `risk-reward-sanity-check` to pressure-test structure
- use `execution-plan-check` to verify the order logic works in the real market
- use `portfolio-concentration` before final sizing if portfolio fit could block the trade
- use `position-sizing` only after the stop is stable
- use `position-management` while the trade is open
- use `journal-pattern-analyzer` to review a batch of trades for repeatable patterns
- use `post-trade-review` after the trade closes

See [docs/composing-skills.md](docs/composing-skills.md) for the shared Trade Context schema and realistic chaining examples.

See the docs for details:

- [Architecture](docs/architecture.md)
- [Examples](docs/examples/README.md)
- [Compatibility and install](docs/compatibility-and-install.md)
- [Composing skills](docs/composing-skills.md)
- [Optional provider support](docs/optional-provider-support.md)
- [Repo conventions](docs/repo-conventions.md)
- [Skill design principles](docs/skill-design-principles.md)
- [Skill template](docs/skill-template.md)
- [New skill checklist](docs/new-skill-checklist.md)
- [Versioning and releases](docs/versioning-and-releases.md)
- [Release checklist](docs/release-checklist.md)
- [Provider support](docs/provider-support.md)

## Validation

Run the repository checks with one command:

```bash
make validate
```

Regenerate the machine-readable catalog and README skill index after metadata changes:

```bash
make catalog
```

The current checks cover:

- every skill directory contains `SKILL.md`
- frontmatter fields exist and match the directory name
- descriptions are specific enough to be useful
- catalog metadata matches the skill folders
- README skill index stays in sync with the catalog
- local references in `SKILL.md` files exist
- README and docs markdown links stay valid
- forbidden artifacts do not leak into tracked files
- public skill names do not leak provider branding
- provider references linked from skills exist
- skill-local markdown stays aligned with the user-data-first workflow
- skill directories stay lean by excluding `fixtures/` and `sample-output.md`

## Next steps after v1

- Add better cross-asset examples for equities, futures, and FX risk workflows
- Expand provider coverage for `macro-event-analysis` and `earnings-preview`
- Add more `data-optional` skills such as workflow wrappers
- Add packaging and release metadata for one-step installation across more skill marketplaces
- Keep the skill folders lean while expanding the capability set
