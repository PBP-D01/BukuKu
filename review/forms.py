from django import forms

from review.models import Review


RATING_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"),)

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', 'rating', 'book', 'reviewer')
        widgets = {
            'text': forms.Textarea(attrs={'type' : 'text', 'placeholder' : 'Masukkan Teks Review', 'class' : 'form-text-control', 'autocomplete' : 'off'}),
            'rating': forms.RadioSelect(attrs={'class' : ''}, choices=RATING_CHOICES),
        }