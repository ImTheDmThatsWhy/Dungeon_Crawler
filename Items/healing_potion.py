# healing_potion.py
from Items.item import Item

class HealingPotion(Item):
    def __init__(self, healing_amount):
        """
        Initialize a healing potion.
        
        :param healing_amount: The amount of health the potion restores
        """
        super().__init__(name="Healing Potion", description=f"Restores {healing_amount} health.")
        self.healing_amount = healing_amount

    def use(self, player):
        """
        Use the healing potion on the player.
        """
        player.health += self.healing_amount
        print(f"{player.name} uses a Healing Potion and restores {self.healing_amount} health! Current health: {player.health}")
