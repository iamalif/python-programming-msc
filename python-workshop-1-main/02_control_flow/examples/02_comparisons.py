"""
02 - Comparisons: Testing Conditions
====================================
Comparison and logical operators return True or False.

Run this file: python 02_comparisons.py
"""

# Comparison operators
print("=== Comparison Operators ===")
print()

price = 99.99
budget = 100

print(f"Price: ${price}, Budget: ${budget}")
print(f"price == budget: {price == budget}")   # Equal to
print(f"price != budget: {price != budget}")   # Not equal to
print(f"price < budget:  {price < budget}")    # Less than
print(f"price > budget:  {price > budget}")    # Greater than
print(f"price <= budget: {price <= budget}")   # Less than or equal
print(f"price >= budget: {price >= budget}")   # Greater than or equal

# Logical operators: and, or, not
print()
print("=== Logical Operators ===")
print()

age = 25
has_license = True
has_insurance = False

# and - Both must be True
can_rent_car = age >= 21 and has_license
print(f"Can rent car (age >= 21 AND has license): {can_rent_car}")

# or - At least one must be True
has_coverage = has_license or has_insurance
print(f"Has coverage (license OR insurance): {has_coverage}")

# not - Inverts the value
needs_insurance = not has_insurance
print(f"Needs insurance: {needs_insurance}")

# Combining operators in real scenarios
print()
print("=== Loan Eligibility Check ===")
print()

credit_score = 720
annual_income = 55000
existing_debt = 10000

# Complex condition
is_eligible = (
    credit_score >= 650 and
    annual_income >= 40000 and
    existing_debt < 20000
)

print(f"Credit Score: {credit_score}")
print(f"Annual Income: ${annual_income:,}")
print(f"Existing Debt: ${existing_debt:,}")
print(f"Loan Eligible: {is_eligible}")

# Data validation example
print()
print("=== Data Validation ===")
print()

username = "john_doe"
password = "secret123"

# Validate username
valid_username = len(username) >= 3 and len(username) <= 20
print(f"Username '{username}' is valid: {valid_username}")

# Validate password (at least 8 characters)
valid_password = len(password) >= 8
print(f"Password is valid: {valid_password}")

# Both must be valid
valid_credentials = valid_username and valid_password
print(f"Credentials are valid: {valid_credentials}")
