"""
03 - User Input: Getting Data from Users
========================================
The input() function pauses the program and waits for user input.

Run this file: python 03_user_input.py
"""

# Basic input - always returns a STRING
print("=== Customer Registration ===")
print()

customer_name = input("Enter customer name: ")
print("Welcome,", customer_name)

# IMPORTANT: input() ALWAYS returns a string!
# Even if the user types a number, it's stored as text

print()
age_text = input("Enter your age: ")
print("You entered:", age_text)
print("Type of input:", type(age_text))  # <class 'str'>

# To use numbers for calculations, convert the string:
# int()   - converts to whole number
# float() - converts to decimal number

print()
print("=== Order Entry ===")
print()

# Convert to integer
quantity = int(input("Enter quantity: "))
print("You ordered", quantity, "items")

# Convert to float
unit_price = float(input("Enter unit price: "))
print("Price per unit:", unit_price)

# Now we can do math!
total = quantity * unit_price
print("Total cost:", total)

# You can combine input and conversion in one line
print()
discount_percent = float(input("Enter discount percentage: "))
discount_amount = total * (discount_percent / 100)
final_price = total - discount_amount
print("Final price after discount:", final_price)
