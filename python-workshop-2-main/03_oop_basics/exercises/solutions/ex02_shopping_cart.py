"""
Exercise 02: Shopping Cart - SOLUTION
=====================================
"""

class Product:
    """Represents a product with name and price."""

    def __init__(self, name, price):
        """Initialize product."""
        self.name = name
        self.price = price


class ShoppingCart:
    """Represents a shopping cart."""

    def __init__(self):
        """Initialize empty cart."""
        self.items = []

    def add_item(self, product):
        """Add a product to the cart."""
        self.items.append(product)
        print(f"Added: {product.name} (${product.price:.2f})")

    def remove_item(self, product_name):
        """Remove a product by name."""
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed: {product_name}")
                return
        print(f"{product_name} not found in cart")

    def get_total(self):
        """Calculate total price."""
        return sum(product.price for product in self.items)

    def display_cart(self):
        """Display cart contents."""
        if not self.items:
            print("Cart is empty")
            return

        print("Cart Contents:")
        for i, product in enumerate(self.items, start=1):
            print(f"  {i}. {product.name} - ${product.price:.2f}")
        print(f"Total: ${self.get_total():.2f}")


# Create products
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 29.99)
keyboard = Product("Keyboard", 79.99)

# Create shopping cart
print("=== Shopping Cart ===")
print()

cart = ShoppingCart()
cart.add_item(laptop)
cart.add_item(mouse)
cart.add_item(keyboard)

# Display cart
print()
cart.display_cart()

# Remove item
print()
cart.remove_item("Mouse")
print()
cart.display_cart()
