#!/usr/bin/env python3
"""
Implements a simple Library Management System using OOP concepts with 
Book and Library classes.
"""

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book (public).
        author (str): The author of the book (public).
        _is_checked_out (bool): Tracks the book's availability (private).
    """
    def __init__(self, title, author):
        """Initializes a new Book instance, default available."""
        self.title = title
        self.author = author
        # Private attribute to manage availability status
        self._is_checked_out = False 

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for user-friendly output."""
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book objects.

    Attributes:
        _books (list): A private list to store Book instances (encapsulation).
    """
    def __init__(self):
        """Initializes a new Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def _find_book(self, title):
        """Helper method to find a Book object by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Checks out a book if it is found and available."""
        book = self._find_book(title)
        if book and book.is_available():
            book.check_out()
            print(f"Successfully checked out: {book.title}")
            return True
        elif book and not book.is_available():
            print(f"Error: {book.title} is already checked out.")
        else:
            print(f"Error: Book '{title}' not found.")
        return False

    def return_book(self, title):
        """Returns a book, marking it as available."""
        book = self._find_book(title)
        if book and not book.is_available():
            book.return_book()
            print(f"Successfully returned: {book.title}")
            return True
        elif book and book.is_available():
            print(f"Error: {book.title} was not checked out.")
        else:
            print(f"Error: Book '{title}' not found.")
        return False

    def list_available_books(self):
        """Prints a list of all currently available books."""
        available_books = [str(book) for book in self._books if book.is_available()]
        
        if available_books:
            for book_str in available_books:
                print(book_str)
        else:
            print("No books currently available.")

# End of library_management.py