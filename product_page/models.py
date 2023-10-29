from django.db import models
from book.models import Book

class Product(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    last_added_to_cart = models.DateField(auto_now_add=True)