from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publishedDate = models.DateField(auto_now_add=True)
    price = models.FloatField()
    imgUrl = models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)
    stars = models.FloatField()
    buys = models.IntegerField(default=0)