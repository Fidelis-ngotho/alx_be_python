# Book class definition
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    # Method to check out a book
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    # Method to return a book
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # Method to check if the book is available
    def is_available(self):
        return not self._is_checked_out


# Library class definition
class Library:
    def __init__(self):
        self._books = []  # Private list to store book instances

    # Method to add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Method to check out a book by title
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"You have successfully checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Sorry, '{title}' is not available in the library.")

    # Method to return a book by title
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been successfully returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Sorry, '{title}' is not a book in this library.")

    # Method to list available books
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")


# Ensure this is saved as 'library_management.py' in the correct directory for main.py to import.
