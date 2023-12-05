from django.urls import path
from catalogue.views import get_books_with_stock, search_books, show_catalogue, add_book, show_json, detail_book, buy_book, delete_book, edit_book, add_book_ajax, get_book_json, get_bookstock_json, search_book, pay_book, tes_satu

app_name = 'catalogue'

urlpatterns = [
    path('', show_catalogue, name="show_catalogue"),
    path('add-book/', add_book, name='add_book'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('json/', show_json, name="show_json"),
    path('book/<int:pk>', detail_book, name='detail_book'),
    path('book/<int:pk>/purchase', buy_book, name="buy_book"),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('get-bookstock/', get_bookstock_json, name='get_bookstock_json'),
    path('search_book/', search_books, name='search_books'),
    path('pay_book/<int:pk>/', pay_book, name='pay_book'),
    path('books_with_stock/', get_books_with_stock, name='get_books_with_stock'),
]