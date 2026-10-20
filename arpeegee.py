import random
from collections import Counter

BATTLE_SCREEN_WIDTH = 60
BATTLE_SCREEN_HEIGHT = 10
horiz_char = "="
vert_char = "|"
SELECT_SCREEN_WIDTH = 60
SELECT_SCREEN_HEIGHT = 5
CRITICAL_ROLL = 20

def print_battle_screen(encounter):
    battle_grid = [[" " for i in range(BATTLE_SCREEN_WIDTH)] for i in range(BATTLE_SCREEN_HEIGHT)]

    # team positions on grid
    battle_grid[2][40] = "F"
    battle_grid[4][40] = "W"
    battle_grid[6][40] = "R"
    battle_grid[8][40] = "C"

    # enemy positions on grid
    battle_grid[2][20] = "B"
    battle_grid[4][20] = "B" # 420 :^)
    battle_grid[6][20] = "B"
    battle_grid[8][20] = "B"

    border = " " + horiz_char * (BATTLE_SCREEN_WIDTH + 1)
    print(border)

    for row in battle_grid:
        print("|" + "".join(row) + "|")
    
    print(border)

def print_selection_screen(encounter):
   select_grid = [[" " for i in range(SELECT_SCREEN_WIDTH)] for i in range(SELECT_SCREEN_HEIGHT)]

   # enemy information
   enemy_name = "Bandit"
   num_enemies = "x4"

   select_grid[0][1:1 + len(enemy_name)] = list(enemy_name)
   select_grid[0][27:27 + len(num_enemies)] = list(num_enemies)

   # ally information
   ally_name1 = "Fighter"
   ally_name2 = "Wizard"
   ally_name3 = "Rogue"
   ally_name4 = "Cleric"

   select_grid[0][32:32 + len(ally_name1)] = list(ally_name1)
   select_grid[1][32:32 + len(ally_name2)] = list(ally_name2)
   select_grid[2][32:32 + len(ally_name3)] = list(ally_name3)
   select_grid[3][32:32 + len(ally_name4)] = list(ally_name4)
   
   # separator line
   select_grid[0][30] = "|"
   select_grid[1][30] = "|"
   select_grid[2][30] = "|"
   select_grid[3][30] = "|"
   select_grid[4][30] = "|"

   border = " " + horiz_char * (SELECT_SCREEN_WIDTH + 1)
   print(border)

   for row in select_grid:
       print("|" + "".join(row) + "|")

   print(border)

# char_select takes user input for the character they want to attack with and the enemy they want to attack
# once input is confirmed and potential misinputs are resolved, char_select sends its selections to attack()
def char_select(encounter):
    
    # take input from user
    while True:
        char_selection = input("Select character to make an attack:\n>").strip().casefold()
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
            print(f"{conf_char_selection.name} can't attack twice in one round!")
            continue
            
        break

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

        if conf_enemy_selection is None:
            print("Enemy not found.")   
            continue

        if conf_enemy_selection.alive == False:
            print(f"{conf_enemy_selection.name} is dead!")
            continue
        break

    attack(conf_char_selection, conf_enemy_selection)


# attack takes two characters as input, one attacker and one defender. first, the function sets the attacker's turn to false, then the function rolls a random number 1-20.
# if the roll is 20, the attacker critically hits. else if the roll is under 20 but still exceeds defender's ac, the attack hits. else the roll is less than the defender's ac, and the attacker misses
def attack(attacker, defender):
    attacker.turn = False
    atk_roll = random.randint(1, 20)

    if atk_roll == CRITICAL_ROLL:
        damage_roll1 = random.randint(1, attacker.damage_die)
        damage_roll2 = random.randint(1, attacker.damage_die)
        final_damage = damage_roll1 + damage_roll2 + attacker.damage_bonus
        
        defender.hp -= final_damage
        # enemy health print statement is for debug, it is intended to be removed
        print(f"{defender.name} curr hp = {defender.hp}")
        print(f"{attacker.name} rolled a {atk_roll}! Critical hit! Damage: {damage_roll1} + {damage_roll2} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")
    
    elif atk_roll + attacker.atk_bonus >= defender.ac:
        damage = random.randint(1, attacker.damage_die)
        final_damage = damage + attacker.damage_bonus
        defender.hp -= final_damage
        print(f"{attacker.name} rolled a {atk_roll} + {attacker.atk_bonus}! Hit! Damage: {damage} + {attacker.damage_bonus} = {final_damage}")
        # enemy health print statement is for debug purposes only, and is intended to be removed in later iterations
        print(f"{defender.name} curr hp = {defender.hp}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")

    else:
        print(f"{attacker.name} rolled a {atk_roll}! Miss!")


#enemy_round iterates through each enemy in the encounter enemy list, decides a random target for them to attack, and then has the enemy attack that target.
#After all enemies attack, the round restarts, and the .turn property of all characters and enemies are reset to true.
def enemy_round(encounter):
    #every enemy is going to make an attack
    for enemy in encounter.enemies:
        #if enemy is alive and has not gone
        if enemy.alive == True and enemy.turn == True:
            #create a list of the valid targets by their index in the party list
            valid_targets = []
            #Check every party member in the list, if they are alive, add them to the valid target list. valid_targets is a list of the indexes of valid targets in the party list. 
            for index, character in enumerate(encounter.party):
                if character.alive == True:
                    valid_targets.append(index)
            #Target is assigned an index from the party member list, randomly selected from the valid targets.
            target = valid_targets[random.randint(0,len(valid_targets)-1)]
            #encounter.party[target] is the party member being attacked
            print(f"{enemy.name} is attacking {encounter.party[target].name}")
            attack(enemy, encounter.party[target])
    #after all enemy attacks happen, reset all .turn properties, as a new round is occuring
    for character in encounter.party:
        character.turn = True
    for enemy in encounter.enemies:
        enemy.turn = True


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
    #delete when not needed for debug
    for enemy in enemies:
        print(enemy.name)

class Encounter:
    def __init__(self, party, enemies):
        self.party = party
        self.enemies = enemies
        self.complete = False
        
def test_encounter():
    return Encounter (
            party = [Fighter(), Wizard(), Rogue(), Cleric()],
            enemies = [Bandit(), Bandit(), Bandit(), Bandit()]
        )

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


def main():
    # load encounter and enumerate duplicate enemies
    encounter = test_encounter()
    enumerate_enemies(encounter.enemies)
    
    # core game loop
    while True:

        # check if the encounter is complete, if it is break
        if encounter.complete == True:
            break

        # print the screens
        # NOTE todo: finish making screens so they reflect gamestate data
        print_battle_screen(encounter)
        print_selection_screen(encounter)

        # attack and defend loop. at any point in the loop if all enemies are dead,
        # set encounter to complete and break
        while True:
            if all(enemies.alive == False for enemies in encounter.enemies):
                encounter.complete = True
                break
            # select a character to attack
            char_select(encounter)
            # if all party members have taken their turn, proceed to enemy round
            if all(characters.turn == False for characters in encounter.party):
                break
        # win condition check
        if all(enemies.alive == False for enemies in encounter.enemies):
            encounter.complete = True
            break
        # enemy round
        enemy_round(encounter)

        # reset party member turns for next player round
        all(characters.turn == True for characters in encounter.party)

    print("You win!")

if __name__ == "__main__":
    main()
