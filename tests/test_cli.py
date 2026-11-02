from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "main.py"


class BattleCliTests(unittest.TestCase):
    def test_seeded_game_replays_and_uses_selected_names(self):
        args = [sys.executable, str(SCRIPT), "--hero-name", "João", "--enemy", "orc", "--seed", "42"]
        first = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
        second = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(first.returncode, 0)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn("João vs Orc Guard", first.stdout)
        self.assertIn("Result:", first.stdout)

    def test_invalid_enemy_and_blank_name_are_rejected(self):
        for args in (["--enemy", "dragon"], ["--hero-name", "  "]):
            with self.subTest(args=args):
                result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
