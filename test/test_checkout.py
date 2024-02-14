import sys
import os
import numpy as np
import unittest
from unittest.mock import patch

sys.path.append(os.environ.get('MODULE_PATH'))
from mypackage.checkout import checkout, configure_logging

class TestCheckout(unittest.TestCase):

    def setUp(self):
        # Configure logging before each test
        configure_logging()
        
    # test baisc function
    @patch('builtins.input', side_effect=['A', 'B', 'A', 'Q'])  # Simulate user input
    def test_checkout_basic(self, mock_input):
        prices_data = {
            'A': {'unit_price': 1.0, 'special_quantity': 3, 'special_price': 2.5},
            'B': {'unit_price': 2.0, 'special_quantity': 2, 'special_price': 3.0},
        }

        # Call the checkout function
        cart, total_items, total_cost = checkout(prices_data)

        # Assert the values of the variables returned by checkout
        self.assertEqual(total_items, 3)
        self.assertEqual(total_cost, 4.0)
        self.assertEqual(cart, {'A': {'quantity': 2, 'total_price': 2.0}, 'B': {'quantity': 1, 'total_price': 2.0}})


    # test speical_offer apply
    @patch('builtins.input', side_effect=['A', 'A', 'A', 'Q'])
    def test_checkout_special(self, mock_input):
        prices_data = {'A': {'unit_price': 9.99, 'special_quantity': 2, 'special_price': 16.99}}
        
        # Call the checkout function
        cart, total_items, total_cost = checkout(prices_data)

        # Assert the values of the variables returned by checkout
        self.assertEqual(total_items, 3)
        self.assertEqual(total_cost, 26.98)
        self.assertEqual(cart, {'A': {'quantity': 3, 'total_price': 26.98}})

    
    # test decimal calculate apply
    @patch('builtins.input', side_effect=['A', 'A', 'Q'])
    def test_checkout_decimal(self, mock_input):
        prices_data = {'A': {'unit_price': 10, 'special_quantity': 2, 'special_price': 18.888}}
        
        # Call the checkout function
        cart, total_items, total_cost = checkout(prices_data)

        # Assert the values of the variables returned by checkout
        self.assertEqual(total_items, 2)
        self.assertEqual(total_cost, 18.89)
        self.assertEqual(cart, {'A': {'quantity': 2, 'total_price': 18.89}})


    # test not exist item won't stop checkout 
    @patch('builtins.input', side_effect=['A', 'B', 'A', 'Q'])
    def test_checkout_nonexist(self, mock_input):
        prices_data = {'A': {'unit_price': 10, 'special_quantity': 2, 'special_price': 15}}
        
        # Call the checkout function
        cart, total_items, total_cost = checkout(prices_data)

        # Assert the values of the variables returned by checkout
        self.assertEqual(total_items, 2)
        self.assertEqual(total_cost, 15)
        self.assertEqual(cart, {'A': {'quantity': 2, 'total_price': 15}})


if __name__ == '__main__':
    unittest.main()
