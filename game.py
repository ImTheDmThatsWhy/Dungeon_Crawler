# game.py

import time
from Dungeon.dungeon_room import DungeonRoom
from Player.player import Player
from Items.healing_potion import HealingPotion
from Enemies.melee_enemy import MeleeEnemy
from Enemies.ranged_enemy import RangedEnemy
from Items.Weapons.sword import Sword
from Items.Weapons.bow import Bow


def show_title_screen():
    print("""\033[31m
          
          
████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄         ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄█          ▄████████    ▄████████ 
███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄      ███    ███   ███    ███   ███    ███ ███     ███ ███         ███    ███   ███    ███ 
███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███      ███    █▀    ███    ███   ███    ███ ███     ███ ███         ███    █▀    ███    ███ 
███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███      ███         ▄███▄▄▄▄██▀   ███    ███ ███     ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███      ███        ▀▀███▀▀▀▀▀   ▀███████████ ███     ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███      ███    █▄  ▀███████████   ███    ███ ███     ███ ███         ███    █▄  ▀███████████ 
███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███      ███    ███   ███    ███   ███    ███ ███ ▄█▄ ███ ███▌    ▄   ███    ███   ███    ███ 
████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀       ████████▀    ███    ███   ███    █▀   ▀███▀███▀  █████▄▄██   ██████████   ███    ███ 
                                                                                                 ███    ███                          ▀                        ███    ███   
          \033[0m""")

    time.sleep(2)
    input("Press Enter to continue...")
    print()

def create_world():
    """
    Create the rooms and connect them.
    """
    room1 = DungeonRoom("\033[3mYou are in a dark, cold room.\033[0m")
    room2 = DungeonRoom("\033[3mThis room is filled with light and strange symbols on the walls.\033[0m")
    
    # Create an enemy in room1
    goblin = MeleeEnemy(name="Goblin", health=30, attack_power=10, range=1, speed=2)
    goblin_archer = RangedEnemy(name="Archer", health=25, attack_power=15, range=5, speed=1)
    
    room1.add_enemy(goblin)
    room2.add_enemy(goblin_archer)
    

    # Create items in rooms
    potion = HealingPotion(20)
    potion2 = HealingPotion(30)
    sword = Sword()  # Melee weapon
    bow = Bow()  # Ranged weapon
    
    room1.add_item(potion)
    room2.add_item(sword)
    room2.add_item(bow)
    room2.add_item(potion2)


    # Connect rooms
    room1.connect_room('north', room2)
    room2.connect_room('south', room1)

    return room1  # Start the game in room1

def goblin_action(player, current_room, distance_to_goblin, distance_to_goblin_archer):
    for enemy in current_room.enemies:
        if isinstance(enemy, RangedEnemy):
            distance = distance_to_goblin_archer
        else:
            distance = distance_to_goblin

        if distance <= enemy.range:
            enemy.attack(player, distance)
        else:
            move_distance = min(enemy.speed, distance - enemy.range)
            distance -= move_distance
            print(f"The {enemy.name} moves {move_distance} units closer to you!")
            if isinstance(enemy, RangedEnemy):
                distance_to_goblin_archer = distance
            else:
                distance_to_goblin = distance

    return distance_to_goblin, distance_to_goblin_archer

def begin_game():
        # Create a player
        player_name = input("Enter your character's name: ")
        player = Player(name=player_name, health=100, attack_power=10)

        current_room = create_world()

        distance_to_goblin = 5  # Initial distance to the goblin for testing (to be calculated during runtime based on positions)
        distance_to_goblin_archer = 3  # Initial distance to the goblin archer for testing (to be calculated during runtime based on positions)

        
        
        while player.is_alive():
            # Describe the current room
            print(current_room.describe())
            
            # List the enemies and items in the room
            print(current_room.list_enemies())
            print(current_room.list_items())
            
            # List the available exits
            print(current_room.get_exits())

            # Get player input
            action = input("\nWhat would you like to do? ").strip().lower()
            
            if action in current_room.exits:
                current_room = current_room.exits[action]
            elif action == "attack":
                if current_room.enemies:
                    enemy = current_room.enemies[0]
                    player_weapon = player.equipped_weapon
                    
                    weapon_range = player_weapon.range if player_weapon else 0

                    
                    if isinstance(enemy, RangedEnemy):
                        distance = distance_to_goblin_archer
                    else:
                        distance = distance_to_goblin

                    if distance <= weapon_range:
                        print(f"You attack the {enemy.name} with your {player_weapon.name if player_weapon else 'fists'}!")
                        enemy.take_damage(player.attack_power)
                        
                        if not enemy.is_alive():
                            current_room.enemies.remove(enemy)
                            print(f"You have defeated the {enemy.name}!")
                    else:
                        print(f"The {enemy.name} is too far for your {player_weapon.name if player_weapon else 'unarmed attack'}!")
                else:
                    print("There are no enemies to attack.")            
            
            elif action.startswith("use"):
                # Use an item (e.g., "use healing potion")
                item_name = action.split("use ")[-1]
                player.use_item(item_name)
            elif action.startswith("equip "):
                item_name = action[6:].lower()  # Extract the item name from the command
                item = next((item for item in player.inventory if item.name.lower() == item_name), None)
                if item:
                    if isinstance(item, (Sword, Bow)):  # Check if item is a weapon
                        player.equip_weapon(item)
                        print(f"You have equipped the {item.name}.")
                    else:
                        print(f"You can't equip the {item.name}.")
                else:
                    print(f"You don't have a {item_name} in your inventory.")

            elif action.startswith("pick up "):
                item_name = action[8:].lower()
                item = next((item for item in current_room.items if item.name.lower() == item_name), None)
                if item:
                    current_room.items.remove(item)
                    player.inventory.append(item)
                    print(f"You picked up {item.name}")
                else:
                    print(f"There is no {item_name} in this room.")

            elif action.startswith("equip "):
                item_name = action[6:].lower()  # Extract the item name from the command
                item = next((item for item in player.inventory if item.name.lower() == item_name), None)
                if item:
                    if isinstance(item, (Sword, Bow)):  # Check if item is a weapon
                        player.equip_weapon(item)
                        print(f"You have equipped the {item.name}.")
                    else:
                        print(f"You can't equip the {item.name}.")
                else:
                    print(f"You don't have a {item_name} in your inventory.")
            elif action == "quit":
                print("Exiting to main menu...")
                break
            else:
                print("Invalid action. Try moving in a direction, 'attack', 'pick up [item]', 'use [item]', or 'quit'.")

            
            if action.lower() != "north" and action.lower() != "south" and action.lower() != "east" and action.lower() != "west"  and action.lower():
                distance_to_goblin, distance_to_goblin_archer = goblin_action(player, current_room, distance_to_goblin, distance_to_goblin_archer)
            
            
                
           
            

def main():
    """
    Main game loop.    """
    show_title_screen()
    
    print("\033[1m\033[36mWelcome to the Dungeon Crawler Game!\033[0m")
    print()
    while True:
        print("--- Main Menu ---")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            begin_game()
        elif choice == "2":
            print("Thanks for playing! Goodbye.")
            break
    
    

if __name__ == "__main__":
    main()

