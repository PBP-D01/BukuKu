from django.shortcuts import render
from book.models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.shortcuts import redirect 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def show_leaderboard(request):
    context = {
        
    }

    return render(request, "leaderboard.html", context)

