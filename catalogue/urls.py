from django.urls import path
from catalogue.views import add_book_flutter, buy_book_ajax, buy_book_flutter, delete_book_flutter, edit_book_flutter, get_book_by_id, get_books_with_stock, get_bookstock_by_id, get_buy_flutter, get_buy_json, search_books, show_catalogue, add_book, show_json, detail_book, buy_book, delete_book, edit_book, add_book_ajax, get_book_json, get_bookstock_json, search_book, pay_book

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
    path('get-bookpurchase/', get_buy_json, name='get_buy_json'),
    path('search_book/', search_books, name='search_books'),
    path('pay_book/<int:pk>/', pay_book, name='pay_book'),
    path('books_with_stock/', get_books_with_stock, name='get_books_with_stock'),
    path('book-json/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('bookstock-json/<int:book_id>/', get_bookstock_by_id, name='get_bookstock_by_id'),
    path('add-book-flutter/', add_book_flutter, name='add_book_flutter'),
    path('delete-book-flutter/<int:pk>/', delete_book_flutter, name='delete_book_flutter'),
    path('edit-book-flutter/<int:pk>/', edit_book_flutter, name='edit_book_flutter'),
    path('buy-book-flutter/', buy_book_flutter, name='buy_book_flutter'),
    path('buy-book-ajax/', buy_book_ajax, name='buy_book_ajax'),
    path('get-bookpurchase/<int:userID>/', get_buy_flutter, name='get_buy_flutter'),
]