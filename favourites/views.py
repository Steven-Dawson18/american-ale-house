""" Favourites Views """
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .models import Favourites


def error_403_view(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    '''404 error view'''
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    404 error view
    """
    return render(request, '500.html', status=500)


@login_required
def favourites_view(request):
    """
    A view that displays users favourites
    """
    favourites_items_count = 0
    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = all_favourites.products.all()
        favourites_items_count = all_favourites.products.all().count()

    if not favourites_items:
        messages.info(request, 'Your favourites list is empty!')

    template = 'favourites/favourites.html'
    context = {
        'favourites_items': favourites_items,
        'favourites_items_count': favourites_items_count
    }

    return render(request, template, context)


@login_required
def add_to_favourites(request, item_id):
    """
    A view that will add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)

    if product in favourites.products.all():
        messages.info(request, 'The product is already in your favourites!')
    else:
        favourites.products.add(product)
        messages.info(request, 'Added the product to your favourites')

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_from_favourites(request, item_id, redirect_from):
    """
    A view that will add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'Removed the product '
                               'from your favourites list')
    else:
        messages.error(request, 'That product is '
                                'not in your favourites list!')
    if redirect_from == 'favourites':
        redirect_url = reverse('favourites')
    else:
        redirect_url = reverse('product_detail', args=[item_id])

    return redirect(redirect_url)
