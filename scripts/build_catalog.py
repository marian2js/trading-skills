#!/usr/bin/env python3
"""Build the repository skill catalog and generated README index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
CATALOG_PATH = REPO_ROOT / "catalog.json"
README_PATH = REPO_ROOT / "README.md"
README_START = "<!-- SKILL_INDEX_START -->"
README_END = "<!-- SKILL_INDEX_END -->"

CATEGORY_ORDER = [
    "risk-management",
    "trade-review",
    "macro",
    "market-data",
    "research",
    "workflow",
]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing opening frontmatter delimiter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter")

    data: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"{path}: invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_bool(value: str | None) -> bool:
    return str(value or "").strip().lower() == "true"


def find_supported_providers(skill_dir: Path) -> list[str]:
    providers_dir = skill_dir / "providers"
    if not providers_dir.exists():
        return []
    return sorted(
        path.name
        for path in providers_dir.iterdir()
        if path.is_dir() and not path.name.startswith("__")
    )


def collect_catalog(repo_root: Path = REPO_ROOT) -> dict:
    skills_dir = repo_root / "skills"
    records = []

    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
        providers_supported = find_supported_providers(skill_dir)
        record = {
            "name": frontmatter["name"],
            "path": f"skills/{skill_dir.name}",
            "description": frontmatter["description"],
            "dependency_class": frontmatter["dependency_class"],
            "category": frontmatter["category"],
            "providers_supported": providers_supported,
            "requires_configuration": parse_bool(frontmatter.get("requires_configuration")),
            "status": frontmatter["status"],
            "asset_coverage": parse_csv(frontmatter.get("asset_coverage")),
            "example_artifact": (
                f"skills/{skill_dir.name}/sample-output.md"
                if (skill_dir / "sample-output.md").exists()
                else None
            ),
            "tags": parse_csv(frontmatter.get("tags")),
        }
        records.append(record)

    records.sort(
        key=lambda record: (
            CATEGORY_ORDER.index(record["category"])
            if record["category"] in CATEGORY_ORDER
            else len(CATEGORY_ORDER),
            record["name"],
        )
    )
    return {"version": 1, "skills": records}


def render_skill_index(catalog: dict) -> str:
    grouped: dict[str, list[dict]] = {}
    for record in catalog["skills"]:
        grouped.setdefault(record["category"], []).append(record)

    parts = [README_START]
    for category in CATEGORY_ORDER:
        records = grouped.get(category)
        if not records:
            continue
        parts.append(f"### {category}")
        parts.append("")
        parts.append("| Skill | Dependency | Status | Config | Example | Summary |")
        parts.append("| --- | --- | --- | --- | --- | --- |")
        for record in records:
            config = "yes" if record["requires_configuration"] else "no"
            example = (
                f"[sample]({record['example_artifact']})"
                if record["example_artifact"]
                else "-"
            )
            parts.append(
                "| "
                f"`{record['name']}` | "
                f"`{record['dependency_class']}` | "
                f"`{record['status']}` | "
                f"`{config}` | "
                f"{example} | "
                f"{record['description']} |"
            )
        parts.append("")
    parts.append(README_END)
    return "\n".join(parts)


def update_readme(readme_text: str, generated_index: str) -> str:
    if README_START not in readme_text or README_END not in readme_text:
        raise ValueError("README is missing skill index markers.")
    before, remainder = readme_text.split(README_START, 1)
    _, after = remainder.split(README_END, 1)
    return before + generated_index + after


def write_catalog_and_readme(catalog: dict) -> None:
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    generated_index = render_skill_index(catalog)
    readme_text = README_PATH.read_text(encoding="utf-8")
    README_PATH.write_text(update_readme(readme_text, generated_index), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build catalog.json and the generated README skill index."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if catalog.json or the README skill index are out of date.",
    )
    args = parser.parse_args()

    catalog = collect_catalog()
    generated_index = render_skill_index(catalog)

    if args.check:
        expected_catalog = json.dumps(catalog, indent=2) + "\n"
        actual_catalog = CATALOG_PATH.read_text(encoding="utf-8") if CATALOG_PATH.exists() else ""
        if expected_catalog != actual_catalog:
            raise SystemExit("catalog.json is out of date. Run `make catalog`.")

        actual_readme = README_PATH.read_text(encoding="utf-8")
        expected_readme = update_readme(actual_readme, generated_index)
        if expected_readme != actual_readme:
            raise SystemExit("README skill index is out of date. Run `make catalog`.")
        print("Catalog and README skill index are up to date.")
        return 0

    write_catalog_and_readme(catalog)
    print("Updated catalog.json and README skill index.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
