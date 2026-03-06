from __future__ import annotations

import json

from tests.helpers import import_module_from_path, iter_skill_dirs, load_json


def test_catalog_matches_generated_skill_metadata(repo_root):
    module = import_module_from_path("build_catalog", repo_root / "scripts/build_catalog.py")
    generated = module.collect_catalog(repo_root)
    checked_in = load_json(repo_root / "catalog.json")
    assert checked_in == generated, "catalog.json should match the generated catalog output"


def test_readme_skill_index_matches_generated_catalog(repo_root):
    module = import_module_from_path("build_catalog", repo_root / "scripts/build_catalog.py")
    catalog = load_json(repo_root / "catalog.json")
    generated_index = module.render_skill_index(catalog)
    readme = (repo_root / "README.md").read_text(encoding="utf-8")
    expected_readme = module.update_readme(readme, generated_index)
    assert readme == expected_readme, "README skill index should be regenerated from catalog.json"


def test_catalog_covers_all_skill_directories(repo_root):
    catalog = load_json(repo_root / "catalog.json")
    catalog_names = {record["name"] for record in catalog["skills"]}
    skill_names = {skill_dir.name for skill_dir in iter_skill_dirs(repo_root)}
    assert catalog_names == skill_names, "catalog.json should contain every skill directory exactly once"


def test_data_backed_catalog_entries_declare_provider_metadata(repo_root):
    catalog = load_json(repo_root / "catalog.json")
    for record in catalog["skills"]:
        if record["dependency_class"] in {"data-required", "data-optional"}:
            if record["name"] in {"economic-calendar", "earnings-calendar"}:
                assert record["providers_supported"], f"{record['name']} should declare supported internal providers"
            if record["dependency_class"] == "data-required":
                assert record["requires_configuration"] is True, (
                    f"{record['name']} should declare that live operation requires configuration"
                )


def test_catalog_field_shapes_are_consistent(repo_root):
    catalog = load_json(repo_root / "catalog.json")
    for record in catalog["skills"]:
        assert isinstance(record["name"], str) and record["name"], "Catalog skill name should be a non-empty string"
        assert record["path"].startswith("skills/"), f"Catalog path should point into skills/: {record['path']}"
        assert isinstance(record["description"], str) and len(record["description"]) >= 40
        assert isinstance(record["providers_supported"], list), "providers_supported should be a list"
        assert isinstance(record["requires_configuration"], bool), "requires_configuration should be boolean"
        assert isinstance(record["asset_coverage"], list) and record["asset_coverage"], (
            f"{record['name']} should declare asset coverage"
        )
        assert isinstance(record["tags"], list) and record["tags"], f"{record['name']} should declare tags"
