# domain/exceptions/domain_exceptions.py
class DomainException(Exception):
    """Base exception for domain-related errors"""
    pass

class BookNotFoundException(DomainException):
    """Raised when a book is not found"""
    def __init__(self, isbn: str):
        super().__init__(f"Book with ISBN {isbn} not found")
        self.isbn = isbn

class BookAlreadyExistsException(DomainException):
    """Raised when attempting to create a book that already exists"""
    def __init__(self, isbn: str):
        super().__init__(f"Book with ISBN {isbn} already exists")
        self.isbn = isbn

class InvalidBookDataException(DomainException):
    """Raised when book data is invalid"""
    pass