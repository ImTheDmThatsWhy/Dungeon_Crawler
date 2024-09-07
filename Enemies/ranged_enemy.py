from Enemies.enemy import Enemy

class RangedEnemy(Enemy):
    def __init__(self, name, health, attack_power, range, speed):
        super().__init__(name, health, attack_power)
        self.range = range
        self.speed = speed

    def attack(self, player, distance):
        """
        Perform a ranged attack on the player if they are within range.
        :param distance: The distance between the enemy and the player
        """
        if distance <= self.range:
            print(f"{self.name} shoots {player.name} from {distance} units away for {self.attack_power} damage!")
            player.take_damage(self.attack_power)
        else:
            print(f"{self.name} cannot reach {player.name}, who is out of range (Range: {self.range}).")
