"""
02 - With Getters and Setters
==============================
Use getter and setter methods for controlled access.

This approach gives us validation but requires method calls.
"""


class Temperature:
    """Represents a temperature with validation."""

    def __init__(self, celsius=0):
        # Private attribute (by convention, starts with __)
        self.__celsius = 0
        # Use setter for validation
        self.set_celsius(celsius)

    def get_celsius(self):
        """Get the temperature value."""
        return self.__celsius

    def set_celsius(self, value):
        """Set the temperature with validation."""
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C (absolute zero) is not possible")
        self.__celsius = value

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""
        return (self.get_celsius() * 1.8) + 32


# Create temperature object
temp = Temperature(25)

print("=== Getters and Setters ===")
print()

# Must use getter/setter methods
print(f"Temperature: {temp.get_celsius()}°C")
temp.set_celsius(30)
print(f"New temperature: {temp.get_celsius()}°C")
print()

# Validation works!
try:
    temp.set_celsius(-500)
except ValueError as e:
    print(f"Error caught: {e}")
print()

# Improvements:
# + Has validation
# + Controlled access
# - Requires method calls (not Pythonic)
# - Verbose: get_celsius() instead of just celsius
