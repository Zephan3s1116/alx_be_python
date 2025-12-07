

class Book:
    """
    A class to represent a Book with title, author, and year,
    demonstrating Python's magic methods.
    """
    def __init__(self, title, author, year):
        """Initializes a new Book instance."""
        self.title = title
        self.author = author
        self.year = year
       

    def __del__(self):
        """Prints a message when the object is about to be destroyed."""
      
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the user-friendly, informal string representation of the object.
        Used by the print() function.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official, unambiguous string representation of the object.
        It should ideally be a valid Python expression to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

