"""
Exercise 02: Todo List Manager
==============================
Create a simple todo list that saves to and loads from a file.

Your task:
1. Create a list of tasks
2. Save the list to 'todos.txt'
3. Read it back and display
4. Add more tasks and save again

Expected output:
----------------
=== Original Todo List ===
1. Buy groceries
2. Study Python
3. Exercise
4. Call mom

Saved to 'todos.txt'

=== Reading from File ===
1. Buy groceries
2. Study Python
3. Exercise
4. Call mom

=== After Adding Tasks ===
1. Buy groceries
2. Study Python
3. Exercise
4. Call mom
5. Finish homework
6. Clean room

Updated 'todos.txt'
"""

# TODO: Create initial todo list
todos = [
    "Buy groceries",
    "Study Python",
    "Exercise",
    "Call mom"
]  # Add some tasks

# TODO: Display original list
print("=== Original Todo List ===\n")
for i, todo in enumerate(todos, start=1):
    print(f"{i}. {todo}")


# TODO: Save to file 'todos.txt'
# Write each task on a new line with numbering

with open("todos.txt", "w") as file:
    for i, todo in enumerate(todos, start=1):
        file.write(f"{i}. {todo}\n")

print("\nSaved to 'todos.txt'\n")


# TODO: Read back from file and display
# Hint: Use 'with open("todos.txt", "r") as file:'
print("=== Reading from File ===")
with open("todos.txt", "r") as file:
    print(file.read())


# TODO: Add 2 more tasks to the list
todos.append("Finish homework")
todos.append("Clean room")


# TODO: Save updated list to file (overwrite)
print("=== After Adding Tasks ===")

with open("todos.txt", "w") as file:
    for i, todo in enumerate(todos, start=1):
        file.write(f"{i}. {todo}\n")

with open("todos.txt", "r") as file:
    print(file.read())

# TODO: Display confirmation

print("Updated 'todos.txt'")