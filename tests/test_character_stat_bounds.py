import unittest
from main import Character


class CharacterStatBoundTests(unittest.TestCase):
    def test_rejects_excessive_statistics_before_battle(self):
        for stats in (
            (1_000_000_001, 5, 2),
            (10, 1_000_000_001, 2),
            (10, 5, 1_000_000_001),
        ):
            with self.subTest(stats=stats), self.assertRaises(ValueError):
                Character("Knight", *stats)

    def test_boundary_values_are_valid(self):
        character = Character("Knight", 1_000_000_000, 1_000_000_000, 1_000_000_000)
        self.assertTrue(character.is_alive())
        self.assertEqual(character.max_hp, 1_000_000_000)


if __name__ == "__main__":
    unittest.main()
