#!/usr/bin/env python3
"""Lock SKILL.md entries that have artifacts.md on disk to the same pointer."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# Issue #3: these 14 had artifacts.md on disk but never pointed at it.
LISTED = (
    "ai-assisted-prototyping",
    "breaking-into-product",
    "coaching-development",
    "defining-product-strategy",
    "founding-exec-team",
    "interviewing-evaluating-candidates",
    "plg-fundamentals",
    "plg-sales-integration",
    "pm-career-growth",
    "positioning",
    "product-tool-stack",
    "retention-engagement",
    "roadmap-prioritization",
    "time-energy-management",
)


class ArtifactsPointerTests(unittest.TestCase):
    def test_listed_skills_point_from_further_reading(self):
        for name in LISTED:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(
                "## 深入探讨",
                text,
                f"{name} is missing 深入探讨",
            )
            after = text.split("## 深入探讨", 1)[1]
            self.assertIn(
                "`references/artifacts.md`",
                after,
                f"{name} 深入探讨 does not point at artifacts.md",
            )
            self.assertIn("`references/guest-insights.md`", after)

    def test_every_artifacts_file_has_a_skill_pointer(self):
        missing = []
        for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            artifacts = skill_dir / "references" / "artifacts.md"
            skill_md = skill_dir / "SKILL.md"
            if artifacts.is_file() and "`references/artifacts.md`" not in skill_md.read_text(
                encoding="utf-8"
            ):
                missing.append(skill_dir.name)
        self.assertEqual(missing, [])

    def test_install_readme_is_unchanged(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "cp -R lenny-skills/skills/writing-prds .claude/skills/",
            readme,
        )
        self.assertIn("## 安装", readme)


if __name__ == "__main__":
    unittest.main()
