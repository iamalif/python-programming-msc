"""
02 - Return Values: Getting Results from Functions
==================================================
The return statement sends a value back to the caller.

Run this file: python 02_return_values.py
"""

# Function that returns a value
def calculate_tax(amount, tax_rate=0.25):
    """Calculate tax on an amount."""
    tax = amount * tax_rate
    return tax


# Using the returned value
print("=== Single Return Value ===")
print()

price = 100
tax = calculate_tax(price)
total = price + tax

print(f"Price: ${price:.2f}")
print(f"Tax (25%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Return value in expressions
print()
final_price = 500 + calculate_tax(500)
print(f"Quick calculation: ${final_price:.2f}")


# Function that returns multiple values
def analyze_sales(sales_list):
    """Analyze sales data and return key metrics."""
    total = sum(sales_list)
    count = len(sales_list)
    average = total / count if count > 0 else 0
    highest = max(sales_list) if count > 0 else 0
    lowest = min(sales_list) if count > 0 else 0

    return total, average, highest, lowest


print()
print("=== Multiple Return Values ===")
print()

weekly_sales = [1200, 950, 1400, 1100, 1800, 2100, 1500]

# Unpack multiple return values
total, avg, high, low = analyze_sales(weekly_sales)

print("Weekly Sales Analysis:")
print(f"Total: ${total:,}")
print(f"Average: ${avg:,.2f}")
print(f"Highest: ${high:,}")
print(f"Lowest: ${low:,}")


# Practical example: Price calculator
def calculate_discounted_price(original_price, discount_percent):
    """Calculate price after discount and savings."""
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price, discount_amount


print()
print("=== Discount Calculator ===")
print()

original = 299.99
discount = 15

new_price, savings = calculate_discounted_price(original, discount)

print(f"Original: ${original:.2f}")
print(f"Discount: {discount}%")
print(f"You save: ${savings:.2f}")
print(f"Final price: ${new_price:.2f}")
