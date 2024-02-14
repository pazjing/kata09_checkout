import unittest
import csv
import os
import sys
from unittest.mock import patch

from mypackage.load_prices import load_prices, extract_unit_price, extract_offer

class TestLoadPrices(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file with test data in the test directory
        self.test_csv_file = 'test_prices.csv'
        with open(self.test_csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['item', 'unit_price', 'special_offer'])
            writer.writerow(['item1', '10.0', '2 for 15'])
            writer.writerow(['item2', '5', ''])

        os.environ['CSV_FILE_PATH'] = self.test_csv_file

    def tearDown(self):
        # Remove the temporary CSV file after the test and reset the enviroment variable
        os.remove(self.test_csv_file)
        os.environ['CSV_FILE_PATH'] = ''

    def test_load_prices_successful(self):
        # Test if the function loads prices successfully from the test CSV file
        prices_data = load_prices()
        self.assertIsNotNone(prices_data)
        self.assertEqual(len(prices_data), 2)
        self.assertIn('item1', prices_data)
        self.assertIn('item2', prices_data)
        self.assertEqual(prices_data['item1']['unit_price'], 10.0)
        self.assertEqual(prices_data['item1']['special_quantity'], 2)
        self.assertEqual(prices_data['item1']['special_price'], 15.0)
        self.assertEqual(prices_data['item2']['unit_price'], 5)
        self.assertEqual(prices_data['item2']['special_quantity'], 0)
        self.assertEqual(prices_data['item2']['special_price'], 0)

    def test_load_prices_file_not_found(self):
        os.environ['CSV_FILE_PATH'] = 'nonexistent_file.csv'
        prices_data = load_prices()
        self.assertIsNone(prices_data)

    def test_load_prices_invalid_unit_price(self):
        # Test if the load prices function skips invalid entries
        with open(self.test_csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['item3', '-5.0', ''])
        prices_data = load_prices()
        self.assertIsNotNone(prices_data)
        self.assertEqual(len(prices_data), 2)    # Only valid entries should be loaded


    def test_extract_unit_price_valid_input(self):
        # test unite price extract
        self.assertEqual(extract_unit_price("10"), 10)
        self.assertEqual(extract_unit_price("10.34"), 10.34)
        self.assertEqual(extract_unit_price("10.3456"), 10.35)
        self.assertEqual(extract_unit_price("10.3445"), 10.34) 
        #  load_prices function will remove this kind of item out from the prices 
        self.assertEqual(extract_unit_price("-10"), -10) 
        self.assertEqual(extract_unit_price("-11.234"), -11.23)   

    def test_extract_unit_price_not_number(self):
        self.assertEqual(extract_unit_price("nil"), 0)  # Only positive number is valid

    def test_extract_offer_no2_numbers(self):
        self.assertEqual(extract_offer("Invalid input"), (0, 0))
        self.assertEqual(extract_offer("3 for unfinished"), (0, 0))
        self.assertEqual(extract_offer("nil now for 10"), (0, 0))

    def test_extract_offer_invalid_numbers(self):
        self.assertEqual(extract_offer("1.1 for 2.98"), (0, 0))
        self.assertEqual(extract_offer("buy -2 are 30 dollar "), (0, 0))
        self.assertEqual(extract_offer("3 now cost -10.00"), (0, 0))

    def test_extract_offer_valid_input(self):
        self.assertEqual(extract_offer("1 for 130"), (1, 130.0))
        self.assertEqual(extract_offer("2 for 23.4056"), (2, 23.41))
        self.assertEqual(extract_offer("3 is going to be 30.002"), (3, 30.00))
        self.assertEqual(extract_offer("offer is buy 3 cost 10 dollar"), (3, 10))

    def test_extract_offer_no2_numbers(self):
        self.assertEqual(extract_offer("Invalid input"), (0, 0))
        self.assertEqual(extract_offer("3 for unfinished"), (0, 0))
        self.assertEqual(extract_offer("nil now for 10"), (0, 0))

    def test_extract_offer_invalid_numbers(self):
        self.assertEqual(extract_offer("1.1 for 2.98"), (0, 0))
        self.assertEqual(extract_offer("buy -2 are 30 dollar "), (0, 0))
        self.assertEqual(extract_offer("3 now cost -10.00"), (0, 0))


if __name__ == '__main__':
    unittest.main()
