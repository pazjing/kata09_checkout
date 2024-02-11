import unittest
from unittest.mock import patch
from src.load_prices import load_prices, extract_numbers

class TestLoadPrices(unittest.TestCase):

    def test_load_prices_invalid_file(self):
        # Mocking open to simulate a missing file
        with patch('builtins.open', side_effect=[FileNotFoundError]):
            result = load_prices('nonexistent_file.csv')
            self.assertIsNone(result)
            
    def test_extract_numbers_valid_input(self):
        result = extract_numbers("3 for 130")
        self.assertEqual(result, (3, 130.0))

    def test_extract_numbers_invalid_input(self):
        result = extract_numbers("Invalid input")
        self.assertEqual(result, (0, 0))
        result = extract_numbers("3 for unfinished")
        self.assertEqual(result, (0, 0))

if __name__ == '__main__':
    unittest.main()
