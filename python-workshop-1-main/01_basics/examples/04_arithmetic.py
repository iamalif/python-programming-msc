"""
04 - Arithmetic: Calculations in Python
=======================================
Python supports all standard mathematical operations.

Run this file: python 04_arithmetic.py
"""

# Basic arithmetic operators
print("=== Basic Operators ===")
print()

a = 100
b = 30

print(f"{a} + {b} = {a + b}")    # Addition
print(f"{a} - {b} = {a - b}")    # Subtraction
print(f"{a} * {b} = {a * b}")    # Multiplication
print(f"{a} / {b} = {a / b}")    # Division (always returns float)
print(f"{a} // {b} = {a // b}")  # Integer division (rounds down)
print(f"{a} % {b} = {a % b}")    # Modulo (remainder)
print(f"{a} ** 2 = {a ** 2}")    # Exponentiation (power)

# Business calculations example
print()
print("=== Revenue Calculations ===")
print()

units_sold = 150
price_per_unit = 49.99
cost_per_unit = 32.50

revenue = units_sold * price_per_unit
cost = units_sold * cost_per_unit
profit = revenue - cost
profit_margin = (profit / revenue) * 100

print(f"Units sold: {units_sold}")
print(f"Revenue: ${revenue}")
print(f"Cost: ${cost}")
print(f"Profit: ${profit}")
print(f"Profit margin: {profit_margin}%")

# Order of operations (PEMDAS: Parentheses, Exponents, *, /, +, -)
print()
print("=== Order of Operations ===")
print()

# Without parentheses - multiplication happens first
result1 = 10 + 5 * 2
print(f"10 + 5 * 2 = {result1}")  # 20, not 30

# With parentheses - addition happens first
result2 = (10 + 5) * 2
print(f"(10 + 5) * 2 = {result2}")  # 30

# Compound assignment operators (shortcuts)
print()
print("=== Compound Operators ===")
print()

stock = 100
print(f"Starting stock: {stock}")

stock += 50   # Same as: stock = stock + 50
print(f"After restock (+50): {stock}")

stock -= 30   # Same as: stock = stock - 30
print(f"After sales (-30): {stock}")

stock *= 2    # Same as: stock = stock * 2
print(f"After doubling (*2): {stock}")
