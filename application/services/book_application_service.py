# application/services/book_application_service.py
from typing import List
from domain.services.book_service import BookDomainService
from application.dtos.book_dtos import BookResponse, CreateBookRequest, UpdateBookRequest

class BookApplicationService:
    """
    Application service orchestrating use cases.
    
    This layer:
    - Coordinates between domain services
    - Handles DTO conversion
    - Manages transactions (if needed)
    - Implements use case workflows
    """
    
    def __init__(self, domain_service: BookDomainService):
        self._domain_service = domain_service
    
    async def create_book(self, request: CreateBookRequest) -> BookResponse:
        """Create a new book"""
        book_data = request.dict()
        book = await self._domain_service.create_book(book_data)
        return BookResponse.from_orm(book)
    
    async def get_book_by_isbn(self, isbn: str) -> BookResponse:
        """Get book by ISBN"""
        book = await self._domain_service.find_book_by_isbn(isbn)
        return BookResponse.from_orm(book)
    
    async def update_book(self, isbn: str, request: UpdateBookRequest) -> BookResponse:
        """Update a book"""
        update_data = {k: v for k, v in request.dict().items() if v is not None}
        book = await self._domain_service.update_book(isbn, update_data)
        return BookResponse.from_orm(book)
    
    async def delete_book(self, isbn: str) -> bool:
        """Delete a book"""
        return await self._domain_service.delete_book(isbn)
    
    async def search_books(self, query: str) -> List[BookResponse]:
        """Search books"""
        books = await self._domain_service.search_books(query)
        return [BookResponse.from_orm(book) for book in books]