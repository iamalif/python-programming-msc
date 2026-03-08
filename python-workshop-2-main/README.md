# Python Workshop 2: Data Structures & OOP

Welcome to Python Workshop 2! Building on fundamental programming concepts, this workshop focuses on organizing data and structuring code using Python's data structures and object-oriented programming.

## Workshop Structure

| Section | Duration | Topics |
|---------|----------|--------|
| [01_data_structures](./01_data_structures/) | ~1.5 hours | Lists, tuples, dictionaries, choosing the right structure |
| [02_file_io](./02_file_io/) | ~1 hour | Reading files, writing files, CSV data, file safety |
| [03_oop_basics](./03_oop_basics/) | ~1.5 hours | Classes, objects, attributes, methods, encapsulation |

## How This Workshop Works

### During Class

1. **Examples first** - We'll go through the example files together
2. **Then exercises** - You'll work on exercises independently
3. **Solutions available** - Check your work against the solutions

### Folder Structure

```
each_section/
├── examples/          # Teaching examples (we cover these together)
└── exercises/
    ├── starter/       # Your working files (edit these!)
    └── solutions/     # Reference solutions
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A code editor (VS Code recommended)
- Completion of Workshop 1 (or equivalent Python fundamentals knowledge)

### Running Files

```bash
# Navigate to the workshop folder
cd python-workshop-2

# Run any Python file
python 01_data_structures/examples/01_lists.py
```

### Check Your Python Version

```bash
python --version
```

## Quick Reference

### Section 1: Data Structures

- **Lists** - Mutable ordered collections (`students = ["Alice", "Bob"]`)
- `.append()`, `.remove()`, `.pop()` - List methods
- Indexing - Access elements (`students[0]`)
- Slicing - Get subsets (`students[1:3]`)
- **Tuples** - Immutable ordered collections (`coords = (10, 20)`)
- **Dictionaries** - Key-value pairs (`student = {"name": "Alice", "gpa": 3.8}`)
- `.get()`, `.keys()`, `.values()` - Dictionary methods

### Section 2: File I/O

- `with open(filename, mode)` - Safe file handling
- `.read()`, `.readlines()` - Read file content
- `.write()`, `.writelines()` - Write to files
- File modes: `"r"` (read), `"w"` (write), `"a"` (append)
- `.split()` - Parse CSV-like data

### Section 3: OOP Basics

- `class ClassName:` - Define a class
- `__init__(self, ...)` - Constructor method
- `self` - Reference to current object
- Attributes - Data stored in objects (`self.name = name`)
- Methods - Functions inside classes
- Instantiation - Create objects (`obj = ClassName()`)

## Beyond the Workshop

Want to go further? Check out the [extras](./extras/) folder for advanced OOP topics:

- **Inheritance & Polymorphism** - Create class hierarchies and write reusable code
- **Properties & Decorators** - Use `@property` for elegant attribute management
- **Advanced OOP Patterns** - Explore sophisticated object-oriented designs

These topics are optional but valuable for writing more sophisticated Python code. Study them after mastering the main workshop content!

## Tips for Success

1. **Run every example** - Don't just read, execute the code
2. **Experiment** - Modify examples to see what happens
3. **Read error messages** - They tell you what went wrong
4. **Start simple** - Get basic version working, then add features
5. **Ask questions** - Don't struggle in silence!

## File Naming Convention

- `01_topic_name.py` - Examples (numbered for order)
- `ex01_task_name.py` - Exercise starter files
- `ex01_task_name.py` - Solutions (in solutions folder)

---

*Ready to start? Head to [01_data_structures](./01_data_structures/) and begin with the first example!*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
