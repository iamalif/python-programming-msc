"""
Exercise 02: Shopping Cart
==========================
Create a ShoppingCart class to manage items and calculate totals.

Your task:
1. Create Product class with name and price
2. Create ShoppingCart class
3. Add methods to add/remove items
4. Add method to calculate total
5. Add method to display cart contents

Expected output:
----------------
=== Shopping Cart ===

Added: Laptop ($999.99)
Added: Mouse ($29.99)
Added: Keyboard ($79.99)

Cart Contents:
  1. Laptop - $999.99
  2. Mouse - $29.99
  3. Keyboard - $79.99
Total: $1,109.97

After removing Mouse:
  1. Laptop - $999.99
  2. Keyboard - $79.99
Total: $1,079.98
"""

# TODO: Define Product class
class Product:
    """Represents a product with name and price."""

    def __init__(self, name, price):
        """Initialize product."""
        # TODO: Set name and price attributes
        self.name = name
        self.price = price


# TODO: Define ShoppingCart class
class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initialize empty cart."""
        # TODO: Create empty list for items
        self.items = []

    def add_item(self, product):
        """Add a product to the cart."""
        # TODO: Append product to items list
        self.items.append(product)
        print(f"Added: {product.name} (${product.price:.2f})")

    def remove_item(self, product_name):
        """Remove a product by name."""
        # TODO: Find and remove product with matching name
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed: {product_name}")
                return
        print(f"{product_name} not found in cart")

    def get_total(self):
        """Calculate total price."""
        # TODO: Sum up all product prices
        return sum(product.price for product in self.items)

    def display_cart(self):
        """Display cart contents."""
        # TODO: Print each item with number and price
        # TODO: Print total
        if not self.items:
            print("Cart is empty")
            return

        print("Cart Contents:")
        for i, product in enumerate(self.items, start=1):
            print(f"  {i}. {product.name} - ${product.price:.2f}")
        print(f"Total: ${self.get_total():.2f}")


# TODO: Create products
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 29.99)
keyboard = Product("Keyboard", 79.99)

# TODO: Create shopping cart and add items
print("=== Shopping Cart ===")
print()

cart = ShoppingCart()
cart.add_item(laptop)
cart.add_item(mouse)
cart.add_item(keyboard)

# TODO: Display cart
cart.display_cart()

# TODO: Remove an item and display again
cart.remove_item("Mouse")
cart.display_cart()
cart.remove_item("Keyboard")
cart.display_cart()
