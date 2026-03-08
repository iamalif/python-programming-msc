"""
Exercise 03: Profit Calculator - SOLUTION
=========================================
"""

# Print header
print("=== Profit Calculator ===")
print()

# Get input from user
product_name = input("Enter product name: ")
cost_price = float(input("Enter cost price per unit: "))
selling_price = float(input("Enter selling price per unit: "))
units_sold = int(input("Enter units sold: "))

# Calculate metrics
revenue = selling_price * units_sold
total_cost = cost_price * units_sold
profit = revenue - total_cost
profit_margin = (profit / revenue) * 100

# Print the profit report
print()
print("--- Profit Report ---")
print(f"Product: {product_name}")
print(f"Units Sold: {units_sold}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
