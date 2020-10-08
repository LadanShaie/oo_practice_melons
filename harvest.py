############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.new_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    
    #all_melon_types = []

    muskmelon = MelonType("musk", "1998", "green", "seedless",
     "bestseller", "Muskmelon")
    muskmelon.add_pairing('Mint')
    
    casaba = MelonType('cas', '2003', 'orange', 'has seeds',
     'not a bestseller', 'Casaba')
    casaba.add_pairing('Strawberries and Mint')
         
    crenshaw = MelonType('cren', '1996', 'green', 'has seeds',
     'not a bestseller', 'Crenshaw')
    crenshaw.add_pairing('Proscuitto')
   
    yellow_watermelon = MelonType('yw', '2013', 'yellow', 'has seeds',
     'bestseller', 'Yellow Watermelon')
    yellow_watermelon.add_pairing('Ice Cream')
    
    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    
    
    # Fill in the rest
    
    return all_melon_types
  
def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for fruit in melon_types:
        name = fruit.name

        for pair in fruit.pairings:
            pairing = pair     
    
        
            print(f'{name} pairs well with: {pairing}.')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest
    dict_melon = {}
    for fruit in melon_types:
        dict_melon[fruit.code] = fruit
    print (dict_melon)



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



