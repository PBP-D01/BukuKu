from django.shortcuts import render
from django.http import JsonResponse

from .forms import ReviewForm
from .models import Review

def add_review(request, book_id):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            
            return JsonResponse({'status': 'success', 'message': 'Review berhasil disimpan'})
    
    return JsonResponse({'status': 'error', 'message': 'Permintaan tidak valid'})

def review_list(request, book_id):

    form = ReviewForm(None, initial=(
        
    ))
    
    return render(request, 'review.html', {'form': form,})
