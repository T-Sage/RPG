from enum import Enum 

#Define what a weapon class looks like
class Weapon:
    def __init__(self, name, type, attack_bonus, damage_die, damage_bonus, damage_type):
        self.name = name
        self.type = type
        self.attack_bonus = attack_bonus
        self.damage_die = damage_die
        self.damage_bonus = damage_bonus
        self.damage_type = damage_type

class Weapon_Type:
    def __init__(self, type_val, damage_type):
        self.type = type_val
        self.damage_type = damage_type

#This Enum class contains constants for every type of weapon in the game. Many weapons will share a weapon type. All swords will have the sword type for instance.
#Damage type is also determined by weapon type. All swords deal slashing damage, all hammer do bludgeoning damage.
#TODO determine which classes can equip which weapon types. Fighter can use swords, but can they use hammers? Classes don't only equip 1 type of weapon.
#TODO add more types? Axes? Spears? Bows? Etc. Whatever is appropriate for the other classes adedd in character_creation
class Weapon_Types(Enum):
    SWORD = Weapon_Type("sword", "slashing")
    HAMMER = Weapon_Type("hammer", "bludgeoning")
    STAFF = Weapon_Type("staff", "bludgeoning")
    FINESSE = Weapon_Type("finesse", "piercing")

#Define each individual instance of a weapon as a constant in the Weapons Enum class. This class holds all data for all specific weapons in our game.
#Other parts of the game only need to import Weapons from weapons.py and then do Weapons.IRON_SWORD.value to return the weapon object associated with, in this example, the iron sword.
class Weapons(Enum):
    #the Iron Sword, once applied to the fighter, should determine their damage_die instead of it being a magic number. And the attack_bonus and damage_bonus should be added to the fighter's.
    #This means that once the figher has this weapon equipped in character_creation.py, he will be functionally identical, but his damage_die will be determined by his weapon not a magic number.
    IRON_SWORD = Weapon(name="Iron Sword", type=Weapon_Types.SWORD.value.type, attack_bonus=0, damage_die=10, damage_bonus=0, damage_type=Weapon_Types.SWORD.damage_type) #Starting sword (Fighter)
    IRON_MACE = Weapon(name="Iron Mace", type=Weapon_Types.HAMMER.value.type, attack_bonus=0, damage_die=8, damage_bonus=0, damage_type=Weapon_Types.HAMMER.damage_type) #Starting Hammer (Cleric)
    STAFF = Weapon(name="Staff", type=Weapon_Types.STAFF.value.type, attack_bonus=0, damage_die=6, damage_bonus=0, damage_type=Weapon_Types.STAFF.damage_type) #Starting Staff (Wizard)
    RAPIER = Weapon(name="Rapier", type=Weapon_Types.FINESSE.value.type, attack_bonus=0, damage_die=8, damage_bonus=0, damage_type=Weapon_Types.FINESSE.damage_type) #Starting Finesse Weapon (Rogue)
    
    #TODO Add starting weapons for the other classes in character_creation.py. If a class would use a weapon that is already made, you don't have to make a new one for that class. Just add their class to the comment
    #TODO Add weapons that are upgrades for each weapon type. Example: (Steel sword is slightly better than iron sword, same damage die but maybe +1 to attack and damage bonus?)