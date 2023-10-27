from django.urls import path
from cart.views import show_cart, get_cart_json, increase_cart, decrease_cart, delete_cart

app_name = "cart"
urlpatterns = [
    path('', show_cart, name="show_cart"),
    path('get-cart/', get_cart_json, name='get_cart_json'),
    path('increase-cart/<int:id>', increase_cart, name='increase_cart'),
    path('decrease-cart/<int:id>', decrease_cart, name='decrease_cart'),
    path('delete-cart/<int:id>', delete_cart, name='delete_cart'),
]