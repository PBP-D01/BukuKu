from django.forms import ModelForm
from cart.models import Cart

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ["book_amount"]