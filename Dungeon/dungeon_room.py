# dungeon_room.py

class DungeonRoom:
    def __init__(self, description, enemies=None, items=None, exits=None):
        """
        Initialize a dungeon room.
        
        :param description: A short description of the room
        :param enemies: List of enemies in the room (default is None)
        :param items: List of items available in the room (default is None)
        :param exits: Dictionary of exits (directions) and the rooms they lead to (default is None)
        """
        self.description = description
        self.enemies = enemies if enemies else []
        self.items = items if items else []
        self.exits = exits if exits else {}

    def describe(self):
        """
        Return a description of the room.
        """
        return self.description

    def list_enemies(self):
        """
        List the enemies in the room.
        """
        if not self.enemies:
            return "The room is empty."
        return f"Enemies in the room: \033[31m{', '.join(enemy.name for enemy in self.enemies)}\033[0m"

    def get_exits(self):
        """
        Return the available exits in the room.
        """
        if not self.exits:
            return "There are no exits."
        return f"Available exits: {', '.join(self.exits.keys())}"

    def add_enemy(self, enemy):
        """
        Add an enemy to the room.
        """
        self.enemies.append(enemy)

    def add_item(self, item):
        """
        Add an item to the room.
        """
        self.items.append(item)

    def connect_room(self, direction, room):
        """
        Connect this room to another room in the given direction.
        
        :param direction: The direction to the other room (e.g., 'north', 'south')
        :param room: The room object that this room connects to
        """
        self.exits[direction] = room

    def list_items(self):
        if not self.items:
            return "There are no items here."
        return "Items in the room: " + ", ".join(f"{item.name}: {item.description}" for item in self.items)