# Section 02: Control Flow

Learn to make decisions and repeat actions in your programs.

## Learning Objectives

After this section, you will be able to:
- Use `if/elif/else` to make decisions
- Compare values and combine conditions
- Repeat code with `while` loops
- Iterate over sequences with `for` loops

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_conditionals.py](examples/01_conditionals.py) | Making decisions | `if`, `elif`, `else`, nesting |
| [02_comparisons.py](examples/02_comparisons.py) | Testing conditions | `==`, `!=`, `<`, `>`, `and`, `or`, `not` |
| [03_while_loops.py](examples/03_while_loops.py) | Repeating actions | `while`, `break`, `continue`, accumulators |
| [04_for_loops.py](examples/04_for_loops.py) | Iterating sequences | `for`, `range()`, running totals |

## Exercises

Work on these in `exercises/starter/`. Check `exercises/solutions/` when done.

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_grade_classifier.py](exercises/starter/ex01_grade_classifier.py) | Convert score to letter grade | `if/elif/else` |
| [ex02_login_system.py](exercises/starter/ex02_login_system.py) | Login with limited attempts | `while`, `break`, conditions |
| [ex03_expense_tracker.py](exercises/starter/ex03_expense_tracker.py) | Track expenses until done | `while True`, accumulator |
| [ex04_sales_analysis.py](exercises/starter/ex04_sales_analysis.py) | Analyze weekly sales | `for` loop, calculations |

## Key Concepts Summary

### Conditionals
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

### Comparison Operators
```python
x == y    # Equal
x != y    # Not equal
x < y     # Less than
x > y     # Greater than
x <= y    # Less than or equal
x >= y    # Greater than or equal
```

### Logical Operators
```python
if age >= 18 and has_license:    # Both must be True
if is_member or total > 100:     # At least one True
if not is_cancelled:             # Inverts the value
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Loop until user wants to stop
while True:
    value = input("Enter value (0 to quit): ")
    if value == "0":
        break
```

### For Loops
```python
# Count from 0 to 4
for i in range(5):
    print(i)

# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count by 2s: 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)
```

---

*Next: [03_functions](../03_functions/) - Learn to create reusable code blocks*
