# api/dependencies.py
from fastapi import Depends
from domain.services.book_service import BookDomainService
from infrastructure.repositories.in_memory_book_repository import InMemoryBookRepository
from application.services.book_application_service import BookApplicationService

# Dependency injection setup
def get_book_repository() -> InMemoryBookRepository:
    """Get book repository instance"""
    return InMemoryBookRepository()

def get_book_domain_service(repository: InMemoryBookRepository = Depends(get_book_repository)) -> BookDomainService:
    """Get book domain service"""
    return BookDomainService(repository)

def get_book_application_service(domain_service: BookDomainService = Depends(get_book_domain_service)) -> BookApplicationService:
    """Get book application service"""
    return BookApplicationService(domain_service)