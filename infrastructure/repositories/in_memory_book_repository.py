# infrastructure/repositories/in_memory_book_repository.py
import uuid
from typing import List, Optional, Dict
from domain.entities.book import Book
from domain.repositories.book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    """
    In-memory implementation of BookRepository.
    
    This is a concrete implementation of the repository interface.
    In a real application, this might be replaced with:
    - SQLAlchemy implementation
    - MongoDB implementation
    - Redis implementation
    etc.
    """
    
    def __init__(self):
        self._books: Dict[str, Book] = {}
    
    async def save(self, book: Book) -> Book:
        """Save a book to memory"""
        if book.id is None:
            book.id = str(uuid.uuid4())
        
        self._books[book.isbn] = book
        return book
    
    async def find_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find book by ISBN"""
        return self._books.get(isbn)
    
    async def find_all(self) -> List[Book]:
        """Get all books"""
        return list(self._books.values())
    
    async def update(self, book: Book) -> Book:
        """Update existing book"""
        if book.isbn in self._books:
            self._books[book.isbn] = book
            return book
        return None
    
    async def delete(self, isbn: str) -> bool:
        """Delete book by ISBN"""
        if isbn in self._books:
            del self._books[isbn]
            return True
        return False
    
    async def search(self, query: str) -> List[Book]:
        """Search books by title or author"""
        return [book for book in self._books.values() 
                if book.matches_search(query)]