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

    def test_invalid_round_limits_show_usage_error_without_traceback(self):
        for value in ("0", "-1", "1001"):
            with self.subTest(rounds=value):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "--rounds", value],
                    capture_output=True, text=True, timeout=10,
                )
                self.assertEqual(result.returncode, 2)
                self.assertIn("rounds must be between 1 and 1000", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_one_round_is_accepted(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--rounds", "1", "--seed", "42"],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Round 1:", result.stdout)
        self.assertIn("Result:", result.stdout)



if __name__ == "__main__":
    unittest.main()
