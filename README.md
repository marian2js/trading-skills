# Trading Skills

[![CI](https://github.com/marian2js/trading-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/marian2js/trading-skills/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

AI skills for better trading and investing decisions.

`trading-skills` is a portable, capability-first collection of `SKILL.md` packages for agent tools. It helps traders and investors think more clearly, prepare better, size cleaner, manage risk more explicitly, and review decisions without hindsight theater.

The point is not to generate magic signals. The point is to give AI structure: better trade prep, better risk process, better execution planning, and better post-trade learning.

The core library is analysis-first. Optional live-trade integrations can sit alongside it as separate, provider-specific skills without changing the default analytical workflows.

If this repo helps your workflow, star it.

## Start Here

If you are not sure where to begin:

- New trade idea and want one go / no-go workflow: `pre-trade-check`
- Preparing around an upcoming report: `earnings-trade-prep`
- Too many names and need triage: `watchlist-review`
- Need to pressure-test the actual claim: `thesis-validation`
- Need to check if the plan is even tradable: `execution-plan-check`
- Need to size the trade conservatively: `position-sizing`
- Need to review portfolio overlap before adding: `portfolio-risk-review`
- Managing an open position: `position-management`
- Reviewing a closed trade: `post-trade-debrief`

## Why Trading Skills

Generic AI gives you words. Trading and investing require process.

This repo is built to improve the parts of decision-making that actually matter:

- Better prep: identify what matters before the trade, not after it.
- Better risk control: make invalidation, structure, concentration, and sizing explicit.
- Better execution discipline: separate a good idea from an executable plan.
- Better review quality: turn journals and post-mortems into repeatable improvements.
- Better trust: disclose assumptions, source quality, and missing information instead of pretending certainty.

This is especially useful if you already use AI but want less confident prose and more rigorous thinking.

## How It Works

The repo contains three useful layers:

- Groups: browsing categories such as market context, idea discovery, and review
- Atomic skills: reusable capabilities such as `thesis-validation`, `risk-reward-sanity-check`, or `position-sizing`
- Workflow skills: wrappers such as `pre-trade-check` and `post-trade-debrief` that chain the minimum necessary atomic skills

The default usage pattern is simple:

1. Start from the user’s actual context.
2. Run the smallest skill or workflow that fits the job.
3. Carry forward a compact trade context, not a pile of chat history.
4. Use external data only when the user’s material is not enough.
5. Keep trust high by disclosing what is known, assumed, and missing.

## Install

The intended UX is capability-first:

```bash
npx skills add marian2js/trading-skills@pre-trade-check
npx skills add marian2js/trading-skills@position-sizing
npx skills add marian2js/trading-skills@earnings-preview
```

You can also install narrower capabilities directly when you already know the job you want to improve.

## Example Prompts

- "Use `pre-trade-check` on this swing idea and tell me if it is actually ready."
- "Use `earnings-trade-prep` on NVDA for next week and tell me whether this is prep-only, pre-event tradeable, or a hold-through candidate."
- "Use `portfolio-risk-review` on my current book before I add more semis."
- "Use `watchlist-review` on these semis for next week and tell me which names actually deserve active attention."
- "Use `thesis-validation` on my semis swing thesis and tell me what evidence is real, what is assumption, and what would invalidate it."
- "Use `execution-plan-check` on my plan to buy a niche ETF at the open and tell me whether the order logic is actually executable."
- "Use `position-sizing` for a $125,000 account risking 0.5% with entry 412.30 and stop 406.80."
- "Use `risk-reward-sanity-check` on a swing long with entry 58.20, stop 55.90, and target 65.50."
- "Use `macro-event-analysis` to summarize macro event risk for the next 48 hours."
- "Use `position-management` on this open long and tell me whether to hold, trim, tighten risk, or exit."
- "Use `post-trade-debrief` on this closed trade and tell me the real lesson."

See [docs/examples/](docs/examples/) for longer walkthroughs.

## Trust Model

High-trust output is a product requirement. Skills should make it obvious:

- what came from the user
- what came from a provider
- how fresh the information is
- what assumptions were made
- what important information is still missing

The repo avoids hype, fake precision, and guaranteed-outcome language.

## Quick Links

- [Examples](docs/examples/README.md)
- [Composing skills](docs/composing-skills.md)
- [Optional provider support](docs/optional-provider-support.md)
- [Compatibility and install](docs/compatibility-and-install.md)
- [Architecture](docs/architecture.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## Available Skills

The current library stays intentionally small and capability-first:

<!-- SKILL_INDEX_START -->
| Skill | Summary | Guide |
| --- | --- | --- |
| `macro-event-analysis` | Prepare for upcoming macro catalysts by identifying the events that matter, mapping the likely transmission channels, and surfacing timing risk for the user's markets or positions. | [guide](docs/examples/macro-event-analysis-example-mode.md) |
| `earnings-preview` | Prepare for an upcoming earnings report or earnings week by identifying the reports that matter, framing the key debates, and surfacing the read-through risk that could affect the user's watchlist or positions. | [guide](docs/examples/earnings-preview-live-mode.md) |
| `market-regime-analysis` | Analyze current market context through trend, volatility, breadth, and event backdrop so the user can choose tactics that fit the environment without relying on black-box regime claims. | [guide](docs/examples/market-regime-analysis-walkthrough.md) |
| `watchlist-review` | Review a watchlist and rank which names deserve active attention, background monitoring, or removal based on catalysts, tradability, redundancy, and evidence quality for the user's style and timeframe. | [guide](docs/examples/watchlist-review-walkthrough.md) |
| `catalyst-map` | Build a ranked map of the catalysts that could move a watchlist, theme, or portfolio by showing what matters, when it matters, and how those events could transmit across related names or exposures. | [guide](docs/examples/catalyst-map-walkthrough.md) |
| `thesis-validation` | Pressure-test a trade or investment thesis by clarifying the core claim, evidence, invalidation, timeframe, and dependency chain before the user turns it into an entry, stop, or size. | [guide](docs/examples/thesis-validation-walkthrough.md) |
| `evidence-gap-check` | Identify the most important missing facts, assumptions, and unresolved questions that should be answered before a trade or investment idea is trusted, sized, or acted on. | [guide](docs/examples/evidence-gap-check-walkthrough.md) |
| `risk-reward-sanity-check` | Use when the user wants to test whether a proposed entry, stop, and target structure is coherent, asymmetric enough, and vulnerable to obvious failure modes before the trade is placed. | [guide](docs/examples/risk-reward-sanity-check-walkthrough.md) |
| `portfolio-concentration` | Evaluate whether a portfolio, account, or planned position is too dependent on a small number of issuers, sectors, themes, or correlated exposures before the user adds or holds more risk. | [guide](docs/examples/portfolio-concentration-walkthrough.md) |
| `position-sizing` | Use when the user needs a conservative position size from account equity, risk budget, entry, stop, and trading friction before entering a trade. | [guide](docs/examples/position-sizing-walkthrough.md) |
| `execution-plan-check` | Review whether a trade plan is operationally executable by checking order type logic, liquidity and spread risk, event timing, stop realism, and whether the user can actually implement the plan cleanly. | [guide](docs/examples/execution-plan-check-walkthrough.md) |
| `position-management` | Review an open position and decide whether to hold, trim, tighten risk, close, or wait by comparing current behavior against the original thesis, invalidation logic, catalyst calendar, and execution constraints. | [guide](docs/examples/position-management-walkthrough.md) |
| `post-trade-review` | Guide a disciplined post-trade review across thesis quality, setup quality, execution, adherence, mistakes, and lessons without turning the result into hindsight theater. | [guide](docs/examples/post-trade-review-walkthrough.md) |
| `journal-pattern-analyzer` | Use when the user has a trade journal or trade log and wants repeated strengths, mistakes, environment-dependent patterns, and process changes without turning the review into hindsight theater. | [guide](docs/examples/journal-pattern-analyzer-walkthrough.md) |
| `pre-trade-check` | Orchestrate a disciplined pre-trade workflow by routing a watchlist or trade idea through the minimum set of underlying skills needed to decide whether the trade is ready, not ready, or should be resized or reworked first. | [guide](docs/examples/pre-trade-check-walkthrough.md) |
| `earnings-trade-prep` | Orchestrate a disciplined earnings-event workflow by deciding which names deserve prep, mapping the key debates and read-through paths, pressure-testing the thesis and structure, and ending with a clear pre-earnings hold, avoid, or trade decision. | [guide](docs/examples/earnings-trade-prep-walkthrough.md) |
| `portfolio-risk-review` | Orchestrate a whole-book risk review by checking concentration, correlated exposure, catalyst clustering, market-context sensitivity, and live-position fragility before the user adds, holds, or reduces portfolio risk. | [guide](docs/examples/portfolio-risk-review-walkthrough.md) |
| `post-trade-debrief` | Orchestrate a disciplined post-trade workflow by reconstructing the original plan, reviewing execution and rule adherence, and deciding whether the lesson is trade-specific or part of a larger repeatable pattern. | [guide](docs/examples/post-trade-debrief-walkthrough.md) |
| `etoro` | Use when the user wants an agent to interact with the eToro API for market data, portfolio and social features, or trade execution. | - |

<!-- SKILL_INDEX_END -->

## Integration Pattern

For agent systems, the cleanest pattern is:

1. gather user context first
2. run the smallest number of skills needed
3. carry forward a compact markdown trade context instead of raw transcript state
4. disclose any provider-based data that was used
5. keep execution and broker actions outside this repo

Recommended composition:

- use `pre-trade-check` when the user wants one readiness verdict instead of manually running each check
- use `earnings-trade-prep` when the main question is how to prepare for or trade around an upcoming report
- use `portfolio-risk-review` when the user needs a whole-book risk view before adding or maintaining exposure
- use `post-trade-debrief` when the user wants one post-trade learning workflow instead of manual review routing
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

## Docs

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

Run `skill-doctor` locally with:

```bash
make doctor
```

The CI workflow also runs the published [`marian2js/skill-doctor`](https://github.com/marian2js/skill-doctor) GitHub Action on the full repository and fails only on analyzer errors.
