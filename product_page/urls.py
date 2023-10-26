from django.urls import path
from .views import *
from . import views

app_name = 'product_page'

urlpatterns = [
    path('', show_product, name='show_product'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
]