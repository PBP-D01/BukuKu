from django.urls import path
from checkout.views import checkout, checkout_flutter, get_item_json, update_cart

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('update_cart/', update_cart, name='update_cart'),
    path('checkout_flutter/', checkout_flutter, name='checkout_flutter'),
]