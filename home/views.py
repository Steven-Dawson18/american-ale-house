"""Home Views"""
from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faqs(request):
    """ A view to return the FAQ's page """

    return render(request, 'home/faqs.html')


def contact(request):
    """ A view to return the Contact Us page """

    return render(request, 'home/contact.html')
