# Section 02: File I/O

Learn to read from and write to files for data persistence.

## Learning Objectives

After this section, you will be able to:

- Read text files in different ways
- Write and append data to files
- Work with CSV-like data
- Handle file operations safely with `with` statements

## Examples (Study These First)

| File | Topic | Key Concepts |
|------|-------|--------------|
| [01_reading_files.py](examples/01_reading_files.py) | Reading files | `open()`, `.read()`, `.readlines()`, `with` |
| [02_writing_files.py](examples/02_writing_files.py) | Writing files | Write mode, append mode, `.writelines()` |
| [03_working_with_csv.py](examples/03_working_with_csv.py) | CSV data | Parsing, manual CSV handling |
| [04_practical_log_file.py](examples/04_practical_log_file.py) | Activity log | Real-world application |

## Exercises

| Exercise | Task | Skills Used |
|----------|------|-------------|
| [ex01_score_analyzer.py](exercises/starter/ex01_score_analyzer.py) | Analyze test scores from file | Reading, parsing |
| [ex02_todo_list_manager.py](exercises/starter/ex02_todo_list_manager.py) | Save/load todo list | Reading, writing |

## Key Concepts

### Reading Files

```python
# Best practice: Use 'with' statement
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed
```

### Writing Files

```python
# Write (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello\n")

# Append (adds to end)
with open("output.txt", "a") as file:
    file.write("More text\n")
```

### File Modes

- `"r"` - Read (default)
- `"w"` - Write (overwrites)
- `"a"` - Append (adds to end)

---

*Next: [03_oop_basics](../03_oop_basics/) - Learn object-oriented programming*
