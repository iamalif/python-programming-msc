"""
Exercise 03: Profit Calculator
==============================
Calculate and display profit metrics for a product.

Your task:
1. Ask the user for: product name, cost price, selling price, units sold
2. Calculate: revenue, total cost, profit, profit margin percentage
3. Display a summary report

Formulas:
- Revenue = selling price × units sold
- Total Cost = cost price × units sold
- Profit = Revenue - Total Cost
- Profit Margin = (Profit / Revenue) × 100

Example interaction:
--------------------
=== Profit Calculator ===

Enter product name: Bluetooth Speaker
Enter cost price per unit: 25.00
Enter selling price per unit: 49.99
Enter units sold: 80

--- Profit Report ---
Product: Bluetooth Speaker
Units Sold: 80
Revenue: $3,999.20
Total Cost: $2,000.00
Profit: $1,999.20
Profit Margin: 49.99%
"""

# TODO: Print header
print("=== Profit Calculator ===")
print()


# TODO: Get input from user (4 inputs)
product_name = input("Enter product name: ")
cost_price = float(input("Enter cost price per unit: "))
selling_price = float(input("Enter selling price per unit: "))
units_sold = int(input("Enter units sold: "))


# TODO: Calculate revenue, total cost, profit, and profit margin
revenue = selling_price * units_sold
total_cost = cost_price * units_sold
profit = revenue - total_cost
profit_margin = (profit / revenue) * 100


# TODO: Print the profit report
print(f"The revenue for {product_name} is: ${revenue:.2f}")
print(f"The total cost for {product_name} is: ${total_cost:.2f}")
print(f"The profit for {product_name} is: ${profit:.2f}")
print(f"The profit margin for {product_name} is: {profit_margin:.2f}%")


