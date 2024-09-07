from Items.Weapons.weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", "A bow that can shoot arrows from a distance.", "ranged", 8, 5)

    def use(self, user, target, distance):
        if distance <= self.range:
            damage = self.damage
            target.take_damage(damage)
            return f"{user.name} shoots an arrow at {target.name} from {distance} units away, dealing {damage} damage!"
        else:
            return f"{user.name} tries to shoot {target.name}, but they are too far away!"