# Compatibility And Install

## What this repo is for

`trading-skills` is designed for agent tools that support portable `SKILL.md`-style skill folders.

A portable skill in this repo means:

- a public `SKILL.md` entrypoint
- minimal frontmatter, usually just `name` and `description`
- supporting references, scripts, fixtures, and assets kept inside the skill directory
- no requirement that users understand provider internals to use the capability

## Expected skill folder shape

Typical skill shape:

```text
skills/<skill-name>/
  SKILL.md
  fixtures/
  references/
  scripts/
  providers/
  assets/
```

Not every skill needs every subdirectory, but `SKILL.md` is required.

## Installing a single skill

Typical install shape for ecosystems that support repo-scoped skill install:

```bash
npx skills add marian2js/trading-skills@position-sizing
npx skills add marian2js/trading-skills@economic-calendar
```

Users should think in terms of capabilities, not providers.

## Repo-specific vs ecosystem-generic

Ecosystem-generic expectations:

- `SKILL.md` as the public skill entrypoint
- lightweight frontmatter metadata
- portable relative references inside the skill folder

Repo-specific conventions:

- capability-first packaging
- internal `providers/` directories for data-backed skills
- a small generated `catalog.json` for browsing and validation
- generated README skill index

## Compatibility guidance for contributors

- avoid hard-coding provider names into public skill names
- keep relative paths inside the skill directory
- prefer standard-library Python helpers where possible
- assume non-technical users may browse the skill before they inspect any code
