# shopping_cart.py

import operator
from datetime import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

user_input = ""
product_scanned = -1
valid_product = False
purchases = []
now = datetime.now()
time_to_print = ""
subtotal = 0.00
final_total = 0.00

TAX_RATE = 0.08

#### SECTION ONE: Recieve inputs from user. 
print("Welcome to the Register System 2000.")
print("A new order has been commenced. Please enter identifying product numbers or 'DONE' when finished. Invalid responses will be rejected.")

while user_input != "DONE" : 
    valid_product = False
    product_scanned = -1
    user_input = input("Please enter product identifier: ")
    #input validation
    for prod in products: 
        if user_input == str(prod['id']):
            product_scanned = prod['id'] - 1
            valid_product = True
    if valid_product:  
        print(products[product_scanned]['name'],"added to cart.")
        purchases.append(products[product_scanned])
        subtotal += products[product_scanned]['price']
    else:
        print("Invalid selection.")

final_total = subtotal * (1 + TAX_RATE)

if now.hour > 12:
    time_to_print = now.strftime("%I:%M") + " PM"
else: 
    time_to_print = now.strftime("%I:%M") + " AM"

#### END SECTION ONE

#### SECTION TWO: 
print(
    "\n\n#############################################",
    "\n         RECEIPT FROM SAM'S GROCERIES        ",
    "\n#############################################",
    "\n   CHECKOUT AT", now.date(), time_to_print,
    "\n#############################################",
    "\n           WWW.SAMSGROCERIES.COM",
    "\n#############################################"
    )
print("             PURCHASE SUMMARY:")
for purch in purchases:
    print(f"- {purch['name']} ({to_usd(purch['price'])})")
print("###########################################")
print("      SUBTOTAL:", to_usd(subtotal))
print("           TAX:", to_usd(subtotal * TAX_RATE))
print("         TOTAL:", to_usd(final_total))
print("###########################################")
print("            THANK YOU! COME AGAIN!")
