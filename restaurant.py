__author__ = '8568922, Wolff'
menu = [
    {
        "id": 1, "name" = "vunky burger", price = "12$"
     }
    {
        
    }
]

class meal:
    def __init__(self, name, type, category, price):
        self.name = name
        self.type = type
        self.category = category
        self.price = price
    def __str__(self):
        return f"Meal(name={self.name}, type={self.type}, category={self.category}, price={self.price})"

# meals mit Klasse hard coden ? oder importen?
# test
vunky_burger = meal("vunky burger", "main", "vegan", "12")
print(vunky_burger)

'''class order:
    def __init__(self, meal, price):
        self.meal = meal
        self.price = price

class table:
    def __init__(self, table_num, customers, order):
        self.table_num = int(table_num)
        self.customers = int(customers)
        self.order = order

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
    # call save_invoice()'''