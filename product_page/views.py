from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from book.models import Book
from django.core import serializers
from cart.models import Cart
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
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
def add_cart(request, id):
    book = Book.objects.get(pk=id)
    # Cart.objects.all().delete()
    # return HttpResponse(b"ADDED", status=201)
    if(Cart.objects.filter(user = request.user.id, book_id= id)):
        cart = Cart.objects.get(user = request.user.id, book_id = id)
        cart.book_amount += 1
        cart.save()
        print('ini if')
        return HttpResponse(b"ADDED", status=201)
    else:
        Cart(user = request.user, book = book, book_amount = 1).save()
        print('ini elsef')
        return HttpResponse(b"ADDED", status=201)

def search_bar(request, value):
    product_item = Book.objects.filter(title__icontains=value)
    print(serializers.serialize('json', product_item))
    return HttpResponse(serializers.serialize('json', product_item))

   