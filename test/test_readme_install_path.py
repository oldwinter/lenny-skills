#!/usr/bin/env python3
"""Lock README install/use next-step: English slugs, copy-all, stay on this fork."""

from __future__ import annotations

import re
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILLS = ROOT / "skills"

COPY_ONE = "cp -R lenny-skills/skills/writing-prds .claude/skills/"
COPY_ALL = "cp -R lenny-skills/skills/. .claude/skills/"


def _section(heading: str) -> str:
    text = README.read_text(encoding="utf-8")
    marker = f"## {heading}"
    start = text.index(marker)
    rest = text[start + len(marker) :]
    nxt = re.search(r"\n## ", rest)
    return rest if nxt is None else rest[: nxt.start()]


def _fenced_bash(section: str) -> list[str]:
    return re.findall(r"```bash\n(.*?)```", section, flags=re.S)


def _frontmatter_name(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    match = re.search(r"^name:\s*(.+)$", text, flags=re.M)
    if not match:
        raise AssertionError(f"missing name in {skill_md}")
    return match.group(1).strip()


class ReadmeInstallPathTests(unittest.TestCase):
    def test_skills_badge_stays_on_this_fork(self) -> None:
        text = README.read_text(encoding="utf-8")
        badge = next(
            line for line in text.splitlines() if line.startswith("[![Skills]")
        )
        self.assertIn("https://github.com/oldwinter/lenny-skills/", badge)
        self.assertNotIn("RefoundAI/lenny-skills", badge)

    def test_install_maps_chinese_titles_to_english_dirs(self) -> None:
        install = _section("安装")
        self.assertIn("`编写PRD` 对应 `writing-prds`", install)
        self.assertIn("`路线图优先级` 对应 `roadmap-prioritization`", install)
        self.assertIn("不要用中文标题", install)
        self.assertIn(".claude/skills/编写PRD", install)
        self.assertNotIn("lenny-skills/skills/编写PRD", install)
        self.assertNotIn("lenny-skills/skills/路线图优先级", install)

    def test_install_has_copy_one_and_copy_all(self) -> None:
        install = _section("安装")
        blocks = _fenced_bash(install)
        joined = "\n".join(blocks)
        self.assertIn("git clone https://github.com/oldwinter/lenny-skills.git", joined)
        self.assertIn(COPY_ONE, joined)
        self.assertIn(COPY_ALL, joined)
        self.assertLess(joined.index(COPY_ONE), joined.index(COPY_ALL))

    def test_usage_asks_for_chinese_task_not_slash_title(self) -> None:
        usage = _section("使用")
        self.assertIn("帮我写一份 PRD", usage)
        self.assertIn("帮我排一下路线图优先级", usage)
        self.assertIn("description", usage)
        self.assertIn("不要输入 `/编写PRD`", usage)
        self.assertIn("复制路径和 frontmatter `name`", usage)

    def test_chinese_title_is_not_a_folder(self) -> None:
        self.assertFalse((SKILLS / "编写PRD").exists())
        self.assertFalse((SKILLS / "路线图优先级").exists())
        self.assertTrue((SKILLS / "writing-prds" / "SKILL.md").is_file())
        self.assertTrue((SKILLS / "roadmap-prioritization" / "SKILL.md").is_file())
        self.assertEqual(_frontmatter_name(SKILLS / "writing-prds" / "SKILL.md"), "writing-prds")
        self.assertEqual(
            _frontmatter_name(SKILLS / "roadmap-prioritization" / "SKILL.md"),
            "roadmap-prioritization",
        )

    def test_readme_copy_one_lands_writing_prds(self) -> None:
        install = _section("安装")
        copy_one = next(
            block
            for block in _fenced_bash(install)
            if "writing-prds" in block and "skills/." not in block
        )
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "lenny-skills").symlink_to(ROOT)
            completed = subprocess.run(
                copy_one,
                shell=True,
                cwd=project,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0)
            landed = project / ".claude" / "skills" / "writing-prds" / "SKILL.md"
            self.assertTrue(landed.is_file())
            self.assertEqual(_frontmatter_name(landed), "writing-prds")
            self.assertFalse((project / ".claude" / "skills" / "编写PRD").exists())

    def test_readme_copy_all_lands_every_skill(self) -> None:
        install = _section("安装")
        copy_all = next(block for block in _fenced_bash(install) if "skills/." in block)
        expected = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
        self.assertEqual(len(expected), 76)
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "lenny-skills").symlink_to(ROOT)
            subprocess.run(copy_all, shell=True, cwd=project, check=True)
            dest = project / ".claude" / "skills"
            landed = sorted(p.name for p in dest.iterdir() if p.is_dir())
            self.assertEqual(landed, expected)
            self.assertTrue((dest / "writing-prds" / "SKILL.md").is_file())
            self.assertTrue((dest / "roadmap-prioritization" / "SKILL.md").is_file())

    def test_chinese_title_copy_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "lenny-skills").symlink_to(ROOT)
            completed = subprocess.run(
                "mkdir -p .claude/skills && cp -R lenny-skills/skills/编写PRD .claude/skills/",
                shell=True,
                cwd=project,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertFalse((project / ".claude" / "skills" / "编写PRD").exists())


if __name__ == "__main__":
    unittest.main()
