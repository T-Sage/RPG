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

def char_select(encounter):
    
    while True:
        char_selection = input("Select character to make an attack: ").strip().casefold()
        conf_char_selection = None
            
        for character in encounter.party:
            if character.name.casefold() == char_selection:
                conf_char_selection = character
                break
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
    
    while True: #todo: implement enemy selection from duplicates
        enemy_selection = input("Select enemy to attack: ").strip().casefold()
        conf_enemy_selection = None

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
        enemy_enumerator(encounter)    
        break

    attack(conf_char_selection, conf_enemy_selection)

def enemy_enumerator(encounter):
    # current work in progress 
    counts = Counter(enemy.name.casefold() for enemy in encounter.enemies)
    enemy_choices = {}
    name_counts = {}

    for enemy in encounter.enemies:
        key = enemy.name.casefold()

        if counts[key] > 1:
            name_counts[key] = name_counts.get(key, 0) + 1
            label = f"{enemy.name} {name_counts[key]}"
        else:
            label = enemy.name

        enemy_choices[label.casefold()] = enemy

    return enemy_choices

def attack(attacker, defender):
    attacker.turn = False
    atk_roll = random.randint(1, 20)

    if atk_roll == CRITICAL_ROLL:
        damage_roll1 = random.randint(1, attacker.damage_die)
        damage_roll2 = random.randint(1, attacker.damage_die)
        final_damage = damage_roll1 + damage_roll2 + attacker.damage_bonus
        
        defender.hp -= final_damage
        print(f"{atk_roll} Critical hit! Damage: {damage_roll1} + {damage_roll2} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")
    
    elif atk_roll >= defender.ac:
        damage = random.randint(1, attacker.damage_die)
        final_damage = damage + attacker.damage_bonus
        defender.hp -= final_damage
        print(f"{atk_roll} Hit! Damage: {damage} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")

    else:
        print(f"{atk_roll} Miss!")
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

            
            






class Encounter:
    def __init__(self, party, enemies):
        self.party = party
        self.enemies = enemies
        
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
    encounter = test_encounter()
    while True:
        print_battle_screen(encounter)
        print_selection_screen(encounter)
        while True:
            char_select(encounter)
            if all(characters.turn == False for characters in encounter.party):
                break
        enemy_round(encounter)


if __name__ == "__main__":
    main()
