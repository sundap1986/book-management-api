# application/dtos/book_dtos.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class CreateBookRequest(BaseModel):
    """DTO for creating a new book"""
    title: str = Field(..., min_length=1, max_length=200, description="Book title")
    author: str = Field(..., min_length=1, max_length=100, description="Book author")
    publication_year: int = Field(..., ge=1000, le=2025, description="Year of publication")
    isbn: str = Field(..., description="Book ISBN (10 or 13 digits)")
    pages: int = Field(..., gt=0, le=10000, description="Number of pages")
    
    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "publication_year": 1925,
                "isbn": "9780743273565",
                "pages": 180
            }
        }

class UpdateBookRequest(BaseModel):
    """DTO for updating a book"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    publication_year: Optional[int] = Field(None, ge=1000, le=2025)
    pages: Optional[int] = Field(None, gt=0, le=10000)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby - Updated Edition",
                "pages": 200
            }
        }

class BookResponse(BaseModel):
    """DTO for book response"""
    id: str
    title: str
    author: str
    publication_year: int
    isbn: str
    pages: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
        schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "publication_year": 1925,
                "isbn": "9780743273565",
                "pages": 180,
                "created_at": "2024-01-01T10:00:00Z",
                "updated_at": "2024-01-01T10:00:00Z"
            }
        }

class ErrorResponse(BaseModel):
    """Standard error response"""
    error: str
    detail: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "error": "Book not found",
                "detail": "Book with ISBN 1234567890 not found"
            }
        }