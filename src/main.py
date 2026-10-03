
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

# Path Parameter
@app.get("/api/v1/books/{book_title}")
def get_book_by_title(book_title: str):
    for book in books:
        if book["Title"].casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}


# Query Parameter
# NOTE: Make sure to add / at the end of the URL when using query parameters
@app.get("/api/v1/books/")
def get_Books_by_Category(category: str):
    filtered_books = [book for book in books if book["Category"].casefold() == category.casefold()]
    return filtered_books


# Path Parameter and Query Parameter
@app.get("/api/v1/books/{book_title/}")
def get_book_by_title_with_query(book_title: str, category: str):
    for book in books:
        if book["Title"].casefold() == book_title.casefold() and book["Category"].casefold() == category.casefold():
            return book
    return {"message": "Book not found"}