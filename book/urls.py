from django.urls import path
from book.views import get_books, get_books_by_title

app_name = "book"

urlpatterns = [
    path("", get_books, name="get_books"),
    path("book_by_title/", get_books_by_title, name='book_by_title')
]