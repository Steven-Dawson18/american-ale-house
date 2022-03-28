"""Favourites Urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_view, name='favourites'),
]
