import unittest
from unittest.mock import patch

from main import Character, battle


class CharacterTests(unittest.TestCase):
    def test_constructor_rejects_invalid_attributes(self):
        with self.assertRaises(ValueError):
            Character(" ", 10, 1, 0)
        with self.assertRaises(ValueError):
            Character("Hero", 0, 1, 0)
        with self.assertRaises(ValueError):
            Character("Hero", 10, -1, 0)

    def test_damage_is_at_least_one_and_health_never_goes_below_zero(self):
        hero = Character("Hero", 10, 1, 0)

        self.assertEqual(hero.take_damage(0), 1)
        self.assertEqual(hero.hp, 9)
        self.assertEqual(hero.take_damage(100), 100)
        self.assertEqual(hero.hp, 0)
        self.assertFalse(hero.is_alive())

    def test_battle_rejects_combatants_that_are_already_defeated(self):
        hero = Character("Hero", 10, 1, 0)
        monster = Character("Monster", 10, 1, 0)
        hero.take_damage(100)

        with self.assertRaises(ValueError):
            battle(hero, monster)

        with self.assertRaises(ValueError):
            battle(monster, hero)

    def test_battle_returns_winner_when_monster_is_defeated(self):
        hero = Character("Hero", 100, 100, 10)
        monster = Character("Monster", 10, 1, 0)

        with patch("main.random.randint", return_value=1):
            result = battle(hero, monster)

        self.assertEqual(result, "Hero")
        self.assertTrue(hero.is_alive())
        self.assertFalse(monster.is_alive())

    def test_battle_returns_draw_when_round_limit_is_reached(self):
        hero = Character("Hero", 100, 0, 100)
        monster = Character("Monster", 100, 0, 100)

        with patch("main.random.randint", return_value=1):
            result = battle(hero, monster)

        self.assertEqual(result, "Draw")
        self.assertTrue(hero.is_alive())
        self.assertTrue(monster.is_alive())


if __name__ == "__main__":
    unittest.main()
