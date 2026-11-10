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