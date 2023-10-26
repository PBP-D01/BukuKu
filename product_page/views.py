from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from book.models import Book
from django.core import serializers

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

def add_to_cart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book.id')
        product_item = Book.objects.get(id=book_id)
        
        response_data = {'message': 'Item berhasil ditambahkan ke keranjang'}
        return JsonResponse(response_data)