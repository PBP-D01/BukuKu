from django.shortcuts import render
import json
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from cart.models import Cart
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='main/login')
def show_cart(request):
    carts = Cart.objects.filter(user = request.user)

    return render(request, "cart.html")

@login_required(login_url='main/login') 
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

@login_required(login_url='main/login')
@csrf_exempt
def increase_cart(request, id):
    book = Cart.objects.get(pk=id)
    book.book_amount += 1
    book.save()

    return HttpResponse(b"INCREASED", status=201)

@login_required(login_url='main/login')
@csrf_exempt
def decrease_cart(request, id):
    book = Cart.objects.get(pk=id)
    if (book.book_amount > 1):
        book.book_amount -= 1
        book.save()
 
    return HttpResponse(b"DECREASED", status=201)

@login_required(login_url='main/login')
@csrf_exempt
def delete_cart(request, id):
    book = Cart.objects.get(pk=id)
    book.delete()

    return HttpResponse(b"DELETED", status=201)