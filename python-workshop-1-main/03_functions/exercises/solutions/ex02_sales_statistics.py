"""
Exercise 02: Sales Statistics - SOLUTION
========================================
"""

def analyze_data(numbers):
    """Analyze a list of numbers and return statistics."""
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

# Analyze Q1 sales
print(f"Q1 Sales: {q1_sales}")
total, avg, minimum, maximum = analyze_data(q1_sales)
print(f"Total: ${total:,}")
print(f"Average: ${avg:,.2f}")
print(f"Minimum: ${minimum:,}")
print(f"Maximum: ${maximum:,}")

# Analyze Q2 sales
print(f"\nQ2 Sales: {q2_sales}")
total, avg, minimum, maximum = analyze_data(q2_sales)
print(f"Total: ${total:,}")
print(f"Average: ${avg:,.2f}")
print(f"Minimum: ${minimum:,}")
print(f"Maximum: ${maximum:,}")
