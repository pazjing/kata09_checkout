# main.py

from load_prices import load_prices
from checkout import checkout

if __name__ == "__main__":
    prices_data = load_prices()

    print("Ready for checkout. ")

    if prices_data: 
        checkout(prices_data)
