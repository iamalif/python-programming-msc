"""
Exercise 03: Discount System
============================
Create a pricing function with tiered discounts.

Your task:
1. Create a function called calculate_price that takes:
   - base_price (required)
   - quantity (optional, default 1)
   - member_discount (optional, default 0)
2. Apply quantity discounts:
   - 10+ items: 5% off
   - 25+ items: 10% off
   - 50+ items: 15% off
3. Apply member discount AFTER quantity discount
4. Return final price and total savings

Expected output:
----------------
=== Discount System ===

Single item ($50):
  Final price: $50.00
  You saved: $0.00

15 items ($50 each):
  Final price: $712.50
  You saved: $37.50

30 items ($50 each), 5% member:
  Final price: $1,282.50
  You saved: $217.50
"""

def calculate_price(base_price, quantity=1, member_discount=0):
    total_cost = base_price * quantity
    discount = 0

    if quantity>50:
       discount = 15
    elif quantity>25:
        discount = 10
    elif quantity>10:
        discount = 5
    
    discount_amount = total_cost*(discount/100)
    new_cost = total_cost - discount_amount

    if member_discount >= 0:
        member_discount_amount = new_cost*(member_discount/100)
    
    final_cost = new_cost - member_discount_amount

    return final_cost

print(calculate_price(50, 15, 5))


# member discount calc faulty
    



# TODO: Define the calculate_price function
# Steps inside function:
#   1. Calculate subtotal (base_price * quantity)
#   2. Determine quantity discount based on quantity
#   3. Apply quantity discount to subtotal
#   4. Apply member discount to the result
#   5. Calculate savings (subtotal - final_price)
#   6. Return final_price and savings


# Test the function
print("=== Discount System ===")
print()

# Test 1: Single item
print("Single item ($50):")
# price, savings = calculate_price(50)
# print(f"  Final price: ${price:.2f}")
# print(f"  You saved: ${savings:.2f}")

# Test 2: 15 items (5% quantity discount)
print("\n15 items ($50 each):")
# price, savings = calculate_price(50, 15)
# print(f"  Final price: ${price:.2f}")
# print(f"  You saved: ${savings:.2f}")

# Test 3: 30 items with 5% member discount (10% qty + 5% member)
print("\n30 items ($50 each), 5% member:")
# price, savings = calculate_price(50, 30, 5)
# print(f"  Final price: ${price:.2f}")
# print(f"  You saved: ${savings:.2f}")

