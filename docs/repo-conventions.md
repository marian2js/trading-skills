# Repo Conventions

## Keep skills lightweight

Most skills in this repo should keep frontmatter minimal:

- `name`
- `description`

Add more metadata only when it has a clear current job in the repo. Do not add fields for speculative taxonomy work.

## Naming conventions

- Use concise, capability-first skill names.
- Prefer names that describe the user job directly, such as `macro-event-analysis` or `position-sizing`.
- Do not expose provider names in public skill names unless the provider-specific behavior is itself the product.

## Capability-first packaging

The public package is the skill capability.

Public skills should describe an analytical job, not a data utility. If the main thing a skill does is fetch or normalize data, that logic probably belongs in small provider references instead of the public `SKILL.md`.

Good:

- `skills/macro-event-analysis/`
- `skills/earnings-preview/`

Bad by default:

- `skills/fmp-macro-events/`
- `skills/provider-x-earnings-preview/`

## Skill directory structure

Use the smallest structure that supports the capability cleanly.

- `SKILL.md`: required public entrypoint
- `references/`: methodology, caveats, domain notes, schema explanations
- `assets/`: reusable templates or non-executable supporting material

Not every skill needs every directory.

For data-aware skills, prefer:

- `references/data-providers.md`
- `references/providers/<provider>.md`
## When provider-specific public skills are allowed

Almost never. They are acceptable only when:

- the provider-specific behavior is meaningfully different to users
- the capability cannot be represented well as one normalized public skill
- the added complexity is justified by clear user demand

If those conditions are not met, keep the provider behind the existing capability skill.

## Output quality standard

Good trading skill output should be:

- conservative
- auditable
- explicit about assumptions
- explicit about data freshness and provider source when relevant
- clear about caveats and incomplete coverage
- separate from execution or recommendation claims

The repo should never reward:

- hype language
- guaranteed outcomes
- black-box confidence theater
- fake precision that is not defensible

## Metadata and generated files

- `catalog.json` stays intentionally small and exists to support browsing, validation, and README generation.
- The generated README skill index should stay simple and user-facing.
- If a field does not improve current install UX, browsing, or validation, do not add it.
