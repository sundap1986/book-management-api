# domain/entities/book.py
from datetime import datetime
from typing import Optional
from dataclasses import dataclass
import re

@dataclass
class Book:
    """
    Book entity representing the core domain object.
    
    This is the heart of our domain model, containing:
    - Business rules and invariants
    - Domain logic
    - Value validation
    """
    title: str
    author: str
    publication_year: int
    isbn: str
    pages: int
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        """Validate domain rules after initialization"""
        self._validate_title()
        self._validate_author()
        self._validate_publication_year()
        self._validate_isbn()
        self._validate_pages()
        
        if self.created_at is None:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def _validate_title(self):
        """Business rule: Title must be non-empty and reasonable length"""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        if len(self.title.strip()) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        self.title = self.title.strip()
    
    def _validate_author(self):
        """Business rule: Author must be non-empty and reasonable length"""
        if not self.author or not self.author.strip():
            raise ValueError("Author cannot be empty")
        if len(self.author.strip()) > 100:
            raise ValueError("Author cannot exceed 100 characters")
        self.author = self.author.strip()
    
    def _validate_publication_year(self):
        """Business rule: Publication year must be reasonable"""
        current_year = datetime.now().year
        if self.publication_year < 1000 or self.publication_year > current_year + 1:
            raise ValueError(f"Publication year must be between 1000 and {current_year + 1}")
    
    def _validate_isbn(self):
        """Business rule: ISBN must follow standard format"""
        if not self.isbn:
            raise ValueError("ISBN cannot be empty")
        
        # Remove hyphens and spaces for validation
        clean_isbn = re.sub(r'[-\s]', '', self.isbn)
        
        # Check if it's ISBN-10 or ISBN-13
        if len(clean_isbn) == 10:
            if not self._is_valid_isbn10(clean_isbn):
                raise ValueError("Invalid ISBN-10 format")
        elif len(clean_isbn) == 13:
            if not self._is_valid_isbn13(clean_isbn):
                raise ValueError("Invalid ISBN-13 format")
        else:
            raise ValueError("ISBN must be 10 or 13 digits")
        
        self.isbn = clean_isbn
    
    def _validate_pages(self):
        """Business rule: Pages must be positive"""
        if self.pages <= 0:
            raise ValueError("Number of pages must be positive")
        if self.pages > 10000:
            raise ValueError("Number of pages cannot exceed 10,000")
    
    def _is_valid_isbn10(self, isbn: str) -> bool:
        """Validate ISBN-10 checksum"""
        if not isbn.isdigit() and isbn[-1].upper() != 'X':
            return False
        
        total = 0
        for i in range(9):
            if not isbn[i].isdigit():
                return False
            total += int(isbn[i]) * (10 - i)
        
        check_digit = isbn[9]
        if check_digit == 'X':
            total += 10
        elif check_digit.isdigit():
            total += int(check_digit)
        else:
            return False
        
        return total % 11 == 0
    
    def _is_valid_isbn13(self, isbn: str) -> bool:
        """Validate ISBN-13 checksum"""
        if not isbn.isdigit():
            return False
        
        total = 0
        for i in range(12):
            digit = int(isbn[i])
            total += digit * (1 if i % 2 == 0 else 3)
        
        check_digit = (10 - (total % 10)) % 10
        return check_digit == int(isbn[12])
    
    def update(self, **kwargs):
        """Update book attributes with validation"""
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
        
        # Re-validate after update
        self.__post_init__()
    
    def matches_search(self, query: str) -> bool:
        """Check if book matches search query in title or author"""
        query_lower = query.lower()
        return (query_lower in self.title.lower() or 
                query_lower in self.author.lower())