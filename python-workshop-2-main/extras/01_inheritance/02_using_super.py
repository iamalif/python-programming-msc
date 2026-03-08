"""
02 - Using super()
==================
Learn how to use super() to call parent class methods.

The super() method allows derived classes to call methods from their parent
class. This is especially useful in constructors to initialize inherited attributes.
"""


class Person:
    """Base class representing a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        """Display person information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    """Student class that extends Person."""

    def __init__(self, name, age, student_id, major):
        # Call the parent class constructor using super()
        super().__init__(name, age)

        # Add student-specific attributes
        self.student_id = student_id
        self.major = major

    def display_info(self):
        """Display student information (extends parent method)."""
        # Call parent's display_info first
        super().display_info()

        # Add student-specific information
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")


# Create and display student
print("=== Using super() Demo ===")
print()

student = Student("Alice", 20, "S12345", "Computer Science")
student.display_info()
print()

# Why use super()?
# - Avoids code duplication
# - Calls parent class methods properly
# - Makes code more maintainable
# - Works correctly with multiple inheritance (advanced topic)
