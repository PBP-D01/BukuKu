from django import views
from django.urls import path
from .views import show_leaderboard


app_name = 'leaderboard'

urlpatterns = [
    path('', show_leaderboard),
]
