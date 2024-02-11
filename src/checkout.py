from load_prices import load_prices

def checkout(prices_data):
    cart = {}
    total_items = 0
    total_cost = 0

    while True:
        item = input("Scan an item (press 'q' to exit): ").upper()

        if item == 'Q':
            print("Exiting checkout.")
            break

        if item not in prices_data:
            print(f"Error: Item '{item}' not found in pricing data.")

        else: 
            unit_price = prices_data[item].get("unit_price")
            special_quantity = prices_data[item].get("special_quantity")
            special_price =  round(prices_data[item].get("special_price"),2)

            # existing item or new item 
            if item in cart:
                cart[item]['quantity'] += 1
            else:
                cart[item] = {'quantity': 1}
            
            # bundle apply the special price, remaining still use the unit price
            if special_quantity > 0:
                special_bundle = cart[item]['quantity'] // special_quantity
                remaining_number = cart[item]['quantity'] % special_quantity
                cart[item]['total_price'] = round(special_bundle * float(special_price) + remaining_number *  float(unit_price),2)
            else:
                cart[item]['total_price'] = round(cart[item]['quantity'] *  float(unit_price),2)
                
            total_items = sum(details['quantity'] for details in cart.values())
            total_cost = round(sum(details['total_price'] for details in cart.values()),2)

        print(f"...Cart: {cart}")

        print(f"...Total Item Quantity: {total_items}, Total Cost: {total_cost}")

if __name__ == "__main__":
    prices_data = load_prices()

    print("Ready for checkout. ")

    if prices_data: 
        checkout(prices_data)
