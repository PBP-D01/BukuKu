from datetime import datetime
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
from django.http import HttpResponseRedirect
# from leaderboard.forms import ProductForm
from django.urls import reverse
from leaderboard.models import LeaderBoard


from django.shortcuts import render 
from book.models import Book

def show_leaderboard(request):
    # Get the last time the leaderboard page was opened from the cookie
    last_opened = request.COOKIES.get('last_opened', None)
    context = {
        'last_opened': last_opened
    }
    # Update the cookie with the current timestamp
    response = render(request, "leaderboard.html", context=context)
    response.set_cookie('last_opened', datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    
    # Display the last time the leaderboard page was opened
    try:
        if last_opened:
            last_opened = datetime.strptime(last_opened, "%Y-%m-%d %H:%M:%S.%f")
        else:
            last_opened = datetime.min  # Set to the minimum datetime value to indicate "N/A"
    except ValueError:
        # Handle the case where the 'last_opened' cookie has an unexpected format
        last_opened = datetime.min  # Set to the minimum datetime value to indicate "N/A"

    
    return response

def get_product_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def search_bar(request, value):
    product_item = Book.objects.filter(title__icontains=value)
    print(serializers.serialize('json', product_item))
    return HttpResponse(serializers.serialize('json', product_item))

