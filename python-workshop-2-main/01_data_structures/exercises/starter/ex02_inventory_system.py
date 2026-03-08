"""
Exercise 02: Store Inventory System
===================================
Create an inventory management system using dictionaries.

Your task:
1. Create a dictionary with products and quantities
2. Display the inventory
3. Sell some items (decrease quantity)
4. Restock items (increase quantity)
5. Check if an item is in stock

Expected output:
----------------
=== Store Inventory ===

laptop: 15
mouse: 45
keyboard: 32
monitor: 8

After selling 3 laptops:
laptop: 12

After restocking 20 mice:
mouse: 65

Is 'printer' in stock? False
Is 'laptop' in stock? True
"""

# TODO: Create inventory dictionary
inventory = {
    "laptop": 15,
    "mouse": 45,
    "keyboard": 32,
    "monitor": 8
}  # Add products with quantities

# TODO: Display inventory
print("=== Store Inventory ===")

for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# TODO: Sell 3 laptops (decrease quantity)
print("\nAfter selling 3 laptops:")
inventory["laptop"] -= 3
print(f"Laptop: {inventory["laptop"]}")

# TODO: Restock 20 mice (increase quantity)
print("\nAfter restocking 20 mice:")
inventory["mouse"] += 20
print(f"Mouse: {inventory["mouse"]}")

# TODO: Check if 'printer' and 'laptop' are in stock
# Hint: Use 'in' operator
print(f"\nIs 'printer' in stock? {"printer" in inventory}")
print(f"Is 'laptop' in stock? {"laptop" in inventory}")
