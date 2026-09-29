#!/usr/bin/env python3
from collections import Counter
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_SKILLS = 76
EXPECTED_RELATED_LINKS = 282
BANNED_TERMS = ("法学硕士", "振动检查", "即时工程", "下午职业发展", "协商赔偿")
TRUNCATED_ENDING = re.compile(r"(?:链接为|[:：,，；;]|基于(?:两个|三个|四个)标准)$")


def validate() -> list[str]:
    errors: list[str] = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} skills, found {len(skill_files)}")

    names: list[str] = []
    related_links = 0
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n") or len(text.split("---", 2)) != 3:
            errors.append(f"{skill_file.relative_to(ROOT)}: malformed frontmatter")
            continue
        frontmatter = text.split("---", 2)[1]
        fields = re.findall(r"(?m)^([A-Za-z0-9_-]+):", frontmatter)
        if fields != ["name", "description"]:
            errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter fields {fields}")
        name = re.search(r"(?m)^name:\s*(.+?)\s*$", frontmatter)
        description = re.search(r"(?m)^description:\s*(.+?)\s*$", frontmatter)
        if name is None or description is None:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing name or description")
            continue
        name_value = name.group(1).strip("\"'")
        names.append(name_value)
        if name_value != skill_file.parent.name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name mismatch {name_value}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name_value):
            errors.append(f"{skill_file.relative_to(ROOT)}: invalid name {name_value}")

        if text.count("```") % 2:
            errors.append(f"{skill_file.relative_to(ROOT)}: unbalanced code fences")
        for term in BANNED_TERMS:
            if term in text:
                errors.append(f"{skill_file.relative_to(ROOT)}: banned term {term}")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith("- **") and TRUNCATED_ENDING.search(line.rstrip()):
                errors.append(f"{skill_file.relative_to(ROOT)}:{line_number}: truncated summary")

        for reference, header, pointer in (
            ("guest-insights.md", "> **中文阅读说明：**", "`references/guest-insights.md`"),
            ("artifacts.md", "> **中文使用说明：**", "`references/artifacts.md`"),
        ):
            path = skill_file.parent / "references" / reference
            if not path.is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing")
                continue
            reference_text = path.read_text(encoding="utf-8")
            if not reference_text.startswith(header):
                errors.append(f"{path.relative_to(ROOT)}: missing Chinese boundary")
            if pointer not in text:
                errors.append(f"{skill_file.relative_to(ROOT)}: missing pointer to {reference}")

        guest_text = (skill_file.parent / "references" / "guest-insights.md").read_text(encoding="utf-8")
        header_count = re.search(r"\*(\d+) sources, (\d+) insights\*", guest_text)
        deep_count = re.search(r"有关 (\d+) 个来源的全部 (\d+) 条见解", text)
        if header_count is None or deep_count is None or header_count.groups() != deep_count.groups():
            errors.append(f"{skill_file.relative_to(ROOT)}: Deep Dive count drift")

        if "## 相关skill" in text:
            entries = [
                line for line in text.split("## 相关skill", 1)[1].splitlines() if line.startswith("- ")
            ]
            for line in entries:
                match = re.fullmatch(r"- \[[^]]+\]\(\.\./([a-z0-9-]+)/\)", line)
                if match is None:
                    errors.append(f"{skill_file.relative_to(ROOT)}: invalid related link {line}")
                    continue
                related_links += 1
                if not (SKILLS / match.group(1) / "SKILL.md").is_file():
                    errors.append(f"{skill_file.relative_to(ROOT)}: missing related target {match.group(1)}")

        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if target and not (skill_file.parent / target).resolve().exists():
                errors.append(f"{skill_file.relative_to(ROOT)}: broken link {link}")

    duplicates = [name for name, count in Counter(names).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate skill names: {duplicates}")
    if related_links != EXPECTED_RELATED_LINKS:
        errors.append(f"expected {EXPECTED_RELATED_LINKS} related links, found {related_links}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_links = set(re.findall(r"\]\((skills/[^)]+/)\)", readme))
    expected_links = {f"skills/{path.parent.name}/" for path in skill_files}
    if readme_links != expected_links:
        errors.append("README skill index does not match skills directory")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print("Validated 76 skills and repository contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
