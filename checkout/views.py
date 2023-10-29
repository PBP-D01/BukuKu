from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import render,redirect
from checkout.forms import CheckoutForm
from django.http import HttpResponse
from checkout.models import Checkout
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from cart.models import Cart 
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.@csrf_exempt
@login_required(login_url='/login')
def get_item_json(request):
    item_product = Checkout.objects.all()
    return HttpResponse(serializers.serialize('json', item_product))

@login_required(login_url='/login')
@csrf_exempt
def checkout(request):
    form = CheckoutForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        checkout = form.save(commit=False)
        checkout.user = request.user
        checkout.save()
    
    last_opened = request.COOKIES.get('last_opened', None)
    context = {
        'last_opened': last_opened,
        'form': form,
        'last_login': request.user.last_login,
    }
    # Update the cookie with the current timestamp
    response = render(request, "checkout.html", context=context)
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

@login_required(login_url='/login')
@csrf_exempt
def update_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    for cart_item in cart_items:
        book = cart_item.book
        book.buys += 1  # Increment the book_buys field

        # Save the updated book and cart_item objects
        book.save()
        cart_item.delete()

    return HttpResponse({'status': 'DELETED'}, status=200)