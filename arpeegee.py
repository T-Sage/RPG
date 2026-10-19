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

def print_battle_screen(encounter):
    # Initialize blank battle grid
    battle_grid = [[" " for _ in range(BATTLE_SCREEN_WIDTH)] for _ in range(BATTLE_SCREEN_HEIGHT)]

    # Draw active party members on the right side
    party_col = 40
    for idx, member in enumerate(encounter.party):
        if member.hp > 0:
            row = 2 + (idx * 2)  # Rows 2, 4, 6, 8
            if row < BATTLE_SCREEN_HEIGHT:
                battle_grid[row][party_col] = member.char

    # Draw active enemies on the left side
    enemy_col = 20
    for idx, enemy in enumerate(encounter.enemies):
        if enemy.hp > 0:
            row = 2 + (idx * 2)  # Rows 2, 4, 6, 8
            if row < BATTLE_SCREEN_HEIGHT:
                battle_grid[row][enemy_col] = enemy.char

    # Render borders and rows to terminal
    border = " " + horiz_char * (BATTLE_SCREEN_WIDTH + 1)
    print(border)

    for row in battle_grid:
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
        print(f"Critical hit! Damage: {damage_roll1} + {damage_roll2} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")
    
    elif atk_roll >= defender.ac:
        damage = random.randint(1, attacker.damage_die)
        final_damage = damage + attacker.damage_bonus
        defender.hp -= final_damage
        print(f"Hit! Damage: {damage} + {attacker.damage_bonus} = {final_damage}")
        if defender.hp <= 0:
            defender.alive = False
            print(f"{defender.name} is dead!")

    else:
        print("Miss!")

#def enemy_round(encounter):



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
        self.damange_bonus = 1
        self.alive = True
        self.turn = True
        self.char = "B"

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

class Rogue:
    def __init__(self):
        self.name = "Rogue"
        self.ac = 14
        self.max_hp = 10
        self.hp = self.max_hp
        self.atk_bonus = 5
        self.damage_die = 6
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
        self.char = "W"

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
