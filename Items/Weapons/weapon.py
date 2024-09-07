# weapon.py
from abc import ABC, abstractmethod
from Items.item import Item

class Weapon(Item, ABC):
    def __init__(self, name, description, damage, weapon_type="melee", range=1):
        """
        Initialize a weapon.
        
        :param name: The weapon's name
        :param description: A description of the weapon
        :param damage: The amount of damage the weapon deals
        :param weapon_type: Either 'melee' or 'ranged' (default is melee)
        :param range: The effective range of the weapon (default is 1 for melee)
        """
        super().__init__(name, description)
        self.damage = damage
        self.weapon_type = weapon_type
        self.range = range

    @abstractmethod
    def use(self, player):
        """
        Abstract method to define how the weapon is used.
        This must be implemented by any subclass.
        """
        pass

    def __str__(self):
        return f"{self.name}: {self.description} (Type: {self.weapon_type}, Damage: {self.damage}, Range: {self.range})"

    def get_damage(self):
        """
        Return the amount of damage the weapon deals.
        """
        return self.damage

    def get_range(self):
        """
        Return the range of the weapon.
        """
        return self.range

    def is_ranged(self):
        """
        Check if the weapon is a ranged weapon.
        """
        return self.weapon_type == "ranged"

    def is_melee(self):
        """
        Check if the weapon is a melee weapon.
        """
        return self.weapon_type == "melee"
