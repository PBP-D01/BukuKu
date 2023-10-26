from django.urls import path
from main.views import show_main
from book.views import get_books

app_name = "book"
urlpatterns = [
    path("", get_books, name="get_books"),
]