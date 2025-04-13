from ninja import NinjaAPI, Schema
from .models import Book
from datetime import date

api = NinjaAPI()

class BookIn(Schema):
    title: str
    author: str
    published: str



class BookOut(Schema):
    id: int
    title: str
    author: str
    published: date

@api.get("/books", response=list[BookOut])
def list_books(request):
    return list(Book.objects.all())

@api.post("/books", response=BookOut)
def create_book(request, data: BookIn):
    book = Book.objects.create(**data.dict())
    return book

@api.get("/books/{book_id}", response=BookOut)
def get_book(request, book_id: int):
    return Book.objects.get(id=book_id)


