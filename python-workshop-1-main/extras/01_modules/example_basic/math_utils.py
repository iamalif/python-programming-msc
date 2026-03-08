"""
math_utils.py - A simple module with math functions
====================================================
This file can be imported by other Python files.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# This code only runs if this file is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    print("Testing math_utils functions:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"divide(5, 3) = {divide(5, 3):.2f}")
