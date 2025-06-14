# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.books import router as books_router

# Create FastAPI application
app = FastAPI(
    title="Book Management System",
    description="""
    A comprehensive book management system built with FastAPI and Domain-Driven Design (DDD).
    
    ## Features
    - **CRUD Operations**: Create, read, update, and delete books
    - **Search**: Find books by title or author
    - **Authentication**: API key-based security
    - **Validation**: Comprehensive input validation including ISBN validation
    - **DDD Architecture**: Clean separation of concerns
    
    ## Authentication
    Most endpoints require an API key. Use one of these demo keys:
    - `demo-api-key-123` (demo user)
    - `admin-key-456` (admin user)
    
    Include the key in the Authorization header: `Bearer your-api-key`
    
    ## Architecture
    This application follows Domain-Driven Design principles:
    - **Domain Layer**: Core business logic and rules
    - **Application Layer**: Use cases and DTOs
    - **Infrastructure Layer**: Data persistence and external services
    - **API Layer**: HTTP interface and routing
    """,
    version="1.0.0",
    contact={
        "name": "Book Management API",
        "email": "support@bookmanagement.com"
    },
    license_info={
        "name": "MIT",
    }
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(books_router)

@app.get("/", tags=["root"])
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to the Book Management System",
        "documentation": "/docs",
        "version": "1.0.0"
    }

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)