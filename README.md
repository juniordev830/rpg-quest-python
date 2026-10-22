# RPG Quest Python

A turn-based RPG engine and dungeon battle system built with Python.

## ⚔️ Game Features

- **Character Stats**: Health, Attack, Defense, and XP progression.
- **Turn-based Combat Engine**: Damage calculations and critical strikes.
- **Inventory & Loot**: Items, potions, and equipment.

## 🚀 How to Run

```bash
python main.py
```

## 📜 License
MIT

---

# Código-fonte completo do projeto


## Arquivo: `.gitignore`

```text
__pycache__/
*.pyc
venv/
.DS_Store
```

## Arquivo: `main.py`

```text
import random

class Character:
    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, dmg: int) -> int:
        effective_dmg = max(1, dmg - self.defense)
        self.hp = max(0, self.hp - effective_dmg)
        return effective_dmg

def battle(hero: Character, monster: Character) -> str:
    print(f"⚔️ Battle started: {hero.name} vs {monster.name}")
    rounds = 0
    while hero.is_alive() and monster.is_alive() and rounds < 10:
        rounds += 1
        dmg = hero.attack + random.randint(1, 5)
        took = monster.take_damage(dmg)
        print(f"Round {rounds}: {hero.name} deals {took} damage to {monster.name} (Monster HP: {monster.hp})")

        if monster.is_alive():
            m_dmg = monster.attack + random.randint(1, 3)
            m_took = hero.take_damage(m_dmg)
            print(f"Round {rounds}: {monster.name} deals {m_took} damage to {hero.name} (Hero HP: {hero.hp})")

    return hero.name if hero.is_alive() else monster.name

if __name__ == "__main__":
    hero = Character("Knight Arthur", hp=100, attack=18, defense=5)
    goblin = Character("Goblin Berserker", hp=40, attack=12, defense=2)
    winner = battle(hero, goblin)
    print(f"🏆 Winner: {winner}")
```
