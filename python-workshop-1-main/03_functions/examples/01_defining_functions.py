"""
01 - Defining Functions: Reusable Code
======================================
Functions let you organize code into reusable blocks.

Run this file: python 01_defining_functions.py
"""

# Basic function - no parameters
def print_separator():
    """Print a line of dashes."""
    print("-" * 40)


# Call the function
print("=== Basic Functions ===")
print_separator()
print("This is between separators")
print_separator()

# Function with parameters
def greet_customer(name):
    """Greet a customer by name."""
    print(f"Welcome, {name}! How can we help you today?")


print()
print("=== Functions with Parameters ===")
greet_customer("Anna")
greet_customer("Erik")
greet_customer("Maria")

# Function with multiple parameters
def calculate_total(price, quantity):
    """Calculate and display total price."""
    total = price * quantity
    print(f"{quantity} items at ${price:.2f} each = ${total:.2f}")


print()
print("=== Multiple Parameters ===")
calculate_total(29.99, 3)
calculate_total(15.50, 10)

# Function that uses other functions
def display_order(customer, product, price, quantity):
    """Display a complete order summary."""
    print_separator()
    print("ORDER CONFIRMATION")
    print_separator()
    greet_customer(customer)
    print(f"Product: {product}")
    calculate_total(price, quantity)
    print_separator()


print()
print("=== Combining Functions ===")
display_order("Johan", "Wireless Mouse", 49.99, 2)

# Why use functions?
# 1. Avoid repetition - write once, use many times
# 2. Organization - break complex tasks into smaller parts
# 3. Readability - give meaningful names to blocks of code
# 4. Maintainability - change in one place, works everywhere
