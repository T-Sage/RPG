from items import Items

class location:
    def __init__(self, location_type, identifier, displayChar, index, items_for_sale=[], ):
        self.location_type = location_type
        self.identifier = identifier
        self.displayChar = displayChar
        self.items_for_sale = items_for_sale
        self.index = index
    
locations = [
    location(location_type = "geography", identifier = "ocean", displayChar = 'o', items_for_sale = None, index = 0), #index 0
    location(location_type = "geography", identifier = "plains", displayChar = "p", items_for_sale = None,  index = 1), #index 1
    location(location_type = "geography", identifier = "forest", displayChar = 'f', items_for_sale = None,  index = 2), #index 2
    location(location_type = "geography", identifier = "desert", displayChar = 'd', items_for_sale = None,  index = 3), #index 3
    location(location_type = "geography", identifier = "mountain", displayChar = 'm', items_for_sale = None, index = 4), #index 4
    None,
    None, #reserving space for new geography types if we can think of any.
    None,
    location(location_type = "town", identifier = "starter town", displayChar = 'T', items_for_sale = [Items.POTION, Items.ANTIDOTE], index = 8), #index 8
    None,
    None,
    None,
    ]