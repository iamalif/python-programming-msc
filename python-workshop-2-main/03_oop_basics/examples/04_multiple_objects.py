"""
04 - Working with Multiple Objects
==================================
Managing collections of objects.

Run this file: python 04_multiple_objects.py
"""

class Book:
    """Represents a book in a library."""

    def __init__(self, title, author, isbn, available=True):
        """Create a new book."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def checkout(self):
        """Borrow the book."""
        if self.available:
            self.available = False
            print(f"'{self.title}' checked out successfully.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        """Return the book."""
        self.available = True
        print(f"'{self.title}' returned successfully.")

    def display_info(self):
        """Show book information."""
        status = "Available" if self.available else "Checked Out"
        print(f"{self.title} by {self.author} [{status}]")


# Library management demo
print("=== Library System ===")
print()

# Create a library (list of books)
library = [
    Book("Python Crash Course", "Eric Matthes", "001"),
    Book("Clean Code", "Robert Martin", "002"),
    Book("The Pragmatic Programmer", "Hunt & Thomas", "003"),
    Book("Design Patterns", "Gang of Four", "004")
]

# Display all books
print("Library Catalog:")
for i, book in enumerate(library, start=1):
    print(f"{i}. ", end="")
    book.display_info()

# Perform operations
print()
print("=== Library Operations ===")
print()

# Checkout some books
library[0].checkout()  # Python Crash Course
library[2].checkout()  # The Pragmatic Programmer

# Try to checkout already borrowed book
library[0].checkout()  # Should fail

# Return a book
library[0].return_book()

# Search for available books
print()
print("=== Available Books ===")
print()

available_books = [book for book in library if book.available]
print(f"Total available: {len(available_books)}")
for book in available_books:
    print(f"  - {book.title}")

# Search by author
print()
print("=== Search by Author ===")
print()

search_author = "Eric Matthes"
for book in library:
    if book.author == search_author:
        book.display_info()
