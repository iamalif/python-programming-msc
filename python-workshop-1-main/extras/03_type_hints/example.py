"""
Type Hints Example
==================
Demonstrates how to use type annotations in Python.

Run this file: python example.py
"""

# Variable type hints
product_name: str = "Laptop"
price: float = 999.99
quantity: int = 5
in_stock: bool = True

print("=== Variable Type Hints ===")
print(f"product_name: {product_name} (type hint: str)")
print(f"price: {price} (type hint: float)")
print(f"quantity: {quantity} (type hint: int)")
print(f"in_stock: {in_stock} (type hint: bool)")


# Function with type hints
def calculate_total(unit_price: float, qty: int, tax_rate: float = 0.25) -> float:
    """
    Calculate total price including tax.

    Args:
        unit_price: Price per unit
        qty: Number of units
        tax_rate: Tax rate as decimal (default 0.25)

    Returns:
        Total price including tax
    """
    subtotal = unit_price * qty
    tax = subtotal * tax_rate
    return subtotal + tax


print()
print("=== Function Type Hints ===")
total = calculate_total(99.99, 3)
print(f"calculate_total(99.99, 3) = {total:.2f}")

total_custom_tax = calculate_total(99.99, 3, 0.12)
print(f"calculate_total(99.99, 3, 0.12) = {total_custom_tax:.2f}")


# Function returning multiple values
def analyze_sales(values: list[float]) -> tuple[float, float, float]:
    """
    Analyze sales data.

    Args:
        values: List of sales values

    Returns:
        Tuple of (total, average, maximum)
    """
    total = sum(values)
    average = total / len(values) if values else 0
    maximum = max(values) if values else 0
    return total, average, maximum


print()
print("=== Complex Type Hints ===")
sales_data: list[float] = [150.0, 200.0, 175.5, 225.0]
total, avg, max_val = analyze_sales(sales_data)
print(f"Sales data: {sales_data}")
print(f"Total: {total}, Average: {avg:.2f}, Max: {max_val}")


# Type hints are NOT enforced!
print()
print("=== Type Hints Are NOT Enforced ===")
price: int = "This is a string!"  # Works, but wrong!
print(f"price (declared as int): '{price}' (actual type: {type(price).__name__})")
print("Python allows this, but it's bad practice.")
