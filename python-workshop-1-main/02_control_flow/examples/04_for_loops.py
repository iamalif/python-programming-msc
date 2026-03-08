"""
04 - For Loops: Iterating Over Sequences
========================================
For loops are perfect when you know how many times to repeat.

Run this file: python 04_for_loops.py
"""

# Basic for loop with range()
print("=== range() Basics ===")
print()

# range(5) generates: 0, 1, 2, 3, 4
print("range(5):")
for i in range(5):
    print(f"  i = {i}")

# range(start, stop) - from start up to (not including) stop
print("\nrange(1, 6):")
for i in range(1, 6):
    print(f"  i = {i}")

# range(start, stop, step) - with custom step
print("\nrange(0, 10, 2) - even numbers:")
for i in range(0, 10, 2):
    print(f"  i = {i}")

# Processing sales data
print()
print("=== Weekly Sales Report ===")
print()

daily_sales = [1250, 980, 1500, 1320, 1680, 2100, 890]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

total_sales = 0

for i in range(7):
    day = days[i]
    sales = daily_sales[i]
    total_sales += sales
    print(f"{day}: ${sales:,}")

print("-" * 15)
print(f"Total: ${total_sales:,}")
print(f"Average: ${total_sales / 7:,.2f}")

# Calculating running totals
print()
print("=== Monthly Revenue Growth ===")
print()

monthly_revenue = [45000, 52000, 48000, 61000, 58000, 72000]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

cumulative = 0
for i in range(len(monthly_revenue)):
    cumulative += monthly_revenue[i]
    print(f"{months[i]}: ${monthly_revenue[i]:>6,}  (YTD: ${cumulative:>7,})")

# Nested loops - multiplication table
print()
print("=== Price Matrix (Qty x Unit Price) ===")
print()

quantities = [1, 5, 10, 25]
unit_price = 12.99

print(f"{'Qty':<6}", end="")
print("Total")
print("-" * 15)

for qty in quantities:
    total = qty * unit_price
    print(f"{qty:<6} ${total:>7.2f}")

# Using enumerate (bonus - shows index and value)
print()
print("=== Top Products (with ranking) ===")
print()

products = ["Laptop", "Phone", "Tablet", "Headphones"]

for rank, product in enumerate(products, start=1):
    print(f"#{rank}: {product}")

# Some personal tests to double-check knowledge
for i in range(5):
    print(i)

test_list = ["a", "b", "c"]
for i in range(len(test_list)):
    print(i)
