from django import views
from django.urls import path
from .views import  show_leaderboard, get_product_json, search_bar, create_comment
from .views import show_xml, show_json, show_xml_by_id, show_json_by_id 




app_name = 'leaderboard'

urlpatterns = [
    # path('', show_leaderboard),
    path('', show_leaderboard, name='show_leaderboard'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('search_bar/<str:value>', search_bar, name='search_bar'),
    path('create_comment', create_comment, name='create_comment'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
