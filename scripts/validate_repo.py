#!/usr/bin/env python3
"""Lightweight repository validator for trading-skills."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from build_catalog import collect_catalog, parse_frontmatter, update_readme, render_skill_index

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
README_PATH = REPO_ROOT / "README.md"
CATALOG_PATH = REPO_ROOT / "catalog.json"
VERSION_PATH = REPO_ROOT / "VERSION"
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.md"

GENERIC_DESCRIPTION_FRAGMENTS = {"skill description", "todo", "placeholder", "tbd", "generic"}
FRONTMATTER_REQUIRED = {"name", "description"}
FRONTMATTER_ALLOWED = {"name", "description"}
DATA_AWARE_SKILLS = {"macro-event-analysis", "earnings-preview", "market-regime-analysis"}

FORBIDDEN_TRACKED_PATTERNS = (
    "__pycache__/",
    ".pytest_cache/",
    ".venv/",
    ".env",
    ".env.",
    ".DS_Store",
)
FORBIDDEN_TRACKED_SUFFIXES = (
    ".pyc",
    ".pyo",
    ".swp",
    ".swo",
    ".tmp",
    ".bak",
)


def validate_frontmatter(path: Path, errors: list[str]) -> None:
    try:
        frontmatter = parse_frontmatter(path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    missing = sorted(FRONTMATTER_REQUIRED - set(frontmatter))
    if missing:
        errors.append(f"{path}: missing frontmatter fields: {', '.join(missing)}")
        return

    unexpected = sorted(set(frontmatter) - FRONTMATTER_ALLOWED)
    if unexpected:
        errors.append(
            f"{path}: unexpected frontmatter fields for this repo style: {', '.join(unexpected)}"
        )

    skill_dir_name = path.parent.name
    if frontmatter["name"] != skill_dir_name:
        errors.append(
            f"{path}: frontmatter name '{frontmatter['name']}' does not match directory '{skill_dir_name}'"
        )

    description = frontmatter["description"].strip()
    if len(description) < 40:
        errors.append(f"{path}: description is too short to be useful")
    lowered = description.lower()
    if any(fragment in lowered for fragment in GENERIC_DESCRIPTION_FRAGMENTS):
        errors.append(f"{path}: description looks generic or placeholder-like")


def validate_skill_structure(errors: list[str]) -> None:
    if not SKILLS_DIR.exists():
        errors.append(f"{SKILLS_DIR}: skills directory is missing")
        return

    for skill_dir in sorted(
        path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith("_")
    ):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        sample_output = skill_dir / "sample-output.md"
        if not sample_output.exists():
            errors.append(f"{skill_dir}: missing sample-output.md")
        validate_frontmatter(skill_md, errors)
        validate_provider_references(skill_dir, errors)
        validate_skill_python_absence(skill_dir, errors)
        validate_public_skill_naming(skill_dir, errors)


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if not target or "://" in target or target.startswith("#"):
            continue
        target_path = (path.parent / target).resolve()
        try:
            target_path.relative_to(REPO_ROOT)
        except ValueError:
            errors.append(f"{path}: link escapes repository root: {target}")
            continue
        if not target_path.exists():
            errors.append(f"{path}: referenced file does not exist: {target}")


def validate_repo_markdown_links(errors: list[str]) -> None:
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if any(part.startswith(".") and part not in {".github"} for part in path.parts):
            continue
        validate_markdown_links(path, errors)


def validate_provider_references(skill_dir: Path, errors: list[str]) -> None:
    if skill_dir.name not in DATA_AWARE_SKILLS:
        return

    data_providers = skill_dir / "references" / "data-providers.md"
    providers_dir = skill_dir / "references" / "providers"
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    if not data_providers.exists():
        errors.append(f"{skill_dir}: data-aware skill is missing references/data-providers.md")
        return
    if "references/data-providers.md" not in skill_text:
        errors.append(f"{skill_dir}: SKILL.md should mention references/data-providers.md directly")
    if "ask which supported provider" not in skill_text.lower():
        errors.append(f"{skill_dir}: SKILL.md should explain how to ask the user to choose a provider")
    if not providers_dir.exists():
        errors.append(f"{skill_dir}: data-aware skill is missing references/providers/")
        return
    provider_docs = [path for path in providers_dir.glob("*.md")]
    if not provider_docs:
        errors.append(f"{skill_dir}: data-aware skill should declare at least one provider reference")


def validate_skill_python_absence(skill_dir: Path, errors: list[str]) -> None:
    python_files = sorted(path.relative_to(REPO_ROOT).as_posix() for path in skill_dir.rglob("*.py"))
    if python_files:
        errors.append(
            f"{skill_dir}: skill-local Python files should be removed for markdown-first support: "
            f"{', '.join(python_files)}"
        )


def validate_shared_library(errors: list[str]) -> None:
    calculations = SKILLS_DIR / "_lib" / "calculations.py"
    if not calculations.exists():
        errors.append(f"{calculations}: missing shared calculations library")

    extra_python = sorted(
        path.relative_to(REPO_ROOT).as_posix()
        for path in SKILLS_DIR.rglob("*.py")
        if path != calculations
    )
    if extra_python:
        errors.append(
            "Unexpected Python files under skills/; keep code limited to skills/_lib/calculations.py: "
            + ", ".join(extra_python)
        )


def validate_public_skill_naming(skill_dir: Path, errors: list[str]) -> None:
    leaked_provider_terms = {"fmp", "fred", "alpaca", "polygon", "ibkr", "interactive-brokers"}
    name_tokens = set(skill_dir.name.split("-"))
    leaked = sorted(name_tokens & leaked_provider_terms)
    if leaked:
        errors.append(
            f"{skill_dir}: public skill name leaks provider branding ({', '.join(leaked)})"
        )


def validate_catalog_and_readme(errors: list[str]) -> None:
    catalog = collect_catalog(REPO_ROOT)
    expected_catalog = json.dumps(catalog, indent=2) + "\n"
    if not CATALOG_PATH.exists():
        errors.append(f"{CATALOG_PATH}: missing generated catalog")
    elif CATALOG_PATH.read_text(encoding="utf-8") != expected_catalog:
        errors.append("catalog.json is out of date; run `make catalog`")

    if not README_PATH.exists():
        errors.append(f"{README_PATH}: missing README")
        return

    actual_readme = README_PATH.read_text(encoding="utf-8")
    try:
        expected_readme = update_readme(actual_readme, render_skill_index(catalog))
    except ValueError as exc:
        errors.append(str(exc))
        return
    if expected_readme != actual_readme:
        errors.append("README skill index is out of date; run `make catalog`")


def validate_fixture_json(errors: list[str]) -> None:
    for fixture in sorted(REPO_ROOT.glob("skills/*/fixtures/*.json")):
        try:
            json.loads(fixture.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{fixture}: invalid JSON fixture: {exc}")


def validate_release_artifacts(errors: list[str]) -> None:
    if not VERSION_PATH.exists():
        errors.append(f"{VERSION_PATH}: missing release version anchor")
    elif not VERSION_PATH.read_text(encoding="utf-8").strip():
        errors.append(f"{VERSION_PATH}: version file is empty")

    if not CHANGELOG_PATH.exists():
        errors.append(f"{CHANGELOG_PATH}: missing changelog")


def validate_forbidden_tracked_artifacts(errors: list[str]) -> None:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        errors.append(f"Unable to inspect tracked files via git: {exc}")
        return

    for relative_path in result.stdout.splitlines():
        if any(pattern in relative_path for pattern in FORBIDDEN_TRACKED_PATTERNS):
            errors.append(f"Tracked forbidden artifact: {relative_path}")
        if relative_path.endswith(FORBIDDEN_TRACKED_SUFFIXES):
            errors.append(f"Tracked forbidden artifact: {relative_path}")


def main() -> int:
    errors: list[str] = []
    validate_skill_structure(errors)
    validate_repo_markdown_links(errors)
    validate_catalog_and_readme(errors)
    validate_fixture_json(errors)
    validate_release_artifacts(errors)
    validate_forbidden_tracked_artifacts(errors)
    validate_shared_library(errors)

    if errors:
        print("Repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
