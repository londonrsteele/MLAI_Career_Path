# Filename : surfshop.py
# Author   : Codecademy, LR Steele
# Info     : Coding project/objective supporting file for "SWE in Python II"
#          :  section of SWE for ML/AI Engineers course in Machine
#          : Learning/AI Engineer Career Path on Codecademy.
import datetime

# "Make an improvement to the exception that gets thrown 
# when too many surfboards are added to the cart. Modify 
# TooManySurfboardsError so that when raised, it has the message
# 'Cart cannot have more than 4 surfboards in it!'"
class TooManyBoardsError(Exception):
    def __str__(self):
        return "Cart cannot have more than 4 surfboards in it!"

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    # "Sam has noticed all of your hard work and the fact that your tests 
    # found a bug. You can now start working on the actual shopping cart 
    # software! Take a look in surfshop.py. Recall that the 
    # ShoppingCart.apply_locals_discount is not setting the 
    # ShoppingCart.locals_discount attribute to True, as it should be. 
    # Can you fix it?"
    # BEFORE:
    # def apply_locals_discount(self):
    #    pass
    # AFTER:
    def apply_locals_discount(self):
        self.locals_discount = True
