__author__ = '8568922, Wolff', '8544494,Aktar'

menu = [
    {"name": "VUNKY-BURGER<", "typ": "main", "categorie": "vegan", "price": 12}
    {"name": "FALAFEL-BURGER", "typ": "main", "categorie": "vegan", "price": 13}
    {"name": "CLASSIC-BURGER", "typ": "main", "categorie": "beef", "price": 9}
    {"name": "CHEESE-BURGER", "typ": "main", "categorie": "beef", "price": 10}
    {"name": "FOREST-BURGER", "typ": "main", "categorie": "veggie", "price": 12 }
    {"name": "CHILT-BURGER", "typ": "main", "categorie": "beef, hot", "price": 12.5 }
    {"name": "PIZZA-MARGARITA", "typ": "main", "categorie": "vegan", "price:" 9}
    {"name": "PIZZA-HAWAI": "typ": "main", "categorie": "pork", "price": 10}
    {"name": "PIZZA-MOZZARELLA", "typ": "main", "categorie" : "vegan", "price": 10} 
    {"name": "WASSER (0,3)", "typ": "drink", "categorie": "alcohol-free", "price": 2}
    {"name": "WASSER (0,5)", "typ": "drink", "categorie": "alcohol-free", "price": 3.5}
    {"name": "COLA (0,4)", "typ": "drink", "categorie": "alcohol-free", "price": 3.5}
    {"name": "COLA (0,2)", "typ": "drink", "categorie": "alcohol-free", "price": 2.5 }
    {"name": "FANTA (0,4)", "typ": "drink", "categorie": "alcohol-free", "price": 3.5 }
    {"name": "FANTA (0,2)", "typ": "drink", "categorie": "alcohol-free", "price": 2.5 }
    {"name": "ICE-TEE (Pfirisch)", "typ": "drink", "categorie": "alcohol-free", "price": 4 }
    {"name": "ICE-TEE (Zitrone))", "typ": "drink", "categorie": "alcohol-free", "price": 4 }
    {"name": "BEER", "typ": "drink", "categorie": "alcohol", "price": 4 }
]

class Order:
    def __init__(self, meal_index: int, total_price, table: int):
        if meal_index < 0 or meal_index >= len(menu):
            raise IndexError("Invalid meal index.")
        self.meal = menu[meal_index]
        self.total_price = self.meal["price"]
        self.table = table
    def __str__(self, meal_index: int, total_price, table: int):
        print(f"Meal ID:" {meal_index}, "Meal:" {menu[meal_index]["name", "price"]}, "table:" {table})

class Table:
    def __init__(self, table_num):
        self.table_num = int(table_num)
    def __str__(self, table_num):
        return self.table_num

def take_order():
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
