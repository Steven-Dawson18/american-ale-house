"""Home Views"""
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from products.models import Product


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


def index(request):
    """ A view to return the index page """
    products = Product.objects.all().order_by('category')

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def faqs(request):
    """ A view to return the FAQ's page """

    return render(request, 'home/faqs.html')


def contact(request):
    """ A view to return the Contact Us page """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['emailaddress']
        message = request.POST['message']

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['fullstacksteve18@gmail.com'])
        messages.success(request,
                         'Email received. We will contact you shortly.')
        return render(request, "home/contact.html")
    else:
        return render(request, "home/contact.html")
