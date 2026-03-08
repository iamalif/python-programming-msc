"""
03 - While Loops: Repeating Actions
===================================
A while loop repeats code as long as a condition is True.

Run this file: python 03_while_loops.py
"""

# Basic while loop
print("=== Basic While Loop ===")
print()

countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1  # Don't forget to update the counter!
print("Liftoff!")

# Accumulator pattern - building up a total
print()
print("=== Order Total Calculator ===")
print()

total = 0
items_scanned = 0

# Simulating scanning items (predefined for demo)
prices = [29.99, 15.50, 8.99, 42.00]
index = 0

while index < len(prices):
    price = prices[index]
    total += price
    items_scanned += 1
    print(f"Item {items_scanned}: ${price:.2f} (Running total: ${total:.2f})")
    index += 1

print(f"\nFinal total: ${total:.2f}")

# while True with break
print()
print("=== Menu System (while True + break) ===")
print()

# Simulating user choices
demo_choices = ["1", "2", "3"]
choice_index = 0

while True:
    print("1. View Balance")
    print("2. Make Deposit")
    print("3. Exit")

    # In real code: choice = input("Enter choice: ")
    choice = demo_choices[choice_index]
    print(f"Choice: {choice}")

    if choice == "1":
        print("-> Balance: $1,250.00\n")
    elif choice == "2":
        print("-> Deposit recorded\n")
    elif choice == "3":
        print("-> Goodbye!")
        break
    else:
        print("-> Invalid choice\n")

    choice_index += 1

# Continue statement - skip current iteration
print()
print("=== Using continue ===")
print()

print("Processing orders (skipping cancelled ones):")
orders = [("ORD001", "completed"), ("ORD002", "cancelled"),
          ("ORD003", "completed"), ("ORD004", "cancelled")]
index = 0

while index < len(orders):
    order_id, status = orders[index]
    index += 1

    if status == "cancelled":
        print(f"  Skipping {order_id} (cancelled)")
        continue

    print(f"  Processing {order_id}...")
