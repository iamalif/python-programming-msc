# Section 03: OOP Basics

Introduction to Object-Oriented Programming - organizing code with classes and objects.

## Learning Objectives

After this section, you will be able to:

- Understand what classes and objects are
- Create your own classes
- Define attributes and methods
- Work with multiple objects

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_intro_to_classes.py](examples/01_intro_to_classes.py) | Classes intro | `class`, `__init__`, `self` |
| [02_bank_account.py](examples/02_bank_account.py) | Practical example | Methods, encapsulation |
| [03_game_character.py](examples/03_game_character.py) | Game character | State management |
| [04_multiple_objects.py](examples/04_multiple_objects.py) | Object collections | Lists of objects |

## Exercises

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_rectangle_class.py](exercises/starter/ex01_rectangle_class.py) | Rectangle with calculations | Classes, methods |
| [ex02_shopping_cart.py](exercises/starter/ex02_shopping_cart.py) | Shopping cart system | Multiple classes, lists |

## Key Concepts

### Defining a Class

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name    # Attribute
        self.gpa = gpa

    def display(self):      # Method
        print(f"{self.name}: GPA {self.gpa}")
```

### Creating Objects

```python
student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.6)

student1.display()  # Call method
print(student1.name)  # Access attribute
```

### Key Terms

- **Class**: Blueprint/template
- **Object**: Instance of a class
- **Attribute**: Data stored in object (`self.name`)
- **Method**: Function inside a class
- **`__init__`**: Constructor - runs when object created
- **`self`**: Reference to current object

---

*Completed all sections! Check [extras](../extras/) for advanced topics.*
