from django.urls import path
from .views import *

app_name = 'product_page'

urlpatterns = [
    path('', show_product, name='show_product'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('add_to_cart/<int:id>', add_cart, name='add_cart'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
]

