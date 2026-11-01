import random


class Character:
    """A combatant with bounded health and basic combat attributes."""

    def __init__(self, name: str, hp: int, attack: int, defense: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Character name cannot be empty.")
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
        if dmg < 0:
            raise ValueError("Damage cannot be negative.")

        effective_dmg = max(1, dmg - self.defense)
        self.hp = max(0, self.hp - effective_dmg)
        return effective_dmg


def battle(hero: Character, monster: Character) -> str:
    """Run up to ten combat rounds and return a winner or 'Draw'."""
    if not hero.is_alive() or not monster.is_alive():
        raise ValueError("Both combatants must be alive when a battle starts.")

    print(f"⚔️ Battle started: {hero.name} vs {monster.name}")
    rounds = 0

    while hero.is_alive() and monster.is_alive() and rounds < 10:
        rounds += 1
        damage = hero.attack + random.randint(1, 5)
        dealt = monster.take_damage(damage)
        print(
            f"Round {rounds}: {hero.name} deals {dealt} damage to "
            f"{monster.name} (Monster HP: {monster.hp})"
        )

        if monster.is_alive():
            monster_damage = monster.attack + random.randint(1, 3)
            received = hero.take_damage(monster_damage)
            print(
                f"Round {rounds}: {monster.name} deals {received} damage to "
                f"{hero.name} (Hero HP: {hero.hp})"
            )

    if hero.is_alive() and monster.is_alive():
        return "Draw"
    return hero.name if hero.is_alive() else monster.name


if __name__ == "__main__":
    hero = Character("Knight Arthur", hp=100, attack=18, defense=5)
    goblin = Character("Goblin Berserker", hp=40, attack=12, defense=2)
    winner = battle(hero, goblin)
    print(f"🏆 Result: {winner}")
