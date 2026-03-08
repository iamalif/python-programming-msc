"""
Exercise 01: Rectangle Class - SOLUTION
=======================================
"""

class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self.width + self.height)

    def display_info(self):
        """Display rectangle information."""
        print(f"Rectangle: {self.width} x {self.height}")
        print(f"  Area: {self.area()}")
        print(f"  Perimeter: {self.perimeter()}")


# Create two Rectangle objects
print("=== Rectangle Demo ===")
print()

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 7)

# Display information
print("Rectangle 1: 5 x 3")
print(f"  Area: {rect1.area()}")
print(f"  Perimeter: {rect1.perimeter()}")
print()

print("Rectangle 2: 10 x 7")
print(f"  Area: {rect2.area()}")
print(f"  Perimeter: {rect2.perimeter()}")

# Change rect1 dimensions
rect1.width = 8
rect1.height = 4

print()
print("After resizing Rectangle 1 to 8 x 4:")
print(f"  Area: {rect1.area()}")
print(f"  Perimeter: {rect1.perimeter()}")
