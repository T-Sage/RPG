import math

# --- HELPER DERIVATION FUNCTIONS ---

def calc_mod(score: int) -> int:
    """Calculates ability modifier: floor((score - 10) / 2)[cite: 1, 3]"""
    return math.floor((score - 10) / 2)

def calc_pb(level: int) -> int:
    """Calculates proficiency bonus based on character level[cite: 4]"""
    return math.ceil(1 + (level / 4))


class Barbarian:
    def __init__(self, name: str = "Barbarian", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 15, "DEX": 13, "CON": 14, "INT": 8, "WIS": 12, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 10 + dex_mod + con_mod
        self.max_hp = max(1, 12 + con_mod + ((level - 1) * (7 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 12
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Bard:
    def __init__(self, name: str = "Bard", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 14, "CON": 12, "INT": 13, "WIS": 10, "CHA": 15}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 11 + dex_mod
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + cha_mod
        self.damage_die = 8
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Cleric:
    def __init__(self, name: str = "Cleric", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 14, "DEX": 10, "CON": 13, "INT": 8, "WIS": 15, "CHA": 12}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 16 + min(2, dex_mod)
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + wis_mod
        self.damage_die = 8
        self.damage_bonus = wis_mod
        self.alive = True
        self.turn = True


class Druid:
    def __init__(self, name: str = "Druid", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 12, "CON": 14, "INT": 13, "WIS": 15, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 13 + dex_mod
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + wis_mod
        self.damage_die = 8
        self.damage_bonus = wis_mod
        self.alive = True
        self.turn = True


class Fighter:
    def __init__(self, name: str = "Fighter", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 15, "DEX": 13, "CON": 14, "INT": 10, "WIS": 12, "CHA": 8}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 18
        self.max_hp = max(1, 10 + con_mod + ((level - 1) * (6 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 8
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Monk:
    def __init__(self, name: str = "Monk", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 10, "DEX": 15, "CON": 13, "INT": 8, "WIS": 14, "CHA": 12}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 10 + dex_mod + wis_mod
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 6
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Paladin:
    def __init__(self, name: str = "Paladin", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 15, "DEX": 10, "CON": 13, "INT": 8, "WIS": 12, "CHA": 14}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 18
        self.max_hp = max(1, 10 + con_mod + ((level - 1) * (6 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod
        self.damage_die = 8
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Ranger:
    def __init__(self, name: str = "Ranger", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 12, "DEX": 15, "CON": 13, "INT": 8, "WIS": 14, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 14 + min(2, dex_mod)
        self.max_hp = max(1, 10 + con_mod + ((level - 1) * (6 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 8
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Rogue:
    def __init__(self, name: str = "Rogue", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 15, "CON": 12, "INT": 13, "WIS": 10, "CHA": 14}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 11 + dex_mod
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod
        self.damage_die = 8
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Sorcerer:
    def __init__(self, name: str = "Sorcerer", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 13, "CON": 14, "INT": 10, "WIS": 12, "CHA": 15}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 10 + dex_mod
        self.max_hp = max(1, 6 + con_mod + ((level - 1) * (4 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + cha_mod
        self.damage_die = 10
        self.damage_bonus = cha_mod
        self.alive = True
        self.turn = True


class Warlock:
    def __init__(self, name: str = "Warlock", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 13, "CON": 14, "INT": 12, "WIS": 10, "CHA": 15}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 11 + dex_mod
        self.max_hp = max(1, 8 + con_mod + ((level - 1) * (5 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + cha_mod
        self.damage_die = 10
        self.damage_bonus = cha_mod
        self.alive = True
        self.turn = True


class Wizard:
    def __init__(self, name: str = "Wizard", level: int = 1, scores: dict = None):
        if scores is None:
            scores = {"STR": 8, "DEX": 14, "CON": 13, "INT": 15, "WIS": 12, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        int_mod = calc_mod(scores["INT"])
        wis_mod = calc_mod(scores["WIS"])
        cha_mod = calc_mod(scores["CHA"])
        pb = calc_pb(level)

        self.name = name
        self.ac = 10 + dex_mod
        self.max_hp = max(1, 6 + con_mod + ((level - 1) * (4 + con_mod)))
        self.hp = self.max_hp
        self.atk_bonus = pb + int_mod
        self.damage_die = 10
        self.damage_bonus = int_mod
        self.alive = True
        self.turn = True