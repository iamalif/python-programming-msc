"""
Exercise 04: Weekly Sales Analysis
==================================
Analyze a week of sales data using a for loop.

Your task:
1. Use the provided sales data
2. Calculate: total, average, best day, worst day
3. Display a formatted report

Data provided:
- Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
- Sales: 1200, 950, 1100, 1350, 1800, 2200, 1400

Expected output:
----------------
=== Weekly Sales Analysis ===

Day-by-day breakdown:
Mon: $1,200
Tue: $950
Wed: $1,100
Thu: $1,350
Fri: $1,800
Sat: $2,200
Sun: $1,400

--- Summary ---
Total Sales: $10,000
Average Daily: $1,428.57
Best Day: Sat ($2,200)
Worst Day: Tue ($950)
"""

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [1200, 950, 1100, 1350, 1800, 2200, 1400]

# TODO: Print header
print("=== Weekly Sales Analysis ===")
print()


# TODO: Print day-by-day breakdown using a for loop
print("Day-by-day breakdown:")

sales_counter = 0
total_sales = 0
best_day = 0
worst_day = sales[0]
for day in days:
    print(f"{day}: ${sales[sales_counter]}")
    total_sales = total_sales + sales[sales_counter]

    if sales[sales_counter] >= best_day:
        best_day = sales[sales_counter]
        best_day_text = day
    
    if sales[sales_counter] <= worst_day:
        worst_day_text = sales[sales_counter]

    sales_counter += 1

daily_average = total_sales / len(sales)


# TODO: Calculate total, average, best day, worst day
# Hint: Track best/worst as you loop, or loop separately


# TODO: Print the summary
print("--- Summary ---")
print(f"Total Sales: ${total_sales}")
print(f"Average Daily: ${daily_average:.2f}")
print(f"Best Day: best_day_text (${best_day})")
print(f"Worst Day: worst_day_text (${worst_day})")


# worst day is incorrect