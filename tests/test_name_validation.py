"""Protege nomes de personagens e a saída JSON/CLI."""
import subprocess
import sys
import unittest
from pathlib import Path
from main import Character

ROOT = Path(__file__).resolve().parents[1]


class NameValidationTests(unittest.TestCase):
    def test_accepts_accented_and_trimmed_names(self):
        self.assertEqual(Character("  João  ", 10, 2, 1).name, "João")

    def test_rejects_control_characters_and_very_long_names(self):
        for name in ("Ana\nB", "Ana\tB", "A\x00B", "X" * 81):
            with self.subTest(name=name[:10]), self.assertRaises(ValueError):
                Character(name, 10, 2, 1)

    def test_cli_reports_bad_name_without_traceback(self):
        process = subprocess.run(
            [sys.executable, str(ROOT / "main.py"), "--hero-name", "X" * 81],
            capture_output=True, text=True,
        )
        self.assertEqual(process.returncode, 2)
        self.assertIn("at most 80", process.stderr)
        self.assertNotIn("Traceback", process.stderr)


if __name__ == "__main__":
    unittest.main()
