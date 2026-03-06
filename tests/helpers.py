from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path


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

ECONOMIC_EVENT_REQUIRED_FIELDS = {
    "schema_version",
    "event_id",
    "provider",
    "event_name",
    "country",
    "currency",
    "scheduled_time_utc",
    "importance",
    "status",
    "source_url",
    "last_updated_utc",
    "coverage_notes",
}

EARNINGS_EVENT_REQUIRED_FIELDS = {
    "schema_version",
    "event_id",
    "provider",
    "company_name",
    "symbol",
    "scheduled_time_utc",
    "report_timing",
    "status",
    "source_url",
    "last_updated_utc",
    "coverage_notes",
}


def skills_dir(repo_root: Path) -> Path:
    return repo_root / "skills"


def iter_skill_dirs(repo_root: Path) -> list[Path]:
    return sorted(path for path in skills_dir(repo_root).iterdir() if path.is_dir())


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md} is missing opening frontmatter.")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{skill_md} has malformed frontmatter.")

    frontmatter: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"{skill_md} has invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [match.group(1).strip() for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text)]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def json_code_blocks(path: Path) -> list[object]:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    return [json.loads(block) for block in blocks]


def import_module_from_path(module_name: str, module_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
