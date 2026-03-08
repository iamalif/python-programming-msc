"""
01 - Conditionals: Making Decisions
===================================
if/elif/else statements let your program make decisions based on conditions.

Run this file: python 01_conditionals.py
"""

# Simple if statement
print("=== Simple if Statement ===")
print()

temperature = 28

if temperature > 25:
    print("It's warm today!")
    print("Consider using air conditioning.")

# if-else: Two possible outcomes
print()
print("=== if-else Statement ===")
print()

balance = 150
withdrawal = 200

if balance >= withdrawal:
    balance = balance - withdrawal
    print(f"Withdrawal successful. New balance: ${balance}")
else:
    print("Insufficient funds!")
    print(f"Your balance is only ${balance}")

# if-elif-else: Multiple conditions
print()
print("=== Customer Tier Classification ===")
print()

annual_spending = 5500

if annual_spending >= 10000:
    tier = "Platinum"
    discount = 20
elif annual_spending >= 5000:
    tier = "Gold"
    discount = 15
elif annual_spending >= 1000:
    tier = "Silver"
    discount = 10
else:
    tier = "Bronze"
    discount = 5

print(f"Annual spending: ${annual_spending:,}")
print(f"Customer tier: {tier}")
print(f"Discount rate: {discount}%")

# Nested if statements
print()
print("=== Nested Conditions ===")
print()

is_member = True
purchase_amount = 75

if is_member:
    if purchase_amount >= 100:
        shipping = "Free"
    else:
        shipping = "$5.99"
else:
    if purchase_amount >= 150:
        shipping = "Free"
    else:
        shipping = "$9.99"

print(f"Member: {is_member}")
print(f"Purchase: ${purchase_amount}")
print(f"Shipping: {shipping}")
