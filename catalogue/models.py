from django.db import models
from user_profile.models import User
from book.models import Book

# Create your models here.
class BookStock(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    

    def edit_stock(self, new_quantity=None, new_price=None):
        if new_quantity is not None:
            self.quantity = new_quantity
        if new_price is not None:
            self.price = new_price
        self.save()


class BookPurchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=30)
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} purchased {self.quantity} copies of "{self.book.title}"'