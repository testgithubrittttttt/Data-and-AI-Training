from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()


# Pydantic model for Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float = Field(..., ge=0, description="Price should not be negative")
    in_stock: bool


# In-memory list to store books
books: List[Book] = [
    Book(id=1, title="Deep Learning", author="Ian Goodfellow", price=1200, in_stock=True),
    Book(id=2, title="Python Tricks", author="Dan Bader", price=600, in_stock=False),
    Book(id=3, title="Fluent Python", author="Luciano Ramalho", price=900, in_stock=True)
]


# ------------------- GET all books -------------------
@app.get("/books", response_model=List[Book])
def get_books():
    return books


# ------------------- GET single book by ID -------------------
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# ------------------- POST: Add new book -------------------
@app.post("/books", status_code=201)
def add_book(book: Book):
    # Check if book ID already exists
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")

    books.append(book)
    return {"message": "Book added successfully", "book": book}


# ------------------- PUT: Update book -------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")


# ------------------- DELETE: Remove book -------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(i)
            return {"message": "Book deleted", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")


# ------------------- GET: Search books -------------------
@app.get("/books/search", response_model=List[Book])
def search_books(author: Optional[str] = None, max_price: Optional[float] = None):
    result = books
    if author:
        result = [book for book in result if author.lower() in book.author.lower()]
    if max_price is not None:
        result = [book for book in result if book.price <= max_price]

    return result


# ------------------- BONUS: Get available books -------------------
@app.get("/books/available", response_model=List[Book])
def get_available_books():
    return [book for book in books if book.in_stock]


# ------------------- BONUS: Get total count of books -------------------
@app.get("/books/count")
def get_books_count():
    return {"count": len(books)}
