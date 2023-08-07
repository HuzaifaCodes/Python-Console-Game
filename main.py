from character import Character #importing Chracter class from character.py
import time #importing time module for delay
#ASCII code for images
warrior_ascii = r"""
    / \__
   (    @\___
   /         O
  /   (_____/
 /_____/
"""

defender_ascii = r"""
  _==/            i     i           \==_
 /XX/             |\___/|            \XX\
/XXXX\            |XXXXX|            /XXXX\
|XXXXX\_         _XXXXXXX_         _2/XXXXX|
\XXXXXX|       |XXXXXXXXX|       |XXXXXX/
 \XXXXX\_     _/XXXXXXXXX\_     _/XXXXX/
  \XXXXX|     |XXXXXXXXXXX|     |XXXXX/
   \XXXXX\_   _/XXXXXXXXXXX\_   _/XXXXX/
    \XXXXX|  |XXXXXXXXXXXXX|  |XXXXX/
     \XXXXX\/XXXXXXXXXXXXXXX\/XXXXX/
      \XXXXXXX/  |  |  \XXXXXXX/
       |XXXXXXXXXXXXXXXXXXXXXXX|
       |XXXXXXXXXXXXXXXXXXXXXXX|
       |XXXXXXXXXXXXXXXXXXXXXXX|
        \XXXXXXX/    \XXXXXXX/
         |XXXXX/      \XXXXX|
         |XXXXX|      |XXXXX|
         |XXXXX|      |XXXXX|
         |XXXXX|      |XXXXX|
          \XXXX/        \XXXX/
"""

enemy1_ascii = r"""
      \|||/
      (o o)
  ooO--(_)--Ooo-
"""

enemy2_ascii = r"""
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/
"""
# Create character objects from character class
warrior = Character("Warrior", 10, 5, 1, 6, 60, warrior_ascii, "Warrior") 
defender = Character("Defender", 10, 7, 2, 2, 40, defender_ascii, "Defender")

# Player character selection
def character_selection(character_options):
    print("Choose Player:")
    for i, character in enumerate(character_options):
        print(f"{i+1}: {character.name}")

    chosen_index = int(input("Enter the number of the character you want to choose: "))
    if 1 <= chosen_index <= len(character_options):
        player = character_options[chosen_index-1]
        print(f"You have chosen {player.name}!")
        print(f"Magic Points (MP): {player.mp}\nJob Class: {player.job_class}")
        if player.job_class == "Defender":
            print("Special Skills(Heal/Thunder Miracle)")
        elif player.job_class == "Warrior":
            print("Special skills (Angel Hand/Overtake/Helping Hand)")    
        return player
    else:
        print("Invalid choice. Please select a valid character.")

# Select target from available characters
def select_target(characters, player):
    valid_targets = [char for char in characters if char != player and char.hp > 0]
    print("Available targets:")
    for i, target in enumerate(valid_targets):
        print(f"{i+1}. {target.name} (HP: {target.hp}/{target.max_hp})")
    target_index = int(input("Select a target: ")) - 1
    return valid_targets[target_index]

# Print character's HP and ASCII art
def print_character_info(character):
    print(f"{character.name} (HP: {character.hp}/{character.max_hp})")
    print(character.image)
    print(f"Attack Points (AP): {character.ap}\nDefense Points (DP): {character.dp}\nSpeed Points (SP): {character.sp}\n Magic points: {character.mp}\n")
        

# Combat scenario
def combat_scenario():
    character_options = [warrior, defender]
    player = character_selection(character_options)

    enemy1 = Character("Enemy 1", 10, 3, 2, 3, 0, enemy1_ascii, "EnemyType1")
    enemy2 = Character("Enemy 2", 10, 4, 3, 5, 0, enemy2_ascii, "EnemyType2")

    characters = [player, enemy1, enemy2]

    while True:
        if all(enemy.hp == 0 for enemy in [enemy1, enemy2]):
            print("You defeated all enemies! You win!")
            break

        if player.hp == 0:
            print("Your character has been defeated. You lose.")
            break

        for character in characters:
            if character.hp > 0:
                print(f"{character.name}'s turn:")
                time.sleep(1)  # Add delay for turn transition

                if character == player:
                    print_character_info(player)
                    action = input("Choose an action (Attack/Defend/Skill): ")
                    if action == "Attack":
                        target = select_target(characters, player)
                        player.attack(target)
                        print(f"You attacked {target.name}!")
                        print_character_info(target)
                    elif action == "Defend":
                        player.defend()
                        print("You are defending!")
                    elif action == "Skill":
                        if player.job_class == "Defender":
                            skill = input("Choose a skill (Heal/Thunder Miracle):")
                        elif player.job_class == "Warrior":
                            skill = input("Choose a skill (Angel Hand/Overtake/Helping Hand:")
                        target = select_target(characters, player)
                        player.use_skill(skill, target)
                        print(f"You used {skill} on {target.name}!")
                        print_character_info(target)
                    else:
                        print("Invalid action. Try again.")
                else:
                    target = player
                    character.attack(target)
                    print(f"{character.name} attacked you!")
                    print_character_info(character)

# Start the combat scenario
combat_scenario()

