"""
Exercise 03: Discount System - SOLUTION
=======================================
"""

def calculate_price(base_price, quantity=1, member_discount=0):
    """
    Calculate final price with quantity and member discounts.

    Quantity discounts:
    - 10+ items: 5% off
    - 25+ items: 10% off
    - 50+ items: 15% off

    Member discount applied after quantity discount.
    """
    # Calculate subtotal
    subtotal = base_price * quantity

    # Determine quantity discount
    if quantity >= 50:
        qty_discount = 0.15
    elif quantity >= 25:
        qty_discount = 0.10
    elif quantity >= 10:
        qty_discount = 0.05
    else:
        qty_discount = 0

    # Apply quantity discount
    after_qty_discount = subtotal * (1 - qty_discount)

    # Apply member discount
    final_price = after_qty_discount * (1 - member_discount / 100)

    # Calculate savings
    savings = subtotal - final_price

    return final_price, savings


# Test the function
print("=== Discount System ===")
print()

# Test 1: Single item
print("Single item ($50):")
price, savings = calculate_price(50)
print(f"  Final price: ${price:.2f}")
print(f"  You saved: ${savings:.2f}")

# Test 2: 15 items (5% quantity discount)
print("\n15 items ($50 each):")
price, savings = calculate_price(50, 15)
print(f"  Final price: ${price:.2f}")
print(f"  You saved: ${savings:.2f}")

# Test 3: 30 items with 5% member discount (10% qty + 5% member)
print("\n30 items ($50 each), 5% member:")
price, savings = calculate_price(50, 30, 5)
print(f"  Final price: ${price:.2f}")
print(f"  You saved: ${savings:.2f}")
