# Python Workshop 1: Fundamentals

Welcome to your first Python workshop! This 4-hour session covers the essential building blocks of Python programming through practical, data-focused examples.

## Workshop Structure

| Section | Duration | Topics |
|---------|----------|--------|
| [01_basics](./01_basics/) | ~1.5 hours | Variables, input/output, arithmetic, string formatting |
| [02_control_flow](./02_control_flow/) | ~1.5 hours | Conditionals, comparison operators, loops |
| [03_functions](./03_functions/) | ~1 hour | Defining functions, return values, default parameters |

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

### Running Files

```bash
# Navigate to the workshop folder
cd workshop_1

# Run any Python file
python 01_basics/examples/01_hello_python.py
```

### Check Your Python Version

```bash
python --version
```

## Quick Reference

### Section 1: Basics

- `print()` - Display output
- Variables - Store data (`name = "Alice"`)
- `input()` - Get user input (always returns string!)
- `int()`, `float()` - Convert strings to numbers
- f-strings - Format output (`f"Hello, {name}"`)

### Section 2: Control Flow

- `if/elif/else` - Make decisions
- `==, !=, <, >, <=, >=` - Compare values
- `and, or, not` - Combine conditions
- `while` - Repeat while condition is true
- `for` - Repeat a set number of times

### Section 3: Functions

- `def` - Define a function
- Parameters - Input to functions
- `return` - Send back a result
- Default parameters - Optional inputs with default values

## Beyond the Workshop

Want to go further? Check out the [extras](./extras/) folder for advanced topics:

- **Modules** - Organize code into separate files
- **Packages** - Create nested module structures
- **Type Hints** - Add type annotations to your code

Feel free to explore them on your own!

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

*Ready to start? Head to [01_basics](./01_basics/) and begin with the first example!*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
