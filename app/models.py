from django.db import models

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    title = models.CharField("Title",max_length=20)
    streaming = models.CharField("Straming",max_length=100)
    server = models.CharField("Server",max_length=100)
    trailer = models.CharField("Trailer",max_length=100)
    year = models.IntegerField("Year")
    description = models.CharField("Description", max_length=30)
    category = models.CharField("Category",max_length=50, choices=(
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('cartoon', 'Cartoon'),

    ))
    image = models.ImageField("Poster",upload_to='images/', blank=True)
    date_added = models.DateTimeField("Created At",default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

  # class Category(models.Model):
  #   manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
  #   name = models.CharField("Name",max_length=20)
  #   date_added = models.DateTimeField("Created At",default=datetime.now)

  #   def __str__(self):
  #       return self.name

  #   class Meta:
  #       ordering = ['-id']
