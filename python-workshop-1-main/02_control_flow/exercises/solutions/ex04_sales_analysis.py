"""
Exercise 04: Weekly Sales Analysis - SOLUTION
=============================================
"""

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [1200, 950, 1100, 1350, 1800, 2200, 1400]

# Print header
print("=== Weekly Sales Analysis ===")
print()

# Initialize tracking variables
total_sales = 0
best_day = days[0]
best_sales = sales[0]
worst_day = days[0]
worst_sales = sales[0]

# Print day-by-day breakdown and calculate stats
print("Day-by-day breakdown:")
for i in range(len(days)):
    day = days[i]
    daily_sales = sales[i]

    print(f"{day}: ${daily_sales:,}")

    # Update total
    total_sales += daily_sales

    # Check for best day
    if daily_sales > best_sales:
        best_sales = daily_sales
        best_day = day

    # Check for worst day
    if daily_sales < worst_sales:
        worst_sales = daily_sales
        worst_day = day

# Calculate average
average_sales = total_sales / len(days)

# Print the summary
print()
print("--- Summary ---")
print(f"Total Sales: ${total_sales:,}")
print(f"Average Daily: ${average_sales:,.2f}")
print(f"Best Day: {best_day} (${best_sales:,})")
print(f"Worst Day: {worst_day} (${worst_sales:,})")
