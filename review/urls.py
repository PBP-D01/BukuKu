from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('<str:book_id>/', views.review_list, name='review_list'),
    path('<str:book_id>/add/', views.add_review, name='add_review'),
    path('api/<str:book_id>/get/', views.get_review_api, name='get_review_api'),
    path('api/<str:book_id>/post/review/', views.post_review_api, name='post_review_api'),
]