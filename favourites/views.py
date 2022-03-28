""" Favourites Views """
from django.shortcuts import (render, get_object_or_404, redirect)
from products.models import Product
from .models import Favourites


def favourites_view(request):
    """
    A view that displays users favourites
    """
    template = 'favourites/favourites.html'
    context = {

    }
    return render(request, template, context)
