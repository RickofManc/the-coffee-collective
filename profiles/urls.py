"""
Profiles URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('single_order/<order_number>',
         views.single_order, name='single_order'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add_to_wishlist/<int:id>',
         views.add_to_wishlist,
         name='user_wishlist'),
]
