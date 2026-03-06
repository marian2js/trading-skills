from __future__ import annotations

import subprocess


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

PROVIDER_LEAK_TERMS = {"fmp", "fred", "alpaca", "polygon", "ibkr", "interactive-brokers"}


def test_no_forbidden_tracked_artifacts(repo_root):
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    tracked = result.stdout.splitlines()
    forbidden = []
    for path in tracked:
        if any(pattern in path for pattern in FORBIDDEN_TRACKED_PATTERNS):
            forbidden.append(path)
        if path.endswith(FORBIDDEN_TRACKED_SUFFIXES):
            forbidden.append(path)
    assert not forbidden, f"Tracked forbidden artifacts found: {sorted(set(forbidden))}"


def test_public_skill_names_do_not_leak_provider_brands(repo_root):
    leaked = []
    for skill_dir in sorted((repo_root / "skills").iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        tokens = set(skill_dir.name.split("-"))
        if tokens & PROVIDER_LEAK_TERMS:
            leaked.append(skill_dir.name)
    assert not leaked, f"Public skill names should not include provider branding: {leaked}"


def test_every_skill_has_sample_output_artifact(repo_root):
    missing = []
    for skill_dir in sorted((repo_root / "skills").iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        if not (skill_dir / "sample-output.md").exists():
            missing.append(skill_dir.name)
    assert not missing, f"Every skill should include sample-output.md for quick evaluation: {missing}"


def test_skills_only_ship_shared_python_library(repo_root):
    python_files = sorted(
        path.relative_to(repo_root).as_posix()
        for path in (repo_root / "skills").rglob("*.py")
    )
    assert python_files == ["skills/_lib/calculations.py"], (
        "Skills should stay markdown-first aside from the shared calculations library: "
        f"{python_files}"
    )


def test_release_artifacts_exist(repo_root):
    assert (repo_root / "CHANGELOG.md").exists(), "Repository should include CHANGELOG.md"
    version_file = repo_root / "VERSION"
    assert version_file.exists(), "Repository should include a VERSION file"
    assert version_file.read_text(encoding="utf-8").strip(), "VERSION file should not be empty"
