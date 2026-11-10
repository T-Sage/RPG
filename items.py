from enum import Enum 

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Items(Enum): #A set of constants, with every item and their relevant attributes. This is where all items within the game are defined. #TODO does this include equipment? maybe? maybe not
#it is worth noting that Items.POTION.value returns the Item object who has the name and value attributes as described in the Item Class. Therefore Items.POTION.value.value is how to
#receive the gold value of the potion item, and Items.POTION.value.name is to receive the name value. 
    POTION = Item("potion", 20)
    ANTIDOTE = Item("antidote", 50)
    BANDAGE = Item("bandage", 5)
