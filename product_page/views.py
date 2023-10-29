from datetime import date
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from book.models import Book
from django.core import serializers
from cart.models import Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from product_page.models import Product


# Create your views here.
@login_required(login_url='/login')
def show_product(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }

    return render(request, "product_page.html", context)

def get_product_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_cart(request):
    
    body = json.loads(
        request.body.decode('utf-8'))
    
    id = body['id']
    
    # product = Product(last_added_to_cart = date.today())
    # product.save()
    
    book = Book.objects.get(pk=id)
    if(Cart.objects.filter(user = request.user.id, book_id= id)):
        cart = Cart.objects.get(user = request.user.id, book_id = id)
        cart.book_amount += 1
        cart.save()
        return HttpResponse(b"ADDED", status=201)
    else:
        Cart(user = request.user, book = book, book_amount = 1).save()
        return HttpResponse(b"ADDED", status=201)

def search_bar(request, value):
    product_item = Book.objects.filter(title__icontains=value)
    print(serializers.serialize('json', product_item))
    return HttpResponse(serializers.serialize('json', product_item))

def search_bar2(request, value):
    product_item = Book.objects.filter(author__icontains=value)
    print(serializers.serialize('json', product_item))
    return HttpResponse(serializers.serialize('json', product_item))

   