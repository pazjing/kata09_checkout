import csv
import re
import os
import numpy as np
import logging
from logging_config import configure_logging

def load_prices():

    csv_file_path = os.environ.get('CSV_FILE_PATH', 'default_prices.csv')

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            prices_data = {}

            for i, row in enumerate(reader, start=2): 
                item = row.get('item')
                unit_price = row.get('unit_price')
                special_offer = row.get('special_offer')

                unit_price_value = extract_unit_price(unit_price)

                if unit_price_value <= 0:
                    logging.warning(f"Line {i}: Invalid unit_price value. Skip. Please check data.")
                    continue
            
                special_quantity_value, special_price_value = extract_offer(special_offer)
                
                prices_data[item] = {
                    'unit_price': unit_price_value,
                    'special_quantity': special_quantity_value,
                    'special_price': special_price_value
                }

        logging.info("Prices loaded successfully.")
        logging.debug(f"prices_data: {prices_data}")
        return prices_data

    except FileNotFoundError:
        logging.error(f"Error: File '{csv_file_path}' not found.")
        return None
    except Exception as e:
        logging.error(f"Error: {e}")
        return None


def extract_unit_price(unit_price):
    try:
        unit_price_value = np.round(float(unit_price), decimals=2)
    except (ValueError):
        return 0
    
    return unit_price_value


def extract_offer(input_string):

    pattern = re.compile(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+')  # matches integers or decimals   

    matches = pattern.findall(input_string)

    # Check if at least two numbers were found
    if len(matches) >= 2:
        try:
            number1 = int(matches[0])
            number2 = np.round(float(matches[1]), decimals=2)

            # Set both numbers to 0 if either of them is 0
            if number1 < 0 or number2 < 0:
                number1 = 0
                number2 = 0

        except (ValueError):
            number1 = 0
            number2 = 0
    else:
        number1 = 0
        number2 = 0

    return number1, number2
