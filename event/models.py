from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    photo = models.URLField(default='https://www.pngkey.com/png/detail/233-2332677_ega-png.png')