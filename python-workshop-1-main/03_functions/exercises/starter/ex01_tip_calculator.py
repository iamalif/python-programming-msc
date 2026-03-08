"""
Exercise 01: Tip Calculator
===========================
Create a function to calculate tips at a restaurant.

Your task:
1. Create a function called calculate_tip that takes:
   - bill_amount (required)
   - tip_percent (optional, default 15)
2. The function should return the tip amount
3. Test with the examples below

Expected output:
----------------
=== Tip Calculator ===

Bill: $85.00
15% tip: $12.75
20% tip: $17.00
10% tip: $8.50
"""

# TODO: Define the calculate_tip function
# Remember: tip = bill_amount * (tip_percent / 100)
def calculate_tip(bill_amount, tip_percent = 15):
    tip_amount = bill_amount * (tip_percent / 100)
    return tip_amount


# Test the function
print("=== Tip Calculator ===")
print()

bill = 85.00
print(f"Bill: ${bill:.2f}")

# TODO: Call calculate_tip with default tip (15%)
# tip_15 = ...
# print(f"15% tip: ${tip_15:.2f}")
tip_15 = calculate_tip(bill)
print(f"15% tip: ${tip_15:.2f}")

# TODO: Call calculate_tip with 20% tip
# tip_20 = ...
# print(f"20% tip: ${tip_20:.2f}")
tip_20 = calculate_tip(bill, 20)
print(f"20% tip: ${tip_20:.2f}")

# TODO: Call calculate_tip with 10% tip
# tip_10 = ...
# print(f"10% tip: ${tip_10:.2f}")
tip_10 = calculate_tip(bill, 10)
print(f"20% tip: ${tip_10:.2f}")

