import csv
import re
import os

def load_prices(filename='prices.csv'):
    
    # Construct the absolute path to the CSV file based on the script's location
    script_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_directory, filename)
   
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            prices_data = {}

            for i, row in enumerate(reader, start=2): 
                item = row.get('item')
                unit_price = row.get('unit_price')
                special_offer = row.get('special_offer')

                try:
                    unit_price_value = float(unit_price)  # only get legal price input
                except ValueError:
                    print(f"Warning: Line {i}: Invalid unit_price value '{unit_price}'. Skip this item. Please check data.")
                    continue

                if special_offer is None:
                    special_quantity = 0
                    special_price = 0
                else:
                    special_quantity, special_price = extract_numbers(special_offer)

                prices_data[item] = {
                    'unit_price': unit_price_value,
                    'special_quantity': special_quantity,
                    'special_price': special_price
                }

        print("Prices loaded successfully.")
        return prices_data

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def extract_numbers(input_string):

    pattern = re.compile(r'\d+\.\d+|\d+')  # matches integers or decimals  

    matches = pattern.findall(input_string)

    # Check if at least two numbers were found
    if len(matches) >= 2:
        number1 = int(matches[0])
        number2 = float(matches[1])
    else:
        number1 = 0
        number2 = 0

    return number1, number2
