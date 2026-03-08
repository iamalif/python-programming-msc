"""
Exercise 01: Tip Calculator - SOLUTION
======================================
"""

def calculate_tip(bill_amount, tip_percent=15):
    """Calculate tip amount based on bill and percentage."""
    tip = bill_amount * (tip_percent / 100)
    return tip


# Test the function
print("=== Tip Calculator ===")
print()

bill = 85.00
print(f"Bill: ${bill:.2f}")

# Call calculate_tip with default tip (15%)
tip_15 = calculate_tip(bill)
print(f"15% tip: ${tip_15:.2f}")

# Call calculate_tip with 20% tip
tip_20 = calculate_tip(bill, 20)
print(f"20% tip: ${tip_20:.2f}")

# Call calculate_tip with 10% tip
tip_10 = calculate_tip(bill, 10)
print(f"10% tip: ${tip_10:.2f}")
