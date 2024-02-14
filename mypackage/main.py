# main.py
import logging
from load_prices import load_prices
from checkout import checkout

if __name__ == "__main__":

    logging.info("Loading up...")

    prices_data = load_prices()

    logging.info("Ready for checkout.")

    if prices_data: 
        checkout(prices_data)
    
