# Filename : tests.py
# Author   : LR Steele
# Info     : Coding project/objective for "SWE in Python II" section of SWE for
#          : ML/AI Engineers course in Machine Learning/AI Engineer Career Path
#          : on Codecademy.
# NOTE     : Any comments in "quotes" are from Codecademy.
import surfshop
import unittest

# "The features that you need to test have been implemented in the 
# surfshop.ShoppingCart class."

class surfshopTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboards(self):
        message = self.cart.add_surfboards(1)
        self.assertEqual(message, "Successfully added 1 surfboard to cart!")

    # "Parameterize the test you wrote in task 4 so that it runs 3 times, 
    # passing 2, 3, and 4 as the arguments to surfshop.add_surfboards(). 
    # This allows us to easily test a single function with a variety of inputs. 
    # Remember to modify the expected return value with the correct number of 
    # surfboards."
    # BEFORE:
    # def test_add_surfboards(self):
    #     message = self.cart.add_surfboards(2)
    #     self.assertEqual(message, "Successfully added 2 surfboards to cart!")
    # AFTER:
    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f"Successfully added {i} surfboards to cart!")
                self.cart = surfshop.ShoppingCart() # reset cart

    # "Sam, the owner of Sam’s Surf Shop, has just informed us that the shop is 
    # heading into the off season and business has slowed down. The store’s 
    # shopping cart no longer needs to enforce the 4 surfboards per customer
    # rule - at least until business picks up again. Go back and modify the 
    # test you wrote in task 5 which checks for a surfshop.TooManySurfboardsError
    # so that it is skipped."
    @unittest.skip
    def test_too_many_surfboards_in_cart(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
    
    # "If you’ve implemented your tests correctly, they should all pass - except 
    # for one! It seems that the ShoppingCart.apply_locals_discount() function 
    # is not working as expected. While you wait for the development team to fix
    # this bug, you don’t want it to cause our tests to fail. Mark this test as
    # an expected failure."
    # BEFORE:
    # @unittest.expectedFailure
    # def test_locals_discount(self):
    #     self.cart.apply_locals_discount()
    #     self.assertTrue(self.cart.locals_discount)
    # "Sam has noticed all of your hard work and the fact that your tests 
    # found a bug. You can now start working on the actual shopping cart 
    # software! Take a look in surfshop.py. Recall that the 
    # ShoppingCart.apply_locals_discount is not setting the 
    # ShoppingCart.locals_discount attribute to True, as it should be. 
    # Can you fix it?"
    # AFTER:
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()