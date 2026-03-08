"""
02 - Variables: Storing Data
============================
Variables are containers that store values for later use.

Run this file: python 02_variables.py
"""

# Creating variables - just assign a value with =
product_name = "Laptop Pro X1"
price = 999.99
quantity_in_stock = 45
is_available = True

# Print the variables
print("Product Information")
print("-------------------")
print("Name:", product_name)
print("Price:", price)
print("In Stock:", quantity_in_stock)
print("Available:", is_available)

# Python has several data types
# str   - text (strings)          "hello", 'world'
# int   - whole numbers           42, -17, 0
# float - decimal numbers         3.14, -0.5, 99.99
# bool  - True or False           True, False

# Check the type of a variable
print()
print("Variable Types")
print("--------------")
print("product_name is:", type(product_name))
print("price is:", type(price))
print("quantity_in_stock is:", type(quantity_in_stock))
print("is_available is:", type(is_available))

# Variables can be updated
print()
print("Updating stock...")
quantity_in_stock = 44  # Sold one item
print("New stock level:", quantity_in_stock)

# Good variable naming conventions:
# - Use lowercase with underscores: customer_name, total_sales
# - Be descriptive: 'price' is better than 'p'
# - Avoid Python keywords: don't use 'print', 'if', 'for', etc.

# Constants (values that shouldn't change) use UPPERCASE
TAX_RATE = 0.25
MAX_DISCOUNT = 0.50

print()
print("Tax rate:", TAX_RATE)
print("Max discount:", MAX_DISCOUNT)
