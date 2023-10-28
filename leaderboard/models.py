from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class LeaderBoard(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # quote = models.TextField(default = "")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)