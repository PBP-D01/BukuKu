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


# Create your views here.
def get_item_json(request):
    item_product = Checkout.objects.all()
    return HttpResponse(serializers.serialize('json', item_product))

@csrf_exempt
def checkout(request):
    form = CheckoutForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        checkout = form.save(commit=False)
        checkout.user = request.user
        checkout.save()

        leaderboard_update = checkout.book
        leaderboard_update.buys += 1
        leaderboard_update.save()

        # Remove the item from the user's cart
        cart_item = Cart.objects.get(user=request.user)
        cart_item.delete()

    user_cart = Cart.objects.filter(user=request.user)
    context = {
        'form': form,
        'user_cart': user_cart,
    }
    return render(request, "checkout.html", context)

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
