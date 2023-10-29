from django.forms import ModelForm
from django import forms
from book.models import Book
from catalogue.models import BookStock

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'year', 'publisher', 'image_url_small', 'image_url_medium', 'image_url_large']


class BookStockForm(ModelForm):
    class Meta:
        model = BookStock
        fields = ['quantity', 'price']

class AddBookForm(ModelForm):
    quantity = forms.IntegerField(label='Quantity')
    price = forms.IntegerField(label='Price')

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'year', 'publisher', 'image_url_small', 'image_url_medium', 'image_url_large']
