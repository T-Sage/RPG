import math

# --- HELPER DERIVATION FUNCTIONS ---

def calc_mod(score: int) -> int:
    """Calculates ability modifier: floor((score - 10) / 2)[cite: 1, 3]"""
    return math.floor((score - 10) / 2)

def calc_pb(level: int) -> int:
    """Calculates proficiency bonus based on character level[cite: 4]"""
    return math.ceil(1 + (level / 4))


# --- INDIVIDUAL CLASS DEFINITIONS ---

class Goblin_Minion:
    def __init__(self, name: str = "Goblin Minion", level: int = 1, scores: dict = None):
        if scores is None:
            # Recommended Goblin Minion array
            scores = {"STR": 8, "DEX": 15, "CON": 10, "INT": 10, "WIS": 8, "CHA": 8}

        int_mod = calc_mod(scores["INT"])
        dex_mod = calc_mod(scores["DEX"])
        con_mod = calc_mod(scores["CON"])
        pb = calc_pb(level)

        # ALL 9 ORIGINAL VARIABLES
        self.name = name
        self.ac = 12  # Unarmored AC[cite: 2]
        self.max_hp = max(1, 7 + con_mod)  # Hit Die d6 + CON mod[cite: 3]
        self.hp = self.max_hp
        self.atk_bonus = pb + int_mod  # Spell Attack Bonus[cite: 4, 5]
        self.damage_die = 6  # e.g., Fire Bolt / Quarterstaff
        self.damage_bonus = int_mod
        self.alive = True
        self.turn = True