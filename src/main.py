
from fastapi import FastAPI

app = FastAPI()

books = [
    {"Title":"The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year": 1925, "Category": "Fiction"},
    {"Title":"To Kill a Mockingbird", "Author": "Harper Lee", "Year": 1960, "Category": "Fiction"},
    {"Title":"1984", "Author": "George Orwell", "Year": 1949, "Category": "Dystopian Fiction"},
]


@app.get("/api/v1/books")
def get_books():
    return books


@app.get("/api/v1/books/{book_title}")
def get_book(book_title: str):
    for book in books:
        if book["Title"].casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}