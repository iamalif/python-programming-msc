"""
Exercise 03: Expense Tracker - SOLUTION
=======================================
"""

# Print header
print("=== Expense Tracker ===")
print()

# Initialize counters
expense_count = 0
total_spent = 0

# Create a while True loop
while True:
    amount = float(input("Enter expense amount (0 to finish): "))

    if amount <= 0:
        break

    total_spent += amount
    expense_count += 1

# Print the summary
print()
print("--- Summary ---")

if expense_count > 0:
    average = total_spent / expense_count
    print(f"Number of expenses: {expense_count}")
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Average expense: ${average:.2f}")
else:
    print("No expenses entered.")
