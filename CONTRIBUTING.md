# Contributing

This repository is for portable trading and investing skills that improve judgment, risk clarity, planning, and review discipline.

Before adding or reshaping a skill, read [docs/repo-conventions.md](docs/repo-conventions.md) and [docs/new-skill-checklist.md](docs/new-skill-checklist.md).

## Contribution standards

Contributions should be:

- capability-first, not provider-first
- conservative in tone and claims
- understandable for non-technical users
- explicit about assumptions, freshness, and limitations
- portable across tools that support `SKILL.md`-style skills

Do not contribute:

- hype-driven "signal" skills with unverifiable claims
- broker execution workflows in v1
- public provider-specific skills unless there is a strong user-facing reason
- giant abstractions that add complexity before the capability is useful

## Skill checklist

Every new public skill should include:

- `skills/<skill-name>/SKILL.md`
- clear frontmatter with a name that matches the directory
- a specific description that explains what the skill does and when to use it
- realistic usage examples
- supporting references in `references/` when the method needs extra detail

If the skill is data-backed, it should also include:

- a canonical schema or a documented dependency on an existing canonical schema
- a provider selection strategy
- at least one concrete adapter
- an example or mock adapter for demos and tests
- realistic fixtures under `skills/<skill>/fixtures/`
- clear behavior when credentials or live data are unavailable

## Writing guidelines

- Write for trust, not drama.
- Prefer plain language over financial theater.
- Do not imply certainty where only context exists.
- Avoid fake precision. Rounded ranges and caveats are often better than false exactness.
- Separate analysis from recommendation. The skill can support a decision without pretending to make it.

## Adding a provider to an existing skill

Do not create a new public skill for a provider unless the provider-specific capability is itself the product.

Instead:

1. Add a new adapter under the existing capability, for example `skills/economic-calendar/providers/<provider>/`.
2. Normalize the provider output into the documented canonical schema.
3. Update the skill instructions or references only if the user-facing workflow changes.
4. Keep source disclosure in the final output.

Read [docs/provider-adapters.md](docs/provider-adapters.md) before adding adapter code.

## Validation

Most tests live in the root `tests/` directory because the highest-value checks in this repo are cross-cutting:

- skill structure
- frontmatter quality
- link integrity
- schema examples
- adapter contracts
- normalization behavior

Keep fixtures near the skill they belong to. Add `skills/<skill>/tests/` only when a skill has substantial local Python logic and co-location clearly improves maintainability.

## Developer workflow

The repo has one metadata source of truth per skill: the `SKILL.md` frontmatter inside `skills/<skill>/`.

Typical contributor flow:

1. Add or update a skill under `skills/<skill>/`.
2. Keep sample inputs, normalized payloads, and demo outputs in `fixtures/`.
3. Add or update tests in the root `tests/` directory unless co-located skill tests are clearly justified.
4. Regenerate the machine-readable catalog and README skill index with `make catalog`.
5. Run `make test` before opening a PR.

Run the full checks before opening a PR:

```bash
make catalog
make test
```

If you only want the fast structural checks, use:

```bash
make validate
```

`make test` creates a local `.venv` automatically if needed. The validator uses only the Python standard library, and the test suite uses pytest with a deliberately small amount of shared helper code.

## Suggested PR scope

Keep pull requests narrow:

- one new skill
- one adapter addition
- one documentation improvement
- one validator improvement

This keeps review focused and preserves the clarity of the repository.
