

class Book:
    """Base class for all book types."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Default string representation for a book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title, author, file_size):
       
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook, including file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class for physical printed books."""
    def __init__(self, title, author, page_count):
        
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook, including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class demonstrating composition, managing a collection of book objects.
    """
    def __init__(self):
       
        self.books = []

    def add_book(self, book):
        """Adds a book instance to the library's collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(f"Error: Cannot add non-Book object to the library.")

    def list_books(self):
        """Prints the details of each book in the library using their __str__ method."""
        for book in self.books:
            print(book)

