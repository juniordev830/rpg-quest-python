import argparse
import random


class Character:
    """A combatant with bounded health and basic combat attributes."""

    def __init__(self, name: str, hp: int, attack: int, defense: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Character name cannot be empty.")
        for attribute, value in (("hp", hp), ("attack", attack), ("defense", defense)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{attribute} must be an integer.")
        if hp <= 0:
            raise ValueError("Maximum health must be greater than zero.")
        if attack < 0 or defense < 0:
            raise ValueError("Attack and defense cannot be negative.")

        self.name = name.strip()
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, dmg: int) -> int:
        if isinstance(dmg, bool) or not isinstance(dmg, int):
            raise TypeError("Damage must be an integer.")
        if dmg < 0:
            raise ValueError("Damage cannot be negative.")

        effective_dmg = max(1, dmg - self.defense)
        actual_dmg = min(self.hp, effective_dmg)
        self.hp -= actual_dmg
        return actual_dmg


def battle(hero: Character, monster: Character, rng=None) -> str:
    """Run up to ten combat rounds and return a winner or 'Draw'."""
    if not hero.is_alive() or not monster.is_alive():
        raise ValueError("Both combatants must be alive when a battle starts.")

    rng = random if rng is None else rng
    print(f"⚔️ Battle started: {hero.name} vs {monster.name}")
    rounds = 0

    while hero.is_alive() and monster.is_alive() and rounds < 10:
        rounds += 1
        damage = hero.attack + rng.randint(1, 5)
        dealt = monster.take_damage(damage)
        print(
            f"Round {rounds}: {hero.name} deals {dealt} damage to "
            f"{monster.name} (Monster HP: {monster.hp})"
        )

        if monster.is_alive():
            monster_damage = monster.attack + rng.randint(1, 3)
            received = hero.take_damage(monster_damage)
            print(
                f"Round {rounds}: {monster.name} deals {received} damage to "
                f"{hero.name} (Hero HP: {hero.hp})"
            )

    if hero.is_alive() and monster.is_alive():
        return "Draw"
    return hero.name if hero.is_alive() else monster.name


def main():
    parser = argparse.ArgumentParser(description="Simulate a turn-based RPG battle")
    parser.add_argument("--hero-name", default="Knight Arthur", help="hero's display name")
    parser.add_argument("--enemy", choices=("goblin", "orc", "spider"), default="goblin")
    parser.add_argument("--seed", type=int, help="replay a battle with a fixed random seed")
    args = parser.parse_args()
    if not args.hero_name.strip():
        parser.error("hero name cannot be empty")

    enemies = {
        "goblin": ("Goblin Berserker", 40, 12, 2),
        "orc": ("Orc Guard", 70, 15, 4),
        "spider": ("Cave Spider", 30, 10, 1),
    }
    hero = Character(args.hero_name, hp=100, attack=18, defense=5)
    monster = Character(*enemies[args.enemy])
    rng = random.Random(args.seed) if args.seed is not None else random
    winner = battle(hero, monster, rng)
    print(f"🏆 Result: {winner}")


if __name__ == "__main__":
    main()
