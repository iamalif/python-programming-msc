"""
03 - Default Parameters: Flexible Functions
===========================================
Default values make parameters optional.

Run this file: python 03_default_parameters.py
"""

# Function with default parameter
def calculate_shipping(order_total, rate=9.99):
    """Calculate shipping cost. Free shipping over $100."""
    if order_total >= 100:
        return 0
    return rate


print("=== Default Parameters ===")
print()

# Using the default rate
print("Order $50, default shipping:", calculate_shipping(50))
print("Order $150, default shipping:", calculate_shipping(150))

# Overriding the default
print("Order $50, express $14.99:", calculate_shipping(50, 14.99))


# Multiple default parameters
def format_price(amount, currency="$", decimals=2, show_symbol=True):
    """Format a price with customizable options."""
    if show_symbol:
        return f"{currency}{amount:,.{decimals}f}"
    else:
        return f"{amount:,.{decimals}f}"


print()
print("=== Multiple Defaults ===")
print()

# Using all defaults
print("Default:", format_price(1234.567))

# Changing some defaults
print("EUR:", format_price(1234.567, "€"))
print("No decimals:", format_price(1234.567, "$", 0))
print("No symbol:", format_price(1234.567, "$", 2, False))

# Using keyword arguments (can skip parameters)
print("Keyword args:", format_price(1234.567, decimals=1))


# Practical example: Sales tax calculator
def calculate_order_total(
    subtotal,
    tax_rate=0.25,
    discount_percent=0,
    shipping=0
):
    """
    Calculate final order total with all adjustments.

    Parameters:
    - subtotal: Base price before adjustments
    - tax_rate: Tax rate as decimal (default 25%)
    - discount_percent: Discount as percentage (default 0%)
    - shipping: Shipping cost (default 0)
    """
    discount = subtotal * (discount_percent / 100)
    after_discount = subtotal - discount
    tax = after_discount * tax_rate
    total = after_discount + tax + shipping

    return total, discount, tax


print()
print("=== Flexible Order Calculator ===")
print()

# Scenario 1: Standard order
print("Standard order ($200):")
total, disc, tax = calculate_order_total(200)
print(f"  Total: ${total:.2f}")

# Scenario 2: Member discount
print("\nMember order ($200, 10% off):")
total, disc, tax = calculate_order_total(200, discount_percent=10)
print(f"  Discount: ${disc:.2f}")
print(f"  Total: ${total:.2f}")

# Scenario 3: International shipping
print("\nInternational order ($200, shipping $25):")
total, disc, tax = calculate_order_total(200, shipping=25)
print(f"  Total: ${total:.2f}")

# Scenario 4: Everything custom
print("\nCustom order ($500, 15% off, 12% tax, $15 shipping):")
total, disc, tax = calculate_order_total(
    500,
    tax_rate=0.12,
    discount_percent=15,
    shipping=15
)
print(f"  Discount: ${disc:.2f}")
print(f"  Tax: ${tax:.2f}")
print(f"  Total: ${total:.2f}")
