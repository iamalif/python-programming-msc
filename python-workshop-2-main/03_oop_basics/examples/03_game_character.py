"""
03 - Game Character Class
=========================
Create a game character with attributes and actions.

Run this file: python 03_game_character.py
"""

class Character:
    """Represents a game character."""

    def __init__(self, name, health=100, attack_power=10):
        """Create a new character."""
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.is_alive = True

    def attack(self, target):
        """Attack another character."""
        if not self.is_alive:
            print(f"{self.name} cannot attack - defeated!")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        """Receive damage."""
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}/{self.max_health}")

        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        """Restore health."""
        if not self.is_alive:
            print(f"{self.name} cannot be healed - defeated!")
            return

        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} heals for {amount}. Health: {self.health}/{self.max_health}")

    def display_stats(self):
        """Show character stats."""
        status = "Alive" if self.is_alive else "Defeated"
        print(f"{self.name} [{status}]:")
        print(f"  Health: {self.health}/{self.max_health}")
        print(f"  Attack Power: {self.attack_power}")


# Game demo
print("=== Battle Arena ===")
print()

# Create characters
hero = Character("Hero", health=120, attack_power=15)
monster = Character("Monster", health=80, attack_power=12)

# Display initial stats
print("Characters:")
hero.display_stats()
print()
monster.display_stats()

# Battle!
print()
print("=== Battle Begin ===")
print()

hero.attack(monster)
print()

monster.attack(hero)
print()

hero.attack(monster)
print()

monster.attack(hero)
print()

hero.attack(monster)  # Should defeat monster
print()

# Try actions on defeated character
monster.attack(hero)  # Can't attack when defeated
print()

hero.heal(20)

# Final stats
print()
print("=== Final Stats ===")
print()

hero.display_stats()
print()
monster.display_stats()
