# domain/services/book_service.py
from typing import List, Optional
from ..entities.book import Book
from ..repositories.book_repository import BookRepository
from ..exceptions.domain_exceptions import BookNotFoundException, BookAlreadyExistsException

class BookDomainService:
    """
    Domain service for complex business operations that don't belong to a single entity.
    
    Handles:
    - Business rules spanning multiple entities
    - Domain logic that doesn't fit naturally into entities
    - Coordination between domain objects
    """
    
    def __init__(self, repository: BookRepository):
        self._repository = repository
    
    async def create_book(self, book_data: dict) -> Book:
        """Create a new book with business rule validation"""
        # Check if book already exists
        existing_book = await self._repository.find_by_isbn(book_data.get('isbn', ''))
        if existing_book:
            raise BookAlreadyExistsException(book_data['isbn'])
        
        # Create and validate book entity
        book = Book(**book_data)
        
        # Save to repository
        return await self._repository.save(book)
    
    async def update_book(self, isbn: str, update_data: dict) -> Book:
        """Update an existing book"""
        existing_book = await self._repository.find_by_isbn(isbn)
        if not existing_book:
            raise BookNotFoundException(isbn)
        
        # Update with validation
        existing_book.update(**update_data)
        
        return await self._repository.update(existing_book)
    
    async def delete_book(self, isbn: str) -> bool:
        """Delete a book by ISBN"""
        existing_book = await self._repository.find_by_isbn(isbn)
        if not existing_book:
            raise BookNotFoundException(isbn)
        
        return await self._repository.delete(isbn)
    
    async def find_book_by_isbn(self, isbn: str) -> Book:
        """Find a book by ISBN"""
        book = await self._repository.find_by_isbn(isbn)
        if not book:
            raise BookNotFoundException(isbn)
        return book
    
    async def search_books(self, query: str) -> List[Book]:
        """Search books by title or author"""
        return await self._repository.search(query)