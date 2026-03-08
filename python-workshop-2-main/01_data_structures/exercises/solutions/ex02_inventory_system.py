"""
Exercise 02: Store Inventory System - SOLUTION
==============================================
"""

# Create inventory
inventory = {
    "laptop": 15,
    "mouse": 45,
    "keyboard": 32,
    "monitor": 8
}

# Display inventory
print("=== Store Inventory ===")
print()
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# Sell 3 laptops
inventory["laptop"] -= 3
print(f"\nAfter selling 3 laptops:")
print(f"laptop: {inventory['laptop']}")

# Restock 20 mice
inventory["mouse"] += 20
print(f"\nAfter restocking 20 mice:")
print(f"mouse: {inventory['mouse']}")

# Check stock
print(f"\nIs 'printer' in stock? {'printer' in inventory}")
print(f"Is 'laptop' in stock? {'laptop' in inventory}")
