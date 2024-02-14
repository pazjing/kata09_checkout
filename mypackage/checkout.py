import numpy as np
import logging
from logging_config import configure_logging

def checkout(prices_data):
    cart = {}
    total_items = 0
    total_cost = 0

    while True:
        item = input("Scan an item (press 'q' to exit): ").upper()

        if item == 'Q':
            logging.info("Exiting checkout.")
            return cart, total_items, total_cost

        if item not in prices_data:
            logging.warning(f"warning: Item '{item}' not found in pricing data.")

        else: 
            unit_price = np.round(prices_data[item].get("unit_price"), decimals=2)
            special_quantity = prices_data[item].get("special_quantity")
            special_price = np.round(prices_data[item].get("special_price"), decimals=2)

            # existing item or new item 
            if item in cart:
                cart[item]['quantity'] += 1
            else:
                cart[item] = {'quantity': 1}
            
            # bundle apply the special price, remaining still use the unit price
            if special_quantity > 0:
                special_bundle = cart[item]['quantity'] // special_quantity
                remaining_number = cart[item]['quantity'] % special_quantity
                cart[item]['total_price'] = np.round(special_bundle * special_price + remaining_number * unit_price, decimals=2)
            else:
                cart[item]['total_price'] = np.round(cart[item]['quantity'] * unit_price, decimals=2)
                
            total_items = sum(details['quantity'] for details in cart.values())
            total_cost = np.round(sum(details['total_price'] for details in cart.values()),decimals=2)

            logging.info(f"...So far Item Quantity: {total_items}, Total Cost: {total_cost}")

