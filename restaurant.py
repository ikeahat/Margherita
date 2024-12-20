__author__ = '8568922, Wolff', '8544494,Aktar'
import csv

# Load the CSV file and create the menu list.
import csv

import csv

menu = []
with open('food.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        row['price'] = float(row['price'].replace(',', '.'))  # Make price a float and change the comma to a dot (bc english standard math notation).
        menu.append(row)

class Order:
    def __init__(self, meal_index: int, table: int):
        if meal_index < 0 or meal_index >= len(menu):
            raise IndexError("Invalid meal index.")
        self.meal = menu[meal_index]
        self.total_price = self.meal["price"]
        self.table = table
        self.special_requests = []

    def __str__(self):
        special_str = f" ({', '.join(self.special_requests)})" if self.special_requests else ""
        return f"Table {self.table}: {self.meal['name']} - ${self.total_price:.2f}{special_str}"
    
    def create_invoice(self):
        # Save invoice to a .txt file
        invoice_filename = f"invoice_table_{self.table}.txt"
        with open(invoice_filename, "a") as f:
            f.write(f"Invoice for Table {self.table}\n")
            f.write(f"Meal: {self.meal['name']}\n")
            f.write(f"Category: {self.meal['categorie']}\n")
            f.write(f"Special Requests: {', '.join(self.special_requests) if self.special_requests else 'None'}\n")
            f.write(f"Total Price: ${self.total_price:.2f}\n")
            f.write("\n" + "-"*40 + "\n")
        print(f"Invoice for Table {self.table} saved to {invoice_filename}")

    def add_special_request(self, request: str):
        if "extra" in request.lower():  # Assuming any request containing "extra" is an add-on
            self.total_price += 1  # Increase the price by 1 Euro
            self.special_requests.append(request)
        elif "no" in request.lower():  # Assuming requests with "no" are removing ingredients
            self.special_requests.append(request)  # No price change for removal

class Table:
    def __init__(self, table_num: int):
        self.table_num = table_num

    def __str__(self):
        return f"Table {self.table_num}"

def take_order():
    orders = []  # List to store all orders for the table
    table_num = int(input("Enter table number: "))  # Input table number

    while True:
        # Display menu
        print("\nMenu:")
        for idx, item in enumerate(menu):
            print(f"{idx}: {item['name']} - {item['categorie']} - ${item['price']:.2f}")

        # Input meal index
        try:
            meal_index = int(input("\nEnter meal index from the menu (or 'stop' to finish): "))
            if meal_index == "stop":
                break

            if meal_index < 0 or meal_index >= len(menu):
                print("Invalid meal index. Please try again.")
                continue
            # Add the order to the list
            order = Order(meal_index=meal_index, table=table_num)
            orders.append(order)
            print(f"Added {menu[meal_index]['name']} to the order.")

            # After adding the item, ask for special requests
            while True:
                special_request = input("\nDo you want to add a special request (e.g., extra cheese, no onions)? (yes/no): ").strip().casefold()
                if special_request in {"yes", "y"}:
                    request = input(f"Enter special request for {menu[meal_index]['name']}: ").strip()
                    order.add_special_request(request)
                    print(f"Added special request: {request}")
                    break
                elif special_request in {"no", "n"}:
                    break
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Ask if the user wants to add more
        more = input("Is that all? (yes/no): ").strip().casefold()
        if more in {"yes", "y"}:
            break
        elif more not in {"no", "n"}:
            print("Invalid response. Assuming 'no'.")
            continue
    
    print("\nOrders for Table:", table_num)
    for order in orders:
        print(order)
    # Calculate and show total price
    total_price = sum(order.total_price for order in orders)
    print(f"\nTotal Price: ${total_price:.2f}")

    # Ask for final changes
    while True:
        change = input("\nWould you like to make changes to the order? (yes/no): ").strip().casefold()
        if change in {"yes", "y"}:
            # Show current orders
            print("\nCurrent Orders:")
            for idx, order in enumerate(orders):
                print(f"{idx}: {order}")

            # Remove or add an item
            action = input("Do you want to (remove/add) an item? ").strip().casefold()
            if action == "remove":
                try:
                    remove_idx = int(input("Enter the index of the item to remove: "))
                    if 0 <= remove_idx < len(orders):
                        removed_order = orders.pop(remove_idx)
                        print(f"Removed {removed_order.meal['name']} from the order.")
                        total_price = sum(order.total_price for order in orders)
                        print(f"Updated Total Price: ${total_price:.2f}")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input.")
            elif action == "add":
                try:
                    meal_index = int(input("Enter meal index to add: "))
                    if 0 <= meal_index < len(menu):
                        new_order = Order(meal_index=meal_index, table=table_num)
                        orders.append(new_order)
                        print(f"Added {menu[meal_index]['name']} to the order.")
                        
                        # After adding the item, ask for special requests
                        while True:
                            special_request = input("\nDo you want to add a special request (e.g., extra cheese, no onions)? (yes/no): ").strip().casefold()
                            if special_request in {"yes", "y"}:
                                request = input(f"Enter special request for {menu[meal_index]['name']}: ").strip()
                                new_order.add_special_request(request)
                                print(f"Added special request: {request}")
                                break
                            elif special_request in {"no", "n"}:
                                break
                            else:
                                print("Invalid response. Please enter 'yes' or 'no'.")
                        
                        total_price = sum(order.total_price for order in orders)
                        print(f"Updated Total Price: ${total_price:.2f}")
                    else:
                        print("Invalid meal index.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("Invalid action. Please enter 'remove' or 'add'.")

        elif change in {"no", "n"}:
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    # Print final orders and create invoice
    print("\nFinal Orders for Table:", table_num)
    for order in orders:
        print(order)

    print(f"\nFinal Total Price: ${total_price:.2f}")
    print("\nCreating Invoice...\n")
    for order in orders:
        order.create_invoice()

take_order()

'''def invoice_check(self, order):
    # Offer user to make final changes. 
    # Add, del or edit items off the list.
    # call create invoice maybe recursively and create a new 
    # invoice with every change? idk if thats possible
    
def create_invoice(self, order):
    print(order)
    
def save_invoice():
    # save final invoice in .txt file
    
def invoice():
    # if SKIP by console input: call create_invoice() 
    # else: call invoice_check() 
    # call save_invoice()
    # if SKIP by console input: call create_invoice() 
    # else: call invoice_check() 
    # call save_invoice()'''
