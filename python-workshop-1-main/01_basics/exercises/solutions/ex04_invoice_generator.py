"""
Exercise 04: Invoice Generator - SOLUTION
=========================================
"""

# Constants
TAX_RATE = 0.25

# Print header and get customer name
print("=== Invoice Generator ===")
print()
customer_name = input("Enter customer name: ")

# Get 3 items with names and prices
item1_name = input("Enter item 1 name: ")
item1_price = float(input("Enter item 1 price: "))
item2_name = input("Enter item 2 name: ")
item2_price = float(input("Enter item 2 price: "))
item3_name = input("Enter item 3 name: ")
item3_price = float(input("Enter item 3 price: "))

# Calculate subtotal, tax, and total
subtotal = item1_price + item2_price + item3_price
tax = subtotal * TAX_RATE
total = subtotal + tax

# Print the formatted invoice
print()
print("=" * 40)
print(f"{'INVOICE':^40}")
print("=" * 40)
print(f"Customer: {customer_name}")
print()
print("Items:")
print(f"  {item1_name:<28} ${item1_price:>7.2f}")
print(f"  {item2_name:<28} ${item2_price:>7.2f}")
print(f"  {item3_name:<28} ${item3_price:>7.2f}")
print("-" * 40)
print(f"{'Subtotal:':<30} ${subtotal:>7.2f}")
print(f"{'Tax (25%):':<30} ${tax:>7.2f}")
print("-" * 40)
print(f"{'TOTAL:':<30} ${total:>7.2f}")
print("=" * 40)
