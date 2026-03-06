from __future__ import annotations

from pathlib import Path


DATA_AWARE_SKILLS = {
    "macro-event-analysis",
    "earnings-preview",
    "market-regime-analysis",
}


def test_data_aware_skills_reference_provider_docs(repo_root):
    for skill_name in DATA_AWARE_SKILLS:
        skill_dir = repo_root / "skills" / skill_name
        skill_md = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        data_providers = skill_dir / "references" / "data-providers.md"
        providers_dir = skill_dir / "references" / "providers"

        assert data_providers.exists(), f"{skill_name} should include references/data-providers.md"
        assert providers_dir.exists(), f"{skill_name} should include references/providers/"

        provider_docs = sorted(path for path in providers_dir.glob("*.md"))
        assert provider_docs, f"{skill_name} should include at least one provider reference doc"
        assert "references/data-providers.md" in skill_md, (
            f"{skill_name} should mention references/data-providers.md directly in SKILL.md"
        )
        assert "If critical data is missing" in skill_md, (
            f"{skill_name} should explain the optional provider fallback pattern"
        )
        assert "ask which supported provider" in skill_md.lower(), (
            f"{skill_name} should explain that it asks the user to choose a provider when needed"
        )
        for provider_doc in provider_docs:
            relative_path = provider_doc.relative_to(skill_dir).as_posix()
            assert relative_path in skill_md or "references/data-providers.md" in skill_md, (
                f"{skill_name} should make provider docs discoverable from SKILL.md"
            )
