from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    publisher = models.CharField(max_length=50)
    image_url_small = models.URLField()
    image_url_medium = models.URLField()
    image_url_large = models.URLField()

    def __str__(self):
        return self.title