from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from book.models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.shortcuts import redirect 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound


from django.shortcuts import render 
from book.models import Book

def leaderboard(request): 
    return render(request, "leaderboard.html") 

def get_product_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def search_bar(request, value):
    product_item = Book.objects.filter(title__icontains=value)
    print(serializers.serialize('json', product_item))
    return HttpResponse(serializers.serialize('json', product_item))
