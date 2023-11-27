from django.urls import path
from main.views import create_product_flutter, show_main, login_user, logout_user, register
from product_page.views import show_product
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('show_product', show_product, name='show_product'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]