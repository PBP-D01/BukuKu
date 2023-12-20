from django.urls import path
from .views import *

app_name = 'product_page'

urlpatterns = [
    path('', show_product, name='show_product'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('add_to_cart', add_cart, name='add_cart'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
    path('search_bar2/<str:value>', search_bar2, name='search_bar2'),
]