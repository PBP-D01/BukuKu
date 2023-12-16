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
from cart.forms import CartForm
from datetime import datetime

# Create your views here.
@login_required(login_url='/login')
def show_cart(request):
    last_opened = request.COOKIES.get('last_opened', None)
    user_name = request.user.username
    context = {
        'last_opened': last_opened,
        'name': user_name,
        'last_login': request.user.last_login
    }

    response = render(request, "cart.html", context)
    response.set_cookie('last_opened', datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

    try:
        if last_opened:
            last_opened = datetime.strptime(last_opened, "%Y-%m-%d %H:%M:%S.%f")
        else:
            last_opened = datetime.min
    except ValueError:
        last_opened = datetime.min 
    
    return response


def get_cart_json(request):
    cart = Cart.objects.filter(user=request.user)

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

def get_cart_json_flutter(request):
    cart = Cart.objects.all()

    cart_data = []
    for cart_book in cart:
        book = cart_book.book
        cart_data.append({
            'user': cart_book.user.id,
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
def increase_cart(request, id):
    book = Cart.objects.get(pk=id)
    book.book_amount += 1
    book.save()

    return HttpResponse(b"INCREASED", status=201)

@csrf_exempt
def increase_cart_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        book.book_amount += 1
        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
@csrf_exempt
def decrease_cart(request, id):
    book = Cart.objects.get(pk=id)
    if (book.book_amount > 1):
        book.book_amount -= 1
        book.save()
 
    return HttpResponse(b"DECREASED", status=201)

@csrf_exempt
def decrease_cart_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        if (book.book_amount > 1):
            book.book_amount -= 1
            book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@login_required(login_url='/login')
@csrf_exempt
def delete_cart(request, id):
    book = Cart.objects.get(pk=id)
    book.delete()

    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def delete_cart_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        book.delete()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
@csrf_exempt
def edit_cart(request, id):
    cart = Cart.objects.get(pk = id)

    form = CartForm(request.POST or None, instance=cart)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('cart:show_cart'))
    
    context = {
    'form': form,
    'book_title': cart.book.title,
    'book_author': cart.book.author,
    'price': round(cart.book.price * 15000,2),
    'img': cart.book.imgUrl,
    }

    return render(request, "edit_cart.html", context)

@csrf_exempt
def edit_cart_ajax(request, id):
    cart = Cart.objects.get(pk=id)
    if request.method == 'POST':
        new_book_amount = request.POST.get("book_amount")

        cart.book_amount = new_book_amount
        cart.save()

        return HttpResponse(b"EDITED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def edit_cart_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        new_book_amount = data['amount']

        book.book_amount = new_book_amount
        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)