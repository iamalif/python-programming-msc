# Section 01: Data Structures

Learn to work with Python's built-in data structures for organizing and managing data.

## Learning Objectives

After this section, you will be able to:

- Create and manipulate lists
- Use tuples for immutable data
- Work with dictionaries for key-value storage
- Choose the right data structure for your needs

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_lists.py](examples/01_lists.py) | Lists | Creating, accessing, modifying, methods |
| [02_tuples.py](examples/02_tuples.py) | Tuples | Immutability, unpacking, when to use |
| [03_dictionaries.py](examples/03_dictionaries.py) | Dictionaries | Key-value pairs, methods, nesting |
| [04_choosing_data_structures.py](examples/04_choosing_data_structures.py) | Decision guide | When to use each type |

## Exercises

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_student_grades.py](exercises/starter/ex01_student_grades.py) | Manage student grades | Lists, iteration |
| [ex02_inventory_system.py](exercises/starter/ex02_inventory_system.py) | Store inventory | Dictionaries |
| [ex03_student_database.py](exercises/starter/ex03_student_database.py) | Student records | List of dicts |

## Key Concepts

### Lists

```python
students = ["Alice", "Bob", "Charlie"]
students.append("Diana")     # Add to end
students[0]                  # Access by index
students[1:3]                # Slicing
```

### Tuples

```python
coordinates = (10, 20)       # Immutable
x, y = coordinates           # Unpacking
```

### Dictionaries

```python
student = {"name": "Alice", "gpa": 3.8}
student["age"] = 20          # Add key
student.get("phone", "N/A")  # Safe access
```

---

*Next: [02_file_io](../02_file_io/) - Learn to read and write files*
