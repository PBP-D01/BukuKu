from django.urls import path
from checkout.views import checkout, get_item_json

app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='checkout'),
    path('get-item/', get_item_json, name='get_item_json'),

]