# domain/repositories/book_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.book import Book

class BookRepository(ABC):
    """
    Abstract repository interface defining contract for book persistence.
    
    This follows the Repository pattern from DDD:
    - Encapsulates data access logic
    - Provides domain-oriented interface
    - Allows for different implementations (in-memory, database, etc.)
    """
    
    @abstractmethod
    async def save(self, book: Book) -> Book:
        """Save a book and return the saved entity"""
        pass
    
    @abstractmethod
    async def find_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find a book by its ISBN"""
        pass
    
    @abstractmethod
    async def find_all(self) -> List[Book]:
        """Retrieve all books"""
        pass
    
    @abstractmethod
    async def update(self, book: Book) -> Book:
        """Update an existing book"""
        pass
    
    @abstractmethod
    async def delete(self, isbn: str) -> bool:
        """Delete a book by ISBN, return True if deleted"""
        pass
    
    @abstractmethod
    async def search(self, query: str) -> List[Book]:
        """Search books by title or author"""
        pass