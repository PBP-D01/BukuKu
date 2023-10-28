from django.urls import path
from checkout.views import checkout, get_item_json, update_buys, update_cart,search_bar

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('update_buys/', update_buys, name='update_buys'),
    path('update_cart/', update_cart, name='update_cart'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
]