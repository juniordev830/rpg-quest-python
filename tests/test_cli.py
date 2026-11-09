import json
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

    def test_json_output_is_machine_readable_and_replayable(self):
        args = [sys.executable, str(SCRIPT), "--hero-name", "João", "--enemy", "orc",
                "--seed", "42", "--format", "json"]
        first = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
        second = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        result = json.loads(first.stdout)
        self.assertIn(result["winner"], ("João", "Orc Guard", "Draw"))
        self.assertEqual(result["hero"]["name"], "João")
        self.assertEqual(result["enemy"]["name"], "Orc Guard")
        self.assertLessEqual(result["hero"]["hp"], result["hero"]["max_hp"])
        self.assertTrue(result["events"])
        self.assertIn("Battle started", result["events"][0])

    def test_invalid_round_limits_are_cli_errors_without_traceback(self):
        for value in ("0", "-1", "1001", "abc"):
            for output_format in ("text", "json"):
                with self.subTest(rounds=value, format=output_format):
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT), "--rounds", value, "--format", output_format],
                        capture_output=True, text=True, encoding="utf-8",
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("error:", result.stderr)
                    self.assertIn("rounds", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertFalse(result.stdout)

    def test_upper_round_limit_is_accepted(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--rounds", "1000", "--seed", "42", "--format", "json"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["max_rounds"], 1000)
    def test_invalid_enemy_and_blank_name_are_rejected(self):
        for args in (["--enemy", "dragon"], ["--hero-name", "  "]):
            with self.subTest(args=args):
                result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
