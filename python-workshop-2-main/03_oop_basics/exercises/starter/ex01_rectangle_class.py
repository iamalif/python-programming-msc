"""
Exercise 01: Rectangle Class
============================
Create a Rectangle class with methods to calculate area and perimeter.

Your task:
1. Create a Rectangle class
2. Add __init__ to accept width and height
3. Add method to calculate area
4. Add method to calculate perimeter
5. Add method to display information

Expected output:
----------------
=== Rectangle Demo ===

Rectangle 1: 5 x 3
  Area: 15
  Perimeter: 16

Rectangle 2: 10 x 7
  Area: 70
  Perimeter: 34

After resizing Rectangle 1 to 8 x 4:
  Area: 32
  Perimeter: 24
"""

# TODO: Define the Rectangle class
class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        # TODO: Set attributes
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area."""
        # TODO: Return width * height
        area = self.width * self.height
        return area

    def perimeter(self):
        """Calculate and return the perimeter."""
        # TODO: Return 2 * (width + height)
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def display_info(self):
        """Display rectangle information."""
        # TODO: Print width, height, area, and perimeter
        print(self.width)
        print(self.height)
        print(self.area())
        print(self.perimeter())


# TODO: Create two Rectangle objects
rect1 = Rectangle(5, 3)  # Replace with Rectangle(5, 3)
rect2 = Rectangle(10, 7)  # Replace with Rectangle(10, 7)

# TODO: Display their information
rect1.display_info()
print()
rect2.display_info()
print()

# TODO: Change rect1's dimensions to 8 x 4 and display again

rect1.width = 8
rect1.height = 4
rect1.display_info()