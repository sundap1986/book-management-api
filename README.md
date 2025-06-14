# Book Management System - FastAPI with Domain-Driven Design (DDD)

## Project Structure:

![image](https://github.com/user-attachments/assets/1c7b26a5-fb04-46f9-ac06-5a5ab3ed71f5)

## 📝 Usage Guide: 
### Running the Application:
1. Install dependencies:
    -  pip install -r requirements.txt
2. Run the server:
    -  python main.py
3. Access API Documentation:
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc
4. Authentication:
-  Use one of these API keys in the Authorization header:
    - demo-api-key-123 (demo user)
    - admin-key-456 (admin user)

## 🏗️ Domain-Driven Design Architecture:

### 1. Domain Layer (Core Business Logic)

#### Book Entity: Contains all business rules and validation logic

-  ISBN validation (both ISBN-10 and ISBN-13 with checksum validation)
-  Title, author, publication year, and page count validation
-  Search matching logic
#### Domain Services : Handle complex business operations
#### Repository Interface: Abstract contract for data persistence
#### Domain Exceptions: Business-specific error handling

### 2. Application Layer (Use Cases):
  #### DTOs (Data Transfer Objects): Pydantic models for API requests/responses
  #### Application Services: Orchestrate use cases and coordinate domain services
  #### Request/Response mapping: Convert between DTOs and domain entities

### 3. Infrastructure Layer (Technical Implementation):

  #### In-Memory Repository: Concrete implementation of the repository pattern
  #### Could be easily replaced with database implementations (PostgreSQL, MongoDB, etc.)

### 4. API Layer (HTTP Interface):

  - FastAPI endpoints with comprehensive documentation
  - Authentication middleware with API key validation
  - Error handling with proper HTTP status codes
  - Dependency injection for clean separation of concerns

## 🚀 Key Features Implemented:
#### Core CRUD Operations:

  - ✅ Create Book: POST /books/ - Creates new book with validation
  - ✅ Get Book: GET /books/{isbn} - Retrieves book by ISBN
  - ✅ Update Book: PUT /books/{isbn} - Updates existing book
  - ✅ Delete Book: DELETE /books/{isbn} - Removes book

#### Bonus Features:

  - ✅ Search: GET /books/search/?q=query - Find books by title/author
  - ✅ API Key Authentication: Bearer token authentication
  - ✅ Comprehensive Validation: Including proper ISBN checksum validation

## 🔐 Authentication:
  The system uses API key authentication with demo keys:

  - demo-api-key-123 (demo user)
  - admin-key-456 (admin user)

Search endpoint allows optional authentication, while CRUD operations require authentication.

## 📊 Validation Features:
#### Business Rules Implemented:

  - Title: Non-empty, max 200 characters
  - Author: Non-empty, max 100 characters
  - Publication Year: Between 1000 and current year + 1
  - ISBN: Valid ISBN-10 or ISBN-13 with checksum validation
  - Pages: Positive number, max 10,000

#### ISBN Validation:

  - Supports both ISBN-10 and ISBN-13 formats
  - Performs mathematical checksum validation
  - Automatically cleans input (removes hyphens/spaces)

## 🛠️ Technical Highlights:

#### Repository Pattern:

  - Abstract interface allows easy swapping of persistence mechanisms
  - Current in-memory implementation for simplicity
  - Easy to extend to SQL databases, NoSQL, or external APIs

#### Dependency Injection:

  - Clean separation using FastAPI's dependency system
  - Easy testing and mocking
  - Follows SOLID principles

#### Error Handling:

  - Domain-specific exceptions
  - Proper HTTP status codes (400, 404, 409, etc.)
  - Detailed error messages with context

#### API Documentation:

  - Auto-generated OpenAPI/Swagger documentation
  - Comprehensive examples for all endpoints
  - Authentication documentation included

## 🎯 DDD Benefits Demonstrated:
#### 1. Separation of Concerns:

  - Domain logic is isolated from infrastructure concerns
  - Business rules are centralized in entities and domain services
  - Data access is abstracted through repository pattern
  - HTTP concerns are isolated in the API layer

#### 2. Testability:

  - Each layer can be unit tested independently
  - Mock repositories can be easily created for testing
  - Domain logic testing doesn't require HTTP or database setup
  - Integration testing can focus on specific layers

#### 3. Maintainability:

  - Clear boundaries between layers prevent tight coupling
  - Business logic changes don't affect API or infrastructure
  - Easy to extend with new features (e.g., book categories, reviews)
  - Technology changes (database, framework) have minimal impact

#### 4. Scalability Considerations:

  - Repository pattern allows easy migration to different databases
  - Domain services can be extended with caching, events, etc.
  - API layer can be scaled independently
  - Microservices transition would be straightforward

## 🔒 Security Features:
#### Authentication System:

  - API Key authentication with Bearer tokens
  - Role-based access (demo vs admin keys)
  - Flexible authentication (required vs optional per endpoint)
  - Easy to extend to JWT, OAuth2, etc.

#### Input Validation:

  - Pydantic models ensure type safety
  - Business rule validation in domain entities
  - SQL injection prevention through proper abstraction
  - ISBN checksum validation prevents invalid data

## 🚀 Advanced Features:
#### Search Functionality:

  - Flexible search across title and author fields
  - Case-insensitive matching
  - Extensible to full-text search engines (Elasticsearch, etc.)
  - No authentication required for public access

#### Error Handling:

  - Domain-specific exceptions with meaningful messages
  - HTTP status code mapping (400, 404, 409, etc.)
  - Structured error responses for API consumers
  - Validation error details for debugging

#### API Documentation:

  - Auto-generated OpenAPI/Swagger documentation
  - Interactive testing interface at /docs
  - Example requests/responses for all endpoints
  - Authentication documentation included

## 📊 Performance Considerations:
#### Current Implementation:

  - In-memory storage for fast development and testing
  - Synchronous domain logic with async API layer
  - Simple data structures for minimal overhead

#### Production Optimizations:

  - Database connection pooling for concurrent requests
  - Caching layer (Redis) for frequently accessed books
  - Pagination for large book collections
  - Database indexing on ISBN and search fields
  - Rate limiting to prevent abuse

## 🧪 Testing Examples:
  - The code includes comprehensive curl examples for testing all endpoints. The API supports:

    - Creating books with full validation
    - Retrieving books by ISBN
    - Updating partial book information
    - Deleting books
    - Searching books by title/author
    - Health check endpoint

## 🔄 Extensibility:
-  The architecture makes it easy to:

    - Add new features: Following the same layered approach
    - Switch databases: Implement new repository classes
    - Enhance authentication: Replace the simple API key system
    - Add caching: Implement decorator pattern on repositories
    - Scale horizontally: The stateless design supports multiple instances
