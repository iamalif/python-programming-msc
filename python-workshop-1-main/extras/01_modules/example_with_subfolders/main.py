"""
main.py - Importing from subfolders
===================================
Run this file: python main.py
"""

# Import modules from the utils subfolder
import utils.formatting as fmt
import utils.calculations as calc

# Or import specific functions
from utils.calculations import calculate_tax, calculate_discount

# Example usage
print(fmt.format_header("Sales Report"))
print()

revenue = 15000
cost = 9000
tax_rate = 0.25

# Using imported module with alias
tax = calc.calculate_tax(revenue, tax_rate)
margin = calc.calculate_profit_margin(revenue, cost)

print(f"Revenue:       {fmt.format_currency(revenue)}")
print(f"Cost:          {fmt.format_currency(cost)}")
print(f"Tax (25%):     {fmt.format_currency(tax)}")
print(f"Profit Margin: {fmt.format_percentage(margin)}")

# Using directly imported function
print()
print(f"After 10% discount: {fmt.format_currency(calculate_discount(revenue, 10))}")
