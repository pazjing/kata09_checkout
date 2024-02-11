import unittest
from unittest.mock import patch
from src.checkout import checkout

class TestCheckout(unittest.TestCase):

    # test baisc function
    @patch('builtins.input', side_effect=['A', 'B', 'C', 'Q'])
    @patch('builtins.print')
    def test_checkout_basic(self, mock_print, mock_input):
        prices_data = {'A': {'unit_price': 10, 'special_quantity': 2, 'special_price': 15},
                       'B': {'unit_price': 5, 'special_quantity': 3, 'special_price': 10},
                       'C': {'unit_price': 2, 'special_quantity': 0, 'special_price': 0}}

        checkout(prices_data)
        mock_print.assert_called_with('...Total Item Quantity: 3, Total Cost: 17.0')

    # test speical_price apply
    @patch('builtins.input', side_effect=['A', 'A', 'A', 'Q'])
    @patch('builtins.print')
    def test_checkout_special(self, mock_print, mock_input):
        prices_data = {'A': {'unit_price': 10, 'special_quantity': 2, 'special_price': 15}}

        checkout(prices_data)
        mock_print.assert_called_with('...Total Item Quantity: 3, Total Cost: 25.0')

    # test not exist item won't stop checkout 
    @patch('builtins.input', side_effect=['A', 'B', 'A', 'Q'])
    @patch('builtins.print')
    def test_checkout_nonexist(self, mock_print, mock_input):
        prices_data = {'A': {'unit_price': 10, 'special_quantity': 2, 'special_price': 15}}

        checkout(prices_data)
        mock_print.assert_called_with('...Total Item Quantity: 2, Total Cost: 15.0')


if __name__ == '__main__':
    unittest.main()
