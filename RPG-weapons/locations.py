from items import Items

class location:
    def __init__(self, location_type, identifier, displayChar, items_for_sale=[]):
        self.location_type = location_type
        self.identifier = identifier
        self.displayChar = displayChar
        self.items_for_sale = items_for_sale
    
locations = [
    location(location_type = "geography", identifier = "ocean", displayChar = 'o'), #index 0
    location(location_type = "geography", identifier = "plains", displayChar = "p"), #index 1
    location(location_type = "geography", identifier = "forest", displayChar = 'f'), #index 2
    location(location_type = "geography", identifier = "desert", displayChar = 'd'), #index 3
    location(location_type = "geography", identifier = "mountain", displayChar = 'm'), #index 4
    None,
    None, #reserving space for new geography types if we can think of any.
    None,
    location(location_type = "town", identifier = "starter town", displayChar = 'T', items_for_sale = [Items.POTION, Items.ANTIDOTE]), #index 8
    None,
    None,
    None,
    ]