# player.py

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.base_attack_power = attack_power
        self.equipped_weapon = None
        self.inventory = []

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        print(f"You equipped the {weapon}")

    @property
    def attack_power(self):
        if self.equipped_weapon == "sword":
            return self.base_attack_power + 5
        elif self.equipped_weapon == "bow":
            return self.base_attack_power + 3
        else:
            return self.base_attack_power

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Current health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated.")

    def add_item(self, item):
        """
        Add an item to the player's inventory.
        """
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")

    def use_item(self, item_name):
        """
        Use an item from the player's inventory.
        """
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                break
        else:
            print(f"You don't have {item_name} in your inventory.")
    
    def get_inventory(self):
        """
        Return a list of items in the player's inventory.
        """
        if not self.inventory:
            return "Your inventory is empty."
        return f"Your inventory: {', '.join(item.name for item in self.inventory)}"

    def is_alive(self):
        return self.health > 0


    def get_item_names(self):
        return [item.name for item in self.inventory]

    def find_item_by_name(self, item_name):
        return next((item for item in self.inventory if item.name.lower() == item_name.lower()), None)
