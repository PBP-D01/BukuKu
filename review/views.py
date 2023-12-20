from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import ReviewForm
from book.models import Book
from .models import Review

import json

@login_required(login_url='/login')
def add_review(request, book_id):

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            
            return JsonResponse({'status': 'success', 'message': 'Review berhasil disimpan', 
                                 'review_rating': review.rating,
                                 "review_reviewer" : str(review.reviewer),
                                 "review_text" : review.text,
            })
    
    return JsonResponse({'status': 'error', 'message': 'Permintaan tidak valid'})

@login_required(login_url='/login')
def review_list(request, book_id):

    # Get book Object (if there is any)
    book = Book.objects.filter(id=book_id)

    if not book:
        raise Http404
    
    book = book.first()

    # Initiate Form Review

    form = ReviewForm(None, initial={
        'book' : book_id,
        'reviewer': request.user.id,
    })

    # Get all review objects
    reviews = Review.objects.filter(book=book)
    return render(request, 'review.html', {
        'form': form, 
        'book_id': book_id,
        'book' : book,
        'reviews' : reviews,
        'rating_range' : range(1, 6),
    })

def get_review_api(request,book_id):
     # Get book Object (if there is any)
    book = Book.objects.filter(id=book_id)

    if not book:
        raise Http404
    
    book = book.first()

    # Get all review objects
    reviews = Review.objects.filter(book=book)
    data = [
        {
            "pk" : book.pk,
            "fields" : {
                "title" : book.title,
                "publishedDate" : book.publishedDate,
                "price" : book.price,
                "imgUrl" : book.imgUrl,
                "stars" : book.stars,
                "category_name" : book.category_name,
                "author" : book.author,
                "reviews": []
            },
        }
    ]

    for review in reviews:
        data[0]["fields"]["reviews"].append({
            "pk" : review.pk,
            "fields" : {
                "text" : review.text,
                "rating" : review.rating,
                "book" : review.book.title,
                "reviewer" : review.reviewer.username,
            },
        })
    return JsonResponse(data,safe=False)

@csrf_exempt
def post_review_api(request,book_id):
    # Get book Object (if there is any)
    book = Book.objects.filter(id=book_id)

    if not book:
        raise Http404
    
    book = book.first()

    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))

        text = data.get("text")
        rating = data.get("rating")
        
        review = Review.objects.create(text=text, rating=rating, book=book, reviewer=request.user)

        return JsonResponse({'status': 'success', 'message': 'Review berhasil disimpan', 
                                'review_rating': review.rating,
                                "review_reviewer" : str(review.reviewer),
                                "review_text" : review.text,
        })
    
    return JsonResponse({'status': 'error', 'message': 'Permintaan tidak valid'})