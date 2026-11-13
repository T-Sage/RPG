import math

# --- HELPER DERIVATION FUNCTIONS ---

def calc_mod(score: int) -> int:
    """Calculates ability modifier: floor((score - 10) / 2)[cite: 1, 3]"""
    return math.floor((score - 10) / 2)

def calc_pb(level: int) -> int:
    """Calculates proficiency bonus based on character level[cite: 4]"""
    return math.ceil(1 + (level / 4))


class Bandit:
    def __init__(self, name: str = "Bandit", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 11, "DEX": 12, "CON": 12, "INT": 10, "WIS": 10, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 12
        self.max_hp = max(1, 9 + (2 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Bandit_Captain:
    def __init__(self, name: str = "Bandit Captain", level: int = 2, scores: dict = None):
        if scores is None:
            scores = {"STR": 15, "DEX": 16, "CON": 14, "INT": 14, "WIS": 11, "CHA": 14}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 15
        self.max_hp = max(1, 36 + (8 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Bandit_Deceiver:
    def __init__(self, name: str = "Bandit Deceiver", level: int = 7, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 16, "CON": 14, "INT": 17, "WIS": 12, "CHA": 16}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 16
        self.max_hp = max(1, 90 + (20 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 4
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Bandit_Crime_Lord:
    def __init__(self, name: str = "Bandit Crime Lord", level: int = 11, scores: dict = None):
        if scores is None:
            scores = {"STR": 10, "DEX": 20, "CON": 14, "INT": 18, "WIS": 14, "CHA": 15}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 17
        self.max_hp = max(1, 117 + (26 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Ghoul:
    def __init__(self, name: str = "Ghoul", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 13, "DEX": 15, "CON": 10, "INT": 7, "WIS": 10, "CHA": 6}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 12
        self.max_hp = max(1, 22 + (5 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Lacedon_Ghoul:
    def __init__(self, name: str = "Lacedon Ghoul", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 13, "DEX": 15, "CON": 10, "INT": 7, "WIS": 10, "CHA": 6}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 12
        self.max_hp = max(1, 22 + (5 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Goblin_Minion:
    def __init__(self, name: str = "Goblin Minion", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 15, "CON": 10, "INT": 10, "WIS": 8, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 12
        self.max_hp = max(1, 7 + (2 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 4
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Goblin_Warrior:
    def __init__(self, name: str = "Goblin Warrior", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 15, "CON": 10, "INT": 10, "WIS": 8, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 15
        self.max_hp = max(1, 10 + (3 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Goblin_Boss:
    def __init__(self, name: str = "Goblin Boss", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 10, "DEX": 15, "CON": 10, "INT": 10, "WIS": 8, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 17
        self.max_hp = max(1, 21 + (6 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Goblin_Hexer:
    def __init__(self, name: str = "Goblin Hexer", level: int = 3, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 16, "CON": 12, "INT": 16, "WIS": 10, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 13
        self.max_hp = max(1, 35 + (10 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + int_mod
        self.damage_die = 8
        self.damage_bonus = int_mod
        self.alive = True
        self.turn = True


class Kobold_Warrior:
    def __init__(self, name: str = "Kobold Warrior", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 7, "DEX": 15, "CON": 9, "INT": 8, "WIS": 7, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 14
        self.max_hp = max(1, 10 + (3 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 4
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Winged_Kobold:
    def __init__(self, name: str = "Winged Kobold", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 7, "DEX": 16, "CON": 9, "INT": 8, "WIS": 7, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 15
        self.max_hp = max(1, 14 + (4 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Skeleton:
    def __init__(self, name: str = "Skeleton", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 10, "DEX": 16, "CON": 15, "INT": 6, "WIS": 8, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 14
        self.max_hp = max(1, 9 + (2 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Warhorse_Skeleton:
    def __init__(self, name: str = "Warhorse Skeleton", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 18, "DEX": 12, "CON": 15, "INT": 2, "WIS": 8, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 13
        self.max_hp = max(1, 16 + (3 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 6
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Minotaur_Skeleton:
    def __init__(self, name: str = "Minotaur Skeleton", level: int = 2, scores: dict = None):
        if scores is None:
            scores = {"STR": 18, "DEX": 11, "CON": 15, "INT": 6, "WIS": 8, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 12
        self.max_hp = max(1, 33 + (6 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 10
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Flaming_Skeleton:
    def __init__(self, name: str = "Flaming Skeleton", level: int = 3, scores: dict = None):
        if scores is None:
            scores = {"STR": 10, "DEX": 14, "CON": 15, "INT": 10, "WIS": 15, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 15
        self.max_hp = max(1, 45 + (10 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + wis_mod
        self.damage_die = 10
        self.damage_bonus = wis_mod
        self.alive = True
        self.turn = True


class Zombie:
    def __init__(self, name: str = "Zombie", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 13, "DEX": 6, "CON": 16, "INT": 3, "WIS": 6, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 8
        self.max_hp = max(1, 9 + (2 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 8
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Ogre_Zombie:
    def __init__(self, name: str = "Ogre Zombie", level: int = 2, scores: dict = None):
        if scores is None:
            scores = {"STR": 19, "DEX": 6, "CON": 18, "INT": 3, "WIS": 6, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 8
        self.max_hp = max(1, 49 + (9 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 8
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Beholder_Zombie:
    def __init__(self, name: str = "Beholder Zombie", level: int = 5, scores: dict = None):
        if scores is None:
            scores = {"STR": 14, "DEX": 8, "CON": 16, "INT": 3, "WIS": 8, "CHA": 5}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 15
        self.max_hp = max(1, 60 + (11 * con_mod))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 6
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True
