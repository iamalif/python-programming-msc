# Properties and Decorators

Learn how to use Python's property decorators for elegant attribute access.

## What You'll Learn

- Why direct attribute access can be problematic
- How getters and setters provide control
- Using `@property` for Pythonic attribute access
- Creating computed properties
- Making read-only attributes

## Examples

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_without_properties.py](01_without_properties.py) | Direct access | Problems with uncontrolled access |
| [02_with_getters_setters.py](02_with_getters_setters.py) | Getter/setter methods | Validation, controlled access |
| [03_with_property_decorator.py](03_with_property_decorator.py) | @property decorator | Pythonic properties, computed values |

## Key Concepts

### The Problem
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

temp = Temperature(-500)  # No validation!
```

### The Solution: @property
```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = 0
        self.celsius = celsius  # Uses setter

    @property
    def celsius(self):
        """Getter."""
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        """Setter with validation."""
        if value < -273.15:
            raise ValueError("Too cold!")
        self.__celsius = value

temp = Temperature(25)
temp.celsius = 30  # Looks like attribute, uses setter!
```

### Read-Only Property
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """Computed property (no setter = read-only)."""
        return 3.14159 * self.radius ** 2
```

## When to Use

- **Validation**: Need to check values before setting
- **Computed values**: Calculate attribute on access
- **Read-only**: Prevent modification of certain attributes
- **Backwards compatibility**: Add logic without changing interface

---

*Part of Workshop 2 extras - self-study material*
