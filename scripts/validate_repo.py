#!/usr/bin/env python3
"""Lightweight repository validator for trading-skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
SCHEMA_DOC = REPO_ROOT / "docs" / "canonical-schemas.md"

GENERIC_DESCRIPTION_FRAGMENTS = {
    "skill description",
    "todo",
    "placeholder",
    "tbd",
    "generic",
}

FRONTMATTER_REQUIRED = {
    "name",
    "version",
    "description",
    "dependency_class",
}

VALID_DEPENDENCY_CLASSES = {
    "static",
    "data-optional",
    "data-required",
    "broker-required",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing opening frontmatter delimiter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter block")

    block = parts[1]
    data: dict[str, str] = {}
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"{path}: invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


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

    dependency_class = frontmatter["dependency_class"]
    if dependency_class not in VALID_DEPENDENCY_CLASSES:
        errors.append(f"{path}: invalid dependency_class '{dependency_class}'")


def validate_skill_structure(errors: list[str]) -> None:
    if not SKILLS_DIR.exists():
        errors.append(f"{SKILLS_DIR}: skills directory is missing")
        return

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        validate_frontmatter(skill_md, errors)
        validate_markdown_links(skill_md, errors)


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


def validate_schema_examples(errors: list[str]) -> None:
    if not SCHEMA_DOC.exists():
        errors.append(f"{SCHEMA_DOC}: missing schema documentation")
        return

    text = SCHEMA_DOC.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not blocks:
        errors.append(f"{SCHEMA_DOC}: no JSON examples found")
        return

    for index, block in enumerate(blocks, start=1):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            errors.append(f"{SCHEMA_DOC}: JSON example #{index} is invalid: {exc}")


def main() -> int:
    errors: list[str] = []
    validate_skill_structure(errors)
    validate_schema_examples(errors)

    if errors:
        print("Repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
