from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('<str:book_id>/', views.review_list, name='review_list'),
    path('<str:book_id>/add/', views.add_review, name='add_review'),
]