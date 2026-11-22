"""Reject invisible direction-control characters in terminal-facing player names."""
import unittest
from main import validated_name


class TerminalNameTests(unittest.TestCase):
    def test_rejects_bidirectional_overrides_and_isolates(self):
        for name in ("Player\u202eexe", "\u2066Knight\u2069", "Hero\u202d", "\u202cBoss"):
            with self.subTest(name=repr(name)), self.assertRaises(ValueError):
                validated_name(name)

    def test_legitimate_unicode_names_still_work(self):
        self.assertEqual(validated_name(" João 🧙 "), "João 🧙")


if __name__ == "__main__":
    unittest.main()
