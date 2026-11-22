"""Tests for preventing a character from fighting the same object instance."""
import random
import unittest
from main import Character, battle


class CombatantIdentityTests(unittest.TestCase):
    def test_same_character_instance_is_rejected_without_damage(self):
        hero = Character("Knight", hp=30, attack=10, defense=2)
        with self.assertRaisesRegex(ValueError, "distinct"):
            battle(hero, hero, rng=random.Random(17), emit=lambda _: None)
        self.assertEqual(hero.hp, 30)

    def test_distinct_instances_with_same_name_are_permitted(self):
        first = Character("Twin", hp=10, attack=5, defense=0)
        second = Character("Twin", hp=10, attack=5, defense=0)
        winner = battle(first, second, rng=random.Random(2), max_rounds=1, emit=lambda _: None)
        self.assertIn(winner, ("Twin", "Draw"))


if __name__ == "__main__":
    unittest.main()
