"""
Exercise 02: Sales Statistics
=============================
Create a function that analyzes sales data and returns multiple statistics.

Your task:
1. Create a function called analyze_data that takes a list of numbers
2. The function should return: total, average, minimum, maximum
3. Test it with the provided sales data

Expected output:
----------------
=== Sales Statistics ===

Q1 Sales: [12500, 15000, 11800]
Total: $39,300
Average: $13,100.00
Minimum: $11,800
Maximum: $15,000

Q2 Sales: [18200, 16500, 19800, 21000]
Total: $75,500
Average: $18,875.00
Minimum: $16,500
Maximum: $21,000
"""

# TODO: Define the analyze_data function
# It should take a list called 'numbers'
# Calculate and return: total, average, minimum, maximum
# Hint: Use sum(), len(), min(), max()
def analyze_data(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum


# Test data
q1_sales = [12500, 15000, 11800]
q2_sales = [18200, 16500, 19800, 21000]

print("=== Sales Statistics ===")
print()

# TODO: Analyze Q1 sales
print(f"Q1 Sales: {q1_sales}")
# total, avg, minimum, maximum = analyze_data(q1_sales)
# Print the results
total, avg, minimum, maximum = analyze_data(q1_sales)
print(total, avg, minimum, maximum)


# TODO: Analyze Q2 sales
print(f"\nQ2 Sales: {q2_sales}")
# total, avg, minimum, maximum = analyze_data(q2_sales)
# Print the results
total, avg, minimum, maximum = analyze_data(q2_sales)
print(total, avg, minimum, maximum)
