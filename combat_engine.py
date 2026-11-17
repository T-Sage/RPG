import random
from collections import Counter
import time

horiz_char = "="
vert_char = "|"

CRITICAL_ROLL = 20

SELECT_SCREEN_WIDTH = 48
SELECT_SCREEN_HEIGHT = 6
SLCT_MIDPOINT = SELECT_SCREEN_WIDTH // 2

# tile types for prototype_battle_grid
GROUND = "."
BARRIER = "#"

# information used by print_battle_grid 
GRID_WIDTH = 24 # must be an even number
GRID_HEIGHT = 16

MIDPOINT = GRID_WIDTH // 2

# information used by generate_starting_positions
ENEMY_COL = (MIDPOINT- 4) - 1 
PLAYER_COL = (MIDPOINT + 5) - 1
STARTFROM_ROW = 2
CHAR_SPACING = 2



class Tile:
    def __init__(self, char, nostep):
        self.char = char
        self.nostep = nostep


class Ground(Tile):
    def __init__(self):
        self.char = "."
        self.nostep = False

class Barrier(Tile):
    def __init__(self):
        self.char = "#"
        self.nostep = True


# takes party and enemies as arguments, and returns their position on a 24x11 battle grid
def generate_starting_positions(party, enemies):
    positions = {}

    for i, character in enumerate(party):
        row = STARTFROM_ROW + i * CHAR_SPACING
        positions[character] = (row, PLAYER_COL)

    for i, enemy in enumerate(enemies):
        row = STARTFROM_ROW + i * CHAR_SPACING
        positions[enemy] = (row, ENEMY_COL)

    return positions

# takes encounter as an argument and then both creates and prints the battle grid
def generate_battle_grid(encounter):
    battle_grid = [
            [
                Barrier() if (row == 0 or row == GRID_HEIGHT - 1 or col == 0 or col == GRID_WIDTH - 1)
                else Ground() for col in range(GRID_WIDTH)
            ] 
            for row in range(GRID_HEIGHT)
        ]
    return battle_grid

def update_combatants(encounter):
    for character in encounter.party + encounter.enemies:
        if character.alive == True:
            row, col = encounter.positions[character]
            encounter.battle_grid[row][col] = character

def print_battle_grid(encounter):
    for row in encounter.battle_grid:
        print(" "  + " ".join(tile.char for tile in row))

def print_selection_screen(encounter):
    select_grid = [[" " for i in range(SELECT_SCREEN_WIDTH)] for i in range(SELECT_SCREEN_HEIGHT)]
    
    # enemy information
    enemy_name1 = encounter.enemies[0].name
    enemy_name2 = encounter.enemies[1].name
    enemy_name3 = encounter.enemies[2].name
    enemy_name4 = encounter.enemies[3].name

    select_grid[0][1:1 + len(enemy_name1)] = list(enemy_name1)
    select_grid[1][1:1 + len(enemy_name2)] = list(enemy_name2)
    select_grid[2][1:1 + len(enemy_name3)] = list(enemy_name3)
    select_grid[3][1:1 + len(enemy_name4)] = list(enemy_name4)

    e1_hp_str = "hp: " + str(encounter.enemies[0].hp)
    e2_hp_str = "hp: " + str(encounter.enemies[1].hp)
    e3_hp_str = "hp: " + str(encounter.enemies[2].hp)
    e4_hp_str = "hp: " + str(encounter.enemies[3].hp)

    enemy_hp_offset = SLCT_MIDPOINT - 9
    select_grid[0][enemy_hp_offset:enemy_hp_offset + len(e1_hp_str)] = list(e1_hp_str)
    select_grid[1][enemy_hp_offset:enemy_hp_offset + len(e2_hp_str)] = list(e2_hp_str)
    select_grid[2][enemy_hp_offset:enemy_hp_offset + len(e3_hp_str)] = list(e3_hp_str)
    select_grid[3][enemy_hp_offset:enemy_hp_offset + len(e4_hp_str)] = list(e4_hp_str)

    # ally information
    ally_name1 = encounter.party[0].name
    ally_name2 = encounter.party[1].name
    ally_name3 = encounter.party[2].name
    ally_name4 = encounter.party[3].name

    rightside_offset = SLCT_MIDPOINT + 2
    select_grid[0][rightside_offset:rightside_offset + len(ally_name1)] = list(ally_name1)
    select_grid[1][rightside_offset:rightside_offset + len(ally_name2)] = list(ally_name2)
    select_grid[2][rightside_offset:rightside_offset + len(ally_name3)] = list(ally_name3)
    select_grid[3][rightside_offset:rightside_offset + len(ally_name4)] = list(ally_name4)

    p1_hp_str = "hp: " + str(encounter.party[0].hp)
    p2_hp_str = "hp: " + str(encounter.party[1].hp)
    p3_hp_str = "hp: " + str(encounter.party[2].hp)
    p4_hp_str = "hp: " + str(encounter.party[3].hp)

    party_hp_offset = SLCT_MIDPOINT + 15
    select_grid[0][party_hp_offset:party_hp_offset + len(p1_hp_str)] = list(p1_hp_str)
    select_grid[1][party_hp_offset:party_hp_offset + len(p2_hp_str)] = list(p2_hp_str)
    select_grid[2][party_hp_offset:party_hp_offset + len(p3_hp_str)] = list(p3_hp_str)
    select_grid[3][party_hp_offset:party_hp_offset + len(p4_hp_str)] = list(p4_hp_str)

    # separator line
    select_grid[0][SLCT_MIDPOINT] = "|"
    select_grid[1][SLCT_MIDPOINT] = "|"
    select_grid[2][SLCT_MIDPOINT] = "|"
    select_grid[3][SLCT_MIDPOINT] = "|"
    select_grid[4][SLCT_MIDPOINT] = "|"
    select_grid[5][SLCT_MIDPOINT] = "|"

    border = " " + horiz_char * SELECT_SCREEN_WIDTH
    print(border)

    for row in select_grid:
        print("|" + "".join(row) + "|")

    print(border)


# char_select takes encounter as an argument, and returns a selected character
# user selects a character they'd like to make an action with using an input string
def char_select(encounter):
    # take input from user
    while True:
        char_selection = input("Select character to make an action:\n>").strip().casefold()
        conf_char_selection = None
        
        # if the input matches a character name in the party, lock in selection and proceed
        for character in encounter.party:
            if character.name.casefold() == char_selection:
                conf_char_selection = character
                break

        # error handling for outlier situations
        if conf_char_selection is None:
            print("Character not found.")
            continue 
        if conf_char_selection.alive == False:
            print(f"{conf_char_selection.name} is dead!")
            continue
        if conf_char_selection.turn == False:
            print(f"{conf_char_selection.name} can't make an action twice in one round!")
            continue

        break

    return conf_char_selection

# enemy_select takes encounter as an argument, and returns a selected enemy
# the user selects an enemy to attack via user input
# the user must input an enemy name and a number if there are any duplicates
def enemy_select(encounter):
    # take input from user
    while True:
        enemy_selection = input("Select enemy to attack:\n>").strip().casefold()
        conf_enemy_selection = None

        # make a list of names that have a "'name' + #" format
        matches = [
            enemy for enemy in encounter.enemies
            if enemy.name.casefold().startswith(enemy_selection + " ")
        ]

        # if input matches an enemy in the list, proceed to attack phase
        for enemy in encounter.enemies:
            if enemy.name.casefold() == enemy_selection:
                conf_enemy_selection = enemy
                break

        # special case for when user inputs the name of an enemy with duplicates but not the number
        if conf_enemy_selection is None and matches:
            number = input(f"Which {enemy_selection}? Type a number:\n>").strip()

            # check if input is actually a number
            if not number.isdigit():
                print("Enter a valid number.")
                continue

            enemy_selection = f"{enemy_selection} {number}"

            # lock in corrected input and proceed to attack phase
            for enemy in encounter.enemies:
                if enemy.name.casefold() == enemy_selection:
                    conf_enemy_selection = enemy
                    break

        # case for mis-input
        if conf_enemy_selection is None:
            print("Enemy not found.")
            continue

        # case to handle dead enemy being targeted
        if conf_enemy_selection.alive == False:
            print(f"{conf_enemy_selection.name} is dead!")
            continue

        break

    return conf_enemy_selectiona


# TODO: make this function decriment a the movement speed of a character by 5 for every move,
# and disallow characters with an available movement speed of 0 from moving
# make it so it's not possible to occupy the same space as another character
# make it so it's not possible to melee attack an enemy unless you're adjacent to them
# solve map barriers. currently a character can cross the top of the map and appear at the bottom
# like pacman!
def move(selected_char, encounter):
    # characters positions are saved "upside-down" i.e.: (y, x)
    # for example figter's default position is (2, 16) zero indexed!
    # meaning the fighter's initial location is 3 down from the top, and 17 to the right 
    print(selected_char.name + "'s position: " + str(encounter.positions[selected_char]))
    
    pos_tuple = list(encounter.positions[selected_char])

    while True:
        mv_selection = input("Input up, down, left, right to move\n>").strip().lower()

        if mv_selection == "up" or "down" or "left" or "right":
            if mv_selection == "up":
                if encounter.battle_grid[pos_tuple[0] - 1][pos_tuple[1]].nostep == False:
                    pos_tuple[0] -= 1
                    encounter.positions[selected_char] = pos_tuple

                    update_combatants(encounter)
                else:
                    print("no")
                    continue

                    #battle_grid

            if mv_selection == "down":
                pos_tuple[0] += 1
                encounter.positions[selected_char] = pos_tuple

            if mv_selection == "left":
                pos_tuple[1] -= 1
                encounter.positions[selected_char] = pos_tuple

            if mv_selection == "right":
                pos_tuple[1] += 1
                encounter.positions[selected_char] = pos_tuple
            break

        else:
            print("Invalid input")
            continue

    print_battle_grid(encounter)
    print_selection_screen(encounter)
    return 0

def action_select(selected_char, encounter):
    print(f"" + selected_char.name + "'s available actions:")
    print("Attack")
    print("Defend")
    print("Move")
    #print("Return") # return option should be made available in the future.

    while True:
        # take input from user
        selection = input(f"What will " + selected_char.name + " do?\n>").strip().casefold()

        # attack selection case
        if selection == "attack":
            # prompt user for the target of their attack
            target = enemy_select(encounter)
            # run attack method with user selections
            attack(selected_char, target)
            break

        # defend selection case
        if selection == "defend":
            defend(selected_char)
            print(f"{selected_char.name} is defending!")
            break

        # move selection case
        if selection == "move":
            move(selected_char, encounter)
            break

        else:
            print("Selection not recognized")
            continue

def defend(character):
    character.defend = True
    character.turn = False


# attack takes two characters as input, one attacker and one defender. first, the function sets 
# the attacker's turn to false, then the function rolls a random number 1-20.
# if the roll is 20, the attacker critically hits. else if the roll is under 20 
# but still exceeds defender's ac, the attack hits. else the roll is less than the defender's ac
# and the attacker misses
def attack(attacker, defender):
    attacker.turn = False
    atk_roll = random.randint(1, 20)

    # hack-ish system for disadvantage. strongly considering adding seperate methods to handle d20 rolls and 
    # d20 rolls with disadvantage to keep the attack method a little cleaner
    if defender.defend == True:
        print(f"{attacker.name} has disadvantage!")
        atk_roll2 = random.randint(1, 20)

        if atk_roll2 < atk_roll:
            atk_roll = atk_roll2

    if atk_roll == CRITICAL_ROLL:
        damage_roll1 = random.randint(1, attacker.damage_die)
        damage_roll2 = random.randint(1, attacker.damage_die)
        final_damage = damage_roll1 + damage_roll2 + attacker.damage_bonus

        defender.hp -= final_damage
        print(f"{attacker.name} rolled a {atk_roll}! Critical hit! Damage: {damage_roll1} + {damage_roll2} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")
    
    elif atk_roll + attacker.atk_bonus >= defender.ac:
        damage = random.randint(1, attacker.damage_die)
        final_damage = damage + attacker.damage_bonus
        defender.hp -= final_damage
        print(f"{attacker.name} rolled a {atk_roll} + {attacker.atk_bonus}! Hit! Damage: {damage} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")

    else:
        print(f"{attacker.name} rolled a {atk_roll}! Miss!")


#enemy_round iterates through each enemy in the encounter enemy list, decides a random target for them to attack, and then has the enemy attack that target.
#After all enemies attack, the round restarts, and the .turn property of all characters and enemies are reset to true.
def enemy_round(encounter):
    print(f"The enemies take their turn.")
    time.sleep(1)
    #every enemy is going to make an attack
    for enemy in encounter.enemies:
        #if enemy is alive and has not gone
        if enemy.alive == True and enemy.turn == True:
            # create a list of the valid targets by their index in the party list
            valid_targets = []
            # Check every party member in the list, if they are alive, add them to the valid target list
            # valid_targets is a list of the indexes of valid targets in the party list. 
            for index, character in enumerate(encounter.party):
                if character.alive == True:
                    valid_targets.append(index)
            # Target is assigned an index from the party member list, randomly selected from the valid targets.
            target = valid_targets[random.randint(0,len(valid_targets)-1)]
            # encounter.party[target] is the party member being attacked
            print(f"{enemy.name} is attacking {encounter.party[target].name}")
            time.sleep(1)
            attack(enemy, encounter.party[target])
            time.sleep(1)
    # after all enemy attacks happen, reset all .turn properties, as a new round is occuring
    for character in encounter.party:
        character.turn = True
    for enemy in encounter.enemies:
        enemy.turn = True
    print(f"Enemy turn over.")
    time.sleep(1)


# enumerate_enemies adds a space followed by an integer to the name string of an enemy
# for each duplicate enemy in the list of enemies of an encounter, starting from 1
def enumerate_enemies(enemies):
    counts = Counter(type(enemy).__name__ for enemy in enemies)
    seen = Counter()

    for enemy in enemies:
        enemy_type = type(enemy).__name__
        seen[enemy_type] += 1

        if counts[enemy_type] == 1:
            enemy.name = enemy_type
        else:
            enemy.name = f"{enemy_type} {seen[enemy_type]}"

class Encounter:
    def __init__(self, party, enemies, positions, battle_grid):
        self.party = party
        self.enemies = enemies
        self.positions = positions
        self.battle_grid = battle_grid
        self.win = False
        self.complete = False

def test_encounter():
    party = [Fighter(), Wizard(), Rogue(), Cleric()]
    enemies = [Bandit(), Bandit(), Bandit(), Bandit()]
    positions = generate_starting_positions(party, enemies)

    return Encounter(party, enemies, positions)

class Bandit:
    def __init__(self):
        self.name = "Bandit"
        self.ac = 12
        self.max_hp = 11
        self.hp = self.max_hp
        self.atk_bonus = 3
        self.damage_die = 6
        self.damage_bonus = 1
        self.alive = True
        self.turn = True
        self.char = "B"
        self.defend = False

class Fighter:
    def __init__(self):
        self.name = "Fighter"
        self.ac = 16
        self.max_hp = 13
        self.hp = self.max_hp
        self.atk_bonus = 5
        self.damage_die = 8
        self.damage_bonus = 5
        self.alive = True
        self.turn = True
        self.char = "F"
        self.defend = False

class Rogue:
    def __init__(self):
        self.name = "Rogue"
        self.ac = 14
        self.max_hp = 10
        self.hp = self.max_hp
        self.atk_bonus = 5
        self.damage_die = 6
        self.damage_bonus = 5
        self.alive = True
        self.turn = True
        self.char = "R"
        self.defend = False

class Wizard:
    def __init__(self):
        self.name = "Wizard"
        self.ac = 12
        self.max_hp = 8
        self.hp = self.max_hp
        self.atk_bonus = 2
        self.damage_die = 6
        self.damage_bonus = 0
        self.alive = True
        self.turn = True
        self.char = "W"
        self.defend = False

class Cleric:
    def __init__(self):
        self.name = "Cleric"
        self.ac = 16
        self.max_hp = 10
        self.hp = self.max_hp
        self.atk_bonus = 4
        self.damage_die = 6
        self.damage_bonus = 2
        self.alive = True
        self.turn = True
        self.char = "C"
        self.defend = False

class Weapon:
    def __init__(self, name, bonus_atk, bonus_dmg_die, bonus_dmg):
        self.name = name
        self.bonus_atk = bonus_atk
        self.bonus_dmg_die = bonus_dmg_die
        self.bonus_dmg = bonus_dmg

#Example weapon subclasses
class IronSword(Weapon):
    def __init__(self):
        super().__init__("Iron Sword", 0, 10, 5)

class WoodenStaff(Weapon):
    def __init__(self):
        super().__init__("Wooden Staff", 0, 10, 2)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 0, 10, 4)
        
# Function to equip a weapon to any of your teammate's character objects
def equip_weapon(character, weapon):
    character.atk_bonus += weapon.bonus_atk
    character.damage_die = weapon.bonus_dmg_die
    character.damage_bonus += weapon.bonus_dmg
    print(f"{character.name} equipped the {weapon.name}!")

#takes in an encounter object
def combat(encounter):
        # load encounter and enumerate duplicate enemies
    enumerate_enemies(encounter.enemies)
    encounter.positions = generate_starting_positions(encounter.party, encounter.enemies)
    encounter.battle_grid = generate_battle_grid(encounter)
    update_combatants(encounter)
    
    # core game loop
    while True:

        # check if the encounter is complete. If it is, break
        if encounter.complete == True:
            break

        # print the screens
        print(encounter.battle_grid[0][0].nostep)
        print_battle_grid(encounter)
        print_selection_screen(encounter)

        # attack and defend loop. at any point in the loop if all enemies are dead,
        # set encounter to complete and break
        while True:
            if all(enemies.alive == False for enemies in encounter.enemies):
                encounter.win = True
                encounter.complete = True
                break
            # select a character, and then an action for the selected character
            selected_char = char_select(encounter)
            action_select(selected_char, encounter)

            # if all party members have taken their turn, proceed to enemy round
            if all(characters.turn == False or characters.alive == False for characters in encounter.party):
                break
        # win condition check
        if all(enemies.alive == False for enemies in encounter.enemies):
            encounter.win = True
            encounter.complete = True
            break
        # enemy round
        enemy_round(encounter)

        for character in encounter.party:
            character.turn = True
            character.defend = False

    if encounter.win == True:
        print("You win!")
    else:
        print("You Lose.")

def main():
    # load encounter and enumerate duplicate enemies
    encounter = test_encounter()
    enumerate_enemies(encounter.enemies)
    
    # core game loop
    while True:

        # check if the encounter is complete. If it is, break
        if encounter.complete == True:
            break

        # print the screens
        print(encounter.battle_grid[0][0].nostep)
        print_battle_grid(encounter)
        print_selection_screen(encounter)

        # attack and defend loop. at any point in the loop if all enemies are dead,
        # set encounter to complete and break
        while True:
            if all(enemies.alive == False for enemies in encounter.enemies):
                encounter.win = True
                encounter.complete = True
                break

            # select a character, and then an action for the selected character
            selected_char = char_select(encounter)
            action_select(selected_char, encounter)

            # if all party members have taken their turn, proceed to enemy round
            if all(characters.turn == False or characters.alive == False for characters in encounter.party):
                break

        # win condition check
        if all(enemies.alive == False for enemies in encounter.enemies):
            encounter.win = True
            encounter.complete = True
            break

        # enemy round
        enemy_round(encounter)

        # reset party member turns for next player round and defend flag
        for character in encounter.party:
            character.turn = True
            character.defend = False

    if encounter.win == True:
        print("You win!")
    else:
        print("You Lose.")

if __name__ == "__main__":
    main()
