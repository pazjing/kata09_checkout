# main.py
import logging
import sys
from load_prices import load_prices
from checkout import checkout

if __name__ == "__main__":

    logging.info("Loading up...")
    
    prices_data = load_prices()

    logging.info("Ready for checkout.")

    if prices_data: 
        cart, total_items, total_cost = checkout(prices_data)
        logging.info(f"...Total Item Quantity: {total_items}, Total Cost: {total_cost}")

    
