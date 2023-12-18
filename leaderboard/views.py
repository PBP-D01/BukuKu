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
from leaderboard.models import LeaderBoard, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from leaderboard.forms import CommentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse


from django.shortcuts import render 
from book.models import Book


def show_xml_by_id(request, id):
    data = Comment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Comment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def show_xml(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_leaderboard(request):
    # Get the last time the leaderboard page was opened from the cookie
    last_opened = request.COOKIES.get('last_opened', None)
    context = {
        'last_opened': last_opened,
        'comments': Comment.objects.all(),
        'name': request.user.username,
        'last_login': request.user.last_login,
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

def create_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_comment.html", context)


def get_leaderboard_flutter(request):
    product_items = Book.objects.all().order_by('-buys')

    # Serialize the sorted products to JSON
    json_data = serializers.serialize('json', product_items)

    # Return the JSON response
    return JsonResponse(json_data, safe=False, status=200)


@csrf_exempt
def create_comment_flutter(request, id):
    if request.method == 'POST':
        msg = request.POST.get('comment')
        comment = Comment.objects.create(comment=msg).save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def get_comment_flutter(request):
    comment_items=Comment.objects.all()
    json_data = serializers.serialize('json', comment_items)
    return JsonResponse(json_data, safe=False, status=200)
