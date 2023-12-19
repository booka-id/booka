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
    
    def edit_book(self, new_isbn=None, new_title=None, new_author=None, new_year=None, 
                  new_publisher=None, new_image_url_large=None):
        if new_isbn:
            self.isbn = new_isbn
        if new_title:
            self.title = new_title
        if new_author:
            self.author = new_author
        if new_year:
            self.year = new_year
        if new_publisher:
            self.publisher = new_publisher
        if new_image_url_large:
            self.image_url_large = new_image_url_large
            self.image_url_medium = new_image_url_large
            self.image_url_small = new_image_url_large
        self.save()