from django.db import models
from book.models import Book

# Create your models here.
class BookStock(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
