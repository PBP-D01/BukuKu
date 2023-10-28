from django.forms import ModelForm
from checkout.models import Checkout

class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = ["first_name", "last_name", "email", "address",]

