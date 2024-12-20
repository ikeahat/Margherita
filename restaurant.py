__author__ = '8568922, Wolff', '8544494,Aktar'

import csv  # To import food.csv-file.
from datetime import datetime  # To save time and date of invoice creation.

menu = []  # To save items in list.

# Read menu data from CSV.
with open('food.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    # Loop thru all rows.
    for row in reader:
        row['price'] = float(row['price'].replace(',', '.'))  
        # Make price a float and change the comma to a dot (bc english standard math notation).
        menu.append(row)  # Add to menu list.

class Order:
    # Initialize the order class.
    def __init__(self, meal_index: int, table: int):
        # Meal index can't be unter 0 oder over the length of the menu - 1
        if meal_index < 0 or meal_index > len(menu) - 1:
            # Raise an error.
            raise IndexError("Invalid meal index.")
        # Start up all parameters of the class.
        self.meal = menu[meal_index]
        # Only looks at the index key, not all values of menu.
        self.total_price = self.meal["price"]  
        # Only looks at the price key, not all values of menu.
        self.table = table
        self.special_requests = []  
        # Empty list to store.

    def __str__(self):
        # Make readable/printable.
        special_str = f" ({', '.join(self.special_requests)})" if self.special_requests else ""
        # Return print statement for good readability of order summary.
        # ":.2f" converts 10 -> 10.00, and 10.5 -> 10.50 !!! 
        # How cool, wth! I shared this piece of code with all my friends and the're all 
        # implementing it now. :D
        # Source: https://www.geeksforgeeks.org/how-to-round-floating-value-to-two-decimals-in-python/
        return f"Table {self.table}: {self.meal['name']} - ${self.total_price:.2f}{special_str}"

    def create_invoice(self):
        timestamp = str(datetime.now())
        # Save invoice to a .txt file
        invoice_filename = f"invoices:_{self.table}.txt"
        # Create name.
        with open(invoice_filename, "a") as f:
            # Create opening text thats being saved.
            f.write(f"Invoice for Table {self.table} {timestamp}\n")
            f.write(f"Meal: {self.meal['name']}\n")
            f.write(f"Category: {self.meal['categorie']}\n")
            f.write(f"Special Requests: {', '.join(self.special_requests) if self.special_requests else 'None'}\n")
            f.write(f"Total Price: ${self.total_price:.2f}\n")
            # 40 "-" long line to separate visually.
            f.write("\n" + "-"*40 + "\n")
        print(f"Invoice for Table {self.table} saved to {invoice_filename}")

    def add_special_request(self, request: str):
        '''
        Allows for adding and removing things off the meals checking for keywords.
        '''
        if "extra" in request.casefold(): 
            # Requests starting with "extra" is an add-on, that increases the price.
            self.total_price += 1
            self.special_requests.append(request)
        elif "no" in request.casefold():  # Requests with "no" are removing ingredients. No price change.
            self.special_requests.append(request)

class Table:
    # Initialize the table class. Saves a number, and is used inside the order function.
    def __init__(self, table_num: int):
        self.table_num = table_num
    # Formats.
    def __str__(self):
        return f"Table {self.table_num}"

number_of_tables = 0  # Number of tables in the restaurant.

def setup():
    global number_of_tables
    while True:
        try:
            number_of_tables = int(input("Enter the number of tables in the restaurant: "))
            if number_of_tables <= 0:
                print("Number of tables must be greater than 0.")
            else:
                print(f"Setup complete! The restaurant has {number_of_tables} tables.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def take_order():
    if number_of_tables <= 0:
        print("Error: Please run the setup first using the '!setup' command.")
        return

    orders = []  # List to store all orders for the table.
    
    # Validate table number input
    while True:
        table_num = int(input("Enter table number: "))  # Input table number.
        if 1 <= table_num <= number_of_tables:
            break
        else:
            print(f"Invalid table number. Please enter a number between 1 and {number_of_tables}.")

    timestamp = str(datetime.now())
    
    while True:
        # Display menu.
        print("\nMenu:")
        for idx, item in enumerate(menu):
            # Prints in a formatted way.
            print(f"{idx}: {item['name']} - {item['categorie']} - ${item['price']:.2f}")

        # Let user know they can quit the program and how.
        user_input = input("""\nEnter meal index from the menu (or enter 'end' to quit the program, 
                           and start over): """).strip().casefold()
        
        if user_input == "end":
            break
        
        try:
            meal_index = int(user_input)
            # Can't have an index that's non-existent in the menu.
            if meal_index < 0 or meal_index >= len(menu):
                print("Invalid meal index. Please try again.")
                continue
            # Add the order to the list.
            order = Order(meal_index=meal_index, table=table_num)
            orders.append(order)
            # Print what's happening.
            print(f"Added {menu[meal_index]['name']} to the order.")

            # After adding the item, ask for special requests.
            while True:
                special_request = input("""\nDo you want to add a special request 
                                        (e.g., extra cheese, no onions)? (yes/no): 
                                        """).strip().casefold()
                if special_request in {"yes", "y"}:
                    while True:
                        request = input(f"""Enter special request for
                                        {menu[meal_index]['name']} (or type 'done' to finish): 
                                        """).strip()
                        # This exists to let the user add multiple special requests to one item.
                        if request.casefold() == "done":
                            # It would be good, if "done" skipped the "Do you want to add a special 
                            # request (e.g., extra cheese, no onions)? (yes/no):" question. because 
                            # why ask twice. Idk how to change this.
                            break
                        order.add_special_request(request)
                        print(f"Added special request: {request}")
                elif special_request in {"no", "n"}:
                    break
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Ask if the user wants to add more.
        more = input("Is that all? (yes/no): ").strip().casefold()
        if more in {"yes", "y"}:
            break
        elif more not in {"no", "n"}:
            # Assume no, because it doesnt matter anyway if they misspell accidentally it will 
            # loop anyways.
            print("Invalid response. Assuming 'no'.")
            continue
    
    # Print provisional bill.
    print("\nOrders for Table:", table_num)
    for order in orders:
        print(order)

    # Calculate and total price.
    total_price = sum(order.total_price for order in orders)
    # Print datetime.
    print(f"\n{timestamp}")

    # Print final orders and create invoice.
    print("\nFinal Orders for Table:", table_num)
    for order in orders:
        print(order)

    print(f"\nFinal Total Price: ${total_price:.2f}")
    print("\nCreating Invoice...\n")
    for order in orders:
        order.create_invoice()


def main():
    '''
    Main() is a setup function that welcoms the user and prints the necessary commands to set up 
    the system (Asks how many tables the restaurant has, so it's customizable, and doesn't let a 
    server accidentally input table 400/ will let them know).
    '''
    print("Welcome to the Restaurant Management System!")
    print("Commands:")
    print("  !setup - Configure the restaurant (number of tables).")
    print("  !order - Take an order.")
    print("  !exit  - Exit the program.")
    while True:
        command = input("\nEnter a command: ").strip().casefold()
        if command == "!setup":
            setup()
        elif command == "!order":
            take_order()
        elif command == "!exit":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")
         
main()