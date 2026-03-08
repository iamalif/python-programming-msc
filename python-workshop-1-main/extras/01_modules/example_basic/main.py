"""
main.py - Demonstrates importing a module
=========================================
Run this file: python main.py
"""

# Method 1: Import the entire module
import math_utils

print("=== Using 'import math_utils' ===")
print(f"5 + 3 = {math_utils.add(5, 3)}")
print(f"5 - 3 = {math_utils.subtract(5, 3)}")


# Method 2: Import with an alias (shorter name)
import math_utils as mu

print()
print("=== Using 'import math_utils as mu' ===")
print(f"5 * 3 = {mu.multiply(5, 3)}")
print(f"5 / 3 = {mu.divide(5, 3):.2f}")


# Method 3: Import specific functions
from math_utils import add, multiply

print()
print("=== Using 'from math_utils import add, multiply' ===")
print(f"10 + 20 = {add(10, 20)}")
print(f"10 * 20 = {multiply(10, 20)}")
