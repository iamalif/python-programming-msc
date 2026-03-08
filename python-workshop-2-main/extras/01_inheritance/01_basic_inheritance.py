"""
01 - Basic Inheritance
======================
Learn how to create classes that inherit from other classes.

Inheritance allows you to create new classes that reuse, extend, and modify
the behavior of existing classes. This promotes code reuse and reduces duplication.
"""

# Base class (also called parent class or superclass)
class Person:
    """Represents a person with a name."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Return a greeting message."""
        return f"Hello, I'm {self.name}!"


# Derived class (also called child class or subclass)
class Student(Person):
    """Represents a student, which is a special type of person."""

    def study(self):
        """Student-specific method."""
        return f"{self.name} is studying."

    # Override the greet() method from Person
    def greet(self):
        """Customize greeting for students."""
        return f"Hi, I'm {self.name} and I'm a student!"


# Create instances
print("=== Inheritance Demo ===")
print()

# Create a regular person
person = Person("Bob")
print(person.greet())
print()

# Create a student (inherits from Person)
student = Student("Alice")
print(student.greet())    # Uses overridden method
print(student.study())    # Student-specific method
print()

# Key concepts:
# - Student inherits all methods and attributes from Person
# - Student can add new methods (like study())
# - Student can override methods (like greet())
# - Use inheritance when there's a clear "is-a" relationship
#   (A Student IS A Person)
