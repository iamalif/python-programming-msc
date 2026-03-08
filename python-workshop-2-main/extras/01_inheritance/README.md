# Inheritance & Polymorphism

Advanced OOP concepts for code reuse and flexibility.

## What You'll Learn

- How to create classes that inherit from other classes
- Using `super()` to call parent class methods
- Understanding and applying polymorphism
- Building class hierarchies

## Examples

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_basic_inheritance.py](01_basic_inheritance.py) | Inheritance basics | Base class, derived class, overriding |
| [02_using_super.py](02_using_super.py) | The super() method | Calling parent constructors, extending methods |
| [03_polymorphism.py](03_polymorphism.py) | Polymorphism | Common interfaces, treating objects uniformly |

## Key Concepts

### Inheritance
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):  # Child inherits from Parent
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
```

### Polymorphism
```python
def process_shape(shape):
    # Works with any shape type!
    print(shape.area())

shapes = [Circle(5), Rectangle(4, 3), Triangle(6, 4)]
for shape in shapes:
    process_shape(shape)  # Polymorphism in action
```

## When to Use

- **Inheritance**: When you have an "is-a" relationship (Student IS A Person)
- **Polymorphism**: When you want to treat different types of objects uniformly
- **super()**: When you need to call or extend parent class functionality

---

*Part of Workshop 2 extras - self-study material*
