import unittest
from unittest.mock import patch
from src.load_prices import load_prices, extract_unit_price, extract_offer

class TestLoadPrices(unittest.TestCase):

    def test_load_prices_invalid_file(self):
        # Mocking open to simulate a missing file
        with patch('builtins.open', side_effect=[FileNotFoundError]):
            result = load_prices('nonexistent_file.csv')
            self.assertIsNone(result)

    def test_extract_unit_price_valid_input(self):
        self.assertEqual(extract_unit_price("10"), 10)
        self.assertEqual(extract_unit_price("10.34"), 10.34)
        self.assertEqual(extract_unit_price("10.3456"), 10.35)
        self.assertEqual(extract_unit_price("10.3445"), 10.34)  

    def test_extract_unit_price_not_number(self):
        self.assertEqual(extract_unit_price("nil"), 0)



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
