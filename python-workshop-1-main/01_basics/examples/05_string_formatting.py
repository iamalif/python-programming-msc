"""
05 - String Formatting: Professional Output
===========================================
f-strings (formatted string literals) are the modern way to format output.

Run this file: python 05_string_formatting.py
"""

# f-strings - prefix the string with 'f' and use {variable}
product = "Wireless Headphones"
price = 79.99
quantity = 3

print("=== Basic f-strings ===")
print()
print(f"Product: {product}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity}")  # Can include expressions!

# Formatting numbers
print()
print("=== Number Formatting ===")
print()

revenue = 15847.4567
percentage = 0.2341

# Decimal places: {value:.Nf} where N is number of decimals
print(f"Revenue: ${revenue:.2f}")      # 2 decimal places
print(f"Percentage: {percentage:.1%}") # As percentage with 1 decimal

# Large numbers with thousand separators
big_number = 1500000
print(f"Sales: ${big_number:,}")       # Adds commas: 1,500,000
print(f"Sales: ${big_number:,.2f}")    # Commas + 2 decimals

# Width and alignment
print()
print("=== Alignment & Padding ===")
print()

# {value:>10} = right align in 10 characters
# {value:<10} = left align in 10 characters
# {value:^10} = center in 10 characters

items = [
    ("Laptop", 999.99),
    ("Mouse", 29.99),
    ("Keyboard", 149.99),
]

print(f"{'Product':<15} {'Price':>10}")
print("-" * 25)
for name, price in items:
    print(f"{name:<15} ${price:>9.2f}")

# Creating a formatted report
print()
print("=== Sales Report ===")
print()

company = "TechStore Inc."
month = "January"
total_sales = 45892.50
target = 50000
achievement = (total_sales / target) * 100

print("=" * 40)
print(f"{'MONTHLY SALES REPORT':^40}")
print("=" * 40)
print(f"Company:     {company}")
print(f"Period:      {month} 2025")
print("-" * 40)
print(f"Total Sales: ${total_sales:>15,.2f}")
print(f"Target:      ${target:>15,.2f}")
print(f"Achievement: {achievement:>15.1f}%")
print("=" * 40)
