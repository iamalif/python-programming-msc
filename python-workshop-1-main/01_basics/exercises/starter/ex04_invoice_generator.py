"""
Exercise 04: Invoice Generator
==============================
Create a simple invoice based on user input.

Your task:
1. Get customer name and 3 items with their prices
2. Calculate subtotal, tax (25%), and total
3. Display a formatted invoice

Example interaction:
--------------------
=== Invoice Generator ===

Enter customer name: Johan Andersson
Enter item 1 name: Laptop Stand
Enter item 1 price: 299.00
Enter item 2 name: USB Hub
Enter item 2 price: 149.00
Enter item 3 name: Mouse Pad
Enter item 3 price: 79.00

========================================
              INVOICE
========================================
Customer: Johan Andersson

Items:
  Laptop Stand                  $299.00
  USB Hub                       $149.00
  Mouse Pad                      $79.00
----------------------------------------
Subtotal:                       $527.00
Tax (25%):                      $131.75
----------------------------------------
TOTAL:                          $658.75
========================================
"""

# Constants
TAX_RATE = 0.25

# TODO: Print header and get customer name
print("=== Invoice Generator ===")
customer_name = input("Enter customer name: ")


# TODO: Get 3 items with names and prices
item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1: "))
item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2: "))
item3_name = input("Enter name of item 3: ")
item3_price = float(input("Enter price of item 3: "))


# TODO: Calculate subtotal, tax, and total
subtotal = item1_price + item2_price + item3_price
tax = subtotal * TAX_RATE
total = subtotal + tax


# TODO: Print the formatted invoice
# Hint: For alignment, try {name:<30} for left-align
# and ${price:>7.2f} for right-aligned prices
print(f"Subtotal: {subtotal}, Tax: {tax}, Total: {total}")

