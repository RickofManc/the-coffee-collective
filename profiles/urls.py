"""
Profiles URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('single_order/<order_number>',
         views.single_order, name='single_order'),
    path('wishlist/', views.user_wish_list, name="wishlist"),
    path('add_to_wishlist/<pk>', views.add_to_wishlist,
         name="add_to_wishlist"),
    path('remove_from_wishlist/<pk>', views.remove_from_wishlist,
         name="remove_from_wishlist")
]
