from Items.Weapons.weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", "A sharp blade for close combat.", "melee", 10, 1)

    def use(self, user, target):
        damage = self.damage
        target.take_damage(damage)
        return f"{user.name} swings the sword at {target.name}, dealing {damage} damage!"