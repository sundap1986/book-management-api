import requests

# Base URL
base_url = "http://localhost:8000"
headers = {"Authorization": "Bearer demo-api-key-123"}

# Create a book
book_data = {
    "title": "1984",
    "author": "George Orwell",
    "publication_year": 1949,
    "isbn": "9780452284234",
    "pages": 328
}

response = requests.post(f"{base_url}/books/", json=book_data, headers=headers)
print(response.json())

# Get the book
response = requests.get(f"{base_url}/books/9780452284234", headers=headers)
print(response.json())

# Search books
response = requests.get(f"{base_url}/books/search/?q=orwell")
print(response.json())