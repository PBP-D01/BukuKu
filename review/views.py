from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from book.models import Book
from .models import Review

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
