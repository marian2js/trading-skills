# trading-skills

`trading-skills` is a portable, capability-first collection of trading and investing skills for agent tools that support `SKILL.md`-style packages.

The goal is not to generate magic signals. The goal is to improve decision quality, risk management, execution planning, and review discipline with transparent, auditable workflows.

Broker integrations are explicitly out of scope for v1. This repo does not ship order execution, portfolio syncing, account management, or brokerage adapters.

## Why this repo exists

Most users think in terms of jobs to be done:

- `earnings-calendar`
- `economic-calendar`
- `position-sizing`
- `market-regime-detector`

They do not want to think in terms of vendor internals such as `fmp-earnings-calendar` or `fred-economic-calendar`.

This repository keeps the public UX capability-first:

- A skill is a user-facing capability.
- A provider is an internal implementation detail in most cases.
- Data-backed skills disclose the source, freshness, and limitations of their output.

The repository also ships a machine-readable [catalog.json](catalog.json) so future install tooling, docs generation, and validation can rely on one metadata source.

`trading-skills` is preferred over `trading-agent-skills` because it is cleaner, easier to remember, and centered on the user job rather than the implementation medium.

## Installation model

The intended UX is simple and capability-first:

```bash
npx skills add marian2js/trading-skills@position-sizing
npx skills add marian2js/trading-skills@economic-calendar
npx skills add marian2js/trading-skills@earnings-calendar
```

## Getting started

Use static skills immediately:

- `position-sizing`
- `risk-reward-sanity-check`
- `post-trade-review`

Use data-backed skills in example mode with no credentials:

- `economic-calendar`
- `earnings-calendar`

Use live data-backed skills after configuring `FMP_API_KEY`:

- `economic-calendar`
- `earnings-calendar`

See [docs/live-data-setup.md](docs/live-data-setup.md) for live/example behavior, fallback rules, and verification steps.

Example walkthroughs for evaluating the current skills live in [docs/examples/](docs/examples/).

Example prompts after installation:

- "Use `position-sizing` for a $125,000 account risking 0.5% with entry 412.30 and stop 406.80."
- "Use `risk-reward-sanity-check` on a swing long with entry 58.20, stop 55.90, and target 65.50."
- "Use `economic-calendar` to summarize macro event risk for the next 48 hours."
- "Use `earnings-calendar` to rank upcoming earnings that matter for NVDA, AMD, and the semiconductor group."
- "Use `market-regime-detector` to classify current context from my observations without pretending to forecast."
- "Use `post-trade-review` to review a trade where I respected the thesis but violated my stop."

## Static vs data-backed skills

This repository uses four dependency classes:

- `static`: no external data or credentials required
- `data-optional`: works without live data, but can improve with inputs or adapters
- `data-required`: needs an external data provider to operate fully
- `broker-required`: needs broker integration; not part of v1

Static skills are installable and immediately useful for non-technical users.

Data-backed skills keep setup small:

- users install the capability, not a provider-specific package
- the skill selects an internal adapter
- if no live provider is configured, the skill explains that clearly and can fall back to an example adapter when available

## Trust model

High-trust output is a product requirement, not a nice-to-have. Data-backed skills should always disclose:

- source or provider used
- freshness or timestamp when available
- coverage gaps and missing fields
- caveats about assumptions, ranking logic, or incomplete visibility

The repo avoids hype, fake precision, and guaranteed-outcome language.

## Initial skills

The current library is grouped into a small number of clear categories:

<!-- SKILL_INDEX_START -->
### risk-management

| Skill | Dependency | Status | Config | Summary |
| --- | --- | --- | --- | --- |
| `position-sizing` | `static` | `beta` | `no` | Compute a conservative position size from account equity, risk budget, entry, stop, and trading friction so the user can inspect exposure before entering a trade. |
| `risk-reward-sanity-check` | `static` | `beta` | `no` | Analyze whether a proposed entry, stop, and target structure is coherent, asymmetric enough, and vulnerable to obvious failure modes before the trade is placed. |

### trade-review

| Skill | Dependency | Status | Config | Summary |
| --- | --- | --- | --- | --- |
| `post-trade-review` | `static` | `beta` | `no` | Guide a disciplined post-trade review across thesis quality, setup quality, execution, adherence, mistakes, and lessons without turning the result into hindsight theater. |

### macro

| Skill | Dependency | Status | Config | Summary |
| --- | --- | --- | --- | --- |
| `economic-calendar` | `data-required` | `experimental` | `yes` | Summarize upcoming macro event risk from a normalized economic calendar so the user can see timing, importance, and coverage caveats without dealing with provider internals. |

### market-data

| Skill | Dependency | Status | Config | Summary |
| --- | --- | --- | --- | --- |
| `earnings-calendar` | `data-required` | `experimental` | `yes` | Summarize upcoming earnings events with normalized fields and conservative relevance ranking so the user can prepare around catalysts without learning provider internals. |
| `market-regime-detector` | `data-optional` | `beta` | `no` | Classify market context conservatively from trend, volatility, breadth, and event backdrop so the user can adapt tactics without relying on black-box regime claims. |

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
  tests/
```

Each public skill lives in `skills/<capability>/` and centers around a `SKILL.md` file. Long notes, methodology, fixtures, and scripts stay in adjacent folders so the skill body stays readable.

## Architecture in one page

- Public packages are capability-first.
- Provider adapters are internal.
- Data-backed skills normalize provider responses into canonical schemas before analysis.
- Skill logic should reason over the normalized schema, not the raw vendor payload.
- v1 uses one primary provider per data-backed capability where appropriate, but the structure supports more later.

See the docs for details:

- [Architecture](docs/architecture.md)
- [Compatibility and install](docs/compatibility-and-install.md)
- [Live data setup](docs/live-data-setup.md)
- [Repo conventions](docs/repo-conventions.md)
- [Skill design principles](docs/skill-design-principles.md)
- [New skill checklist](docs/new-skill-checklist.md)
- [Versioning and releases](docs/versioning-and-releases.md)
- [Release checklist](docs/release-checklist.md)
- [Provider adapters](docs/provider-adapters.md)
- [Canonical schemas](docs/canonical-schemas.md)

## Testing and validation

This repo keeps most tests in the root [tests/](tests/) directory so contributors can find cross-cutting checks in one place. Skill-specific sample data lives next to the skill in `skills/<skill>/fixtures/`, which keeps demo data and normalization fixtures close to the capability they describe.

Per-skill `tests/` directories are intentionally not the default. Add them only when a skill grows substantial local executable logic that is easier to maintain beside the code.

Run the full repository checks with one command:

```bash
make test
```

This runs the lightweight validator, bootstraps a local `.venv` if needed, and executes the pytest suite. The validator remains available separately if you want a fast structural pass:

```bash
make validate
```

Regenerate the machine-readable catalog and README skill index after metadata changes:

```bash
make catalog
```

Mirror the GitHub Actions checks locally:

```bash
make ci
```

The current checks cover:

- every skill directory contains `SKILL.md`
- frontmatter fields exist and match the directory name
- descriptions are specific enough to be useful
- catalog metadata matches the skill folders
- README skill index stays in sync with the catalog
- local references in `SKILL.md` files exist
- JSON examples in the schema docs parse successfully
- fixture JSON files parse successfully
- forbidden artifacts do not leak into tracked files
- public skill names do not leak provider branding
- provider adapters conform to the internal contract
- normalization fixtures match the canonical schemas
- representative scripts work in smoke-test mode

## Next steps after v1

- Add better cross-asset examples for equities, futures, and FX risk workflows
- Expand provider coverage for `economic-calendar` and `earnings-calendar`
- Add more `data-optional` skills such as watchlist review and catalyst maps
- Add packaging and release metadata for one-step installation across more skill marketplaces
- Add test fixtures and golden outputs for skill examples
