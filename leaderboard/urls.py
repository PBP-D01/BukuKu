from django import views
from django.urls import path
from .views import  show_leaderboard, get_product_json, search_bar


app_name = 'leaderboard'

urlpatterns = [
    # path('', show_leaderboard),
    path('', show_leaderboard, name='show_leaderboard'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
]
