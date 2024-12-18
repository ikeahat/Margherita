__author__ = '8568922, Wolff', '8544494,Aktar'

menu = [
    {"name": "VUNKY-BURGER", "type": "main", "category": "vegan", "price": 12},
    {"name": "FALAFEL-BURGER", "type": "main", "category": "vegan", "price": 13},
    {"name": "CLASSIC-BURGER", "type": "main", "category": "beef", "price": 9},
    {"name": "CHEESE-BURGER", "type": "main", "category": "beef", "price": 10},
    {"name": "FOREST-BURGER", "type": "main", "category": "veggie", "price": 12},
    {"name": "CHILI-BURGER", "type": "main", "category": "beef, hot", "price": 12.5},
    {"name": "PIZZA-MARGARITA", "type": "main", "category": "vegan", "price": 9},
    {"name": "PIZZA-HAWAII", "type": "main", "category": "pork", "price": 10},
    {"name": "PIZZA-MOZZARELLA", "type": "main", "category": "vegan", "price": 10}, 
    {"name": "WATER (0.3L)", "type": "drink", "category": "alcohol-free", "price": 2},
    {"name": "WATER (0.5L)", "type": "drink", "category": "alcohol-free", "price": 3.5},
    {"name": "COLA (0.4L)", "type": "drink", "category": "alcohol-free", "price": 3.5},
    {"name": "COLA (0.2L)", "type": "drink", "category": "alcohol-free", "price": 2.5},
    {"name": "FANTA (0.4L)", "type": "drink", "category": "alcohol-free", "price": 3.5},
    {"name": "FANTA (0.2L)", "type": "drink", "category": "alcohol-free", "price": 2.5},
    {"name": "ICE-TEA (Peach)", "type": "drink", "category": "alcohol-free", "price": 4},
    {"name": "ICE-TEA (Lemon)", "type": "drink", "category": "alcohol-free", "price": 4},
    {"name": "BEER", "type": "drink", "category": "alcohol", "price": 4},
]


class Order:
    def __init__(self, meal_index: int, table: int):
        if meal_index < 0 or meal_index >= len(menu):
            raise IndexError("Invalid meal index.")
        self.meal = menu[meal_index]
        self.total_price = self.meal["price"]
        self.table = table

    def __str__(self):
        return f"Table {self.table}: {self.meal['name']} (${self.total_price})"

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
            print(f"{idx}: {item['name']} - {item['category']} - ${item['price']}")

        # Input meal index
        try:
            meal_index = int(input("\nEnter meal index from the menu: "))
            if meal_index < 0 or meal_index >= len(menu):
                print("Invalid meal index. Please try again.")
                continue
            # Add the order to the list
            orders.append(Order(meal_index=meal_index, table=table_num))
            print(f"Added {menu[meal_index]['name']} to the order.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Ask if the user wants to add more
        more = input("Is that all? (yes/no): ").strip().lower()
        if more in {"yes", "y"}:
            break
        elif more not in {"no", "n"}:
            print("Invalid response. Assuming 'no'.")
            continue

    # Print all orders for the table
    print("\nOrders for Table:", table_num)
    for order in orders:
        print(order)

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
