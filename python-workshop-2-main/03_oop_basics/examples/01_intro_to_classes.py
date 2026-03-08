"""
01 - Introduction to Classes
============================
Classes are blueprints for creating objects that combine data and behavior.

Run this file: python 01_intro_to_classes.py
"""

# Without OOP - using separate variables
print("=== Without Classes (Procedural) ===")
print()

student1_name = "Alice"
student1_age = 20
student1_gpa = 3.8

student2_name = "Bob"
student2_age = 21
student2_gpa = 3.6

print(f"{student1_name}: GPA {student1_gpa}")
print(f"{student2_name}: GPA {student2_gpa}")
print("Problem: Data is scattered, hard to manage!")

# With OOP - using a class
print()
print("=== With Classes (Object-Oriented) ===")
print()

class Student:
    """A class to represent a student."""

    def __init__(self, name, age, gpa):
        """Initialize a new student."""
        self.name = name
        self.age = age
        self.gpa = gpa

    def display_info(self):
        """Display student information."""
        print(f"{self.name}: Age {self.age}, GPA {self.gpa}")

# Creating objects (instances of the class)
student1 = Student("Alice", 20, 3.8)
student2 = Student("Bob", 21, 3.6)

# Using the objects
student1.display_info()
student2.display_info()

# Accessing attributes
print()
print("=== Accessing Attributes ===")
print()

print(f"Student 1 name: {student1.name}")
print(f"Student 2 GPA: {student2.gpa}")

# Modifying attributes
student1.gpa = 3.9
print(f"Student 1 updated GPA: {student1.gpa}")

# Class terminology
print()
print("=== Key Terms ===")
print()
print("Class: Blueprint (Student)")
print("Object/Instance: Specific student (student1, student2)")
print("Attributes: Data (name, age, gpa)")
print("Methods: Behaviors (display_info)")
print("__init__: Constructor - runs when object is created")
print("self: Reference to the current object")
