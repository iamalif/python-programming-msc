"""
01 - Without Properties
========================
See what happens when we don't use properties or encapsulation.

This example shows direct attribute access - simple but with potential problems.
"""


class Temperature:
    """Represents a temperature value."""

    def __init__(self, celsius=0):
        self.celsius = celsius

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""
        return (self.celsius * 1.8) + 32


# Create temperature object
temp = Temperature(25)

print("=== Direct Attribute Access ===")
print()

# Reading is straightforward
print(f"Temperature: {temp.celsius}°C")
print(f"In Fahrenheit: {temp.to_fahrenheit():.1f}°F")
print()

# But there's a problem - no validation!
temp.celsius = -500  # This is impossible (below absolute zero)!
print(f"Set to impossible value: {temp.celsius}°C")
print()

# Problems with this approach:
# - No validation of values
# - No control over how attributes are accessed
# - Can't add logic later without breaking code
# - Hard to debug when invalid values are set
