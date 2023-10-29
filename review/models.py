from django.db import models
from django.contrib.auth.models import User

from book.models import Book

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)