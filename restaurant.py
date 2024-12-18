__author__ = '8568922, Wolff'

menu = [
    {
        "id": 1, "name": "vunky burger", "price": "12$"
        }
]

class order:
    def __init__(self, meal_index: int, total_price, table: int):
        if meal_index < 0 or meal_index >= len(menu):
            raise IndexError("Invalid meal index.")
        self.meal = menu[meal_index]
        self.total_price = self.meal["price"]
        self.table = table
    def __str__(self, meal_index: int, total_price, table: int):
        print(f"Meal ID:" {meal_index}, "Meal:" {menu[meal_index]["name"]}, "table:" )

class table:
    def __init__(self, table_num):
        self.table_num = int(table_num)


def take_order(table_num):
    table_num = input(table_num)
    table_order = input("Order: \n")
    if table_order in menu

def invoice_check(self, order):
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
