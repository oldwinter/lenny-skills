#!/usr/bin/env python3
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class RepositoryIntegrityTests(unittest.TestCase):
    def test_integrity_validator_passes(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "validate_repository.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_python_bytecode_is_ignored(self):
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", gitignore)
        self.assertIn("*.py[cod]", gitignore)

    def test_contributing_matches_chinese_runtime(self):
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("## 如何提供帮助", contributing)
        self.assertIn("当用户需要……时使用", contributing)
        self.assertNotIn("## How to Help", contributing)
        self.assertNotIn('以 "Help users [verb]" 开头', contributing)

    def test_ci_runs_tests_and_validator_with_read_only_contents(self):
        workflow = (ROOT / ".github" / "workflows" / "repository-integrity.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("contents: read", workflow)
        self.assertIn("python3 -m unittest discover", workflow)
        self.assertIn("python3 scripts/validate_repository.py", workflow)


if __name__ == "__main__":
    unittest.main()
