import math

# --- HELPER DERIVATION FUNCTIONS ---

def calc_mod(score: int) -> int:
    """Calculates ability modifier: floor((score - 10) / 2)[cite: 1, 3]"""
    return math.floor((score - 10) / 2)

def calc_pb(level: int) -> int:
    """Calculates proficiency bonus based on character level[cite: 4]"""
    return math.ceil(1 + (level / 4))


# --- INDIVIDUAL CLASS DEFINITIONS ---

class Wizard:
    def __init__(self, name: str = "Wizard", level: int = 1, scores: dict = None):
        if scores is None:
            # Recommended Wizard array: INT high, DEX medium, CON medium
            scores = {"STR": 8, "DEX": 14, "CON": 12, "INT": 15, "WIS": 12, "CHA": 10}

        int_mod = calc_mod(scores["INT"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        pb = calc_pb(level)

        # ALL 9 ORIGINAL VARIABLES
        self.name = name
        self.ac = 10 + dex_mod  # Unarmored AC[cite: 2]
        self.max_hp = max(1, 6 + con_mod)  # Hit Die d6 + CON mod[cite: 3]
        self.hp = self.max_hp
        self.atk_bonus = pb + int_mod  # Spell Attack Bonus[cite: 4, 5]
        self.damage_die = 6  # e.g., Fire Bolt / Quarterstaff
        self.damage_bonus = int_mod
        self.alive = True
        self.turn = True


class Fighter:
    def __init__(self, name: str = "Fighter", level: int = 1, scores: dict = None):
        if scores is None:
            # Recommended Fighter array: STR high, CON high, DEX medium
            scores = {"STR": 15, "DEX": 12, "CON": 14, "INT": 8, "WIS": 10, "CHA": 10}

        str_mod = calc_mod(scores["STR"])
        con_mod = calc_mod(scores["CON"])
        pb = calc_pb(level)

        # ALL 9 ORIGINAL VARIABLES
        self.name = name
        self.ac = 16  # Chain Mail (Heavy Armor)[cite: 2]
        self.max_hp = max(1, 10 + con_mod)  # Hit Die d10 + CON mod[cite: 3]
        self.hp = self.max_hp
        self.atk_bonus = pb + str_mod  # Weapon Attack Bonus[cite: 4, 5]
        self.damage_die = 8  # e.g., Longsword
        self.damage_bonus = str_mod
        self.alive = True
        self.turn = True


class Rogue:
    def __init__(self, name: str = "Rogue", level: int = 1, scores: dict = None):
        if scores is None:
            # Recommended Rogue array: DEX high, CHA medium, CON medium
            scores = {"STR": 10, "DEX": 15, "CON": 12, "INT": 12, "WIS": 10, "CHA": 13}

        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        pb = calc_pb(level)

        # ALL 9 ORIGINAL VARIABLES
        self.name = name
        self.ac = 11 + dex_mod  # Leather Armor (Light Armor)[cite: 2]
        self.max_hp = max(1, 8 + con_mod)  # Hit Die d8 + CON mod[cite: 3]
        self.hp = self.max_hp
        self.atk_bonus = pb + dex_mod  # Finesse Weapon Attack Bonus[cite: 4, 5]
        self.damage_die = 6  # e.g., Shortsword
        self.damage_bonus = dex_mod
        self.alive = True
        self.turn = True


class Cleric:
    def __init__(self, name: str = "Cleric", level: int = 1, scores: dict = None):
        if scores is None:
            # Recommended Cleric array: WIS high, CON medium, STR medium
            scores = {"STR": 13, "DEX": 10, "CON": 14, "INT": 8, "WIS": 15, "CHA": 12}

        wis_mod = calc_mod(scores["WIS"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        pb = calc_pb(level)

        # ALL 9 ORIGINAL VARIABLES
        self.name = name
        self.ac = 14 + min(2, dex_mod)  # Scale Mail (Medium Armor)[cite: 2]
        self.max_hp = max(1, 8 + con_mod)  # Hit Die d8 + CON mod[cite: 3]
        self.hp = self.max_hp
        self.atk_bonus = pb + wis_mod  # Spell/Weapon Attack Bonus[cite: 4, 5]
        self.damage_die = 8  # e.g., Mace / Sacred Flame
        self.damage_bonus = wis_mod
        self.alive = True
        self.turn = True