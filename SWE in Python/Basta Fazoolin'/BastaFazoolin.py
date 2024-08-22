# Filename : BastaFazoolin.py
# Author   : LR Steele
# Info     : Coding project/objective for "SWE in Python I" section of SWE for
#          : ML/AI Engineers course in Machine Learning/AI Engineer Career Path
#          : on Codecademy.

class Item:
    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return str(self.name + ": " + self.price)

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return str(self.name + " - Available from " + str(self.start_time) + " - " + str(self.end_time) )

    def calculate_bill(self, purchased_items):
        total_price = 0.00
        for item in purchased_items:
            total_price += item.price
        return total_price

def create_list_of_Items(dict_of_items):
        items = []
        for item, value in dict_of_items.items():
            items.append(Item(item, value))
        return items

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available = []
        if (time >= 11) & (time < 16):
            available.append(brunch)
        if (time >= 11) & (time < 21):
            available.append(kids)
        if (time >= 15) & (time < 18):
            available.append(early_bird)
        if (time >= 17) & (time < 23):
            available.append(dinner)
        return available

class Business:
    def __init__(self, name, list_of_franchises):
        self.name = name
        self.franchises = list_of_franchises

# Create Menu #1
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = create_list_of_Items(brunch_items)
brunch = Menu("Brunch", start_time=11, end_time=16, items=brunch_menu)

# Create Menu #2
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = create_list_of_Items(early_bird_items)
early_bird = Menu("Early-Bird", start_time=15, end_time=18, items=early_bird_menu)

# Create Menu #3
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = create_list_of_Items(dinner_items)
dinner = Menu("Dinner", start_time=17, end_time=23, items=dinner_menu)

# Create Menu #4
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = create_list_of_Items(kids_items)
kids = Menu("Kids", start_time=11, end_time=21, items=kids_menu)

# Test __repr__
print(brunch)

# Print bill with all of brunch items
print(brunch.calculate_bill(brunch_menu))

# Print bill from breakfast for the given items
breakfast_bill_items = {'pancakes': 7.50, 'home fries': 4.50, 'coffee': 1.50}
breakfast_bill_Items = create_list_of_Items(breakfast_bill_items)
print(brunch.calculate_bill(breakfast_bill_Items))

# Create Franchises
list_of_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", list_of_menus)
new_installment = Franchise("12 East Mulberry Street", list_of_menus)

# Test __repr__
print(flagship_store)

# Test available_menus
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# Create Business
Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Create new arepa menu, franchise, and business
arepa_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa_menu = create_list_of_Items(arepa_items)
arepa = Menu("Take a' Arepa", start_time=10, end_time=20, items=arepa_menu)
arepas_place = Franchise("189 Fitzgerald Avenue", arepa)
arepa_businees = Business("Take a' Arepa!", [arepas_place])