from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, name, health, attack_power):
        """
        Base class for all enemies.
        
        :param name: Name of the enemy
        :param health: Health points of the enemy
        :param attack_power: Attack power of the enemy
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        """
        Reduce the enemy's health when they take damage.
        """
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

    def is_alive(self):
        """
        Check if the enemy is still alive.
        """
        return self.health > 0

    @abstractmethod
    def attack(self, player):
        """
        Abstract method for attacking the player.
        Must be implemented by subclasses.
        """
        pass
