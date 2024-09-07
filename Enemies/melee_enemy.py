from .enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, name, health, attack_power, range, speed):
        super().__init__(name, health, attack_power)
        self.range = range  # Melee range, e.g., 1 unit
        self.speed = speed  # How much the enemy can move each turn

    def attack(self, player, distance):
        """
        Perform a melee attack if the player is within range, otherwise move closer.
        
        :param distance: The distance between the enemy and the player
        """
        if distance <= self.range:
            print(f"{self.name} strikes {player.name} with a melee attack for {self.attack_power} damage!")
            player.take_damage(self.attack_power)
        else:
            print(f"{self.name} is too far to attack and moves closer.")
            # Move closer to the player by reducing the distance by the enemy's speed
            new_distance = max(0, distance - self.speed)
            print(f"{self.name} moves closer by {self.speed} units. New distance: {new_distance} units.")
            return new_distance  # Return the new distance to the player
