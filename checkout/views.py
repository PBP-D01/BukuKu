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
    context = {
        'form': form,
    }
    return render(request, "checkout.html", context)

@login_required(login_url='/login')
def get_cart_json(request):
    cart = Cart.objects.filter(user = request.user)

    cart_data = []
    for cart_book in cart:
        book = cart_book.book
        cart_data.append({
            'id': cart_book.id,
            'book_title': book.title,
            'book_author': book.author,
            'book_price': book.price,
            'book_img' : book.imgUrl,
            'book_amount': cart_book.book_amount,
        })

    # Convert the list of dictionaries to a JSON string
    cart_json = json.dumps(cart_data)

    return HttpResponse(cart_json, content_type='application/json')

@login_required(login_url='/login')
@csrf_exempt
def update_buys(request):
        leaderboard_update = Cart.objects.get(user=request.user)
        leaderboard_update.buys += 1
        leaderboard_update.save()
        return HttpResponse(b"ADDED", status=201)

@login_required(login_url='/login')
@csrf_exempt
def update_cart(request):
        cart_item = Cart.objects.get(user=request.user)
        cart_item.delete()
        return HttpResponse(b"DELETED", status=201)

@login_required(login_url='/login')
@csrf_exempt
def search_bar(request, value):
    print(f"Search value received: {value}")  # Debugging line
    product_items = Book.objects.filter(book__title__icontains=value) | Cart.objects.filter(book__author__icontains=value)
    product_data = serializers.serialize('json', product_items)
    return HttpResponse(product_data, content_type='application/json')