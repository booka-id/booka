from django.forms import ModelForm
from book.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'year', 'publisher', 'image_url_small', 'image_url_medium', 'image_url_large']