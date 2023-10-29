from django.urls import path
from catalogue.views import show_catalogue, add_book

app_name = 'catalogue'

urlpatterns = [
    path('', show_catalogue, name="show_catalogue"),
    path('add_book/', add_book, name='add_book'),
]