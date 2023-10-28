from django import views
from django.urls import path
from .views import leaderboard, get_product_json, search_bar


app_name = 'leaderboard'

urlpatterns = [
    # path('', show_leaderboard),
    path('', leaderboard),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
]
