# api/endpoints/books.py
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from application.services.book_application_service import BookApplicationService
from application.dtos.book_dtos import BookResponse, CreateBookRequest, UpdateBookRequest, ErrorResponse
from domain.exceptions.domain_exceptions import BookNotFoundException, BookAlreadyExistsException, InvalidBookDataException
from api.dependencies import get_book_application_service
from api.middleware import verify_api_key, optional_verify_api_key

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", 
            response_model=BookResponse,
            status_code=201,
            responses={400: {"model": ErrorResponse}, 409: {"model": ErrorResponse}})
async def create_book(
    request: CreateBookRequest,
    service: BookApplicationService = Depends(get_book_application_service),
    current_user: str = Depends(verify_api_key)
):
    """
    Create a new book.
    
    Requires API key authentication.
    """
    try:
        return await service.create_book(request)
    except BookAlreadyExistsException as e:
        raise HTTPException(status_code=409, detail=str(e))
    except (ValueError, InvalidBookDataException) as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{isbn}",
           response_model=BookResponse,
           responses={404: {"model": ErrorResponse}})
async def get_book(
    isbn: str,
    service: BookApplicationService = Depends(get_book_application_service),
    current_user: str = Depends(verify_api_key)
):
    """
    Get a book by its ISBN.
    
    Requires API key authentication.
    """
    try:
        return await service.get_book_by_isbn(isbn)
    except BookNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{isbn}",
           response_model=BookResponse,
           responses={400: {"model": ErrorResponse}, 404: {"model": ErrorResponse}})
async def update_book(
    isbn: str,
    request: UpdateBookRequest,
    service: BookApplicationService = Depends(get_book_application_service),
    current_user: str = Depends(verify_api_key)
):
    """
    Update an existing book.
    
    Requires API key authentication.
    """
    try:
        return await service.update_book(isbn, request)
    except BookNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (ValueError, InvalidBookDataException) as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{isbn}",
              status_code=204,
              responses={404: {"model": ErrorResponse}})
async def delete_book(
    isbn: str,
    service: BookApplicationService = Depends(get_book_application_service),
    current_user: str = Depends(verify_api_key)
):
    """
    Delete a book by its ISBN.
    
    Requires API key authentication.
    """
    try:
        await service.delete_book(isbn)
    except BookNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/search/", response_model=List[BookResponse])
async def search_books(
    q: str = Query(..., description="Search query for title or author"),
    service: BookApplicationService = Depends(get_book_application_service),
    current_user: Optional[str] = Depends(optional_verify_api_key)
):
    """
    Search books by title or author.
    
    API key authentication is optional for this endpoint.
    """
    return await service.search_books(q)