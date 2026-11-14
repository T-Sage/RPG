#The overworld's height, the overworld's width, and the number of tiles the party can see in any direction.
import sys
import random
import time
from overworldTemplate import overworldTemplate
from items import Item, Items
from locations import locations
from classes import *
from arpeegee import Encounter, Bandit, combat
OVERWORLD_HEIGHT = 50
OVERWORLD_WIDTH = 50
PARTY_VISION_RANGE = 3
MAP_BOUNDARY = PARTY_VISION_RANGE    #The number of tiles away from the edge of the map the party must be. This is to prevent negative index lookups.
overworldMap = []
#TODO create an actual starting location other than the top left of the continent.
player_x_coordinate = 6
player_y_coordinate = 6
#these two variables are used to handle tutorial text that only gets said one time. the same index in both represent the same tutorial.
#i.e. tutorial_status[0] corresponds to TUTORIAL_TEXT[0]. tutorial_status = True indicates that the tutorial text needs to be printed the next time it is appropriate to do so.
tutorial_status = [True, True]
TUTORIAL_TEXT = ["To select what direction to move, type north, east, south, or west, or n, e, s, or w.", "At a town, you may buy, sell, rest, or exit."]
party = [Fighter(), Wizard(), Rogue(), Cleric()]

class Inventory:
    def __init__(self):
        self.gold = 100
        self.items = [[3, Items.POTION], [2, Items.ANTIDOTE], [3, Items.BANDAGE]]

user_inventory = Inventory()

def setupMap():
    #instantiate overworldMap as an OVERWORLD_HEIGHT X OVERWORLD_WIDTH 2d array filled with None objects.
    for i in range(0,OVERWORLD_HEIGHT):
        overworldMap.append([])
        for j in range(0, OVERWORLD_WIDTH):
            overworldMap[i].append(None)
    
    #for every element in every row of the overworld template, fill overworldMap at the corresponding index with a pointer to the correct location based on the template
    for indexI, row in enumerate(overworldTemplate):
        for  indexJ, element in enumerate(row):
            result = -1
            if element == 'o':
                result = 0 #index 0 is ocean
            elif element == 'p':
                result = 1 #index 1 is plains
            elif element == 'f':
                result = 2 #index 2 is forest
            elif element == 'd':
                result = 3 #index 3 is desert
            elif element == 'm':
                result = 4 #index 4 is mountain
            elif element == 'T':
                result = 8 #index 8 is starter town
            else:
                break
            overworldMap[indexI][indexJ] = locations[result]

# print out a grid around the player location PARTY_VISION_RANGE away from the player in all directions
def player_view():
    for i in range(PARTY_VISION_RANGE * 2 + 1):
        for j in range(PARTY_VISION_RANGE * 2 + 1):
            if i == PARTY_VISION_RANGE and j == PARTY_VISION_RANGE:
                print("X ", end="")
            else:
                print(f"{overworldMap[player_y_coordinate - PARTY_VISION_RANGE + i][player_x_coordinate - PARTY_VISION_RANGE + j].displayChar} ", end="")
        print()

#debug function, print the entire overworld map.
def print_map():
    for index, row in enumerate(overworldMap):
        print(index, end=" ")
        for element in row:
            if element != None:
                print(f"{element.displayChar} ", end="")
            else:
                print(f"-", end="")
        print()

def printInventory():
    global user_inventory
    user_inventory.items = sorted(user_inventory.items, key=lambda x: x[1].name) #sort the inventory alphabetically before printing
    print(f"Inventory: \nGold: {user_inventory.gold}", end="")
    for item in user_inventory.items:
        print(f", {item[0]} {item[1].value.name}s", end="")
    print(".")

def printParty():
    for index, character in enumerate(party):
        print(f"{character.name}: HP: {character.hp}/{character.max_hp}", end="")
        if(index < len(party) -1):
            print(", ", end ="")
        else:
            print(".")

#handles text input and player movement. Might want to split up text input and handling player movement in separate functions in the future.
def handle_input():
    global player_y_coordinate
    global player_x_coordinate
    global tutorial_status
    if tutorial_status[0] == True:
        print(TUTORIAL_TEXT[0])
        tutorial_status[0] = False
    while True:
        selection = input().strip().casefold()
        # menu options
        #if selection == "menu": print out a menu, or something like that.
        if selection == "quit":
            sys.exit(0)

        elif selection == "fight":
            initiate_combat()

        elif selection == "inventory" or selection == "bag":
            printInventory()
            
        elif selection == "status" or selection == "party":
            printParty()

        elif selection == "map":
            player_view()

        #debug commands
        elif selection == "damage":
            char_selection = input("Select character to damage:\n>").strip().casefold()
            conf_char_selection = None
            # if the input matches a character name in the party, lock in selection and proceed
            for character in party:
                if character.name.casefold() == char_selection:
                    conf_char_selection = character
                    break
            if conf_char_selection == None:
                print("selection invalid.")
                continue
            else:
                damage = int(input("select amount of damage: \n"))
                conf_char_selection.hp = conf_char_selection.hp - damage
                
                

        # movement options
        elif selection == "n" or selection == "north":
            print(1)
            if player_y_coordinate <= MAP_BOUNDARY: #if player is on the topmost boundary of the world
                print("Cannot enter the ocean.")
                continue #nonsuccessful move, so loop again
            else:
                player_y_coordinate = player_y_coordinate - 1
                break #successful move, leave loop
        elif selection == "e" or selection == "east":
            print(2)
            if player_x_coordinate >= OVERWORLD_WIDTH - MAP_BOUNDARY - 1: #if player is on the rightmost boundary of the world
                print("Cannot enter the ocean.")
                continue #nonsuccessful move, so loop again
            else:
                player_x_coordinate = player_x_coordinate + 1
                break
        elif selection == "s" or selection == "south":
            print(3)
            if player_y_coordinate >= OVERWORLD_HEIGHT - MAP_BOUNDARY - 1: #if player is on the bottommost boundary of the world
                print("Cannot enter the ocean.")
                continue #nonsuccessful move, so loop again
            else:
                player_y_coordinate = player_y_coordinate + 1
                break
        elif selection == "w" or selection == "west":
            print(4)
            if player_x_coordinate <= MAP_BOUNDARY: #if player is on the leftmmost boundary of the world
                print("Cannot enter the ocean.")
                continue #nonsuccessful move, so loop again
            else:
                player_x_coordinate = player_x_coordinate - 1
                break
        else:
            print("Invalid command, please try again.")
            continue #unsuccessful command, so loop again.
    player_view()
    check_new_position()

    
#The function that handles what is supposed to happen when the player moves onto a new space. 
def check_new_position():
    new_position = overworldMap[player_y_coordinate][player_x_coordinate]
    #print(f"The identifier of the tile you stepped on is {new_position.identifier}.") #debug print statement
    if new_position.location_type == "geography":
        #if random.randint(1,5) == 5:
            #initiate_combat()
        print(f"You entered a {new_position.identifier}") #if the player has landed on a generic piece of land
    elif new_position.location_type == "town": #if the player lands on a town
        entered_town(new_position)
    
# handles when a player enters a town
def entered_town(town):
    global tutorial_status
    
    while True:
        print(f"You are in {town.identifier}")
        if tutorial_status[1] == True:
            print(TUTORIAL_TEXT[1])
            tutorial_status[1] = False
        selection = input().strip().casefold()
        
        if selection == "buy":
            buy(town.items_for_sale)
            continue
        elif selection == "sell":
            sell()
            continue
        elif selection == "rest":
            for character in party:
                character.hp = character.max_hp
            print("You rest at the inn. HP Restored.")
        elif selection == "exit":
            player_view()
            print("You leave the town.")
            break
        else:
            print("Invalid command, please try again.")
            continue #unsuccessful command, so loop again.

def buy(items_for_sale):
    #print out what items can be bought from the town
    print("Items for sale:", end = " ")
    for index, item in enumerate(items_for_sale):
        end = ""
        if index == len(items_for_sale) - 1:
            end = ".\n"
        else:
            end = ", "
        print(f"{item.value.name}: {item.value.value} gold", end=end)
    
    item_selection = input("Select item to buy:\n>").strip().casefold()
    conf_item_selection = None
    conf_item_index = None
    # if the input matches an item name in the inventory, lock in selection and proceed
    for index, item in enumerate(items_for_sale):
        if item.value.name.casefold() == item_selection:
            conf_item_selection = item
            conf_item_index = index
            break
    if conf_item_selection == None:
        print("selection invalid.")
        return
    else:
        num_to_buy = int(input(f"Select amount to buy: \n"))
        value = num_to_buy * conf_item_selection.value.value
        if value > user_inventory.gold:
            print(f"You do not have enough gold to buy {num_to_buy} {conf_item_selection.value.name}s.")
        else:
            #check if user_inventory already has the item
            user_has_item = False
            for item in user_inventory.items:
                if item[1] == conf_item_selection:
                    item[0] = item[0] + num_to_buy
                    user_inventory.gold = user_inventory.gold - value
                    user_has_item = True
            if(user_has_item == False):
                user_inventory.items.append([num_to_buy, conf_item_selection])
            print("Purchase complete.")
                
    

def sell():
    global user_inventory
    printInventory()
    item_selection = input("Select item to sell:\n>").strip().casefold()
    conf_item_selection = None
    conf_item_index = None
    # if the input matches an item name in the inventory, lock in selection and proceed
    for index, item in enumerate(user_inventory.items):
        if item[1].value.name.casefold() == item_selection:
            conf_item_selection = item
            conf_item_index = index
            break
                
    if conf_item_selection == None:
        print("selection invalid.")
        return
    else:
        num_to_sell = int(input(f"you have {item[0]}. Select amount to sell: \n"))
        if num_to_sell > item[0]: #if number to sell is higher than the amount owned
            print("Invalid amount.")
            return
        user_inventory.gold = user_inventory.gold + (item[1].value.value * num_to_sell)
        conf_item_selection[0] = conf_item_selection[0] - num_to_sell
        if conf_item_selection[0] == 0: #if player now has 0 of the item
            del user_inventory[conf_item_index]
        print("Sale Complete.")
                
def initiate_combat():
    print("You are being attacked!")
    time.sleep(2)
    combat(Encounter(party,[Bandit(), Bandit(), Bandit(), Bandit()]))



def main():
    setupMap()
    player_view()
    while True:
        handle_input() # handle player movement
if __name__ == "__main__":
    main()