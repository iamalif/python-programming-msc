"""
Exercise 01: Sales Report - SOLUTION
====================================
"""

# Create variables for all the data
store_name = "Downtown Electronics"
date = "January 15, 2025"
items_sold = 127
total_revenue = 8459.50
avg_transaction = 66.61

# Print the formatted report
print("=" * 32)
print(f"{'DAILY SALES REPORT':^32}")
print("=" * 32)
print(f"Store: {store_name}")
print(f"Date:  {date}")
print("-" * 32)
print(f"Items Sold:      {items_sold:>10}")
print(f"Total Revenue:   ${total_revenue:>9,.2f}")
print(f"Avg Transaction: ${avg_transaction:>9,.2f}")
print("=" * 32)
