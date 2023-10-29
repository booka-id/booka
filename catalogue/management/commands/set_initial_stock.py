from django.core.management.base import BaseCommand
from book.models import Book
from catalogue.models import BookStock
import random

class Command(BaseCommand):
    help = 'Set initial stock for existing books'

    def handle(self, *args, **kwargs):
        for book in BookStock.objects.all():
            # BookStock.objects.get_or_create(book=book, defaults={'quantity': random.randrange(15,100,10), 'price': random.randrange(100000, 1000000000,25000)})
            book.quantity = random.randrange(15,100,10) # Menghasilkan angka acak dari 1 hingga 100 untuk quantity
            book.price = random.randrange(100000, 1000000,25000)
            book.save()
            
            self.stdout.write(self.style.SUCCESS(f'Stock {book.quantity} and price {book.price} already set for book "{book.book.title}"'))
