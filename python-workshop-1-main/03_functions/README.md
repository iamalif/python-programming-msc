# Section 03: Functions

Learn to organize code into reusable blocks.

## Learning Objectives

After this section, you will be able to:
- Define functions with `def`
- Use parameters to pass data into functions
- Return values from functions
- Create flexible functions with default parameters

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_defining_functions.py](examples/01_defining_functions.py) | Creating functions | `def`, parameters, calling functions |
| [02_return_values.py](examples/02_return_values.py) | Getting results back | `return`, multiple returns |
| [03_default_parameters.py](examples/03_default_parameters.py) | Optional parameters | Default values, keyword arguments |

## Exercises

Work on these in `exercises/starter/`. Check `exercises/solutions/` when done.

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_tip_calculator.py](exercises/starter/ex01_tip_calculator.py) | Calculate restaurant tips | Functions, default parameters |
| [ex02_sales_statistics.py](exercises/starter/ex02_sales_statistics.py) | Analyze sales data | Multiple return values |
| [ex03_discount_system.py](exercises/starter/ex03_discount_system.py) | Tiered discount pricing | All function concepts |

## Key Concepts Summary

### Defining Functions
```python
def greet(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

greet("Alice")  # Call the function
```

### Return Values
```python
def calculate_tax(amount):
    return amount * 0.25

tax = calculate_tax(100)  # tax = 25.0
```

### Multiple Return Values
```python
def analyze(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

total, avg = analyze([10, 20, 30])
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Carol", greeting="Hey")  # Hey, Carol! (keyword arg)
```

### Why Use Functions?

1. **Avoid repetition** - Write once, use many times
2. **Organization** - Break complex tasks into smaller parts
3. **Readability** - Give meaningful names to code blocks
4. **Maintainability** - Change in one place, works everywhere

---

*Congratulations! You've completed Workshop 1. See you in Workshop 2!*
