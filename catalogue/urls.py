from django.urls import path
from catalogue.views import show_catalogue, add_book, show_json, detail_book, buy_book, delete_book, edit_book

app_name = 'catalogue'

urlpatterns = [
    path('', show_catalogue, name="show_catalogue"),
    path('add_book/', add_book, name='add_book'),
    path('json/', show_json, name="show_json"),
    path('book/<int:pk>', detail_book, name='detail_book'),
    path('book/<int:pk>/purchase', buy_book, name="buy_book"),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]