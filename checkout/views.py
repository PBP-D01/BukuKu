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
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "checkout.html", context)

@login_required(login_url='/login')
@csrf_exempt
def update_cart(request):
    cart_item = Cart.objects.get(user=request.user)
    cart_item.delete()
    return HttpResponse({'status': 'DELETED'}, status=200)
