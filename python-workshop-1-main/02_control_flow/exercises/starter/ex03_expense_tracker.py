"""
Exercise 03: Expense Tracker
============================
Track expenses until the user is done entering them.

Your task:
1. Use a while loop to keep asking for expenses
2. User enters 0 (or negative) to finish
3. Track the count and total of expenses
4. Show a summary at the end

Example:
--------
=== Expense Tracker ===

Enter expense amount (0 to finish): 45.50
Enter expense amount (0 to finish): 120.00
Enter expense amount (0 to finish): 33.25
Enter expense amount (0 to finish): 0

--- Summary ---
Number of expenses: 3
Total spent: $198.75
Average expense: $66.25
"""

# TODO: Print header
print("=== Expense Tracker ===")

# TODO: Initialize counters (count and total)
count = 0
total = 0


# TODO: Create a while True loop
# Inside the loop:
#   - Get expense amount from user
#   - If amount <= 0, break out of loop
#   - Otherwise, add to total and increment count
while True:
    expense = float(input("Please enter expense: "))
    if expense <= 0:
        break
    else:
        total += expense
        count += 1

# TODO: Print the summary
# Include: number of expenses, total, and average
# Handle the case where no expenses were entered!
average_expense = total/count
print("--- Summary ---")
print(f"Number of expenses: {count}")
print(f"Total spent: {total}")
print(f"Average expense: {average_expense}")
