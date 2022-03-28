"""Favourites Urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_view, name='favourites'),
    path('add_to_favourites/<item_id>/',
         views.add_to_favourites, name='add_to_favourites'),
    path('remove_from_favourites/<item_id>/<redirect_from>/',
         views.remove_from_favourites, name='remove_from_favourites'),
]
