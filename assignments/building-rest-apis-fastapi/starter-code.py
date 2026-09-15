from fastapi import FastAPI, Query, status
from pydantic import BaseModel


app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
    {"id": 2, "title": "Kindred", "author": "Octavia E. Butler"},
]


class BookCreate(BaseModel):
    # TODO: Declare the required title and author fields.
    pass


@app.get("/")
def read_root():
    # TODO: Return {"message": "Book API is running"}.
    pass


@app.get("/books")
def list_books(author: str | None = Query(default=None)):
    # TODO: Return every book, or only books matching the optional author.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Generate an id, store the new book, and return it.
    pass