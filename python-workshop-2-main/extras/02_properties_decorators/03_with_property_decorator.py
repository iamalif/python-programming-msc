"""
03 - With @property Decorator
==============================
The modern Pythonic way to use properties.

@property allows you to use method calls like attributes!
"""


class Temperature:
    """Represents a temperature with property-based validation."""

    def __init__(self, celsius=0):
        self.__celsius = 0
        # Set using the property
        self.celsius = celsius

    @property
    def celsius(self):
        """Get the temperature value."""
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature with validation."""
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C (absolute zero) is not possible")
        self.__celsius = value

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""
        return (self.celsius * 1.8) + 32


# Create temperature object
temp = Temperature(25)

print("=== @property Decorator ===")
print()

# Looks like direct attribute access, but uses our methods!
print(f"Temperature: {temp.celsius}°C")
temp.celsius = 30  # Calls the setter automatically
print(f"New temperature: {temp.celsius}°C")
print()

# Validation still works!
try:
    temp.celsius = -500
except ValueError as e:
    print(f"Error caught: {e}")
print()

# Benefits of @property:
# + Clean, Pythonic syntax (looks like attribute access)
# + Has validation and control
# + Can add logic without breaking existing code
# + Read-only properties (omit setter)
# + Computed properties (calculate on access)

print("=== Computed Property Example ===")
print()


class Circle:
    """Circle with computed area property."""

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """Compute area on the fly."""
        return 3.14159 * self.radius ** 2


circle = Circle(5)
print(f"Circle radius: {circle.radius}")
print(f"Circle area: {circle.area:.2f}")  # Computed automatically!
