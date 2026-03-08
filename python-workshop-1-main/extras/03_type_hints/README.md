# Type Hints: Documenting Your Code

**Type hints** (or type annotations) let you specify what types of values variables and functions should use.

> **Important:** Python does NOT enforce type hints - they are for documentation and tooling only.

## Why Use Type Hints?

1. **Documentation** - Makes code easier to understand
2. **IDE Support** - Better autocomplete and error detection
3. **Static Analysis** - Tools can catch errors before running

## Basic Syntax

```python
# Variable type hints
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True

# Function type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
```

## Run the Example

```bash
cd extras/03_type_hints
python example.py
```
