"""
03 - Polymorphism
=================
Learn how polymorphism allows different classes to be used interchangeably.

Polymorphism means "many forms" - it allows objects of different classes to be
treated as objects of a common parent class. This is a powerful concept for
writing flexible and extensible code.
"""


class Shape:
    """Base class for all shapes."""

    def area(self):
        """Calculate area - to be overridden by derived classes."""
        pass

    def describe(self):
        """Describe the shape."""
        return "This is a shape"


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate circle area."""
        return 3.14159 * self.radius ** 2

    def describe(self):
        """Describe the circle."""
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate rectangle area."""
        return self.length * self.width

    def describe(self):
        """Describe the rectangle."""
        return f"Rectangle with dimensions {self.length}x{self.width}"


class Triangle(Shape):
    """Triangle shape."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """Calculate triangle area."""
        return 0.5 * self.base * self.height

    def describe(self):
        """Describe the triangle."""
        return f"Triangle with base {self.base} and height {self.height}"


# Polymorphism in action!
# We can treat different shapes uniformly
def print_shape_info(shape):
    """Print information about any shape."""
    print(f"{shape.describe()}")
    print(f"Area: {shape.area():.2f}")
    print()


# Create different shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8),
    Circle(3)
]

print("=== Polymorphism Demo ===")
print()

# Process all shapes the same way, even though they're different types!
for shape in shapes:
    print_shape_info(shape)

# Benefits of polymorphism:
# - Write code that works with any shape type
# - Easy to add new shape types without changing existing code
# - Makes code more flexible and extensible
# - Allows for cleaner, more organized code structure
